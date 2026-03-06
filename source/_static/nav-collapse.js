(function () {
  function initSidebarCollapse() {
    var sidebar = document.querySelector('.bd-sidebar-primary');
    if (!sidebar) return;

    var rootLists = sidebar.querySelectorAll('.sidebar-primary-item > ul, .sidebar-primary-item nav ul');
    if (!rootLists.length) return;

    rootLists.forEach(function (rootList) {
      rootList.querySelectorAll('li').forEach(function (li) {
        var childList = Array.from(li.children).find(function (el) {
          return el.tagName && el.tagName.toLowerCase() === 'ul';
        });
        var link = Array.from(li.children).find(function (el) {
          return el.tagName && el.tagName.toLowerCase() === 'a';
        });

        if (!childList || !link) return;
        if (li.querySelector(':scope > .nav-collapse-toggle')) return;

        li.classList.add('has-children');

        var toggle = document.createElement('button');
        toggle.className = 'nav-collapse-toggle';
        toggle.type = 'button';
        toggle.setAttribute('aria-label', 'Toggle submenu');

        var isCurrentBranch = li.classList.contains('current') || !!li.querySelector('.current');
        var expanded = isCurrentBranch;

        toggle.setAttribute('aria-expanded', expanded ? 'true' : 'false');
        if (!expanded) {
          childList.hidden = true;
        }

        toggle.addEventListener('click', function () {
          var nowExpanded = toggle.getAttribute('aria-expanded') !== 'true';
          toggle.setAttribute('aria-expanded', nowExpanded ? 'true' : 'false');
          childList.hidden = !nowExpanded;
        });

        li.insertBefore(toggle, link);
      });
    });
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', initSidebarCollapse);
  } else {
    initSidebarCollapse();
  }
})();
