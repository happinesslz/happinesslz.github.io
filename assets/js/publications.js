(function () {
  "use strict";

  var root = document.getElementById("publication-browser");
  if (!root) return;

  var groups = Array.from(root.querySelectorAll(".publication-group"));
  var cards = Array.from(root.querySelectorAll(".paper-box")).map(function (card) {
    return {
      element: card,
      home: card.closest(".publication-group"),
      topics: card.dataset.topics.split(" "),
      order: Number(card.dataset.dateOrder)
    };
  }).sort(function (a, b) { return a.order - b.order; });
  var flat = root.querySelector(".publication-flat");
  var flatPapers = root.querySelector(".publication-flat-papers");
  var topicButtons = Array.from(root.querySelectorAll("[data-publication-topic]"));
  var topic = "all";

  function render() {
    // Keep one DOM node per paper so existing News links and paper IDs stay valid.
    cards.forEach(function (card) { card.home.appendChild(card.element); });
    var grouped = topic === "all";
    groups.forEach(function (group) { group.hidden = !grouped; });
    flat.hidden = grouped;

    var visible = cards.filter(function (card) {
      return topic === "all" || card.topics.includes(topic);
    });

    if (!grouped) {
      visible.forEach(function (card) { flatPapers.appendChild(card.element); });
      var group = groups.find(function (item) { return item.dataset.topic === topic; });
      root.querySelector(".publication-flat-title").textContent = group
        ? group.querySelector("h2").firstChild.textContent.trim()
        : "All Publications";
      root.querySelector(".publication-flat-description").textContent = group
        ? group.querySelector(".publication-group-heading p").textContent
        : "Latest publications first.";
    }

    topicButtons.forEach(function (button) {
      button.setAttribute("aria-pressed", String(button.dataset.publicationTopic === topic));
    });
  }

  topicButtons.forEach(function (button) {
    button.addEventListener("click", function () {
      topic = button.dataset.publicationTopic;
      render();
    });
  });

  function revealTarget(hash) {
    var id;
    try { id = decodeURIComponent(hash.slice(1)); }
    catch (error) { return; }
    var target = document.getElementById(id);
    if (!target || !root.contains(target) || target === root) return;
    if (target.closest("[hidden]")) {
      topic = "all";
      render();
    }
    return target;
  }

  function revealHashTarget() {
    var target = revealTarget(window.location.hash);
    if (target) {
      window.requestAnimationFrame(function () { target.scrollIntoView({ block: "start" }); });
    }
  }

  render();
  root.querySelector(".publication-controls").hidden = false;
  window.addEventListener("hashchange", revealHashTarget);
  // Reveal before the theme's smooth-scroll handler measures the target position.
  document.addEventListener("click", function (event) {
    if (event.button !== 0 || event.metaKey || event.ctrlKey || event.shiftKey || event.altKey) return;
    var link = event.target.closest("a[href^='#']");
    if (link) revealTarget(link.getAttribute("href"));
  }, true);
  revealHashTarget();
})();
