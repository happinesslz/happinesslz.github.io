#!/usr/bin/env python3
"""Build Zhe Liu's CV from the homepage publications and the records below.

Requires Python 3.9+ and reportlab. No network access or scheduled tasks are used.
Run from any directory:
    python3 scripts/build_cv.py --output output/pdf/cv_zheliu_hku.pdf

Review the rendered PDF, then copy it to data/cv_zheliu_hku.pdf for publication.
The optional --font-dir must contain Times New Roman and Arial Unicode TTFs.
"""

import argparse
from dataclasses import dataclass, field
from html import escape
from html.parser import HTMLParser
from pathlib import Path
import re

from reportlab.lib import colors
from reportlab.lib.enums import TA_LEFT
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import (
    HRFlowable, KeepTogether, PageBreak, Paragraph, SimpleDocTemplate, Spacer,
)


ROOT = Path(__file__).resolve().parents[1]
INK = colors.HexColor("#202936")
BLUE = colors.HexColor("#193e65")
MUTED = colors.HexColor("#5b6470")
RULE = colors.HexColor("#cbd4de")
SCHOLAR = "https://scholar.google.com/citations?hl=en&user=yprv7EsAAAAJ"


@dataclass
class Element:
    tag: str
    attrs: dict = field(default_factory=dict)
    children: list = field(default_factory=list)

    def text(self):
        return "".join(c.text() if isinstance(c, Element) else c for c in self.children)

    def find_all(self, class_name=None, tag=None):
        result = []
        for child in self.children:
            if not isinstance(child, Element):
                continue
            if (class_name is None or class_name in child.attrs.get("class", "").split()) and (tag is None or child.tag == tag):
                result.append(child)
            result.extend(child.find_all(class_name, tag))
        return result


class HomepageParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.root = Element("root")
        self.stack = [self.root]

    def handle_starttag(self, tag, attrs):
        node = Element(tag, dict(attrs))
        self.stack[-1].children.append(node)
        if tag not in {"img", "br", "hr", "input", "meta", "link", "source"}:
            self.stack.append(node)

    def handle_endtag(self, tag):
        for i in range(len(self.stack) - 1, 0, -1):
            if self.stack[i].tag == tag:
                del self.stack[i:]
                break

    def handle_data(self, data):
        self.stack[-1].children.append(data)


def plain(text):
    return text.replace("\u2011", "-").replace("\u2013", "-").replace("\u2014", "-").replace("\u00a0", " ")


def symbol(text):
    return text.replace("✉", '<font name="Symbols">✉</font>')


def author_markup(node, in_sup=False):
    if isinstance(node, str):
        value = escape(plain(node))
        for mark in ("*", "†", "‡", "✉"):
            value = value.replace(mark, symbol(mark) if in_sup else "<super>" + symbol(mark) + "</super>")
        return value
    body = "".join(author_markup(child, in_sup or node.tag == "sup") for child in node.children)
    if node.tag in ("strong", "b"):
        return "<b>" + body + "</b>"
    if node.tag == "sup":
        return "<super>" + body + "</super>"
    return body


def read_homepage():
    source = (ROOT / "_pages/about.md").read_text()
    parser = HomepageParser()
    parser.feed(source)
    papers = []
    for card in parser.root.find_all("paper-box"):
        title = card.find_all("paper-title")[0]
        authors = card.find_all("paper-authors")[0]
        venue = card.find_all("paper-venue")[0].text()
        papers.append({
            "title": plain(title.text()),
            "url": title.find_all(tag="a")[0].attrs["href"],
            "authors": author_markup(authors),
            "venue": plain(venue),
            "year": int(re.search(r"\b(20\d{2})\b", venue).group(1)),
            "links": [(a.text().strip("[]"), a.attrs["href"]) for a in card.find_all("paper-links")[0].find_all(tag="a")],
        })
    metrics = re.search(r"reports ([\d,]+) citations, an h-index of (\d+), and an i10-index of (\d+)", source)
    count = re.search(r"published (\d+\+) papers", source)
    if not papers or not metrics or not count:
        raise ValueError("Homepage publications or profile metrics could not be read")
    return papers, metrics.groups(), count.group(1)


def register_fonts(directory):
    names = {
        "CV": "Times New Roman.ttf",
        "CV-Bold": "Times New Roman Bold.ttf",
        "CV-Italic": "Times New Roman Italic.ttf",
        "CV-BoldItalic": "Times New Roman Bold Italic.ttf",
        "Symbols": "Arial Unicode.ttf",
    }
    for family, filename in names.items():
        font = TTFont(family, str(directory / filename))
        pdfmetrics.registerFont(font)
    pdfmetrics.registerFontFamily("CV", normal="CV", bold="CV-Bold", italic="CV-Italic", boldItalic="CV-BoldItalic")
    if ord("✉") not in pdfmetrics.getFont("Symbols").face.charToGlyph:
        raise ValueError("The symbol font must contain the corresponding-author envelope")


STYLES = {}


def make_styles():
    base = dict(fontName="CV", fontSize=10.5, leading=13.1, textColor=INK, alignment=TA_LEFT)
    STYLES["body"] = ParagraphStyle("body", **base, spaceAfter=5)
    STYLES["small"] = ParagraphStyle("small", **{**base, "fontSize": 9.6, "leading": 12}, spaceAfter=4)
    STYLES["name"] = ParagraphStyle("name", **{**base, "fontName": "CV-Bold", "fontSize": 29, "leading": 33}, spaceAfter=3)
    STYLES["subtitle"] = ParagraphStyle("subtitle", **{**base, "fontSize": 11.4, "leading": 14.2}, spaceAfter=2)
    STYLES["section"] = ParagraphStyle("section", **{**base, "fontName": "CV-Bold", "fontSize": 13.3, "leading": 16, "textColor": BLUE}, spaceBefore=10, spaceAfter=6, keepWithNext=True)
    STYLES["page_title"] = ParagraphStyle("page_title", **{**base, "fontName": "CV-Bold", "fontSize": 18.3, "leading": 22, "textColor": BLUE}, spaceAfter=9, keepWithNext=True)
    STYLES["pub_title"] = ParagraphStyle("pub_title", **{**base, "fontSize": 10.5, "leading": 12.6}, leftIndent=23, bulletIndent=0, bulletFontName="CV", bulletFontSize=10.5, spaceAfter=1)
    STYLES["pub_authors"] = ParagraphStyle("pub_authors", **{**base, "fontSize": 9.9, "leading": 12}, leftIndent=23, spaceAfter=1)
    STYLES["pub_venue"] = ParagraphStyle("pub_venue", **{**base, "fontSize": 9.9, "leading": 12}, leftIndent=23, spaceAfter=7)
    STYLES["bullet"] = ParagraphStyle("bullet", **base, leftIndent=10, bulletIndent=0, bulletFontName="CV", bulletFontSize=10.5, spaceAfter=4)
    STYLES["bullet_small"] = ParagraphStyle("bullet_small", **{**base, "fontSize": 9.6, "leading": 12}, leftIndent=10, bulletIndent=0, bulletFontName="CV", bulletFontSize=9.6, spaceAfter=4)


def p(text, style="body"):
    return Paragraph(text, STYLES[style])


def link(label, url):
    return '<link href="' + escape(url, quote=True) + '" color="#193e65">' + escape(label) + '</link>'


def section(story, title):
    story.append(p(escape(title), "section"))


def bullet(story, text, small=False):
    story.append(Paragraph(text, STYLES["bullet_small" if small else "bullet"], bulletText="-"))


def page_title(story, title, note=None):
    story.append(p(title, "page_title"))
    if note:
        story.append(p(note, "small"))
    story.append(HRFlowable(width="100%", thickness=0.6, color=RULE, spaceAfter=10))


def footer(canvas, doc):
    canvas.saveState()
    width, height = A4
    canvas.setStrokeColor(RULE)
    canvas.setLineWidth(0.5)
    canvas.line(44, 34, width - 44, 34)
    canvas.setFillColor(MUTED)
    canvas.setFont("CV", 8.8)
    canvas.drawString(44, 21, "Zhe Liu | Curriculum Vitae")
    canvas.drawRightString(width - 44, 21, str(doc.page))
    if doc.page > 1:
        canvas.setFont("CV", 8.6)
        canvas.drawString(44, height - 25, "Zhe Liu")
        canvas.drawRightString(width - 44, height - 25, "The University of Hong Kong")
    canvas.restoreState()


def publication(story, paper, number):
    venue = paper["venue"]
    if "arXiv" in venue:
        arxiv = re.search(r"(\d{4}\.\d{4,5})", paper["url"])
        label = f"arXiv:{arxiv.group(1)}, {paper['year']}" if arxiv else f"arXiv preprint, {paper['year']}"
    else:
        abbreviation = re.search(r"\(([^)]+)\)", venue)
        label = f"{abbreviation.group(1)}, {paper['year']}" if abbreviation else venue.rstrip(".")
        if "Spotlight" in venue:
            label += " - Spotlight"
        if "Oral" in venue:
            label += " - Oral presentation"
    # Preserve all available links without labelling an unreleased repository as code.
    links = " &nbsp; ".join(link("[" + label + "]", url) for label, url in paper["links"])
    story.append(KeepTogether([
        Paragraph(f"<b>{link(paper['title'], paper['url'])}</b>", STYLES["pub_title"], bulletText=f"{number:02d}."),
        p(paper["authors"], "pub_authors"),
        p("<b>" + escape(label) + ".</b> &nbsp; " + links, "pub_venue"),
    ]))


def build(output, font_dir):
    register_fonts(font_dir)
    make_styles()
    papers, (citations, hindex, i10index), paper_count = read_homepage()
    recent = [x for x in papers if x["year"] == 2026 and "arXiv" not in x["venue"]]
    preprints = [x for x in papers if "arXiv" in x["venue"]]
    earlier = [x for x in papers if x not in recent and x not in preprints]
    if len(recent) + len(preprints) + len(earlier) != len(papers):
        raise ValueError("Publication grouping is incomplete")
    story = []

    story.extend([
        p("Zhe Liu", "name"),
        p("Postdoctoral Researcher in Embodied AI and 3D Perception", "subtitle"),
        p("Department of Computer Science, The University of Hong Kong", "subtitle"),
        p(link("happinesslzcq@gmail.com", "mailto:happinesslzcq@gmail.com") + " &nbsp; | &nbsp; " + link("happinesslz.github.io", "https://happinesslz.github.io/") + " &nbsp; | &nbsp; " + link("Google Scholar", SCHOLAR), "small"),
        HRFlowable(width="100%", thickness=1, color=BLUE, spaceBefore=6, spaceAfter=7),
    ])
    section(story, "Research Profile")
    story.append(p("I develop embodied intelligence systems that connect spatial perception, multimodal reasoning, world modeling, and executable actions. My work spans autonomous driving, 3D perception, vision-language-action models, 4D MLLMs, and world-action models, building on over eight years of research in autonomous driving and 3D perception."))
    story.append(p(f"<b>{paper_count} papers</b> in TPAMI, TIP, CVPR, ICCV, ECCV, NeurIPS, ICML, AAAI, IROS, TITS, and ICRA. " + link("Google Scholar", SCHOLAR) + f": <b>{citations} citations</b>; h-index <b>{hindex}</b>; i10-index <b>{i10index}</b>."))

    section(story, "Academic Appointment and Education")
    story.append(p("<b>2025 - Present &nbsp; Postdoctoral Researcher, The University of Hong Kong.</b><br/>Department of Computer Science; working with Prof. " + link("Hengshuang Zhao", "https://hszhao.github.io/") + "."))
    story.append(p("<b>2020 - 2025 &nbsp; Ph.D., Huazhong University of Science and Technology.</b><br/>School of Electronic Information and Communications; advisor: Prof. " + link("Xiang Bai", "https://xbai.vlrlab.net/") + "."))

    section(story, "Research Experience")
    story.append(p("<b>Jan 2022 - Dec 2024 &nbsp; Research Intern, Baidu Vision Technology Department.</b><br/>Multimodal 3D object perception for autonomous driving."))
    story.append(p("<b>Sep 2020 - Dec 2020 &nbsp; Research Intern, Huawei Noah's Ark Lab.</b><br/>End-to-end 3D object tracking algorithms."))

    section(story, "Research Agenda")
    for text in [
        "<b>Embodied data engines:</b> egocentric human data, human-to-robot data transformation, and corner-case feedback for scalable robotic learning.",
        "<b>VLA, world-action models, and VLN:</b> spatial-temporal reasoning and executable actions for manipulation, navigation, and long-horizon tasks.",
        "<b>4D world models and simulation:</b> physical and attention-based modeling for virtual evaluation, policy learning, and sim-to-real transfer.",
        "<b>Efficient streaming inference:</b> model distillation, acceleration, and streaming policies for real-time robotic deployment.",
        "<b>Intelligent robotic OS:</b> unified input/output interfaces and foundation models for cross-embodiment deployment.",
    ]:
        bullet(story, text)

    section(story, "Selected Research Projects, 2025-2026")
    for text in [
        "<b>AI glasses (Huawei):</b> efficient spatial intelligence for 3D perception, understanding, and memory retrieval on edge devices.",
        "<b>4D MLLM (Huawei):</b> unifying vision-action and vision-language-action capabilities in a 0.5B model.",
        "<b>4D world model (Huawei):</b> 4D occupancy representations for high-resolution, long-term, physically informed video generation.",
        "<b>World models and RL (Changan):</b> efficient attention-based world modeling for autonomous driving.",
        "<b>Streaming VLA (ACE Robotics):</b> memory-dependent, spatially aware vision-language-action models.",
        "<b>Ongoing:</b> efficient world models, efficient VLAs, and an embodied OS for physical agents.",
    ]:
        bullet(story, text, small=True)

    legend = '* Equal contribution; <font name="Symbols">✉</font> Corresponding author; † Project leader; ‡ Equal advising.'
    story.append(PageBreak())
    page_title(story, "Selected Publications | 2026", "Accepted and published papers. " + legend)
    number = 1
    for paper in recent:
        publication(story, paper, number)
        number += 1

    story.append(PageBreak())
    page_title(story, "Recent Preprints | 2026-2025", legend)
    for paper in preprints:
        publication(story, paper, number)
        number += 1
    section(story, "Industry Collaborations")
    story.append(p("Previous collaborations with companies and research teams: Huawei Noah's Ark Lab; Huawei Auto BU / Yinwang; Baidu; Changan Automobile; Li Auto; ByteDance Seed; ACE Robotics; and Langyi Robotics."))

    story.append(PageBreak())
    page_title(story, "Selected Publications | 2025-2019", legend)
    for paper in earlier:
        publication(story, paper, number)
        number += 1

    story.append(PageBreak())
    page_title(story, "Academic Service and Other Activities")
    section(story, "Academic Service")
    story.append(p("<b>Conference Area Chair:</b> <b>ICLR 2027</b> (invited in early September 2026); <b>ICLR 2026</b>."))
    story.append(p("<b>Conference Reviewer:</b> CVPR, ICCV, ECCV, ICLR, ICML, NeurIPS, AAAI, IJCAI, ICRA, ICASSP, and ACM Multimedia Asia."))
    story.append(p("<b>Journal Reviewer:</b> IEEE TPAMI, IEEE TIP, IEEE TCSVT, IEEE TITS, IEEE RA-L, Science China Information Sciences (SCIS), and IEEE TGRS."))

    section(story, "Invited Talks")
    for text in [
        "<b>Machine Intelligence (Jiqizhixin), 2020:</b> TANet.",
        "<b>Midea Research Institute, 2020:</b> 3D Object Detection in Point Clouds.",
        "<b>3D CVer, 2024:</b> LION.",
        "<b>Shuzihuanyu, 2024:</b> LION and SEED.",
        "<b>The Heart of Autonomous Driving:</b> UniLION and DrivePI.",
        "<b>Huawei Yinwang Intelligent Technology, Nov 2025:</b> a two-hour talk on LION, UniLION, and DrivePI, attended by over 100 researchers.",
    ]:
        bullet(story, text)

    section(story, "Teaching and Community Service")
    bullet(story, "<b>Teaching, 2023:</b> delivered the Multimodal Fusion 3D Object Detection Tutorial for The Heart of Autonomous Driving (more than eight hours).")
    bullet(story, "<b>Volunteer, 2023:</b> China-Africa Text Recognition and Natural Language Processing Innovation Forum.")

    section(story, "Honors and Awards")
    bullet(story, "<b>Fall 2019:</b> Master's National Scholarship, School of Artificial Intelligence and Automation, Huazhong University of Science and Technology.")
    bullet(story, "<b>Spring 2020:</b> NavInfo Scholarship (top 3 among 300+ candidates).")

    section(story, "Patents")
    for text in [
        "<b>Three-dimensional object detection method and system based on weighted channel features of point cloud.</b> Xin Zhao, Kaiqi Huang, <b>Zhe Liu</b>. U.S. patent.",
        "<b>A robust three-dimensional object detection method based on ternary attention mechanism.</b> Xiang Bai, <b>Zhe Liu</b>, Yu Zhou, Tengteng Huang. Chinese patent; granted.",
        "<b>A three-dimensional object detection method, device and system based on DETR structure.</b> Xiang Bai, <b>Zhe Liu</b>, Jinghua Hou. Chinese patent application; submitted.",
        "<b>A three-dimensional object detection method, device and system.</b> Xiang Bai, <b>Zhe Liu</b>, Jinghua Hou, Xinyu Wang, Hengshuang Zhao. Chinese patent application; submitted.",
    ]:
        bullet(story, text, small=True)

    output.parent.mkdir(parents=True, exist_ok=True)
    doc = SimpleDocTemplate(str(output), pagesize=A4, rightMargin=44, leftMargin=44,
                            topMargin=43, bottomMargin=45, title="Zhe Liu - Curriculum Vitae",
                            author="Zhe Liu", subject="Academic curriculum vitae: embodied AI and 3D perception")
    doc.build(story, onFirstPage=footer, onLaterPages=footer)
    print(f"Built {output}: {len(recent)} accepted/published 2026 papers, {len(preprints)} preprints, {len(earlier)} earlier papers.")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, default=ROOT / "output/pdf/cv_zheliu_hku.pdf")
    parser.add_argument("--font-dir", type=Path, default=Path("/System/Library/Fonts/Supplemental"))
    args = parser.parse_args()
    build(args.output, args.font_dir)
