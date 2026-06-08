'use strict';

// Ensure every search form exposes a submit control.
//
// The pydata-sphinx-theme search forms (the navbar search dialog and the
// dedicated search page) ship without a submit button, which fails WCAG 2.1 AA
// (H32.2) on every page. The search is JavaScript-driven, so adding the button
// from JavaScript is consistent with the theme. See issue #133.
(function () {
  function addSubmitButton(form) {
    if (
      form.querySelector(
        'button[type="submit"], input[type="submit"], input[type="image"]'
      )
    ) {
      return;
    }
    var button = document.createElement('button');
    button.type = 'submit';
    button.className = 'visually-hidden';
    button.textContent = 'Search';
    form.appendChild(button);
  }

  function enhanceSearchForms() {
    document.querySelectorAll('form.bd-search').forEach(addSubmitButton);
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', enhanceSearchForms);
  } else {
    enhanceSearchForms();
  }
})();

