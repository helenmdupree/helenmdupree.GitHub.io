
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

  /* V1.75 live audit: strengthen the Experience page and remove repetitive language. */
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

    const patterns=document.querySelector('#experience-patterns');
    if(patterns){
      patterns.innerHTML='<div class="wrap"><p class="kicker">STRATEGIC, COMMERCIAL &amp; FINANCIAL DEPTH</p><h2 class="experience-pattern-title">The résumé shows the roles.<br/>The work behind them shows the strategic, commercial, and financial depth.</h2><p class="experience-pattern-lead">A recurring pattern of building the commercial architecture around complex technical offerings, then helping turn that architecture into revenue.</p><div class="experience-progression"><article><h3>Commercial Architect</h3><ul><li>Growth models</li><li>GTM architecture</li><li>Pricing &amp; margin</li><li>Operating economics</li><li>Resource priorities</li></ul></article><article><h3>Market Builder</h3><ul><li>Market diagnosis</li><li>Segmentation</li><li>Competitive position</li><li>Advocacy ecosystems</li><li>Whitespace</li></ul></article><article><h3>Product Strategist</h3><ul><li>Voice of customer</li><li>R&amp;D collaboration</li><li>Use-case design</li><li>Product-market fit</li><li>Commercialization</li></ul></article><article><h3>Enterprise Seller</h3><ul><li>Complex pursuits</li><li>Business cases</li><li>MSAs / contracts</li><li>Pilots</li><li>Revenue delivery</li></ul></article></div><div class="experience-core-thesis"><span>CORE THESIS</span><strong>Commercial growth is created when market truth is translated into an executable system.</strong><p>Across companies, technologies, and market conditions, the pattern is consistent: understand what is true in the market, identify where growth is being lost or overlooked, translate customer evidence into commercial and product action, quantify the economics, align the organization, and execute.</p></div><div class="actions"><a class="btn secondary" href="/about/career-in-motion/">View A Career in Motion</a></div></div>';
    }
  }
})();
