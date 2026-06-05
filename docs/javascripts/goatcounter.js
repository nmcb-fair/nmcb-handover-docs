/* GoatCounter: countUrl from goatcounter-env.js (CI) or analytics-config.json. */
(function () {
  function withHttps(url) {
    if (!url) return url;
    if (/^https?:\/\//i.test(url)) return url;
    return "https://" + url.replace(/^\/+/, "");
  }

  function pagePath() {
    return location.pathname + location.search;
  }

  function countEndpoint(countUrl) {
    var base = withHttps(countUrl).replace(/\/count\/?$/, "");
    return base + "/count";
  }

  function beacon(countUrl) {
    var img = new Image();
    img.referrerPolicy = "no-referrer-when-downgrade";
    img.src =
      countEndpoint(countUrl) +
      "?p=" +
      encodeURIComponent(pagePath()) +
      "&t=" +
      encodeURIComponent(document.title);
  }

  function sendCount() {
    if (!window.goatcounter || typeof window.goatcounter.count !== "function") {
      return false;
    }
    window.goatcounter.count({
      path: pagePath(),
      title: document.title,
    });
    return true;
  }

  function loadCounter(countUrl) {
    countUrl = withHttps(countUrl);
    if (!countUrl || window.__nmcbGcLoading) return;
    window.__nmcbGcLoading = true;

    window.goatcounter = window.goatcounter || {};
    window.goatcounter.no_onload = true;

    var s = document.createElement("script");
    s.async = true;
    s.dataset.goatcounter = countUrl;
    s.src = "https://gc.zgoat.net/count.js";

    var attempts = 0;
    function tryCount() {
      if (sendCount()) return;
      if (++attempts < 40) {
        setTimeout(tryCount, 50);
        return;
      }
      beacon(countUrl);
    }

    s.onload = tryCount;
    s.onerror = function () {
      window.__nmcbGcLoading = false;
      beacon(countUrl);
    };
    (document.head || document.body).appendChild(s);
  }

  function start(cfg) {
    if (cfg && cfg.enabled && cfg.countUrl) loadCounter(cfg.countUrl);
  }

  if (window.NMCB_GC_COUNT_URL) {
    start({ enabled: true, countUrl: window.NMCB_GC_COUNT_URL });
    return;
  }

  fetch(window.nmcbAssetUrl("javascripts/analytics-config.json"))
    .then(function (r) {
      return r.json();
    })
    .then(start)
    .catch(function () {});
})();
