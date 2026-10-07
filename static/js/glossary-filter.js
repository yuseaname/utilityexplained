/* glossary-filter.js — client-side term filter + A–Z nav enhancement for
   /utilities-glossary/. Loaded deferred from layouts/_default/baseof.html
   (house pattern: same as /js/spike-triage.js). No dependencies. */
(function () {
  'use strict';

  function init() {
    var input = document.getElementById('glossary-filter');
    var azNav = document.getElementById('glossary-az');
    var countEl = document.getElementById('glossary-count');
    var emptyEl = document.getElementById('glossary-empty');
    var content = document.querySelector('.article-content');
    if (!input || !content) return;

    var headings = content.querySelectorAll('h2, h3');
    if (!headings.length) return;

    // 1. Wrap each term (h3 + following siblings until the next h2/h3)
    //    into a .glossary-entry div so it can be shown/hidden as a unit.
    var entries = [];
    var byId = {};
    var sections = []; // {h2, entries: []}
    var currentSection = null;
    for (var i = 0; i < headings.length; i++) {
      var h = headings[i];
      if (h.tagName === 'H2') {
        currentSection = { h2: h, entries: [] };
        sections.push(currentSection);
        continue;
      }
      var entry = document.createElement('div');
      entry.className = 'glossary-entry';
      h.parentNode.insertBefore(entry, h);
      var sib = h.nextSibling; // capture BEFORE moving h (appendChild detaches it)
      entry.appendChild(h); // the heading itself
      while (sib && !(sib.tagName === 'H2' || sib.tagName === 'H3')) {
        var next = sib.nextSibling;
        entry.appendChild(sib);
        sib = next;
      }
      if (h.id) byId[h.id] = entry;
      entries.push(entry);
      if (currentSection) currentSection.entries.push(entry);
    }

    var total = entries.length;
    var letters = azNav ? azNav.querySelectorAll('a[data-letter]') : [];

    function isHidden(el) { return el.hasAttribute('hidden'); }

    function apply() {
      var q = input.value.trim().toLowerCase();
      var visible = 0;
      for (var i = 0; i < entries.length; i++) {
        var e = entries[i];
        var hit = !q || e.textContent.toLowerCase().indexOf(q) !== -1;
        if (hit) { e.removeAttribute('hidden'); visible++; }
        else { e.setAttribute('hidden', ''); }
      }
      // Hide section headers only while filtering; with no query all are restored
      for (var s = 0; s < sections.length; s++) {
        var sec = sections[s];
        var any = !q;
        if (q) {
          for (var j = 0; j < sec.entries.length; j++) {
            if (!isHidden(sec.entries[j])) { any = true; break; }
          }
        }
        if (any) { sec.h2.removeAttribute('hidden'); }
        else { sec.h2.setAttribute('hidden', ''); }
      }
      if (countEl) {
        countEl.textContent = q ? 'Showing ' + visible + ' of ' + total + ' terms' : '';
      }
      if (emptyEl) {
        if (q && visible === 0) { emptyEl.removeAttribute('hidden'); }
        else { emptyEl.setAttribute('hidden', ''); }
      }
      // Dim A–Z letters whose target entry is hidden
      for (var l = 0; l < letters.length; l++) {
        var id = letters[l].getAttribute('href').slice(1);
        var target = byId[id];
        if (target && isHidden(target)) { letters[l].classList.add('az-off'); }
        else { letters[l].classList.remove('az-off'); }
      }
    }

    input.addEventListener('input', apply);

    // Clicking a dimmed letter under an active filter: clear filter so the jump works
    if (azNav) {
      azNav.addEventListener('click', function (ev) {
        var a = ev.target.closest ? ev.target.closest('a[data-letter]') : null;
        if (!a) return;
        var id = a.getAttribute('href').slice(1);
        var e = byId[id];
        if (e && isHidden(e)) { input.value = ''; apply(); }
      });
    }
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', init);
  } else {
    init();
  }
})();
