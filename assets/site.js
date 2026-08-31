
(function(){
  const btn = document.querySelector('.menu-toggle');
  const menu = document.querySelector('.mobile-menu');
  if(!btn || !menu) return;
  btn.addEventListener('click', function(){
    const open = menu.classList.toggle('open');
    btn.setAttribute('aria-expanded', open ? 'true' : 'false');
    document.body.style.overflow = open ? 'hidden' : '';
  });
  menu.querySelectorAll('a').forEach(a => a.addEventListener('click', () => {
    menu.classList.remove('open');
    btn.setAttribute('aria-expanded','false');
    document.body.style.overflow = '';
  }));
})();
