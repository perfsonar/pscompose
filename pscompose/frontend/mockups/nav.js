document.addEventListener('DOMContentLoaded', function() {
  fetch('/mockups/nav.html')
    .then(response => response.text())
    .then(html => {
      document.getElementById('nav-container').innerHTML = html;

      document.querySelectorAll('.left-nav-item-button').forEach(button => {
        button.addEventListener('click', function(e) {
          e.preventDefault();
          const content = this.nextElementSibling;
          content.classList.toggle('active');
        });
      });

    });

  fetch('/mockups/top-nav.html')
  .then(response => response.text())
  .then(html => {
    document.getElementById('top-nav-container').innerHTML = html;
  });

});


// submenu toggle
document.addEventListener('click', function(e) {
  if (!e.target.closest('.left-nav-item')) {
    document.querySelectorAll('.submenu').forEach(menu => {
      menu.classList.remove('active');
    });
  }
});







