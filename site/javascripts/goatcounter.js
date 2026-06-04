/* Load GoatCounter when analytics-config.json has countUrl (set in CI from secrets). */
(function () {
  function loadCounter(countUrl) {
    if (!countUrl || window.goatcounter) return;
    window.goatcounter = { no_onload: true };
    var s = document.createElement("script");
    s.async = true;
    s.dataset.goatcounter = countUrl;
    s.src = "https://gc.zgoat.net/count.js";
    (document.head || document.body).appendChild(s);
  }

  fetch(new URL("analytics-config.json", document.baseURI))
    .then(function (r) {
      return r.json();
    })
    .then(function (cfg) {
      if (cfg && cfg.enabled && cfg.countUrl) loadCounter(cfg.countUrl);
    })
    .catch(function () {});
})();
