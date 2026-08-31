(function(){
  const path = location.pathname.replace(/\/+$/,'/') || '/';

  /* Signature-series discoverability: The Integrity Shift belongs directly under Intelligence. */
  document.querySelectorAll('.desktop-nav .dropdown').forEach(group=>{
    const button=group.querySelector('.dropbtn');
    const panel=group.querySelector('.dropdown-panel');
    if(button?.textContent.trim()==='Intelligence' && panel && !panel.querySelector('a[href="/insights/integrity-shift/"]')){
      const a=document.createElement('a');
      a.href='/insights/integrity-shift/';
      a.textContent='The Integrity Shift';
      panel.appendChild(a);
    }
  });
  document.querySelectorAll('.mobile-menu .group').forEach(group=>{
    const title=group.querySelector('.group-title');
    if(title?.textContent.trim()==='Intelligence' && !group.querySelector('a[href="/insights/integrity-shift/"]')){
      const a=document.createElement('a');
      a.href='/insights/integrity-shift/';
      a.textContent='The Integrity Shift';
      a.className='sub';
      const analysis=group.querySelector('a[href="/analysis-perspectives/"]');
      if(analysis) analysis.insertAdjacentElement('afterend',a); else group.appendChild(a);
    }
  });

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

  /* Homepage: Operational Trust gets one concise invitation, not a duplicated two-column definition. */
  if(path==='/'){
    const ot=[...document.querySelectorAll('main > section.dark')].find(section=>section.querySelector('.eyebrow')?.textContent.trim()==='OPERATIONAL TRUST');
    if(ot){
      ot.classList.add('home-ot-compact');
      ot.innerHTML='<div class="wrap home-ot-row"><div><p class="eyebrow">OPERATIONAL TRUST</p><h2>Trust has to survive the handoff.</h2><p class="section-intro">Evidence, judgment, decisions, and field execution stay connected to the outcome.</p></div><a class="home-ot-link" href="/operational-trust/">Explore Operational Trust →</a></div>';
      if(!document.querySelector('#home-ot-compact-style')){
        const style=document.createElement('style');
        style.id='home-ot-compact-style';
        style.textContent=`
          .home-ot-compact{padding:34px 0!important}
          .home-ot-row{display:flex;align-items:flex-end;justify-content:space-between;gap:36px}
          .home-ot-row h2{font-size:clamp(1.65rem,2.5vw,2.35rem);line-height:1.08;letter-spacing:-.025em;margin:.12rem 0 .45rem;max-width:650px}
          .home-ot-row .section-intro{font-size:.96rem;line-height:1.5;max-width:690px}
          .home-ot-link{color:#79d0d2;text-decoration:none;font-weight:850;white-space:nowrap;padding-bottom:4px}
          @media(max-width:760px){.home-ot-row{display:block}.home-ot-link{display:inline-block;margin-top:16px;white-space:normal}}
        `;
        document.head.appendChild(style);
      }
    }
  }

  /* Corrosion knowledge: clearer technical language and accessible contrast. */
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
      const h2=source.querySelector('h2');
      const p=source.querySelector('.section-intro');
      if(h2) h2.textContent='Use the right source for the right decision.';
      if(p) p.textContent='SOUBEL provides practical context and connects evidence across corrosion-control and integrity work. Standards, regulations, company procedures, original technical literature, and qualified engineering judgment govern asset-specific criteria, calculations, and technical decisions.';
      const resource=source.querySelector('a[href="/resources/"]');
      if(resource) resource.remove();
    }

    if(!document.querySelector('#cp-knowledge-contrast-style')){
      const style=document.createElement('style');
      style.id='cp-knowledge-contrast-style';
      style.textContent=`
        .cp-knowledge-page #fundamentals{padding:38px 0}
        .cp-knowledge-page #fundamentals>.wrap>h2{font-size:clamp(1.65rem,2.45vw,2.3rem);line-height:1.08;letter-spacing:-.025em;max-width:800px}
        .cp-knowledge-page #fundamentals>.wrap>.section-intro{max-width:930px;color:#425960!important;font-size:.98rem;line-height:1.58}
        .cp-knowledge-page #fundamentals .content-grid{gap:32px;margin-top:18px}
        .cp-knowledge-page #fundamentals .prose h2{font-size:1.28rem;line-height:1.2;margin:.25rem 0 .6rem;color:#20363c}
        .cp-knowledge-page #fundamentals .prose p{font-size:.94rem;line-height:1.58;color:#465d65}
        .cp-knowledge-page #field .trust-note{margin-top:20px;padding:13px 16px;background:#edf4f4;color:#24474f!important;border-left:3px solid var(--teal);border-radius:0 8px 8px 0}
        .cp-knowledge-page #field .trust-note strong{color:#18363d!important}
        .cp-knowledge-page .section.dark .kicker{color:#79d0d2!important}
        .cp-knowledge-page .section.dark h2{color:#f4f7f7!important}
        .cp-knowledge-page .section.dark .section-intro,.cp-knowledge-page .section.dark p{color:#dce6e8!important}
        .cp-knowledge-page .section.dark .btn.secondary{color:#f4f7f7!important;border-color:#9cb4ba!important}
        .cp-knowledge-page .section.dark .actions{margin-top:20px}
        @media(max-width:760px){.cp-knowledge-page #fundamentals{padding:34px 0}.cp-knowledge-page #fundamentals .content-grid{gap:20px}}
      `;
      document.head.appendChild(style);
    }
  }

  /* Integrity Shift articles: editorial scale, not billboard scale. */
  if(path.startsWith('/insights/integrity-shift/') && path!=='/insights/integrity-shift/' && document.querySelector('.article-hero')){
    document.body.classList.add('integrity-shift-article-audit');
    if(!document.querySelector('#integrity-shift-article-audit-style')){
      const style=document.createElement('style');
      style.id='integrity-shift-article-audit-style';
      style.textContent=`
        .integrity-shift-article-audit .article-hero{padding:44px 0 38px}
        .integrity-shift-article-audit .article-hero .article-shell{max-width:900px}
        .integrity-shift-article-audit .article-hero h1{max-width:880px;font-size:clamp(2.15rem,4vw,3.75rem);line-height:1.03;letter-spacing:-.038em;margin:10px 0 13px}
        .integrity-shift-article-audit .article-deck{max-width:760px;font-size:1rem;line-height:1.5;margin-top:0}
        .integrity-shift-article-audit .article-byline{font-size:.88rem;margin-top:18px}
        .integrity-shift-article-audit .article-figure{max-width:820px;margin:24px auto 30px;border-radius:14px;background:#07141b;aspect-ratio:16/8.5;display:flex;align-items:center;justify-content:center}
        .integrity-shift-article-audit .article-figure img{width:100%;height:100%;max-height:none;object-fit:contain;object-position:center;background:#07141b}
        .integrity-shift-article-audit .article-content-section{padding-top:8px}
        .integrity-shift-article-audit .article-body{max-width:760px;margin-left:auto;margin-right:auto}
        @media(max-width:760px){
          .integrity-shift-article-audit .article-hero{padding:36px 0 32px}
          .integrity-shift-article-audit .article-hero h1{font-size:clamp(2rem,8.5vw,3rem)}
          .integrity-shift-article-audit .article-figure{max-width:calc(100% - 32px);margin:18px auto 24px;aspect-ratio:16/9}
        }
      `;
      document.head.appendChild(style);
    }
  }

  /* Connect the Operational Trust flagship page to the signature editorial series. */
  if(path==='/operational-trust/' && !document.querySelector('#integrity-shift-connection')){
    const close=document.querySelector('.ot-close-v2');
    if(close){
      const section=document.createElement('section');
      section.className='section alt';
      section.id='integrity-shift-connection';
      section.innerHTML='<div class="wrap"><p class="kicker">FROM THE INTEGRITY SHIFT</p><h2>The thinking continues in the signature series.</h2><p class="section-intro"><em>Operational Trust Is Becoming the New Standard</em> develops the idea beyond the framework: why industrial transformation has to move from visibility toward information, decisions, execution, evidence, and outcomes the organization can actually rely on.</p><div class="link-row"><a href="/insights/integrity-shift/operational-trust-new-standard/">Read the Operational Trust perspective →</a><a href="/insights/integrity-shift/">Explore The Integrity Shift →</a></div></div>';
      close.parentNode.insertBefore(section,close);
    }
  }

  /* Experience page: keep the opening concise, remove repeated framing, and make the hierarchy quieter. */
  if(path==='/about/experience/'){
    document.body.classList.add('experience-page-audit');
    if(!document.querySelector('#experience-page-audit-style')){
      const style=document.createElement('style');
      style.id='experience-page-audit-style';
      style.textContent=`
        .experience-page-audit .experience-hero{padding:42px 0 38px}
        .experience-page-audit .experience-hero h1{max-width:900px;font-size:clamp(2.15rem,3.5vw,3.25rem);line-height:1.03;letter-spacing:-.035em;font-weight:720}
        .experience-page-audit .experience-hero p{max-width:830px;font-size:1rem;line-height:1.55;margin-top:14px}
        .experience-page-audit #career-context{padding-top:38px;padding-bottom:42px}
        .experience-page-audit #career-context h2,.experience-page-audit #selected-experience h2{font-size:clamp(1.55rem,2.4vw,2.2rem);line-height:1.1;letter-spacing:-.025em}
        .experience-page-audit #experience-patterns{padding:42px 0}
        .experience-page-audit #experience-patterns .experience-pattern-title{font-size:clamp(1.65rem,2.55vw,2.35rem);line-height:1.08;max-width:930px}
        .experience-page-audit .experience-core-thesis{margin-top:22px}
        .experience-page-audit .experience-motion-row{margin-top:18px}
        .experience-page-audit .experience-motion-link{display:inline-flex;color:var(--teal);font-size:.92rem;font-weight:800;text-decoration:none;border-bottom:1px solid rgba(17,133,139,.35);padding-bottom:2px}
        .experience-page-audit .experience-motion-link:hover{border-bottom-color:var(--teal)}
        .experience-page-audit .experience-leadership-section{padding:46px 0}
        .experience-page-audit .experience-leadership-section h2{font-size:clamp(1.55rem,2.25vw,2.15rem);line-height:1.08;letter-spacing:-.025em;margin-bottom:20px;max-width:none}
        .experience-page-audit .experience-leadership{margin-top:20px}
        @media(min-width:960px){.experience-page-audit .experience-leadership-section h2{white-space:nowrap}}
        @media(max-width:620px){.experience-page-audit .experience-hero{padding:34px 0 30px}.experience-page-audit .experience-leadership-section{padding:38px 0}}
      `;
      document.head.appendChild(style);
    }

    const hero=document.querySelector('.experience-hero');
    if(hero){
      const crumb=hero.querySelector('.crumb');
      const kicker=hero.querySelector('.kicker');
      const h1=hero.querySelector('h1');
      const copy=hero.querySelector('h1 + p');
      const actions=hero.querySelector('.actions');
      if(crumb) crumb.textContent='About';
      if(kicker) kicker.textContent='THE WORK BEHIND SOUBEL';
      if(h1) h1.textContent='From field execution to market creation.';
      if(copy) copy.textContent='Across industrial products, field services, enterprise software, and complex customer environments, the work behind SOUBEL has consistently connected technical capability, commercial judgment, and execution.';
      if(actions) actions.remove();
    }

    const context=document.querySelector('#career-context');
    if(context){
      const kicker=context.querySelector('.kicker');
      const h2=context.querySelector('h2');
      if(kicker) kicker.textContent='CAREER HISTORY';
      if(h2) h2.textContent='Industrial products, services, software, and field organizations.';
    }

    const patterns=document.querySelector('#experience-patterns');
    if(patterns){
      patterns.innerHTML='<div class="wrap"><p class="kicker">STRATEGIC, COMMERCIAL &amp; FINANCIAL DEPTH</p><h2 class="experience-pattern-title">The résumé shows the roles.<br/>The work behind them shows the strategic, commercial, and financial depth.</h2><p class="experience-pattern-lead">A recurring pattern of building the commercial architecture around complex technical offerings, then helping turn that architecture into revenue.</p><div class="experience-progression"><article><h3>Commercial Architect</h3><ul><li>Growth models</li><li>GTM architecture</li><li>Pricing &amp; margin</li><li>Operating economics</li><li>Resource priorities</li></ul></article><article><h3>Market Builder</h3><ul><li>Market diagnosis</li><li>Segmentation</li><li>Competitive position</li><li>Advocacy ecosystems</li><li>Whitespace</li></ul></article><article><h3>Product Strategist</h3><ul><li>Voice of customer</li><li>R&amp;D collaboration</li><li>Use-case design</li><li>Product-market fit</li><li>Commercialization</li></ul></article><article><h3>Enterprise Seller</h3><ul><li>Complex pursuits</li><li>Business cases</li><li>MSAs / contracts</li><li>Pilots</li><li>Revenue delivery</li></ul></article></div><div class="experience-core-thesis"><span>CORE THESIS</span><strong>Commercial growth is created when market truth is translated into an executable system.</strong></div><div class="experience-motion-row"><a class="experience-motion-link" href="/about/career-in-motion/">View A Career in Motion →</a></div></div>';
    }

    const selected=document.querySelector('#selected-experience');
    if(selected){
      const digital=[...selected.querySelectorAll('.experience-grid article')].find(article=>article.querySelector('span')?.textContent.trim()==='ASSET PERFORMANCE & DIGITAL');
      if(digital){
        const h3=digital.querySelector('h3');
        const p=digital.querySelector('h3 + p');
        const contribution=digital.querySelector('.experience-contribution');
        if(h3) h3.textContent='Translating digital capability into operating value.';
        if(p) p.textContent='Work around asset-performance platforms, digital twins, analytics, AI, and industrial software reinforced a recurring lesson: technology creates value when it improves context, decision quality, execution, adoption, or measurable operating outcomes.';
        if(contribution) contribution.innerHTML='<strong>What it contributes to SOUBEL:</strong> Digital transformation is evaluated by operational usefulness and measurable value.';
      }
    }

    const leadership=[...document.querySelectorAll('main > section')].find(section=>section.querySelector('.kicker')?.textContent.trim()==='INDUSTRY LEADERSHIP');
    if(leadership){
      leadership.classList.add('experience-leadership-section');
      const h2=leadership.querySelector('h2');
      if(h2) h2.textContent='Helping shape the industry conversation.';
    }
  }
})();