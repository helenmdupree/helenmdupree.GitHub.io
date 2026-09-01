(function(){
  const path = location.pathname.replace(/\/+$/,'/') || '/';
  const currentYear = String(new Date().getFullYear());
  document.querySelectorAll('[data-current-year]').forEach(el => el.textContent = currentYear);

  const resourceLinks=[
    ['/resources/','Resources Overview'],
    ['/resources/pipeline-integrity-metallurgy-phmsa/','Pipeline Integrity, Metallurgy & PHMSA'],
    ['/resources/when-asset-condition-changes/','When Asset Condition Changes'],
    ['/resources/lifecycle-decision-comparison/','Lifecycle Decision Comparison'],
    ['/resources/reliability-maintenance-decision-workbook/','Reliability & Maintenance Decision Workbook']
  ];

  if(!document.querySelector('#resources-nav-foundation-style')){
    const style=document.createElement('style');
    style.id='resources-nav-foundation-style';
    style.textContent='.desktop-nav .resources-dropdown .dropdown-panel{left:auto!important;right:0!important;max-width:min(390px,calc(100vw - 28px))!important}.desktop-nav .resources-dropdown .dropdown-panel a{white-space:normal!important}';
    document.head.appendChild(style);
  }

  function populateResourcePanel(panel){
    if(!panel) return;
    panel.innerHTML='';
    resourceLinks.forEach(([href,text])=>{const a=document.createElement('a');a.href=href;a.textContent=text;panel.appendChild(a);});
  }

  function normalizeAimLink(root){
    if(!root) return;
    const link=root.querySelector('a[href="/expertise/pipeline-asset-integrity/"],a[href="/expertise/asset-integrity-management/"]');
    if(link){
      link.href='/expertise/asset-integrity-management/';
      link.textContent='Asset Integrity Management';
    }
  }

  function normalizeLegacyAimLinks(root){
    if(!root) return;
    root.querySelectorAll('a[href="/expertise/pipeline-asset-integrity/"]').forEach(link=>{
      link.href='/expertise/asset-integrity-management/';
      if((link.textContent||'').includes('Pipeline & Asset Integrity')){
        link.textContent=link.textContent.replace('Pipeline & Asset Integrity','Asset Integrity Management');
      }
    });
  }

  function ensureDesktopNav(){
    document.querySelectorAll('.desktop-nav').forEach(nav=>{
      const expertise=[...nav.children].find(el=>el.classList?.contains('dropdown') && el.querySelector('.dropbtn')?.textContent.trim()==='Expertise');
      normalizeAimLink(expertise?.querySelector('.dropdown-panel'));

      const intelligence=[...nav.children].find(el=>el.classList?.contains('dropdown') && el.querySelector('.dropbtn')?.textContent.trim()==='Intelligence');
      const ipanel=intelligence?.querySelector('.dropdown-panel');
      if(ipanel && !ipanel.querySelector('a[href="/insights/integrity-shift/"]')){
        const a=document.createElement('a'); a.href='/insights/integrity-shift/'; a.textContent='The Integrity Shift'; ipanel.appendChild(a);
      }

      let resources=[...nav.children].find(el=>el.classList?.contains('dropdown') && el.querySelector('.dropbtn')?.textContent.trim()==='Resources');
      if(!resources){
        const direct=[...nav.children].find(el=>el.tagName==='A' && el.getAttribute('href')==='/resources/');
        resources=document.createElement('div'); resources.className='dropdown resources-dropdown';
        const button=document.createElement('button'); button.className='dropbtn'; button.textContent='Resources';
        const panel=document.createElement('div'); panel.className='dropdown-panel';
        resources.append(button,panel);
        if(direct) direct.replaceWith(resources);
        else {
          const about=[...nav.children].find(el=>el.classList?.contains('dropdown') && el.querySelector('.dropbtn')?.textContent.trim()==='About');
          if(about) nav.insertBefore(resources,about); else nav.appendChild(resources);
        }
      }
      resources.classList.add('resources-dropdown');
      populateResourcePanel(resources.querySelector('.dropdown-panel'));

      const about=[...nav.children].find(el=>el.classList?.contains('dropdown') && el.querySelector('.dropbtn')?.textContent.trim()==='About');
      const panel=about?.querySelector('.dropdown-panel');
      if(panel && !panel.querySelector('a[href="/about/career-in-motion/"]')){
        const a=document.createElement('a'); a.href='/about/career-in-motion/'; a.textContent='A Career in Motion';
        const exp=panel.querySelector('a[href="/about/experience/"]');
        if(exp) exp.insertAdjacentElement('afterend',a); else panel.appendChild(a);
      }
    });
  }

  function buildMobileMenu(){
    if(document.querySelector('.mobile-menu')) return;
    const nav=document.querySelector('.desktop-nav');
    if(!nav) return;
    const menu=document.createElement('div'); menu.className='mobile-menu';
    [...nav.children].forEach(child=>{
      if(child.classList?.contains('dropdown')){
        const title=child.querySelector('.dropbtn')?.textContent.trim();
        const panel=child.querySelector('.dropdown-panel');
        if(!title||!panel) return;
        const group=document.createElement('div'); group.className='group';
        const heading=document.createElement('div'); heading.className='group-title'; heading.textContent=title; group.appendChild(heading);
        panel.querySelectorAll('a').forEach(src=>{const a=document.createElement('a');a.href=src.getAttribute('href');a.textContent=src.textContent;a.className='sub';group.appendChild(a);});
        menu.appendChild(group);
      } else if(child.tagName==='A'){
        const group=document.createElement('div'); group.className='group';
        const a=document.createElement('a'); a.href=child.getAttribute('href'); a.textContent=child.textContent; group.appendChild(a); menu.appendChild(group);
      }
    });
    document.querySelector('.site-header')?.insertAdjacentElement('afterend',menu);
  }

  function normalizeMobileMenu(){
    buildMobileMenu();
    document.querySelectorAll('.mobile-menu').forEach(menu=>{
      if(!menu.querySelector('.mobile-home-group')){
        const homeGroup=document.createElement('div'); homeGroup.className='group mobile-home-group';
        const home=document.createElement('a'); home.href='/'; home.textContent='Home'; home.className='mobile-home'; home.setAttribute('aria-label','SOUBEL home');
        homeGroup.appendChild(home);
        menu.insertBefore(homeGroup,menu.firstChild);
      }

      const expertise=[...menu.querySelectorAll('.group')].find(g=>g.querySelector('.group-title')?.textContent.trim()==='Expertise');
      normalizeAimLink(expertise);

      let intelligence=[...menu.querySelectorAll('.group')].find(g=>g.querySelector('.group-title')?.textContent.trim()==='Intelligence');
      if(intelligence && !intelligence.querySelector('a[href="/insights/integrity-shift/"]')){
        const a=document.createElement('a');a.href='/insights/integrity-shift/';a.textContent='The Integrity Shift';a.className='sub';intelligence.appendChild(a);
      }
      let resources=[...menu.querySelectorAll('.group')].find(g=>g.querySelector('.group-title')?.textContent.trim()==='Resources');
      if(!resources){
        resources=document.createElement('div');resources.className='group resources-group';
        const title=document.createElement('div');title.className='group-title';title.textContent='Resources';resources.appendChild(title);
        const about=[...menu.querySelectorAll('.group')].find(g=>g.querySelector('.group-title')?.textContent.trim()==='About');
        if(about) menu.insertBefore(resources,about); else menu.appendChild(resources);
      }
      resources.querySelectorAll('a').forEach(a=>a.remove());
      resourceLinks.forEach(([href,text])=>{const a=document.createElement('a');a.href=href;a.textContent=text;a.className='sub';resources.appendChild(a);});
      const about=[...menu.querySelectorAll('.group')].find(g=>g.querySelector('.group-title')?.textContent.trim()==='About');
      if(about && !about.querySelector('a[href="/about/career-in-motion/"]')){
        const a=document.createElement('a');a.href='/about/career-in-motion/';a.textContent='A Career in Motion';a.className='sub';
        const exp=about.querySelector('a[href="/about/experience/"]');
        if(exp) exp.insertAdjacentElement('afterend',a); else about.appendChild(a);
      }
    });
  }

  ensureDesktopNav();
  normalizeMobileMenu();
  normalizeLegacyAimLinks(document);

  const btn=document.querySelector('.menu-toggle');
  const menu=document.querySelector('.mobile-menu');
  if(btn&&menu){
    btn.addEventListener('click',()=>{
      const open=menu.classList.toggle('open');
      btn.setAttribute('aria-expanded',open?'true':'false');
      document.body.style.overflow=open?'hidden':'';
    });
    menu.querySelectorAll('a').forEach(a=>a.addEventListener('click',()=>{menu.classList.remove('open');btn.setAttribute('aria-expanded','false');document.body.style.overflow='';}));
  }

  document.querySelectorAll('a[href^="/downloads/"][href$=".pdf"]').forEach(a=>{a.target='_blank';a.rel='noopener';});

  if(path==='/'){
    const ot=[...document.querySelectorAll('main > section.dark')].find(section=>section.querySelector('.eyebrow')?.textContent.trim()==='OPERATIONAL TRUST');
    if(ot){
      ot.classList.add('home-ot-compact');
      ot.innerHTML='<div class="wrap home-ot-row"><div><p class="eyebrow">OPERATIONAL TRUST</p><h2>Trust has to survive the handoff.</h2><p class="section-intro">Evidence, judgment, decisions, and field execution stay connected to the outcome.</p></div><a class="home-ot-link" href="/operational-trust/">Explore Operational Trust →</a></div>';
      if(!document.querySelector('#home-ot-compact-style')){
        const style=document.createElement('style');style.id='home-ot-compact-style';style.textContent='.home-ot-compact{padding:34px 0!important}.home-ot-row{display:flex;align-items:flex-end;justify-content:space-between;gap:36px}.home-ot-row h2{font-size:clamp(1.65rem,2.5vw,2.35rem);line-height:1.08;letter-spacing:-.025em;margin:.12rem 0 .45rem;max-width:650px}.home-ot-row .section-intro{font-size:.96rem;line-height:1.5;max-width:690px}.home-ot-link{color:#79d0d2;text-decoration:none;font-weight:850;white-space:nowrap;padding-bottom:4px}@media(max-width:760px){.home-ot-row{display:block}.home-ot-link{display:inline-block;margin-top:16px;white-space:normal}}';document.head.appendChild(style);
      }
    }
  }

  if(path==='/knowledge-library/corrosion-cathodic-protection/'){
    const fundamentals=document.querySelector('#fundamentals');
    if(fundamentals){
      const h2=fundamentals.querySelector(':scope > .wrap > h2');
      const intro=fundamentals.querySelector(':scope > .wrap > .section-intro');
      const proseH2=fundamentals.querySelector('.prose h2');
      if(h2) h2.textContent='A CP reading only matters in context.';
      if(intro) intro.textContent='Cathodic protection is evaluated through measurements, but a number by itself does not establish protection. The reading has to be understood alongside the reference electrode, location, operating condition, current distribution, coating condition, interruption method, continuity, and interference.';
      if(proseH2) proseH2.textContent='The conditions behind the number.';
    }
    const source=[...document.querySelectorAll('main > section.dark')].find(section=>section.querySelector('.kicker')?.textContent.trim()==='SOURCE DISCIPLINE');
    if(source){
      const h2=source.querySelector('h2');const p=source.querySelector('.section-intro');
      if(h2) h2.textContent='Use the right source for the right decision.';
      if(p) p.textContent='SOUBEL provides practical context and connects evidence across corrosion-control and integrity work. Standards, regulations, company procedures, original technical literature, and qualified engineering judgment govern asset-specific criteria, calculations, and technical decisions.';
    }
  }

  if(path.startsWith('/insights/integrity-shift/') && path!=='/insights/integrity-shift/' && document.querySelector('.article-hero')){
    document.body.classList.add('integrity-shift-article-audit');
  }

  if(path==='/operational-trust/' && !document.querySelector('#integrity-shift-connection')){
    const close=document.querySelector('.ot-close-v2');
    if(close){
      const section=document.createElement('section');section.className='section alt';section.id='integrity-shift-connection';
      section.innerHTML='<div class="wrap"><p class="kicker">FROM THE INTEGRITY SHIFT</p><h2>The thinking continues in the signature series.</h2><p class="section-intro"><em>Operational Trust Is Becoming the New Standard</em> develops the idea beyond the framework: why industrial transformation has to move from visibility toward information, decisions, execution, evidence, and outcomes the organization can actually rely on.</p><div class="link-row"><a href="/insights/integrity-shift/operational-trust-new-standard/">Read the Operational Trust perspective →</a><a href="/insights/integrity-shift/">Explore The Integrity Shift →</a></div></div>';
      close.parentNode.insertBefore(section,close);
    }
  }
})();