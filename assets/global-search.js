/* SOUBEL global site search — lazy-loads the existing search index */
(function(){
  'use strict';

  function init(){
    if(document.querySelector('.soubel-global-search-toggle')) return;
    const header=document.querySelector('.site-header');
    const inner=header && header.querySelector('.header-inner');
    if(!header || !inner) return;

    const menuToggle=inner.querySelector('.menu-toggle');
    const button=document.createElement('button');
    button.type='button';
    button.className='soubel-global-search-toggle';
    button.setAttribute('aria-label','Search SOUBEL');
    button.setAttribute('aria-expanded','false');
    button.innerHTML='<svg aria-hidden="true" viewBox="0 0 24 24"><circle cx="11" cy="11" r="6.5"></circle><path d="M16 16l5 5"></path></svg>';
    if(menuToggle) inner.insertBefore(button,menuToggle); else inner.appendChild(button);

    const overlay=document.createElement('div');
    overlay.className='soubel-global-search';
    overlay.hidden=true;
    overlay.innerHTML=`
      <div class="soubel-search-backdrop" data-search-close></div>
      <section class="soubel-search-panel" role="dialog" aria-modal="true" aria-label="Search SOUBEL">
        <div class="soubel-search-panel-inner">
          <div class="soubel-search-topline">
            <div>
              <div class="soubel-search-kicker">SEARCH SOUBEL</div>
              <h2>Find the work behind the topic.</h2>
            </div>
            <button class="soubel-search-close" type="button" aria-label="Close search" data-search-close>×</button>
          </div>
          <form class="soubel-search-form" role="search">
            <label class="soubel-search-label" for="soubel-global-search-input">Search across SOUBEL</label>
            <div class="soubel-search-control">
              <svg aria-hidden="true" viewBox="0 0 24 24"><circle cx="11" cy="11" r="6.5"></circle><path d="M16 16l5 5"></path></svg>
              <input id="soubel-global-search-input" type="search" autocomplete="off" spellcheck="false" placeholder="PHMSA, corrosion, digital twins, operational trust…" />
              <button type="submit">Search</button>
            </div>
          </form>
          <div class="soubel-search-suggestions" aria-label="Suggested searches">
            <button type="button" data-query="PHMSA">PHMSA</button>
            <button type="button" data-query="Asset Integrity">Asset Integrity</button>
            <button type="button" data-query="Corrosion">Corrosion</button>
            <button type="button" data-query="Digital Twins">Digital Twins</button>
            <button type="button" data-query="Operational Trust">Operational Trust</button>
          </div>
          <div class="soubel-search-status" aria-live="polite"></div>
          <div class="soubel-search-results"></div>
        </div>
      </section>`;
    document.body.appendChild(overlay);

    if(!document.querySelector('#soubel-global-search-style')){
      const style=document.createElement('style');
      style.id='soubel-global-search-style';
      style.textContent=`
.soubel-global-search-toggle{flex:0 0 auto;width:40px;height:40px;display:inline-flex;align-items:center;justify-content:center;border:1px solid rgba(255,255,255,.18);border-radius:10px;background:transparent;color:#dce8ea;cursor:pointer;transition:border-color .18s ease,background .18s ease,color .18s ease}
.soubel-global-search-toggle:hover,.soubel-global-search-toggle:focus-visible{border-color:rgba(121,208,210,.72);background:rgba(121,208,210,.08);color:#fff;outline:none}
.soubel-global-search-toggle svg,.soubel-search-control svg{width:19px;height:19px;fill:none;stroke:currentColor;stroke-width:1.8;stroke-linecap:round}
.soubel-global-search[hidden]{display:none!important}.soubel-global-search{position:fixed;inset:0;z-index:2400}.soubel-search-backdrop{position:absolute;inset:0;background:rgba(3,10,14,.68);backdrop-filter:blur(4px)}
.soubel-search-panel{position:absolute;top:82px;left:0;right:0;max-height:calc(100vh - 82px);overflow:auto;background:#fff;border-top:1px solid rgba(255,255,255,.08);box-shadow:0 24px 70px rgba(0,0,0,.28)}
.soubel-search-panel-inner{width:min(980px,calc(100% - 40px));margin:0 auto;padding:34px 0 42px}.soubel-search-topline{display:flex;align-items:flex-start;justify-content:space-between;gap:24px}.soubel-search-kicker{color:#11858b;font-size:.72rem;letter-spacing:.16em;font-weight:900}.soubel-search-topline h2{margin:.2rem 0 0;font-size:clamp(1.55rem,3vw,2.35rem);line-height:1.08;letter-spacing:-.03em;color:#071016}.soubel-search-close{width:38px;height:38px;border:1px solid #dce6e7;border-radius:10px;background:#fff;color:#40565e;font-size:1.65rem;line-height:1;cursor:pointer}.soubel-search-label{position:absolute;width:1px;height:1px;padding:0;margin:-1px;overflow:hidden;clip:rect(0,0,0,0);white-space:nowrap;border:0}.soubel-search-form{margin-top:24px}.soubel-search-control{display:grid;grid-template-columns:auto minmax(0,1fr) auto;align-items:center;gap:10px;border:1px solid #cfdcde;border-radius:14px;background:#fff;padding:7px 8px 7px 15px;box-shadow:0 10px 30px rgba(7,20,27,.06);color:#60747c}.soubel-search-control:focus-within{border-color:#11858b;box-shadow:0 0 0 3px rgba(17,133,139,.10)}.soubel-search-control input{min-width:0;border:0;outline:0;background:transparent;color:#071016;font:inherit;font-size:1rem;padding:9px 0}.soubel-search-control input::placeholder{color:#82949a}.soubel-search-control button{border:0;border-radius:10px;background:#0b6f75;color:#fff;font:inherit;font-weight:800;padding:10px 16px;cursor:pointer}.soubel-search-suggestions{display:flex;gap:8px;flex-wrap:wrap;margin-top:13px}.soubel-search-suggestions button{border:1px solid #dce6e7;border-radius:999px;background:#f7fafa;color:#40565e;padding:6px 10px;font:inherit;font-size:.82rem;font-weight:700;cursor:pointer}.soubel-search-suggestions button:hover{border-color:#93c8ca;color:#0b6f75}.soubel-search-status{min-height:25px;margin-top:22px;color:#60747c;font-size:.9rem}.soubel-search-results{display:grid;gap:10px}.soubel-search-result{display:grid;grid-template-columns:minmax(0,1fr) auto;gap:18px;padding:17px 18px;border:1px solid #dce6e7;border-radius:13px;text-decoration:none;color:#071016;background:#fff}.soubel-search-result:hover{border-color:#9bc9cb;box-shadow:0 10px 28px rgba(7,20,27,.06)}.soubel-search-result-type{margin-bottom:4px;color:#0b6f75;font-size:.68rem;letter-spacing:.12em;font-weight:900;text-transform:uppercase}.soubel-search-result h3{margin:0;font-size:1.03rem;line-height:1.28}.soubel-search-result p{margin:5px 0 0;color:#60747c;font-size:.9rem;line-height:1.48}.soubel-search-result-arrow{align-self:center;color:#11858b;font-weight:900;font-size:1.1rem}.soubel-search-empty{padding:22px 0;color:#60747c}.soubel-search-empty strong{color:#071016}
@media(max-width:1050px){.soubel-global-search-toggle{margin-left:auto}.soubel-search-panel{top:82px;max-height:calc(100vh - 82px)}}
@media(max-width:620px){.soubel-global-search-toggle{width:40px;height:40px}.soubel-search-panel{top:62px;max-height:calc(100vh - 62px)}.soubel-search-panel-inner{width:calc(100% - 28px);padding:25px 0 34px}.soubel-search-topline h2{font-size:1.5rem}.soubel-search-control{grid-template-columns:auto minmax(0,1fr);padding-right:13px}.soubel-search-control button{grid-column:1 / -1;width:100%;margin-top:2px}.soubel-search-suggestions{gap:6px}.soubel-search-result{grid-template-columns:1fr;padding:15px}.soubel-search-result-arrow{display:none}}
`;
      document.head.appendChild(style);
    }

    const input=overlay.querySelector('#soubel-global-search-input');
    const form=overlay.querySelector('.soubel-search-form');
    const status=overlay.querySelector('.soubel-search-status');
    const results=overlay.querySelector('.soubel-search-results');
    let indexPromise=null;
    let lastReportedQuery='';

    function loadIndex(){
      if(Array.isArray(window.SOUBEL_SEARCH_INDEX)) return Promise.resolve(window.SOUBEL_SEARCH_INDEX);
      if(indexPromise) return indexPromise;
      indexPromise=new Promise((resolve,reject)=>{
        const s=document.createElement('script');
        s.src='/assets/library-search-index.js';
        s.onload=()=>Array.isArray(window.SOUBEL_SEARCH_INDEX)?resolve(window.SOUBEL_SEARCH_INDEX):reject(new Error('Search index unavailable'));
        s.onerror=()=>reject(new Error('Search index failed to load'));
        document.head.appendChild(s);
      });
      return indexPromise;
    }

    function clean(value){
      return String(value||'').toLowerCase().normalize('NFKD').replace(/[\u0300-\u036f]/g,'').replace(/[^a-z0-9]+/g,' ').trim();
    }

    function scoreItem(item,query){
      const q=clean(query);
      if(!q) return 0;
      const tokens=q.split(/\s+/).filter(Boolean);
      const title=clean((item.title||'')+' '+(item.h1||''));
      const desc=clean((item.description||'')+' '+(item.headings||''));
      const body=clean(item.text||'');
      let score=0;
      if(title.includes(q)) score+=80;
      if(desc.includes(q)) score+=45;
      if(body.includes(q)) score+=18;
      tokens.forEach(t=>{
        if(title.includes(t)) score+=18;
        else if(desc.includes(t)) score+=8;
        else if(body.includes(t)) score+=2;
      });
      if(tokens.length>1 && tokens.every(t=>title.includes(t))) score+=30;
      if(tokens.every(t=>(title+' '+desc+' '+body).includes(t))) score+=12;
      return score;
    }

    function escapeHtml(value){
      return String(value||'').replace(/[&<>'"]/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;',"'":'&#39;','"':'&quot;'}[c]));
    }

    function render(query,index){
      const q=query.trim();
      if(q.length<2){
        status.textContent='Type at least two characters to search the SOUBEL site.';
        results.innerHTML='';
        return;
      }
      const ranked=index.map(item=>({item,score:scoreItem(item,q)})).filter(x=>x.score>0).sort((a,b)=>b.score-a.score).slice(0,10);
      status.textContent=ranked.length ? `${ranked.length} ${ranked.length===1?'result':'results'} for “${q}”` : `No results for “${q}”`;
      if(!ranked.length){
        results.innerHTML=`<div class="soubel-search-empty"><strong>Try a broader term.</strong> Search works best with subjects such as PHMSA, corrosion, asset integrity, AI, reliability, commercial growth, or operational trust.</div>`;
        return;
      }
      results.innerHTML=ranked.map(({item})=>{
        const type=escapeHtml(item.type||'SOUBEL');
        const title=escapeHtml(item.h1||item.title||'SOUBEL');
        const description=escapeHtml(item.description||'Open this SOUBEL page.');
        const url=escapeHtml(item.url||'/');
        return `<a class="soubel-search-result" href="${url}"><div><div class="soubel-search-result-type">${type}</div><h3>${title}</h3><p>${description}</p></div><span class="soubel-search-result-arrow" aria-hidden="true">→</span></a>`;
      }).join('');
    }

    async function doSearch(query){
      const q=query.trim();
      status.textContent=q.length>=2?'Searching SOUBEL…':'Type at least two characters to search the SOUBEL site.';
      results.innerHTML='';
      try{
        const index=await loadIndex();
        render(q,index);
        if(q.length>=2 && q.toLowerCase()!==lastReportedQuery){
          lastReportedQuery=q.toLowerCase();
          if(typeof window.gtag==='function') window.gtag('event','site_search',{search_term:q,page_path:location.pathname});
        }
      }catch(e){
        status.textContent='Search is temporarily unavailable.';
        results.innerHTML='<div class="soubel-search-empty">Please use the main navigation while the search index reloads.</div>';
      }
    }

    function openSearch(){
      const menu=document.querySelector('.mobile-menu');
      const menuBtn=document.querySelector('.menu-toggle');
      if(menu && menu.classList.contains('open')) menu.classList.remove('open');
      if(menuBtn) menuBtn.setAttribute('aria-expanded','false');
      overlay.hidden=false;
      button.setAttribute('aria-expanded','true');
      document.body.dataset.soubelSearchOverflow=document.body.style.overflow||'';
      document.body.style.overflow='hidden';
      setTimeout(()=>input.focus(),25);
    }

    function closeSearch(){
      overlay.hidden=true;
      button.setAttribute('aria-expanded','false');
      document.body.style.overflow=document.body.dataset.soubelSearchOverflow||'';
      delete document.body.dataset.soubelSearchOverflow;
      button.focus();
    }

    button.addEventListener('click',()=>overlay.hidden?openSearch():closeSearch());
    overlay.querySelectorAll('[data-search-close]').forEach(el=>el.addEventListener('click',closeSearch));
    overlay.querySelectorAll('[data-query]').forEach(el=>el.addEventListener('click',()=>{input.value=el.dataset.query||'';doSearch(input.value);input.focus();}));
    form.addEventListener('submit',e=>{e.preventDefault();doSearch(input.value);});
    input.addEventListener('input',()=>{
      const q=input.value.trim();
      if(q.length===0){status.textContent='';results.innerHTML='';return;}
      if(q.length>=2) doSearch(q);
    });
    document.addEventListener('keydown',e=>{
      if(e.key==='Escape' && !overlay.hidden){e.preventDefault();closeSearch();}
      if((e.metaKey||e.ctrlKey) && e.key.toLowerCase()==='k'){
        e.preventDefault();
        if(overlay.hidden) openSearch(); else input.focus();
      }
    });
  }

  if(document.readyState==='loading') document.addEventListener('DOMContentLoaded',()=>setTimeout(init,0));
  else setTimeout(init,0);
})();
