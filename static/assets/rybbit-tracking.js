(() => {
  "use strict";

  if (window.__ueRybbitEnhance) return;
  window.__ueRybbitEnhance = true;

  window.__analyticsSink = function (name, params) {
    if (window.rybbit && typeof window.rybbit.event === "function") {
      try {
        window.rybbit.event(name, params || {});
      } catch (e) {}
    }
  };

  function track(name, params) {
    try {
      var sink = window.__analyticsSink;
      if (typeof sink === "function") sink(name, params || {});
      else if (typeof window.gtag === "function") window.gtag("event", name, params || {});
    } catch (e) {}
  }

  function pageId() {
    var p = location.pathname.replace(/\/+$/, "");
    return p === "" ? "home" : p.split("/").pop();
  }

  function pageType() {
    var p = location.pathname;
    if (p === "/") return "home";
    if (/^\/electricity-explained\//.test(p)) return "hub";
    if (/^\/gas-explained\//.test(p)) return "hub";
    if (/^\/water-explained\//.test(p)) return "hub";
    if (/^\/heating-cooling-explained\//.test(p)) return "hub";
    if (/^\/utility-bills-costs-explained\//.test(p)) return "hub";
    if (/^\/utilities-glossary\//.test(p)) return "hub";
    if (/^\/blog\/category\//.test(p)) return "category";
    if (/-review\/$/.test(p)) return "review";
    if (/-vs-|versus/.test(p)) return "vs";
    if (/^\/blog\/ccf-calculator\//.test(p)) return "tool";
    if (/^\/(about|contact|affiliate-disclosure|editorial-policy|review-methodology|privacy-policy|terms|disclaimer|corrections|methodology|editorial-team)\/?$/.test(p) || /404/.test(p)) return "trust";
    if (/^\/blog\//.test(p)) return "article";
    return "informational";
  }

  var seenDepth = {};
  window.addEventListener("scroll", function () {
    var doc = document.documentElement;
    var pct = ((window.scrollY + window.innerHeight) / (doc.scrollHeight || 1)) * 100;
    [25, 50, 75, 90].forEach(function (m) {
      if (pct >= m && !seenDepth[m]) {
        seenDepth[m] = true;
        track("scroll_depth", { milestone: m, page_id: pageId(), page_type: pageType() });
      }
    });
  }, { passive: true });

  var t0 = Date.now();
  document.addEventListener("visibilitychange", function () {
    if (document.visibilityState === "hidden") {
      var s = Math.round((Date.now() - t0) / 1000);
      var b = s < 5 ? "lt5s" : s < 15 ? "5_15s" : s < 45 ? "15_45s" : s < 120 ? "45s_2m" : "gt2m";
      track("engagement", { engagement_bucket: b, page_id: pageId(), page_type: pageType() });
    }
  });

  document.addEventListener("submit", function (e) {
    var form = e.target;
    if (!form || form.tagName !== "FORM") return;

    if (form.classList && form.classList.contains("newsletter-form")) {
      track("contact_submit", { form_id: "newsletter", page_id: pageId(), page_type: pageType() });
    }
  }, { passive: true });

  document.addEventListener("click", function (e) {
    var btn = e.target && e.target.closest ? e.target.closest("#ccf-go") : null;
    if (btn) {
      track("tool_completion", { tool_id: "ccf_calculator", event_subtype: "calc_run", page_id: pageId() });
    }
  }, { passive: true });
})();