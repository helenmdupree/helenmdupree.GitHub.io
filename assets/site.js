
(function(){
  const btn = document.querySelector('.menu-toggle');
  const menu = document.querySelector('.mobile-menu');
  if(btn && menu){
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
  }

  const path = location.pathname.replace(/\/+$/,'/') || '/';

  /* V1.75 live audit: remove repetitive "experience" language from the Experience hero. */
  if(path==='/about/experience/'){
    const hero=document.querySelector('.experience-hero');
    if(hero){
      const crumb=hero.querySelector('.crumb');
      const kicker=hero.querySelector('.kicker');
      const h1=hero.querySelector('h1');
      const copy=hero.querySelector('h1 + p');
      const primary=hero.querySelector('.btn.primary');
      if(crumb) crumb.textContent='About';
      if(kicker) kicker.textContent='THE WORK BEHIND SOUBEL';
      if(h1) h1.textContent='A career built across industry, field operations, and commercial growth.';
      if(copy) copy.textContent='Helen M. Dupree’s career spans commercial growth, strategic accounts, pipeline and asset integrity, corrosion and cathodic protection, asset performance, and digital transformation. That background was built through customers, field environments, industry relationships, and the practical work of turning technical capability into commercial and operational value.';
      if(primary){ primary.textContent='View career highlights'; primary.setAttribute('href','#career-context'); }
    }
    const context=document.querySelector('#career-context');
    if(context){
      const kicker=context.querySelector('.kicker');
      const h2=context.querySelector('h2');
      if(kicker) kicker.textContent='CAREER HISTORY';
      if(h2) h2.textContent='Across industrial products, services, software, and field organizations.';
    }
  }
})();
