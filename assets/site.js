(function(){
  const path = location.pathname.replace(/\/+$/,'/') || '/';
  const currentYear = String(new Date().getFullYear());
  document.querySelectorAll('[data-current-year]').forEach(el => el.textContent = currentYear);

  const marketsLinks=[
    ['/markets/','Markets Overview'],
    ['/markets/midstream-pipelines/','Midstream & Pipelines'],
    ['/markets/downstream-refining/','Downstream & Refining'],
    ['/markets/utilities-industrial-infrastructure/','Utilities & Industrial Infrastructure']
  ];

  const expertiseLinks=[
    ['/expertise/commercial-growth-strategic-accounts/','Commercial Growth & Strategic Accounts'],
    ['/expertise/commercial-growth-strategic-accounts/playbook-system/','Commercial Growth Playbook System',true],
    ['/expertise/commercial-growth-strategic-accounts/revenue-strategy/','Revenue Strategy',true],
    ['/expertise/commercial-growth-strategic-accounts/strategic-accounts/','Strategic Accounts',true],
    ['/expertise/commercial-growth-strategic-accounts/channel-strategy-partner-management/','Channel Strategy & Partner Management',true],
    ['/expertise/commercial-growth-strategic-accounts/revenue-forecasting/','Revenue Forecasting',true],
    ['/expertise/corrosion-cathodic-protection/','Corrosion & Cathodic Protection'],
    ['/expertise/asset-integrity-management/','Asset Integrity Management'],
    ['/expertise/asset-performance/','Asset Performance'],
    ['/expertise/operational-risk/','Operational Risk'],
    ['/expertise/digital-transformation-ai/','Digital Transformation & AI']
  ];

  const knowledgeLinks=[
    ['/knowledge-library/','Knowledge Library',false],
    ['/knowledge-library/asset-integrity-management/','Asset Integrity Management',false],
    ['/knowledge-library/pipeline-asset-integrity/','Pipeline Integrity',false],
    ['/knowledge-library/tank-terminal-integrity/','Tank & Terminal Integrity',false],
    ['/knowledge-library/corrosion-cathodic-protection/','Corrosion & Cathodic Protection',false],
    ['/knowledge-library/asset-performance/','Asset Performance',false],
    ['/knowledge-library/digital-transformation-ai/','Digital & AI Knowledge',false],
    ['/analysis-perspectives/','Analysis & Perspectives',false]
  ];

  const resourceLinks=[
    ['/resources/','Resources Home'],
    ['/resources/when-asset-condition-changes/','When Asset Condition Changes'],
    ['/resources/lifecycle-decision-comparison/','Lifecycle Decision Comparison'],
    ['/resources/reliability-maintenance-decision-workbook/','Reliability & Maintenance Decision Workbook'],
    ['/resources/pipeline-integrity-metallurgy-phmsa/','Pipeline Integrity, Metallurgy & PHMSA']
  ];

  knowledgeLinks.push(...resourceLinks.map(([href,text])=>[href,text,false]));

  const aboutLinks=[
    ['/about/','About SOUBEL',false],
    ['/about/experience/','Experience',false],
    ['/about/career-in-motion/','Career in Motion',false],
    ['/about/reading-influence/','Reading & Influence',false],
    ['/about/reading-influence/thought-pieces/','Thought Pieces',true],
    ['/about/reading-influence/books/','Books That Stayed',true]
  ];

  if(!document.querySelector('#canonical-nav-style')){
    const style=document.createElement('style');
    style.id='canonical-nav-style';
    style.textContent='\
      .desktop-nav .resources-dropdown .dropdown-panel{left:auto!important;right:0!important;max-width:min(390px,calc(100vw - 28px))!important}\
      .desktop-nav .resources-dropdown .dropdown-panel a{white-space:normal!important}\
      .desktop-nav .knowledge-dropdown .dropdown-panel{min-width:300px!important;max-width:min(390px,calc(100vw - 28px))!important}\
      .desktop-nav .knowledge-dropdown .dropdown-panel a{white-space:normal!important}\
      .desktop-nav .expertise-dropdown .dropdown-panel{min-width:390px!important;max-width:min(430px,calc(100vw - 28px))!important}\
      .desktop-nav .expertise-dropdown .dropdown-panel a{white-space:normal!important}\
      .desktop-nav .dropdown-panel .knowledge-subitem{padding-left:30px!important;font-size:.91em!important;color:#496169!important}\
      .desktop-nav .expertise-dropdown .knowledge-subitem{color:#7ea7b0!important;padding-top:11px!important;padding-bottom:11px!important}\
      .desktop-nav .dropdown-panel .knowledge-subitem::before{content:"↳";margin-right:7px;color:#11858b}\
      .mobile-menu .knowledge-subitem{padding-left:30px!important;font-size:.93em!important;color:#60747b!important}\
    ';
    document.head.appendChild(style);
  }

  function makeAnchor(href,text,className){
    const a=document.createElement('a');
    a.href=href;
    a.textContent=text;
    if(className) a.className=className;
    return a;
  }

  function makeDropdown(title,links,extraClass){
    const wrap=document.createElement('div');
    wrap.className='dropdown'+(extraClass?' '+extraClass:'');
    const button=document.createElement('button');
    button.className='dropbtn';
    button.textContent=title;
    const panel=document.createElement('div');
    panel.className='dropdown-panel';
    links.forEach(item=>{
      const [href,text,isSub]=item;
      panel.appendChild(makeAnchor(href,text,isSub?'dropdown-subitem knowledge-subitem':''));
    });
    wrap.append(button,panel);
    return wrap;
  }

  function ensureDesktopNav(){
    document.querySelectorAll('.desktop-nav').forEach(nav=>{
      nav.innerHTML='';
      nav.appendChild(makeAnchor('/','Home','nav-home'));
      nav.appendChild(makeDropdown('Markets',marketsLinks));
      nav.appendChild(makeDropdown('Expertise',expertiseLinks,'expertise-dropdown'));
      nav.appendChild(makeAnchor('/industry-intelligence/oil-gas-ai-lab/','Oil & Gas AI Lab'));
      nav.appendChild(makeAnchor('/ask-soubel/','Ask SOUBEL'));
      nav.appendChild(makeAnchor('/whoqual-iq/','WhoQual-IQ'));
      nav.appendChild(makeDropdown('Knowledge',knowledgeLinks,'knowledge-dropdown'));
      nav.appendChild(makeDropdown('About',aboutLinks));
    });
  }

  function buildMobileGroup(title,links){
    const group=document.createElement('div');
    group.className='group';
    const heading=document.createElement('div');
    heading.className='group-title';
    heading.textContent=title;
    group.appendChild(heading);
    links.forEach(item=>{
      const [href,text,isSub]=item;
      const a=makeAnchor(href,text,'sub'+(isSub?' knowledge-subitem':''));
      group.appendChild(a);
    });
    return group;
  }

  function buildMobileLink(href,text){
    const group=document.createElement('div');
    group.className='group';
    group.appendChild(makeAnchor(href,text));
    return group;
  }

  function normalizeMobileMenu(){
    document.querySelectorAll('.mobile-menu').forEach(menu=>menu.remove());
    const header=document.querySelector('.site-header');
    if(!header) return;
    const menu=document.createElement('div');
    menu.className='mobile-menu';

    const homeGroup=document.createElement('div');
    homeGroup.className='group mobile-home-group';
    const home=makeAnchor('/','Home','mobile-home');
    home.setAttribute('aria-label','SOUBEL home');
    homeGroup.appendChild(home);
    menu.appendChild(homeGroup);

    menu.appendChild(buildMobileGroup('Markets',marketsLinks));
    menu.appendChild(buildMobileGroup('Expertise',expertiseLinks));
    menu.appendChild(buildMobileLink('/industry-intelligence/oil-gas-ai-lab/','Oil & Gas AI Lab'));
    menu.appendChild(buildMobileLink('/ask-soubel/','Ask SOUBEL'));
    menu.appendChild(buildMobileLink('/whoqual-iq/','WhoQual-IQ'));
    menu.appendChild(buildMobileGroup('Knowledge',knowledgeLinks));
    menu.appendChild(buildMobileGroup('About',aboutLinks));
    header.insertAdjacentElement('afterend',menu);
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

  function connectTerminalIntegrity(){
    const terminalUrl='/knowledge-library/tank-terminal-integrity/';

    if(path==='/expertise/asset-integrity-management/'){
      const deeper=[...document.querySelectorAll('main > section')].find(section=>section.querySelector('.kicker')?.textContent.trim()==='EXPLORE DEEPER');
      const grid=deeper?.querySelector('.grid-3');
      if(grid && !grid.querySelector('a[href="'+terminalUrl+'"]')){
        const a=document.createElement('a');a.className='knowledge-card';a.href=terminalUrl;
        a.innerHTML='<span>TANK &amp; TERMINAL INTEGRITY</span><h3>Storage, transfer, corrosion, controls, and containment</h3><p>Follow integrity across tanks, terminal piping, transfer equipment, corrosion-control systems, overfill prevention, containment, inspection, and lifecycle decisions.</p>';
        const pipeline=grid.querySelector('a[href="/knowledge-library/pipeline-asset-integrity/"]');
        if(pipeline) grid.insertBefore(a,pipeline); else grid.appendChild(a);
      }
    }

    if(path==='/expertise/asset-integrity-management/application-domains/'){
      const terminal=[...document.querySelectorAll('main > section')].find(section=>section.querySelector('.kicker')?.textContent.trim()==='TERMINALS, TANK FARMS & STORAGE');
      const wrap=terminal?.querySelector('.wrap');
      if(wrap && !wrap.querySelector('a[href="'+terminalUrl+'"]')){
        const actions=document.createElement('div');actions.className='actions';actions.innerHTML='<a class="btn primary" href="'+terminalUrl+'">Explore Tank &amp; Terminal Integrity</a><a class="btn secondary" href="/knowledge-library/corrosion-cathodic-protection/">Corrosion &amp; CP Knowledge</a>';
        wrap.appendChild(actions);
      }
    }

    if(path==='/expertise/corrosion-cathodic-protection/'){
      const connected=[...document.querySelectorAll('main > section')].find(section=>section.querySelector('.kicker')?.textContent.trim()==='CONNECTED KNOWLEDGE');
      if(connected && !document.querySelector('#cp-application-environments')){
        const section=document.createElement('section');section.className='section';section.id='cp-application-environments';
        section.innerHTML='<div class="wrap"><p class="kicker">APPLICATION ENVIRONMENTS</p><h2>Corrosion-control decisions span multiple asset environments.</h2><p class="section-intro">Materials, exposure, protection methods, inspection evidence, operating conditions, and consequences change with the asset and its environment. SOUBEL carries the corrosion-control perspective across the systems where those decisions have to work.</p><div class="grid-2"><article class="card"><span class="label">PIPELINES &amp; TRANSMISSION</span><h3>Buried and aboveground linear assets</h3><p>Coatings, cathodic protection, interference, field surveys, monitoring, excavation evidence, and integrity assessment.</p></article><a class="knowledge-card" href="'+terminalUrl+'"><span>TERMINALS, TANK FARMS &amp; STORAGE</span><h3>Tanks, transfer systems, and facility corrosion</h3><p>Tank bottoms, shells and roofs, foundations, linings, cathodic protection, transfer piping, buried and aboveground assets, water and product exposure, and corrosion evidence across the terminal.</p></a><article class="card"><span class="label">PROCESS FACILITIES &amp; FIXED EQUIPMENT</span><h3>Materials and process environment together</h3><p>Process chemistry, temperature, pressure, external exposure, coatings, insulation, materials, inspection, and maintenance history shape the corrosion question.</p></article><article class="card"><span class="label">INDUSTRIAL &amp; ENERGY INFRASTRUCTURE</span><h3>Protection across connected facility systems</h3><p>Buried infrastructure, structures, grounding and electrical interfaces, utility systems, atmospheric exposure, coatings, and monitoring.</p></article></div></div>';
        connected.parentNode.insertBefore(section,connected);
      }
    }

    if(path==='/knowledge-library/corrosion-cathodic-protection/'){
      const data=document.querySelector('#data');
      if(data && !document.querySelector('#tanks-terminals')){
        const section=document.createElement('section');section.className='section';section.id='tanks-terminals';
        section.innerHTML='<div class="wrap"><p class="kicker">TANKS, TERMINALS &amp; STORAGE</p><h2>Corrosion control changes with the exposure.</h2><p class="section-intro">Terminal facilities can place steel against soil, atmosphere, product, water, coatings, linings, insulation, concrete, and electrical systems within one operating environment. The corrosion mechanism, protection method, evidence, and consequence can change as the product moves through the facility.</p><div class="grid-3"><article class="card"><span class="label">STORAGE TANKS</span><h3>Bottom, shell, roof, and foundation each add evidence.</h3><p>Soil-side and internal bottom corrosion, water accumulation, coatings and linings, cathodic protection, atmospheric exposure, drainage, settlement, and inspection history contribute to the condition picture.</p></article><article class="card"><span class="label">TRANSFER SYSTEMS</span><h3>Corrosion continues through piping and equipment.</h3><p>Buried and aboveground piping, dead legs, low points, supports, coatings, CP where applicable, atmospheric exposure, insulation, process conditions, and service changes shape the threat.</p></article><article class="card"><span class="label">FACILITY CONTEXT</span><h3>Environment and operating history remain attached to the evidence.</h3><p>Soil and groundwater, drainage, containment, electrical interference, product and water chemistry, previous repairs, operating changes, and monitoring can alter what a corrosion finding means.</p></article></div><div class="actions"><a class="btn primary" href="'+terminalUrl+'">Explore Tank &amp; Terminal Integrity</a></div></div>';
        data.parentNode.insertBefore(section,data);
      }
    }
  }

  function enhanceCommercialGrowth(){
    if(path!=='/expertise/commercial-growth-strategic-accounts/') return;
    const main=document.querySelector('main');
    if(!main) return;

    const thesis=[...main.querySelectorAll(':scope > section')].find(section=>section.querySelector('.kicker')?.textContent.trim()==='THE COMMERCIAL THESIS');
    if(thesis){
      thesis.id='revenue-strategy';
      const wrap=thesis.querySelector('.wrap');
      if(wrap){
        wrap.classList.remove('commercial-thesis');
        wrap.innerHTML='<p class="kicker">REVENUE STRATEGY</p><h2>Growth has to be built from evidence.</h2><p class="section-intro">Revenue strategy begins with a credible answer to three questions: where can profitable growth come from, what is preventing capture today, and which opportunities deserve investment.</p><div class="prose"><p>SOUBEL evaluates market demand, existing accounts, whitespace, competitive position, pricing, commercial capacity, channel performance, and operational constraints together. The objective is to separate attractive ideas from opportunities the organization can actually win, deliver, and sustain.</p><p>The result is a prioritized growth path tied to measurable revenue, margin, timing, ownership, and execution requirements.</p></div>';
      }
    }

    const applications=document.querySelector('#applications');
    if(applications && !document.querySelector('#strategic-accounts')){
      const section=document.createElement('section');
      section.className='section';
      section.id='strategic-accounts';
      section.innerHTML='<div class="wrap"><p class="kicker">STRATEGIC ACCOUNTS</p><h2>Large accounts require more than relationship coverage.</h2><p class="section-intro">Strategic-account growth depends on understanding how the customer actually buys, where value is created, who owns the problem, what evidence is required, and where credible whitespace exists across the organization.</p><div class="prose"><p>SOUBEL examines account structure, operating priorities, decision pathways, existing footprint, competitive position, budget ownership, technical requirements, and commercial economics to identify where deeper penetration is justified.</p><p>The goal is not more account activity. It is a focused account strategy that connects customer need to executable revenue opportunities.</p></div></div>';
      applications.parentNode.insertBefore(section,applications);
    }

    const channel=document.querySelector('#channel-management');
    if(channel){
      const wrap=channel.querySelector('.wrap');
      if(wrap){
        const intro=wrap.querySelector('.section-intro');
        if(intro) intro.textContent='Productive channels require more than distributor coverage or representative agreements. They depend on clear market roles, aligned economics, local seller activation, account ownership, technical capability, reliable performance data, and a recurring management cadence that connects partner activity to measurable commercial outcomes.';
      }
    }

    if(channel && !document.querySelector('#revenue-forecasting')){
      const section=document.createElement('section');
      section.className='section alt';
      section.id='revenue-forecasting';
      section.innerHTML='<div class="wrap"><p class="kicker">REVENUE FORECASTING</p><h2>A forecast should explain where the number comes from.</h2><p class="section-intro">Revenue forecasting is more than adding opportunities in a CRM and applying probability percentages. A useful forecast distinguishes committed revenue from probable revenue, identifies what must happen for an opportunity to advance, and exposes where timing, evidence, customer action, or internal execution could change the outcome.</p><div class="commercial-rows"><div class="commercial-row"><div class="num">01 · EVIDENCE</div><div><h3>Build the forecast from the underlying commercial evidence.</h3><p>Opportunity stage, customer commitment, buying process, technical qualification, competitive position, pricing, partner involvement, delivery capacity, historical conversion, timing, and known dependencies all shape forecast confidence.</p></div></div><div class="commercial-row"><div class="num">02 · MOTION</div><div><h3>Separate revenue motions that behave differently.</h3><p>Existing-account expansion, new-logo growth, channel revenue, recurring revenue, project-based sales, and one-time transactions should not be treated as though they carry the same level of predictability.</p></div></div><div class="commercial-row"><div class="num">03 · ACTION</div><div><h3>Make the assumptions visible enough to manage.</h3><p>The objective is a forecast leadership can interrogate, understand, and act on, with clear assumptions, confidence levels, risks, and next actions behind the number.</p></div></div></div></div>';
      channel.insertAdjacentElement('afterend',section);
    }
  }

  ensureDesktopNav();
  normalizeMobileMenu();
  normalizeLegacyAimLinks(document);
  connectTerminalIntegrity();
  enhanceCommercialGrowth();

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
      ot.innerHTML='<div class="wrap home-ot-row"><div><p class="eyebrow">OPERATIONAL TRUST</p><h2>Trust has to survive the handoff.</h2><p class="section-intro">Evidence, judgment, decisions, and field execution stay connected to the outcome.</p></div></div>';
      if(!document.querySelector('#home-ot-compact-style')){
        const style=document.createElement('style');style.id='home-ot-compact-style';style.textContent='.home-ot-compact{padding:34px 0!important}.home-ot-row{display:flex;align-items:flex-end;justify-content:space-between;gap:36px}.home-ot-row h2{font-size:clamp(1.65rem,2.5vw,2.35rem);line-height:1.08;letter-spacing:-.025em;margin:.12rem 0 .45rem;max-width:650px}.home-ot-row .section-intro{font-size:.96rem;line-height:1.5;max-width:690px}@media(max-width:760px){.home-ot-row{display:block}}';document.head.appendChild(style);
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