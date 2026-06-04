/* Load GoatCounter when analytics-config.json has countUrl (set in CI from secrets). */
(function () {
  function withHttps(url) {
    if (!url) return url;
    if (/^https?:\/\//i.test(url)) return url;
    return "https://" + url.replace(/^\/+/, "");
  }

  function loadCounter(countUrl) {
    countUrl = withHttps(countUrl);
    if (!countUrl || window.goatcounter) return;
    window.goatcounter = { no_onload: true };
    var s = document.createElement("script");
    s.async = true;
    s.dataset.goatcounter = countUrl;
    s.src = "https://gc.zgoat.net/count.js";
    (document.head || document.body).appendChild(s);
  }

  fetch(window.nmcbAssetUrl("javascripts/analytics-config.json"))
    .then(function (r) {
      return r.json();
    })
    .then(function (cfg) {
      if (cfg && cfg.enabled && cfg.countUrl) loadCounter(cfg.countUrl);
    })
    .catch(function () {});
})();
