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
          <i data-lucide="user-circle-2" style="width: 48px; height: 48px; color: #31B63F"></i>
        </div>
      </div>
      
      <nav class="backdrop">
      <div class="left-nav">
        <ul>
          <li><a class="left-nav-item" href="/mockups/pages/templates.html">
          <i data-lucide="locate" style="width: 48px; height: 48px;"></i>
          Templates</a></li>
          <li>
   
          <a class="left-nav-item" href="/mockups/pages/tasks.html">
          <i data-lucide="clipboard-list" style="width: 48px; height: 48px;"></i>
          Tasks</a></li>

          <li><a class="left-nav-item" href="/mockups/pages/contexts.html">
          <i data-lucide="file-question" style="width: 48px; height: 48px;"></i>
          Context</a></li>

          <li><a class="left-nav-item" href="/mockups/pages/tests.html">
          <i data-lucide="flask-conical" style="width: 48px; height: 48px;"></i>
          Tests</a></li>

          <li><a class="left-nav-item" href="/mockups/pages/archives.html">
          <i data-lucide="database" style="width: 48px; height: 48px;"></i>
          Archives</a></li>

          <li><a class="left-nav-item" href="/mockups/pages/schedules.html">
          <i data-lucide="calendar-check" style="width: 48px; height: 48px;"></i>
          Schedules</a></li>

          <li><a class="left-nav-item" href="/mockups/pages/groups.html">
          <i data-lucide="group" style="width: 48px; height: 48px;"></i>
          Groups</a></li>
          
          <li><a class="left-nav-item" href="/mockups/pages/hosts.html">
          <i data-lucide="hard-drive-download" style="width: 48px; height: 48px;"></i>
          Hosts</a></li>

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
  loadPageContent();
  lucide.createIcons();
}

function loadPageContent() {
  const pageContent = document.getElementById('page-content');
  const currentPage = window.location.pathname.split("/").pop() || 'index.html';
  fetch(currentPage)
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
  script.onload = initializePage; // Initialize page after Lucide is loaded
  document.head.appendChild(script);
});