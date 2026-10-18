---
permalink: /
title: ""
excerpt: ""
author_profile: true
redirect_from:
  - /about/
  - /about.html
---

<span class='anchor' id='about-me'></span>

I am a postdoctoral researcher in the Department of Computer Science at The University of Hong Kong, working with Prof. [Hengshuang Zhao](https://hszhao.github.io/). I received my Ph.D. from the School of Electronic Information and Communications at Huazhong University of Science and Technology, supervised by Prof. [Xiang Bai](https://xbai.vlrlab.net/).

I have **eight years of experience in autonomous driving** and **two years in embodied AI**. My current research focuses on **Physical AI** and **embodied foundation models**, spanning vision-language-action (VLA) models, world models, embodied reasoning, and efficient inference for real-world deployment.

<div class="research-focus">
  <div><strong>Physical AI / Embodied Foundation Models</strong><br>Multimodal foundation models, robotic learning, and cross-embodiment generalization.</div>
  <div><strong>VLA / Embodied Reasoning</strong><br>Vision-language-action models, reasoning-to-action, streaming policies, and task execution.</div>
  <div><strong>World / World-Action Models</strong><br>Action-conditioned prediction, physics-aware modeling, simulation, and policy learning.</div>
  <div><strong>Efficient Inference</strong><br>Real-time execution, adaptive test-time computation, and action verification.</div>
</div>

**Job Market:** I am open to private conversations about research and technical leadership opportunities in embodied AI and multimodal foundation models, particularly those involving research direction, core team building, and real-world deployment.

I am also interested in faculty positions at universities, where I can build an independent research group in Physical AI, mentor students, and contribute to teaching in AI and robotics. Please feel free to reach out at [happinesslzcq@gmail.com](mailto:happinesslzcq@gmail.com).

# Research Vision

My long-term goal is to build general-purpose embodied intelligence systems that integrate data, models, simulation, evaluation, and deployment. The current blueprint is organized around embodied data engines, embodied foundation models, 4D world models and simulation, efficient streaming inference, and an intelligent robotic OS for manipulation, navigation, autonomous driving, and cross-embodiment deployment.

<div class="vision-figure">
  <img src="Our_embodied_system.png" alt="Embodied intelligence system overview">
</div>

# News

<div class="news-scroll" role="region" aria-labelledby="news" tabindex="0" markdown="1">

- **Oct 2026:** 🚀 [VeriVLA](#verivla) is released, using latent world models for adaptive test-time verification of flow-based VLA actions.
- **Oct 2026:** 🚀 [Atomic-WAM](#atomic-wam) is released, connecting task reasoning to robotic action through execution-grounded atomic-motion descriptions.
- **Oct 2026:** 🚀 [DVD](#dvd) is released, enabling efficient MLLM-based 2D and 3D perception with dynamic vector decoding.
- **Sep 2026:** 🚀 [PanoVLN](#panovln) is released, exploring effective panoramic vision-and-language navigation.
- **Sep 2026:** 🎉 Six papers are accepted by **NeurIPS 2026**: [StreamPI](#streampi), [Read It Back / SpectraReward](#spectrareward) (**Spotlight ✨**), [EO-WM](#eowm), [FlowR2A](#flowr2a), [FASTER](#faster), and [SRL-MPC](#srlmpc).
- **Early Sep 2026:** 🎉 Invited to serve as an **Area Chair (AC)** for **ICLR 2027**.
- **Aug 2026:** 🚀 [StreamPI](https://happinesslz.github.io/projects/StreamPI/) and [SRL-MPC](https://hanruihua.github.io/srl_mpc_project/) are released.
- **Jul 2026:** 🚀 [Read It Back / SpectraReward](https://huangrh99.github.io/projects/SpectraReward/) is released.
- **Jul 2026:** 🚀 [ACE-Brain-0.5](#ace-brain-05) is released.
- **Jun 2026:** 🎉 [Visual Spatial Tuning](#visual-spatial-tuning) is accepted by **ECCV 2026**.
- **Jun 2026:** [EO-WM](#eowm), [FlowR2A](#flowr2a), [Metis](#metis), and [IR-SIM](#ir-sim) are released.
- **May 2026:** 🎉 [AlphaGRPO](#alphagrpo) is accepted by **ICML 2026**.
- **May 2026:** [MCNav](#mcnav) and [AlphaGRPO](#alphagrpo) are released.
- **Mar 2026:** [FASTER](#faster) and [ACE-Brain-0](#ace-brain-0) are released.
- **Feb 2026:** 🎉 [DrivePI](#drivepi) and [GenieDrive](#geniedrive) are accepted by **CVPR 2026**.
- **Dec 2025:** [DrivePI](#drivepi) and [GenieDrive](#geniedrive) are released.
- **Nov 2025:** [UniLION](#unilion) and [Visual Spatial Tuning](#visual-spatial-tuning) are released.
- **Nov 2025:** Invited to give a talk at Huawei Yinwang Intelligent Technology, with over 100 researchers attending.
- **Sep 2024:** 🎉 [LION](#lion) is accepted by **NeurIPS 2024**.
- **Jul 2024:** 🎉 [SEED](#seed) and [OPEN](#open) are accepted by **ECCV 2024**.
- **Sep 2023:** 🎉 [QTNet](#qtnet) is accepted by **NeurIPS 2023**.
- **Nov 2022:** 🎉 [StereoDistill](#stereodistill) is accepted by **AAAI 2023** and [EPNet++](#epnet-plus-plus) is accepted by **TPAMI**.
- **Nov 2019:** 🎉 [TANet](#tanet) is accepted by **AAAI 2020** as an oral presentation.

</div>

# Publications

I have published 40+ papers in venues including **TPAMI**, **TIP**, **CVPR**, **ICCV**, **ECCV**, **NeurIPS**, **ICML**, **AAAI**, **IROS**, **TITS**, and **ICRA**. [Google Scholar](https://scholar.google.com/citations?hl=en&user=yprv7EsAAAAJ&view_op=list_works&sortby=pubdate) reports 2,603 citations, an h-index of 18, and an i10-index of 22.

Selected publications and recent arXiv preprints are listed below. [Full publication list on Google Scholar](https://scholar.google.com/citations?hl=en&user=yprv7EsAAAAJ&view_op=list_works&sortby=pubdate).

*: Equal contribution, ✉: Corresponding Author, †: Project Leader, ‡: Equal advising.

<div class="publication-browser" id="publication-browser">
  <div class="publication-controls" hidden>
    <div class="publication-topics" role="group" aria-label="Filter publications by research area">
      <button type="button" data-publication-topic="all" aria-pressed="true">All areas</button>

      <button type="button" data-publication-topic="foundation" aria-pressed="false">Embodied Foundation Models &amp; VLA</button>

      <button type="button" data-publication-topic="world" aria-pressed="false">World Models &amp; World-Action Models</button>

      <button type="button" data-publication-topic="reasoning" aria-pressed="false">Embodied Reasoning &amp; Planning</button>

      <button type="button" data-publication-topic="efficient" aria-pressed="false">Efficient Inference &amp; Test-Time Scaling</button>

      <button type="button" data-publication-topic="representation" aria-pressed="false">3D/4D &amp; Multimodal Representation Learning</button>

    </div>
  </div>
  <div class="publication-flat" hidden>
    <header class="publication-group-heading">
      <h2 class="publication-flat-title"></h2>
      <p class="publication-flat-description"></p>
    </header>
    <div class="publication-flat-papers"></div>
  </div>

  <section class="publication-group" data-topic="foundation" aria-labelledby="pub-topic-foundation">
    <header class="publication-group-heading">
      <h2 id="pub-topic-foundation">Embodied Foundation Models &amp; VLA <span class="publication-group-count">6 papers</span></h2>
      <p>General-purpose embodied intelligence through VLA policies, cross-embodiment learning, and multimodal foundation model training and alignment.</p>
    </header>

<div class="paper-box" id="streampi" data-topics="foundation" data-date-order="4">
  <div class='paper-box-image'>
    <div class="paper-image-frame"><div class="badge">NeurIPS 2026</div><img src='projects/StreamPI/StreamPI_files/streampi_intro.png' alt="StreamPI streaming multimodal temporal modeling" loading="lazy"></div>
  </div>
  <div class='paper-box-text'>
    <div class='paper-title'><a href="https://arxiv.org/abs/2608.26067">StreamPI: Streaming Multimodal Temporal Modeling for Vision-Language-Action Models</a></div>
    <div class='paper-authors'><strong>Zhe Liu*</strong>, Jinghua Hou*, Yuxiang Lu, Zhenya Yang, Xianzhe Fan, Junwei Luo, Junyi Li, Ruihua Han, Zhi Hou, Hengshuang Zhao<sup title="Corresponding author">✉</sup></div>
    <div class='paper-venue'><strong>Neural Information Processing Systems (NeurIPS), 2026</strong>.</div>
    <div class='paper-links'><a href="https://happinesslz.github.io/projects/StreamPI/">[Project]</a><a href="https://arxiv.org/abs/2608.26067">[Paper]</a><a href="https://github.com/hku-sail/StreamPI">[Code]</a></div>
    <div class="paper-topics" aria-label="Research areas"><span>Embodied Foundation Models &amp; VLA</span></div>
  </div>
</div>

<div class="paper-box" id="spectrareward" data-topics="foundation" data-date-order="5">
  <div class='paper-box-image'>
    <div class="paper-image-frame"><div class="badge">NeurIPS 2026 · Spotlight ✨</div><img src='images/spectrareward.jpg' alt="SpectraReward overview and training progress" loading="lazy"></div>
  </div>
  <div class='paper-box-text'>
    <div class='paper-title'><a href="https://arxiv.org/abs/2607.11886">Read It Back: Pretrained MLLMs Are Zero-Shot Reward Models for Text-to-Image Generation</a></div>
    <div class='paper-authors'>Runhui Huang, Qihui Zhang, <strong>Zhe Liu</strong>, Yu Gao, Jie Wu, Hengshuang Zhao</div>
    <div class='paper-venue'><strong>Neural Information Processing Systems (NeurIPS), 2026</strong>. <strong>Spotlight ✨</strong>.</div>
    <div class='paper-links'><a href="https://huangrh99.github.io/projects/SpectraReward/">[Project]</a><a href="https://arxiv.org/abs/2607.11886">[Paper]</a><a href="https://github.com/huangrh99/AlphaGRPO">[Code]</a></div>
    <div class="paper-topics" aria-label="Research areas"><span>Embodied Foundation Models &amp; VLA</span></div>
  </div>
</div>

<div class="paper-box" id="ace-brain-05" data-topics="foundation" data-date-order="10">
  <div class='paper-box-image'>
    <div class="paper-image-frame"><div class="badge">arXiv 2026</div><img src='images/acebrain05.png' alt="ACE-Brain-0.5 architecture" loading="lazy"></div>
  </div>
  <div class='paper-box-text'>
    <div class='paper-title'><a href="https://arxiv.org/abs/2607.04426">ACE-Brain-0.5: A Unified Embodied Foundational Model for Physical Agentic AI</a></div>
    <div class='paper-authors'>ACE-Brain Team: Ziyang Gong, Haoming Gu, Zehang Luo, Tianyi Zhang, Tao Tao, Yixiao Chi, <strong>Zhe Liu</strong>, Lingsi Zhu, Jingyuan Liu, Anke Tang, et al.</div>
    <div class='paper-venue'>arXiv preprint, 2026.</div>
    <div class='paper-links'><a href="https://ace-brain-team.github.io/ACE-Brain-0.5/">[Project]</a><a href="https://arxiv.org/abs/2607.04426">[Paper]</a><a href="https://github.com/ACE-BRAIN-Team/ACE-Brain-0.5">[Code]</a></div>
    <div class="paper-topics" aria-label="Research areas"><span>Embodied Foundation Models &amp; VLA</span></div>
  </div>
</div>

<div class="paper-box" id="alphagrpo" data-topics="foundation" data-date-order="14">
  <div class='paper-box-image'>
    <div class="paper-image-frame"><div class="badge">ICML 2026</div><img src='images/alphagrpo.png' alt="AlphaGRPO" loading="lazy"></div>
  </div>
  <div class='paper-box-text'>
    <div class='paper-title'><a href="https://arxiv.org/abs/2605.12495">AlphaGRPO: Unlocking Self-Reflective Multimodal Generation in UMMs via Decompositional Verifiable Reward</a></div>
    <div class='paper-authors'>Runhui Huang, Jie Wu, Rui Yang, <strong>Zhe Liu</strong>, Hengshuang Zhao</div>
    <div class='paper-venue'><strong>International Conference on Machine Learning (ICML), 2026</strong>.</div>
    <div class='paper-links'><a href="https://huangrh99.github.io/AlphaGRPO/">[Project]</a><a href="https://arxiv.org/abs/2605.12495">[Paper]</a><a href="https://github.com/huangrh99/AlphaGRPO">[Code]</a></div>
    <div class="paper-topics" aria-label="Research areas"><span>Embodied Foundation Models &amp; VLA</span></div>
  </div>
</div>

<div class="paper-box" id="ace-brain-0" data-topics="foundation" data-date-order="15">
  <div class='paper-box-image'>
    <div class="paper-image-frame"><div class="badge">arXiv 2026</div><img src='images/acebrain.png' alt="ACE-Brain-0" loading="lazy"></div>
  </div>
  <div class='paper-box-text'>
    <div class='paper-title'><a href="https://arxiv.org/abs/2603.03198">ACE-Brain-0: Spatial Intelligence as a Shared Scaffold for Universal Embodiments</a></div>
    <div class='paper-authors'>Ziyang Gong*, Zehang Luo*, Anke Tang*, <strong>Zhe Liu*</strong>, Shi Fu, Zhi Hou, Ganlin Yang, Weiyun Wang, Xiaofeng Wang, Jianbo Liu, et al.</div>
    <div class='paper-venue'>arXiv preprint, 2026.</div>
    <div class='paper-links'><a href="https://arxiv.org/abs/2603.03198">[Paper]</a></div>
    <div class="paper-topics" aria-label="Research areas"><span>Embodied Foundation Models &amp; VLA</span></div>
  </div>
</div>

<div class="paper-box" id="drivepi" data-topics="foundation reasoning representation" data-date-order="17">
  <div class='paper-box-image'>
    <div class="paper-image-frame"><div class="badge">CVPR 2026</div><img src='images/drivepi.png' alt="DrivePI" loading="lazy"></div>
  </div>
  <div class='paper-box-text'>
    <div class='paper-title'><a href="https://arxiv.org/abs/2512.12799">DrivePI: Spatial-aware 4D MLLM for Unified Autonomous Driving Understanding, Perception, Prediction and Planning</a></div>
    <div class='paper-authors'><strong>Zhe Liu</strong>, Runhui Huang, Rui Yang, Siming Yan, Zining Wang, Lu Hou, Di Lin, Xiang Bai, Hengshuang Zhao<sup title="Corresponding author">✉</sup></div>
    <div class='paper-venue'><strong>Computer Vision and Pattern Recognition (CVPR), 2026</strong>.</div>
    <div class='paper-links'><a href="https://github.com/happinesslz/DrivePI">[Project]</a><a href="https://arxiv.org/abs/2512.12799">[Paper]</a><a href="https://github.com/happinesslz/DrivePI">[Code]</a></div>
    <div class="paper-topics" aria-label="Research areas"><span>Embodied Foundation Models &amp; VLA</span><span>Embodied Reasoning &amp; Planning</span><span>3D/4D &amp; Multimodal Representation Learning</span></div>
  </div>
</div>

  </section>

  <section class="publication-group" data-topic="world" aria-labelledby="pub-topic-world">
    <header class="publication-group-heading">
      <h2 id="pub-topic-world">World Models &amp; World-Action Models <span class="publication-group-count">4 papers</span></h2>
      <p>Action-conditioned world modeling, joint world-action prediction, and physics-aware simulation.</p>
    </header>

<div class="paper-box" id="atomic-wam" data-topics="world foundation reasoning" data-date-order="1">
  <div class='paper-box-image'>
    <div class="paper-image-frame"><div class="badge">arXiv 2026</div><img src='images/atomic-wam.png' alt="Atomic-WAM framework connecting atomic-motion reasoning to joint video and robotic action prediction" style="object-fit: contain;" loading="lazy"></div>
  </div>
  <div class='paper-box-text'>
    <div class='paper-title'><a href="https://arxiv.org/abs/2610.20157">Atomic-WAM: Execution-Grounded Atomic-Motion Reasoning for World Action Models</a></div>
    <div class='paper-authors'>Shijun Shi*, <strong>Zhe Liu*</strong>, Zhi Hou, Yinan Chen, Tao Zhang, Kai Hu<sup title="Equal advising">‡</sup>, Yong Liu, Jiangning Zhang<sup title="Equal advising">‡</sup></div>
    <div class='paper-venue'>arXiv preprint, 2026.</div>
    <div class='paper-links'><a href="https://ssj9596.github.io/Atomic-WAM-project/">[Project]</a><a href="https://arxiv.org/abs/2610.20157">[Paper]</a><a href="https://github.com/ssj9596/Atomic-WAM">[Code]</a></div>
    <div class="paper-topics" aria-label="Research areas"><span>World Models &amp; World-Action Models</span><span>Embodied Foundation Models &amp; VLA</span><span>Embodied Reasoning &amp; Planning</span></div>
  </div>
</div>

<div class="paper-box" id="eowm" data-topics="world" data-date-order="6">
  <div class='paper-box-image'>
    <div class="paper-image-frame"><div class="badge">NeurIPS 2026</div><img src='images/eowm.png' alt="EO-WM architecture" loading="lazy"></div>
  </div>
  <div class='paper-box-text'>
    <div class='paper-title'><a href="https://arxiv.org/abs/2606.27277">EO-WM: A Physically Informed World Model for Probabilistic Earth Observation Forecasting</a></div>
    <div class='paper-authors'>Junwei Luo, Shuai Yuan, Zhenya Yang, Yansheng Li, <strong>Zhe Liu</strong>, Hengshuang Zhao</div>
    <div class='paper-venue'><strong>Neural Information Processing Systems (NeurIPS), 2026</strong>.</div>
    <div class='paper-links'><a href="https://arxiv.org/abs/2606.27277">[Paper]</a><a href="https://github.com/Luo-Z13/EO-WM">[Code]</a></div>
    <div class="paper-topics" aria-label="Research areas"><span>World Models &amp; World-Action Models</span></div>
  </div>
</div>

<div class="paper-box" id="metis" data-topics="world reasoning efficient" data-date-order="11">
  <div class='paper-box-image'>
    <div class="paper-image-frame"><div class="badge">arXiv 2026</div><img src='images/metis.png' alt="Metis architecture" loading="lazy"></div>
  </div>
  <div class='paper-box-text'>
    <div class='paper-title'><a href="https://arxiv.org/abs/2606.15869">Metis: A Generalizable and Efficient World-Action Model for Autonomous Driving and Urban Navigation</a></div>
    <div class='paper-authors'>Jingyu Li*, <strong>Zhe Liu*</strong>, Dongnan Hu, Junjie Wu, Zipei Ma, Wenxiao Wu, Chao Han, Zhihui Hao, Zhikang Liu, Kun Zhan, et al.</div>
    <div class='paper-venue'>arXiv preprint, 2026.</div>
    <div class='paper-links'><a href="https://arxiv.org/abs/2606.15869">[Paper]</a><a href="https://github.com/LogosRoboticsGroup/Metis">[Code]</a></div>
    <div class="paper-topics" aria-label="Research areas"><span>World Models &amp; World-Action Models</span><span>Embodied Reasoning &amp; Planning</span><span>Efficient Inference &amp; Test-Time Scaling</span></div>
  </div>
</div>

<div class="paper-box" id="geniedrive" data-topics="world representation" data-date-order="16">
  <div class='paper-box-image'>
    <div class="paper-image-frame"><div class="badge">CVPR 2026</div><img src='images/geniedrive.png' alt="GenieDrive" loading="lazy"></div>
  </div>
  <div class='paper-box-text'>
    <div class='paper-title'><a href="https://arxiv.org/abs/2512.12751">GenieDrive: Towards Physics-Aware Driving World Model with 4D Occupancy Guided Video Generation</a></div>
    <div class='paper-authors'>Zhenya Yang, <strong>Zhe Liu†</strong>, Yuxiang Lu, Liping Hou, Chenxuan Miao, Siyi Peng, Bailan Feng, Xiang Bai, Hengshuang Zhao<sup title="Corresponding author">✉</sup></div>
    <div class='paper-venue'><strong>Computer Vision and Pattern Recognition (CVPR), 2026</strong>.</div>
    <div class='paper-links'><a href="https://arxiv.org/abs/2512.12751">[Paper]</a><a href="https://github.com/Huster-YZY/GenieDrive">[Code]</a></div>
    <div class="paper-topics" aria-label="Research areas"><span>World Models &amp; World-Action Models</span><span>3D/4D &amp; Multimodal Representation Learning</span></div>
  </div>
</div>

  </section>

  <section class="publication-group" data-topic="reasoning" aria-labelledby="pub-topic-reasoning">
    <header class="publication-group-heading">
      <h2 id="pub-topic-reasoning">Embodied Reasoning &amp; Planning <span class="publication-group-count">6 papers</span></h2>
      <p>Connecting multimodal understanding and memory to navigation, planning, and control.</p>
    </header>

<div class="paper-box" id="panovln" data-topics="reasoning" data-date-order="3">
  <div class='paper-box-image'>
    <div class="paper-image-frame"><div class="badge">arXiv 2026</div><img src='images/panovln.webp' alt="PanoVLN panoramic navigation overview with simulation and real-world examples" loading="lazy"></div>
  </div>
  <div class='paper-box-text'>
    <div class='paper-title'><a href="https://arxiv.org/abs/2609.34759">PanoVLN: Towards Effective Panoramic Vision-and-Language Navigation</a></div>
    <div class='paper-authors'>Zhen Wang, Changpeng Wang, <strong>Zhe Liu</strong>, Zhangyang Qi, Yuxiang Lu, Zimo Zeng, Donglian Qi, Xi Chen</div>
    <div class='paper-venue'>arXiv preprint, 2026.</div>
    <div class='paper-links'><a href="https://wangzhen-w.github.io/PanoVLN/">[Project]</a><a href="https://arxiv.org/abs/2609.34759">[Paper]</a><a href="https://github.com/wangzhen-w/PanoVLN">[Code]</a></div>
    <div class="paper-topics" aria-label="Research areas"><span>Embodied Reasoning &amp; Planning</span></div>
  </div>
</div>

<div class="paper-box" id="flowr2a" data-topics="reasoning" data-date-order="7">
  <div class='paper-box-image'>
    <div class="paper-image-frame"><div class="badge">NeurIPS 2026</div><img src='images/flowr2a.png' alt="FlowR2A architecture" loading="lazy"></div>
  </div>
  <div class='paper-box-text'>
    <div class='paper-title'><a href="https://arxiv.org/abs/2606.24231">FlowR2A: Learning Reward-to-Action Distribution for Multimodal Driving Planning</a></div>
    <div class='paper-authors'>Xirui Li, <strong>Zhe Liu†</strong>, Xiaoqing Ye<sup title="Corresponding author">✉</sup>, Wenhua Han, Yifeng Pan, Junyu Han, Hengshuang Zhao<sup title="Corresponding author">✉</sup></div>
    <div class='paper-venue'><strong>Neural Information Processing Systems (NeurIPS), 2026</strong>.</div>
    <div class='paper-links'><a href="https://lixirui142.github.io/flowr2a-ad/">[Project]</a><a href="https://arxiv.org/abs/2606.24231">[Paper]</a><a href="https://github.com/lixirui142/FlowR2A">[Code]</a></div>
    <div class="paper-topics" aria-label="Research areas"><span>Embodied Reasoning &amp; Planning</span></div>
  </div>
</div>

<div class="paper-box" id="srlmpc" data-topics="reasoning" data-date-order="9">
  <div class='paper-box-image'>
    <div class="paper-image-frame"><div class="badge">NeurIPS 2026</div><img src='images/srlmpc.png' alt="SRL-MPC shape-aware reinforcement learned model predictive control architecture" loading="lazy"></div>
  </div>
  <div class='paper-box-text'>
    <div class='paper-title'><a href="https://arxiv.org/abs/2608.21175">SRL-MPC: Shape-Aware Reinforcement Learned Model Predictive Control</a></div>
    <div class='paper-authors'>Ruihua Han, Rui Gao, <strong>Zhe Liu</strong>, Xinyi Wang, Chang Chen, Shuai Wang, Qi Hao, Jia Pan, Hengshuang Zhao</div>
    <div class='paper-venue'><strong>Neural Information Processing Systems (NeurIPS), 2026</strong>.</div>
    <div class='paper-links'><a href="https://hanruihua.github.io/srl_mpc_project/">[Project]</a><a href="https://arxiv.org/abs/2608.21175">[Paper]</a><a href="https://github.com/hku-sail/srl_mpc">[Code (coming soon)]</a></div>
    <div class="paper-topics" aria-label="Research areas"><span>Embodied Reasoning &amp; Planning</span></div>
  </div>
</div>

<div class="paper-box" id="ir-sim" data-topics="reasoning" data-date-order="12">
  <div class='paper-box-image'>
    <div class="paper-image-frame"><div class="badge">arXiv 2026</div><img src='images/irsim.png' alt="IR-SIM system workflow" loading="lazy"></div>
  </div>
  <div class='paper-box-text'>
    <div class='paper-title'><a href="https://arxiv.org/abs/2606.08729">IR-SIM: A Lightweight Skill-Native Simulator for Navigation, Learning, and Benchmarking</a></div>
    <div class='paper-authors'>Ruihua Han, Shuai Wang, Chengyang Li, Rui Gao, Xinyi Wang, <strong>Zhe Liu</strong>, Guoliang Li, Yupu Lu, Qi Hao, Jia Pan, Hengshuang Zhao</div>
    <div class='paper-venue'>arXiv preprint, 2026.</div>
    <div class='paper-links'><a href="https://arxiv.org/abs/2606.08729">[Paper]</a><a href="https://github.com/hanruihua/ir-sim">[Code]</a></div>
    <div class="paper-topics" aria-label="Research areas"><span>Embodied Reasoning &amp; Planning</span></div>
  </div>
</div>

<div class="paper-box" id="mcnav" data-topics="reasoning" data-date-order="13">
  <div class='paper-box-image'>
    <div class="paper-image-frame"><div class="badge">arXiv 2026</div><img src='images/mcnav.png' alt="MCNav" loading="lazy"></div>
  </div>
  <div class='paper-box-text'>
    <div class='paper-title'><a href="https://arxiv.org/abs/2605.19594">MCNav: Memory-Aware Dynamic Cognitive Map for Zero-shot Goal-oriented Navigation</a></div>
    <div class='paper-authors'>Jingyu Li*, <strong>Zhe Liu*</strong>, Wenxiao Wu, Li Zhang</div>
    <div class='paper-venue'>arXiv preprint, 2026.</div>
    <div class='paper-links'><a href="https://arxiv.org/abs/2605.19594">[Paper]</a></div>
    <div class="paper-topics" aria-label="Research areas"><span>Embodied Reasoning &amp; Planning</span></div>
  </div>
</div>

<div class="paper-box" id="unilion" data-topics="reasoning representation" data-date-order="20">
  <div class='paper-box-image'>
    <div class="paper-image-frame"><div class="badge">arXiv 2025</div><img src='images/UniLION.png' alt="UniLION" loading="lazy"></div>
  </div>
  <div class='paper-box-text'>
    <div class='paper-title'><a href="https://arxiv.org/abs/2511.01768">UniLION: Towards Unified Autonomous Driving Model with Linear Group RNNs</a></div>
    <div class='paper-authors'><strong>Zhe Liu</strong>, Jinghua Hou, Xiaoqing Ye, Jingdong Wang, Hengshuang Zhao<sup title="Corresponding author">✉</sup>, Xiang Bai<sup title="Corresponding author">✉</sup></div>
    <div class='paper-venue'>arXiv preprint, 2025.</div>
    <div class='paper-links'><a href="https://github.com/happinesslz/UniLION">[Project]</a><a href="https://arxiv.org/abs/2511.01768">[Paper]</a><a href="https://github.com/happinesslz/UniLION">[Code]</a></div>
    <div class="paper-topics" aria-label="Research areas"><span>Embodied Reasoning &amp; Planning</span><span>3D/4D &amp; Multimodal Representation Learning</span></div>
  </div>
</div>

  </section>

  <section class="publication-group" data-topic="efficient" aria-labelledby="pub-topic-efficient">
    <header class="publication-group-heading">
      <h2 id="pub-topic-efficient">Efficient Inference &amp; Test-Time Scaling <span class="publication-group-count">3 papers</span></h2>
      <p>Real-time model execution through compact decoding, adaptive computation, and test-time verification.</p>
    </header>

<div class="paper-box" id="verivla" data-topics="efficient foundation world" data-date-order="0">
  <div class='paper-box-image'>
    <div class="paper-image-frame"><div class="badge">arXiv 2026</div><img src='images/verivla.webp' alt="VeriVLA identifies high-variance action states and adaptively triggers additional sampling and verification" style="object-fit: contain;" loading="lazy"></div>
  </div>
  <div class='paper-box-text'>
    <div class='paper-title'><a href="https://arxiv.org/abs/2610.21985">VeriVLA: Adaptive Test-Time Verification for Flow-Based VLAs with Latent World Models</a></div>
    <div class='paper-authors'>Xueli Sun, Yuxiang Lu, Yantong Liu, Xianzhe Fan, Xi Chen, <strong>Zhe Liu†</strong>, Hengshuang Zhao<sup title="Corresponding author">✉</sup></div>
    <div class='paper-venue'>arXiv preprint, 2026.</div>
    <div class='paper-links'><a href="https://shirley430316.github.io/projects/verivla/">[Project]</a><a href="https://arxiv.org/abs/2610.21985">[Paper]</a><a href="https://github.com/shirley430316/VeriVLA">[Code]</a></div>
    <div class="paper-topics" aria-label="Research areas"><span>Efficient Inference &amp; Test-Time Scaling</span><span>Embodied Foundation Models &amp; VLA</span><span>World Models &amp; World-Action Models</span></div>
  </div>
</div>

<div class="paper-box" id="dvd" data-topics="efficient representation" data-date-order="2">
  <div class='paper-box-image'>
    <div class="paper-image-frame"><div class="badge">arXiv 2026</div><img src='images/dvd.png' alt="DVD dynamic vector decoding overview for efficient 2D and 3D perception" loading="lazy"></div>
  </div>
  <div class='paper-box-text'>
    <div class='paper-title'><a href="https://arxiv.org/abs/2610.12266">DVD: Dynamic Vector Decoding for Efficient MLLM-based Perception</a></div>
    <div class='paper-authors'>Jinghua Hou, <strong>Zhe Liu†</strong>, Hengshuang Zhao<sup title="Corresponding author">✉</sup></div>
    <div class='paper-venue'>arXiv preprint, 2026.</div>
    <div class='paper-links'><a href="https://almoonysl.github.io/projects/DVD/">[Project]</a><a href="https://arxiv.org/abs/2610.12266">[Paper]</a><a href="https://github.com/AlmoonYsl/DVD">[Code]</a></div>
    <div class="paper-topics" aria-label="Research areas"><span>Efficient Inference &amp; Test-Time Scaling</span><span>3D/4D &amp; Multimodal Representation Learning</span></div>
  </div>
</div>

<div class="paper-box" id="faster" data-topics="efficient foundation" data-date-order="8">
  <div class='paper-box-image'>
    <div class="paper-image-frame"><div class="badge">NeurIPS 2026</div><img src='images/faster.png' alt="FASTER" loading="lazy"></div>
  </div>
  <div class='paper-box-text'>
    <div class='paper-title'><a href="https://arxiv.org/abs/2603.19199">FASTER: Rethinking Real-Time Flow VLAs</a></div>
    <div class='paper-authors'>Yuxiang Lu, <strong>Zhe Liu†</strong>, Xianzhe Fan, Zhenya Yang, Jinghua Hou, Junyi Li, Kaixin Ding, Hengshuang Zhao</div>
    <div class='paper-venue'><strong>Neural Information Processing Systems (NeurIPS), 2026</strong>.</div>
    <div class='paper-links'><a href="https://innovator-zero.github.io/FASTER/">[Project]</a><a href="https://arxiv.org/abs/2603.19199">[Paper]</a><a href="https://github.com/innovator-zero/FASTER">[Code]</a></div>
    <div class="paper-topics" aria-label="Research areas"><span>Efficient Inference &amp; Test-Time Scaling</span><span>Embodied Foundation Models &amp; VLA</span></div>
  </div>
</div>

  </section>

  <section class="publication-group" data-topic="representation" aria-labelledby="pub-topic-representation">
    <header class="publication-group-heading">
      <h2 id="pub-topic-representation">3D/4D &amp; Multimodal Representation Learning <span class="publication-group-count">19 papers</span></h2>
      <p>Learning spatial, spatiotemporal, and cross-modal representations for scene understanding and embodied intelligence.</p>
    </header>

<div class="paper-box" id="geoteacher" data-topics="representation" data-date-order="18">
  <div class='paper-box-image'>
    <div class="paper-image-frame"><div class="badge">ICRA 2026</div><img src='images/geoteacher.png' alt="GeoTeacher" loading="lazy"></div>
  </div>
  <div class='paper-box-text'>
    <div class='paper-title'><a href="https://arxiv.org/abs/2512.23147">GeoTeacher: Geometry-Guided Semi-Supervised 3D Object Detection</a></div>
    <div class='paper-authors'>Jingyu Li, Xiaolong Zhao, <strong>Zhe Liu</strong>, Wenxiao Wu, Li Zhang</div>
    <div class='paper-venue'><strong>International Conference on Robotics and Automation (ICRA), 2026</strong>.</div>
    <div class='paper-links'><a href="https://arxiv.org/abs/2512.23147">[Paper]</a><a href="https://github.com/SII-Whaleice/GeoTeacher">[Code]</a></div>
    <div class="paper-topics" aria-label="Research areas"><span>3D/4D &amp; Multimodal Representation Learning</span></div>
  </div>
</div>

<div class="paper-box" id="visual-spatial-tuning" data-topics="representation" data-date-order="19">
  <div class='paper-box-image'>
    <div class="paper-image-frame"><div class="badge">ECCV 2026</div><img src='images/vst.png' alt="Visual Spatial Tuning" loading="lazy"></div>
  </div>
  <div class='paper-box-text'>
    <div class='paper-title'><a href="https://arxiv.org/abs/2511.05491">Visual Spatial Tuning</a></div>
    <div class='paper-authors'>Rui Yang, Ziyu Zhu, Yanwei Li, Jingjia Huang, Shen Yan, Siyuan Zhou, <strong>Zhe Liu</strong>, Xiangtai Li, Shuangye Li, Wenqian Wang, Yi Lin, Hengshuang Zhao</div>
    <div class='paper-venue'><strong>European Conference on Computer Vision (ECCV), 2026</strong>.</div>
    <div class='paper-links'><a href="https://arxiv.org/abs/2511.05491">[Paper]</a></div>
    <div class="paper-topics" aria-label="Research areas"><span>3D/4D &amp; Multimodal Representation Learning</span></div>
  </div>
</div>

<div class="paper-box" id="dac" data-topics="representation" data-date-order="21">
  <div class='paper-box-image'>
    <div class="paper-image-frame"><div class="badge">ICCV 2025</div><img src='images/dac.png' alt="DAC" loading="lazy"></div>
  </div>
  <div class='paper-box-text'>
    <div class='paper-title'><a href="https://openaccess.thecvf.com/content/ICCV2025/html/Wang_Describe_Adapt_and_Combine_Empowering_CLIP_Encoders_for_Open-set_3D_ICCV_2025_paper.html">Describe, Adapt and Combine: Empowering CLIP Encoders for Open-set 3D Object Retrieval</a></div>
    <div class='paper-authors'>Zhichuan Wang, Yang Zhou, <strong>Zhe Liu</strong>, Rui Yu, Song Bai, Yulong Wang, Xinwei He, Xiang Bai</div>
    <div class='paper-venue'><strong>International Conference on Computer Vision (ICCV), 2025</strong>.</div>
    <div class='paper-links'><a href="https://openaccess.thecvf.com/content/ICCV2025/html/Wang_Describe_Adapt_and_Combine_Empowering_CLIP_Encoders_for_Open-set_3D_ICCV_2025_paper.html">[Paper]</a><a href="https://github.com/wangzhichuan123/DAC">[Code]</a></div>
    <div class="paper-topics" aria-label="Research areas"><span>3D/4D &amp; Multimodal Representation Learning</span></div>
  </div>
</div>

<div class="paper-box" id="hybridtm" data-topics="representation" data-date-order="22">
  <div class='paper-box-image'>
    <div class="paper-image-frame"><div class="badge">IROS 2025</div><img src='images/hybridtm.png' alt="HybridTM" loading="lazy"></div>
  </div>
  <div class='paper-box-text'>
    <div class='paper-title'><a href="https://arxiv.org/abs/2507.18575">HybridTM: Combining Transformer and Mamba for 3D Semantic Segmentation</a></div>
    <div class='paper-authors'>Xinyu Wang, Jinghua Hou, <strong>Zhe Liu</strong>, Yingying Zhu</div>
    <div class='paper-venue'><strong>IEEE/RSJ International Conference on Intelligent Robots and Systems (IROS), 2025</strong>.</div>
    <div class='paper-links'><a href="https://arxiv.org/abs/2507.18575">[Paper]</a><a href="https://github.com/deepinact/HybridTM">[Code]</a></div>
    <div class="paper-topics" aria-label="Research areas"><span>3D/4D &amp; Multimodal Representation Learning</span></div>
  </div>
</div>

<div class="paper-box" id="lion" data-topics="representation" data-date-order="24">
  <div class='paper-box-image'>
    <div class="paper-image-frame"><div class="badge">NeurIPS 2024</div><img src='images/lion.png' alt="LION" loading="lazy"></div>
  </div>
  <div class='paper-box-text'>
    <div class='paper-title'><a href="https://arxiv.org/abs/2407.18232">LION: Linear Group RNN for 3D Object Detection in Point Clouds</a></div>
    <div class='paper-authors'><strong>Zhe Liu*</strong>, Jinghua Hou*, Xingyu Wang, Xiaoqing Ye, Jingdong Wang, Hengshuang Zhao, Xiang Bai</div>
    <div class='paper-venue'><strong>Neural Information Processing Systems (NeurIPS), 2024</strong>.</div>
    <div class='paper-links'><a href="https://happinesslz.github.io/projects/LION/">[Project]</a><a href="https://arxiv.org/abs/2407.18232">[Paper]</a><a href="https://github.com/happinesslz/LION">[Code]</a></div>
    <div class="paper-topics" aria-label="Research areas"><span>3D/4D &amp; Multimodal Representation Learning</span></div>
  </div>
</div>

<div class="paper-box" id="seed" data-topics="representation" data-date-order="25">
  <div class='paper-box-image'>
    <div class="paper-image-frame"><div class="badge">ECCV 2024</div><img src='images/seed.png' alt="SEED" loading="lazy"></div>
  </div>
  <div class='paper-box-text'>
    <div class='paper-title'><a href="https://arxiv.org/pdf/2407.10749">SEED: A Simple and Effective 3D DETR in Point Clouds</a></div>
    <div class='paper-authors'><strong>Zhe Liu*</strong>, Jinghua Hou*, Xiaoqing Ye, Tong Wang, Jingdong Wang, Xiang Bai</div>
    <div class='paper-venue'><strong>European Conference on Computer Vision (ECCV), 2024</strong>.</div>
    <div class='paper-links'><a href="https://arxiv.org/pdf/2407.10749">[Paper]</a><a href="https://github.com/happinesslz/SEED">[Code]</a></div>
    <div class="paper-topics" aria-label="Research areas"><span>3D/4D &amp; Multimodal Representation Learning</span></div>
  </div>
</div>

<div class="paper-box" id="open" data-topics="representation" data-date-order="26">
  <div class='paper-box-image'>
    <div class="paper-image-frame"><div class="badge">ECCV 2024</div><img src='images/open.jpg' alt="OPEN" loading="lazy"></div>
  </div>
  <div class='paper-box-text'>
    <div class='paper-title'><a href="https://arxiv.org/pdf/2407.10753">OPEN: Object-wise Position Embedding for Multi-view 3D Object Detection</a></div>
    <div class='paper-authors'>Jinghua Hou, Tong Wang, Xiaoqing Ye, <strong>Zhe Liu</strong>, Shi Gong, Xiao Tan, Errui Ding, Jingdong Wang, Xiang Bai</div>
    <div class='paper-venue'><strong>European Conference on Computer Vision (ECCV), 2024</strong>.</div>
    <div class='paper-links'><a href="https://arxiv.org/pdf/2407.10753">[Paper]</a><a href="https://github.com/AlmoonYsl/OPEN">[Code]</a></div>
    <div class="paper-topics" aria-label="Research areas"><span>3D/4D &amp; Multimodal Representation Learning</span></div>
  </div>
</div>

<div class="paper-box" id="fbmnet" data-topics="representation" data-date-order="27">
  <div class='paper-box-image'>
    <div class="paper-image-frame"><div class="badge">TITS 2024</div><img src='images/fbmnet.png' alt="FBMNet" loading="lazy"></div>
  </div>
  <div class='paper-box-text'>
    <div class='paper-title'><a href="https://arxiv.org/pdf/2305.07713">Multi-Modal 3D Object Detection by Box Matching</a></div>
    <div class='paper-authors'><strong>Zhe Liu</strong>, Xiaoqing Ye, Zhikang Zou, Xinwei He, Xiao Tan, Errui Ding, Jingdong Wang, Xiang Bai</div>
    <div class='paper-venue'><strong>IEEE Transactions on Intelligent Transportation Systems (TITS), 2024</strong>.</div>
    <div class='paper-links'><a href="https://arxiv.org/pdf/2305.07713">[Paper]</a><a href="https://github.com/happinesslz/FBMNet">[Code]</a></div>
    <div class="paper-topics" aria-label="Research areas"><span>3D/4D &amp; Multimodal Representation Learning</span></div>
  </div>
</div>

<!-- https://doi.org/10.1007/s11432-023-3943-6; figure: arXiv:2306.02245, Figure 1(a) -->
<div class="paper-box" id="sam3d" data-topics="representation" data-date-order="28">
  <div class='paper-box-image'>
    <div class="paper-image-frame"><div class="badge">SCIS 2024</div><img src='images/sam3d.png' alt="SAM3D pipeline adapting Segment Anything to bird’s-eye-view images for zero-shot object detection" loading="lazy"></div>
  </div>
  <div class='paper-box-text'>
    <div class='paper-title'><a href="https://arxiv.org/abs/2306.02245">SAM3D: Zero-Shot 3D Object Detection via the Segment Anything Model</a></div>
    <div class='paper-authors'>Dingyuan Zhang, Dingkang Liang, Hongcheng Yang, Zhikang Zou, Xiaoqing Ye, <strong>Zhe Liu</strong>, Xiang Bai<sup title="Corresponding author">✉</sup></div>
    <div class='paper-venue'><strong>Science China Information Sciences (SCIS), 2024</strong>.</div>
    <div class='paper-links'><a href="https://arxiv.org/abs/2306.02245">[Paper]</a><a href="https://github.com/DYZhang09/SAM3D">[Code]</a></div>
    <div class="paper-topics" aria-label="Research areas"><span>3D/4D &amp; Multimodal Representation Learning</span></div>
  </div>
</div>

<div class="paper-box" id="qtnet" data-topics="representation" data-date-order="29">
  <div class='paper-box-image'>
    <div class="paper-image-frame"><div class="badge">NeurIPS 2023</div><img src='images/qtnet.png' alt="QTNet" loading="lazy"></div>
  </div>
  <div class='paper-box-text'>
    <div class='paper-title'><a href="https://openreview.net/pdf?id=gySmwdmVDF">Query-based Temporal Fusion with Explicit Motion for 3D Object Detection</a></div>
    <div class='paper-authors'>Jinghua Hou*, <strong>Zhe Liu*</strong>, Dingkang Liang, Zhikang Zou, Xiaoqing Ye, Xiang Bai</div>
    <div class='paper-venue'><strong>Neural Information Processing Systems (NeurIPS), 2023</strong>.</div>
    <div class='paper-links'><a href="https://openreview.net/pdf?id=gySmwdmVDF">[Paper]</a><a href="https://github.com/AlmoonYsl/QTNet">[Code]</a></div>
    <div class="paper-topics" aria-label="Research areas"><span>3D/4D &amp; Multimodal Representation Learning</span></div>
  </div>
</div>

<!-- arXiv:2401.15319, accepted August 2023; figure: Figure 2 -->
<div class="paper-box" id="yolobu" data-topics="representation" data-date-order="30">
  <div class='paper-box-image'>
    <div class="paper-image-frame"><div class="badge">RA-L 2023</div><img src='images/yolobu.png' alt="YOLOBU architecture with column-based cross attention and row-based reverse cumulative sum" loading="lazy"></div>
  </div>
  <div class='paper-box-text'>
    <div class='paper-title'><a href="https://arxiv.org/abs/2401.15319">You Only Look Bottom-Up for Monocular 3D Object Detection</a></div>
    <div class='paper-authors'>Kaixin Xiong*, Dingyuan Zhang*, Dingkang Liang, <strong>Zhe Liu</strong>, Hongcheng Yang, Wondimu Dikubab, Jianwei Cheng, Xiang Bai<sup title="Corresponding author">✉</sup></div>
    <div class='paper-venue'><strong>IEEE Robotics and Automation Letters (RA-L), 2023</strong>.</div>
    <div class='paper-links'><a href="https://arxiv.org/abs/2401.15319">[Paper]</a></div>
    <div class="paper-topics" aria-label="Research areas"><span>3D/4D &amp; Multimodal Representation Learning</span></div>
  </div>
</div>

<div class="paper-box" id="wss3d" data-topics="representation" data-date-order="31">
  <div class='paper-box-image'>
    <div class="paper-image-frame"><div class="badge">ICCV 2023</div><img src='images/wss3d.jpg' alt="WSS3D" loading="lazy"></div>
  </div>
  <div class='paper-box-text'>
    <div class='paper-title'><a href="https://openaccess.thecvf.com/content/ICCV2023/papers/Zhang_A_Simple_Vision_Transformer_for_Weakly_Semi-supervised_3D_Object_Detection_ICCV_2023_paper.pdf">A Simple Vision Transformer for Weakly Semi-supervised 3D Object Detection</a></div>
    <div class='paper-authors'>Dingyuan Zhang*, Dingkang Liang*, Zhikang Zou*, Jingyu Li, Xiaoqing Ye, <strong>Zhe Liu</strong>, Xiao Tan, Xiang Bai</div>
    <div class='paper-venue'><strong>International Conference on Computer Vision (ICCV), 2023</strong>.</div>
    <div class='paper-links'><a href="https://openaccess.thecvf.com/content/ICCV2023/papers/Zhang_A_Simple_Vision_Transformer_for_Weakly_Semi-supervised_3D_Object_Detection_ICCV_2023_paper.pdf">[Paper]</a></div>
    <div class="paper-topics" aria-label="Research areas"><span>3D/4D &amp; Multimodal Representation Learning</span></div>
  </div>
</div>

<div class="paper-box" id="dds3d" data-topics="representation" data-date-order="32">
  <div class='paper-box-image'>
    <div class="paper-image-frame"><div class="badge">ICRA 2023</div><img src='images/dds3d.png' alt="DDS3D" loading="lazy"></div>
  </div>
  <div class='paper-box-text'>
    <div class='paper-title'><a href="https://arxiv.org/pdf/2303.05079">DDS3D: Dense Pseudo-Labels with Dynamic Threshold for Semi-Supervised 3D Object Detection</a></div>
    <div class='paper-authors'>Jingyu Li*, <strong>Zhe Liu*</strong>, Jinghua Hou, Dingkang Liang</div>
    <div class='paper-venue'><strong>International Conference on Robotics and Automation (ICRA), 2023</strong>.</div>
    <div class='paper-links'><a href="https://arxiv.org/pdf/2303.05079">[Paper]</a><a href="https://github.com/Whale-ice/DDS3D">[Code]</a></div>
    <div class="paper-topics" aria-label="Research areas"><span>3D/4D &amp; Multimodal Representation Learning</span></div>
  </div>
</div>

<div class="paper-box" id="stereodistill" data-topics="representation" data-date-order="33">
  <div class='paper-box-image'>
    <div class="paper-image-frame"><div class="badge">AAAI 2023</div><img src='images/stereo_distill.png' alt="StereoDistill" loading="lazy"></div>
  </div>
  <div class='paper-box-text'>
    <div class='paper-title'><a href="https://ojs.aaai.org/index.php/AAAI/article/download/25268/25040">StereoDistill: Pick the Cream from LiDAR for Distilling Stereo-based 3D Object Detection</a></div>
    <div class='paper-authors'><strong>Zhe Liu</strong>, Xiaoqing Ye, Xiao Tan, Errui Ding, Xiang Bai</div>
    <div class='paper-venue'><strong>AAAI Conference on Artificial Intelligence (AAAI), 2023</strong>.</div>
    <div class='paper-links'><a href="https://ojs.aaai.org/index.php/AAAI/article/download/25268/25040">[Paper]</a></div>
    <div class="paper-topics" aria-label="Research areas"><span>3D/4D &amp; Multimodal Representation Learning</span></div>
  </div>
</div>

<div class="paper-box" id="epnet-plus-plus" data-topics="representation" data-date-order="34">
  <div class='paper-box-image'>
    <div class="paper-image-frame"><div class="badge">TPAMI 2022</div><img src='images/epnet++.png' alt="EPNet++" loading="lazy"></div>
  </div>
  <div class='paper-box-text'>
    <div class='paper-title'><a href="https://arxiv.org/pdf/2112.11088">EPNet++: Cascade Bi-directional Fusion for Multi-Modal 3D Object Detection</a></div>
    <div class='paper-authors'><strong>Zhe Liu</strong>, Tengteng Huang, Bingling Li, Xiwu Chen, Xi Wang, Xiang Bai</div>
    <div class='paper-venue'><strong>IEEE Transactions on Pattern Analysis and Machine Intelligence (TPAMI), 2022</strong>.</div>
    <div class='paper-links'><a href="https://arxiv.org/pdf/2112.11088">[Paper]</a><a href="https://github.com/happinesslz/EPNetV2">[Code]</a></div>
    <div class="paper-topics" aria-label="Research areas"><span>3D/4D &amp; Multimodal Representation Learning</span></div>
  </div>
</div>

<!-- https://doi.org/10.1109/TIP.2021.3072214; figure: arXiv:2112.04903, Figure 1 -->
<div class="paper-box" id="pranet" data-topics="representation" data-date-order="35">
  <div class='paper-box-image'>
    <div class="paper-image-frame"><div class="badge">TIP 2021</div><img src='images/pranet.png' alt="PRA-Net intra-region structure learning with local and global point features" loading="lazy"></div>
  </div>
  <div class='paper-box-text'>
    <div class='paper-title'><a href="https://arxiv.org/abs/2112.04903">PRA-Net: Point Relation-Aware Network for 3D Point Cloud Analysis</a></div>
    <div class='paper-authors'>Silin Cheng*, Xiwu Chen*, Xinwei He, <strong>Zhe Liu</strong>, Xiang Bai<sup title="Corresponding author">✉</sup></div>
    <div class='paper-venue'><strong>IEEE Transactions on Image Processing (TIP), 2021</strong>.</div>
    <div class='paper-links'><a href="https://arxiv.org/abs/2112.04903">[Paper]</a><a href="https://github.com/XiwuChen/PRA-Net">[Code]</a></div>
    <div class="paper-topics" aria-label="Research areas"><span>3D/4D &amp; Multimodal Representation Learning</span></div>
  </div>
</div>

<div class="paper-box" id="epnet" data-topics="representation" data-date-order="36">
  <div class='paper-box-image'>
    <div class="paper-image-frame"><div class="badge">ECCV 2020</div><img src='images/epnet.png' alt="EPNet" loading="lazy"></div>
  </div>
  <div class='paper-box-text'>
    <div class='paper-title'><a href="https://arxiv.org/pdf/2007.08856">EPNet: Enhancing Point Features with Image Semantics for 3D Object Detection</a></div>
    <div class='paper-authors'>Tengteng Huang*, <strong>Zhe Liu*</strong>, Xiwu Chen, Xiang Bai</div>
    <div class='paper-venue'><strong>European Conference on Computer Vision (ECCV), 2020</strong>.</div>
    <div class='paper-links'><a href="https://arxiv.org/pdf/2007.08856">[Paper]</a><a href="https://github.com/happinesslz/EPNet">[Code]</a></div>
    <div class="paper-topics" aria-label="Research areas"><span>3D/4D &amp; Multimodal Representation Learning</span></div>
  </div>
</div>

<div class="paper-box" id="tanet" data-topics="representation" data-date-order="37">
  <div class='paper-box-image'>
    <div class="paper-image-frame"><div class="badge">AAAI 2020</div><img src='images/tanet.jpg' alt="TANet" loading="lazy"></div>
  </div>
  <div class='paper-box-text'>
    <div class='paper-title'><a href="https://arxiv.org/pdf/1912.05163">TANet: Robust 3D Object Detection from Point Clouds with Triple Attention</a></div>
    <div class='paper-authors'><strong>Zhe Liu</strong>, Xin Zhao, Tengteng Huang, Ruolan Hu, Yu Zhou, Xiang Bai</div>
    <div class='paper-venue'><strong>AAAI Conference on Artificial Intelligence (AAAI), 2020</strong>. Oral presentation.</div>
    <div class='paper-links'><a href="https://arxiv.org/pdf/1912.05163">[Paper]</a><a href="https://github.com/happinesslz/TANet">[Code]</a></div>
    <div class="paper-topics" aria-label="Research areas"><span>3D/4D &amp; Multimodal Representation Learning</span></div>
  </div>
</div>

<div class="paper-box" id="sifrnet" data-topics="representation" data-date-order="38">
  <div class='paper-box-image'>
    <div class="paper-image-frame"><div class="badge">AAAI 2019</div><img src='images/SIFRNet.png' alt="SIFRNet" loading="lazy"></div>
  </div>
  <div class='paper-box-text'>
    <div class='paper-title'><a href="https://arxiv.org/abs/1901.02237">3D Object Detection Using Scale Invariant and Feature Reweighting Networks</a></div>
    <div class='paper-authors'>Xin Zhao, <strong>Zhe Liu<sup title="Corresponding author">✉</sup></strong>, Ruolan Hu, Kaiqi Huang</div>
    <div class='paper-venue'><strong>AAAI Conference on Artificial Intelligence (AAAI), 2019</strong>.</div>
    <div class='paper-links'><a href="https://arxiv.org/abs/1901.02237">[Paper]</a></div>
    <div class="paper-topics" aria-label="Research areas"><span>3D/4D &amp; Multimodal Representation Learning</span></div>
  </div>
</div>

  </section>

</div>

<script src="{{ "/assets/js/publications.js" | relative_url }}" defer></script>

# Professional Service

- **Conference Area Chair:** **ICLR 2027**, **ICLR 2026**.
- **Conference Reviewer:** **CVPR**, **ICCV**, **ECCV**, **ICLR**, **ICML**, **NeurIPS**, **AAAI**, **IJCAI**, **ICRA**, **ICASSP**, **ACM Multimedia Asia**.
- **Journal Reviewer:** **TPAMI**, **TIP**, **TCSVT**, **TITS**, **RA-L**, **SCIS**, **TGRS**.
- **Invited Talks:** Machine Intelligence, Midea Research Institute, 3D CVer, Shuzihuanyu, The Heart of Autonomous Driving, and Huawei Yinwang Intelligent Technology.

# Industry Collaborations

I have previously collaborated with the following companies and research teams.

<ul class="collaboration-grid">
{% for company in site.data.industry_collaborations %}
  <li>
    <a class="collaboration-card" href="{{ company.url }}" target="_blank" rel="noopener noreferrer" style="--company-accent: {{ company.accent }}; --company-tint: {{ company.tint }};">
      <span class="collaboration-arrow" aria-hidden="true">↗</span>
      <span class="collaboration-logo {{ company.logo_class }}"><img src="{{ company.logo | relative_url }}" alt="" loading="lazy" decoding="async"></span>
      <span class="collaboration-name">{{ company.name }}</span>
      <span class="collaboration-name-zh" lang="zh-CN">{{ company.name_zh }}</span>
    </a>
  </li>
{% endfor %}
</ul>

# Contact

- **Email:** [happinesslzcq@gmail.com](mailto:happinesslzcq@gmail.com)
- **CV:** [Download CV](data/cv_zheliu_hku.pdf)
- **Google Scholar:** [Profile](https://scholar.google.com/citations?hl=zh-CN&user=yprv7EsAAAAJ&view_op=list_works)
- **GitHub:** [happinesslz](https://github.com/happinesslz/)
