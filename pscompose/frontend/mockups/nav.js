function createLayout() {
  const layoutHtml =  `
   <body class="packets-ui">
    <div class="bg-surface-bg">
      <div class="top-nav">
        <div class="top-left">
          <a href="/mockups/home.html">
          <img class="Logo" src="/mockups/static/perfsonar-icon.png"></img>
          <p class="pscompose"> pSCompose </p>
          </a>
        </div>

        <div class="top-right">
          <p class="readme"> README </p>
          <i data-lucide="user-circle-2" style="width: 48px; height: 48px; color: var(--success-color)"></i>
        </div>
      </div>
      
      <nav class="backdrop">
      <div class="left-nav">
        <ul>

          <li class="parent-item" data-submenu="submenu-templates">
            <a class="left-nav-item">
              <i data-lucide="locate" style="width: 48px; height: 48px;"></i>
              Templates
            </a>
          </li>

          <li class="parent-item" data-submenu="submenu-tasks">
            <a class="left-nav-item">
              <i data-lucide="clipboard-list" style="width: 48px; height: 48px;"></i>
              Tasks
            </a>
          </li>

          <li class="parent-item" data-submenu="submenu-contexts">
            <a class="left-nav-item">
              <i data-lucide="file-question" style="width: 48px; height: 48px;"></i>
              Contexts
            </a>
          </li>

          <li class="parent-item" data-submenu="submenu-tests">
            <a class="left-nav-item">
              <i data-lucide="flask-conical" style="width: 48px; height: 48px;"></i>
              Tests
            </a>
          </li>

          <li class="parent-item" data-submenu="submenu-archives">
            <a class="left-nav-item">
              <i data-lucide="database" style="width: 48px; height: 48px;"></i>
              Archives
            </a>
          </li>

          <li class="parent-item" data-submenu="submenu-schedules">
            <a class="left-nav-item">
              <i data-lucide="calendar-check" style="width: 48px; height: 48px;"></i>
              Schedules
            </a>
          </li>

          <li class="parent-item" data-submenu="submenu-groups">
            <a class="left-nav-item">
              <i data-lucide="group" style="width: 48px; height: 48px;"></i>
              Groups
            </a>
          </li>

          <li class="parent-item" data-submenu="submenu-hosts">
            <a class="left-nav-item">
              <i data-lucide="hard-drive-download" style="width: 48px; height: 48px;"></i>
              Hosts
            </a>
          </li>

        </ul>
      </div>

      <div class="submenu-container">
        <ul id="submenu-templates" class="submenu">
          <h1>Templates</h1>
          <li><i data-lucide="plus" style="width: 36px; height: 36px;"></i><a href="/mockups/pages/templates.html">New Template</a></li>
          <li><i data-lucide="locate" style="width: 36px; height: 36px;"></i><a href="#">Template A</a></li>
          <li><i data-lucide="locate" style="width: 36px; height: 36px;"></i><a href="#">Template B</a></li>
        </ul>

        <ul id="submenu-tasks" class="submenu">
          <h1>Tasks</h1>
          <li><i data-lucide="plus" style="width: 36px; height: 36px;"></i><a href="/mockups/pages/tasks.html">New Task</a></li>
          <li><i data-lucide="clipboard-list" style="width: 36px; height: 36px;"></i><a href="#">Task A</a></li>
          <li><i data-lucide="clipboard-list" style="width: 36px; height: 36px;"></i><a href="#">Task B</a></li>
        </ul>

        <ul id="submenu-contexts" class="submenu">
          <h1>Contexts</h1>
          <li><i data-lucide="plus" style="width: 36px; height: 36px;"></i><a href="/mockups/pages/contexts.html">New Context</a></li>
          <li><i data-lucide="file-question" style="width: 36px; height: 36px;"></i><a href="#">Context A</a></li>
          <li><i data-lucide="file-question" style="width: 36px; height: 36px;"></i><a href="#">Context B</a></li>
        </ul>

        <ul id="submenu-tests" class="submenu">
          <h1>Tests</h1>
          <li><i data-lucide="plus" style="width: 36px; height: 36px;"></i><a href="/mockups/pages/tests.html">New Test</a></li>
          <li><i data-lucide="flask-conical" style="width: 36px; height: 36px;"></i><a href="#">Test A</a></li>
          <li><i data-lucide="flask-conical" style="width: 36px; height: 36px;"></i><a href="#">Test B</a></li>
        </ul>

        <ul id="submenu-archives" class="submenu">
          <h1>Archives</h1>
          <li><i data-lucide="plus" style="width: 36px; height: 36px;"></i><a href="/mockups/pages/archives.html">New Archive</a></li>
          <li><i data-lucide="database" style="width: 36px; height: 36px;"></i><a href="#">Archive A</a></li>
          <li><i data-lucide="database" style="width: 36px; height: 36px;"></i><a href="#">Archive B</a></li>
        </ul>

        <ul id="submenu-schedules" class="submenu">
          <h1>Schedules</h1>
          <li><i data-lucide="plus" style="width: 36px; height: 36px;"></i><a href="/mockups/pages/schedules.html">New Schedule</a></li>
          <li><i data-lucide="calendar-check" style="width: 36px; height: 36px;"></i><a href="#">Schedule A</a></li>
          <li><i data-lucide="calendar-check" style="width: 36px; height: 36px;"></i><a href="#">Schedule B</a></li>
        </ul>

        <ul id="submenu-groups" class="submenu">
          <h1>Groups</h1>
          <li><i data-lucide="plus" style="width: 36px; height: 36px;"></i><a href="/mockups/pages/groups.html">New Group</a></li>
          <li><i data-lucide="group" style="width: 36px; height: 36px;"></i><a href="#">Group A</a></li>
          <li><i data-lucide="group" style="width: 36px; height: 36px;"></i><a href="#">Group B</a></li>
        </ul>

        <ul id="submenu-hosts" class="submenu">
          <h1>Hosts</h1>
          <li><i data-lucide="plus" style="width: 36px; height: 36px;"></i><a href="/mockups/pages/hosts.html">New Host</a></li>
          <li><i data-lucide="hard-drive-download" style="width: 36px; height: 36px;"></i><a href="#">Host A</a></li>
          <li><i data-lucide="hard-drive-download" style="width: 36px; height: 36px;"></i><a href="#">Host B</a></li>
        </ul>
      </div>

      <main id="page-content">
          <!-- This is where the page-specific content will be inserted -->
      </main>
      </nav>
    </div>
    </body>
    
    `;
    return layoutHtml;
}

function initializePage() {
  document.body.innerHTML = createLayout();
  loadPageContent().then(() => {
    lucide.createIcons();
    
    document.querySelectorAll('.parent-item').forEach(parent => {
      parent.addEventListener('click', function(event) {
        // Prevent default link behavior if needed
        event.preventDefault();
        
        // Get the ID of the submenu to show
        const submenuId = parent.getAttribute('data-submenu');
        
        // Get the submenu element
        const submenuToShow = document.getElementById(submenuId);
        
        // Check if the submenu is already visible
        if (submenuToShow.classList.contains('show')) {
          // Hide the submenu
          submenuToShow.classList.remove('show');
        } else {
          // Hide all submenus
          document.querySelectorAll('.submenu').forEach(submenu => {
            submenu.classList.remove('show');
          });
          
          // Show the specific submenu
          if (submenuToShow) {
            submenuToShow.classList.add('show');
          }
        }
      });
    });
    
    
  });
}

function loadPageContent() {
  const pageContent = document.getElementById('page-content');
  const currentPage = window.location.pathname.split("/").pop() || 'index.html';
  return fetch(currentPage)
    .then(response => response.text())
    .then(html => {
      const parser = new DOMParser();
      const doc = parser.parseFromString(html, 'text/html');
      const content = doc.querySelector('body').innerHTML;
      pageContent.innerHTML = content;
    })
    .catch(error => console.error('Error loading page content:', error));
}

document.addEventListener('DOMContentLoaded', () => {
  // Load Lucide script
  const script = document.createElement('script');
  script.src = "https://unpkg.com/lucide@latest";
  script.onload = initializePage; 
  document.head.appendChild(script);
});
