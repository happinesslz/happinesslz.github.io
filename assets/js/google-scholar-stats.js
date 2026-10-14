(function () {
  "use strict";

  const script = document.currentScript;
  const elements = document.querySelectorAll("[data-scholar-metric]");
  if (!script || !elements.length) return;

  const scholarId = script.dataset.scholarId;
  const storageKey = "google-scholar-stats:" + scholarId;
  const metrics = ["citedby", "hindex", "i10index"];
  const formatter = new Intl.NumberFormat("en-US");
  let newestUpdate = Date.parse(script.dataset.baselineUpdated) || 0;

  elements.forEach(function (element) {
    const value = Number(element.textContent.replace(/,/g, ""));
    if (Number.isSafeInteger(value) && value >= 0) {
      element.textContent = formatter.format(value);
    }
  });

  function applyStats(data) {
    if (!data || data.scholar_id !== scholarId || data.schema_version !== 1) return false;
    if (!metrics.every(key => Number.isSafeInteger(data[key]) && data[key] >= 0)) return false;
    const updated = Date.parse(data.updated);
    if (!Number.isFinite(updated) || updated < newestUpdate || updated > Date.now() + 300000) return false;
    if (data.hindex > data.citedby || data.i10index > data.citedby) return false;

    elements.forEach(function (element) {
      const key = element.dataset.scholarMetric;
      if (metrics.includes(key)) element.textContent = formatter.format(data[key]);
    });
    newestUpdate = updated;
    return true;
  }

  // Keep the latest successful snapshot available if the network is unavailable.
  try {
    applyStats(JSON.parse(localStorage.getItem(storageKey)));
  } catch (_) {}

  const controller = new AbortController();
  const timeout = setTimeout(() => controller.abort(), 8000);
  const url = new URL(script.dataset.statsUrl);
  url.searchParams.set("t", Date.now());
  fetch(url, { cache: "no-store", signal: controller.signal })
    .then(function (response) {
      if (!response.ok) throw new Error("Scholar statistics unavailable");
      return response.json();
    })
    .then(function (data) {
      if (applyStats(data)) {
        try {
          localStorage.setItem(storageKey, JSON.stringify(data));
        } catch (_) {}
      }
    })
    .catch(function () {
      // Retain the cached or server-rendered values after a failed refresh.
    })
    .finally(() => clearTimeout(timeout));
})();
