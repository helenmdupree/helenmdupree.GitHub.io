(function(){
  const form=document.querySelector('.library-search');
  const input=document.getElementById('library-search');
  const results=document.getElementById('library-search-results');
  const status=document.getElementById('library-search-status');
  if(!form||!input||!results||!status||!Array.isArray(window.SOUBEL_SEARCH_INDEX)) return;

  const index=window.SOUBEL_SEARCH_INDEX;
  const esc=s=>String(s||'').replace(/[&<>"']/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[c]));
  const norm=s=>String(s||'').toLowerCase().replace(/[^a-z0-9&+\-\s]/g,' ').replace(/\s+/g,' ').trim();
  const tokens=q=>norm(q).split(' ').filter(Boolean);

  function score(item, words, phrase){
    const title=norm(item.title), h1=norm(item.h1), heads=norm(item.headings), desc=norm(item.description), body=norm(item.text);
    let n=0, matched=0;
    words.forEach(w=>{
      let hit=false;
      if(title.includes(w)){n+=24;hit=true;}
      if(h1.includes(w)){n+=20;hit=true;}
      if(heads.includes(w)){n+=12;hit=true;}
      if(desc.includes(w)){n+=8;hit=true;}
      if(body.includes(w)){n+=2;hit=true;}
      if(hit) matched++;
    });
    if(words.length>1 && matched===words.length) n+=16;
    if(phrase && title.includes(phrase)) n+=32;
    else if(phrase && (h1.includes(phrase)||heads.includes(phrase))) n+=18;
    else if(phrase && desc.includes(phrase)) n+=10;
    if(item.type==='Knowledge Library') n+=5;
    return {score:n,matched};
  }

  function snippet(item, words){
    const source=item.description || item.text || '';
    if(item.description) return item.description;
    const low=source.toLowerCase();
    let pos=-1;
    for(const w of words){ const p=low.indexOf(w); if(p>=0 && (pos<0||p<pos)) pos=p; }
    if(pos<0) return source.slice(0,190)+(source.length>190?'…':'');
    const start=Math.max(0,pos-70), end=Math.min(source.length,start+210);
    return (start?'…':'')+source.slice(start,end).trim()+(end<source.length?'…':'');
  }

  function render(q){
    const phrase=norm(q), words=tokens(q);
    results.innerHTML='';
    if(!phrase){ results.hidden=true; status.textContent=''; return; }
    if(phrase.length<2){ results.hidden=false; status.textContent='Type at least two characters.'; return; }

    const ranked=index.map(item=>({item,...score(item,words,phrase)}))
      .filter(x=>x.matched>0)
      .sort((a,b)=>b.score-a.score || a.item.title.localeCompare(b.item.title))
      .slice(0,10);

    results.hidden=false;
    if(!ranked.length){
      status.textContent='No matches found.';
      results.innerHTML='<div class="library-search-empty"><strong>No results for “'+esc(q)+'”.</strong><p>Try a broader term such as corrosion, PHMSA, asset performance, AI, reliability, risk, or revenue strategy.</p></div>';
      return;
    }

    status.textContent=ranked.length+(ranked.length===1?' result':' results')+' shown for “'+q+'”.';
    results.innerHTML=ranked.map(({item})=>
      '<a class="library-search-result" href="'+esc(item.url)+'">'+
        '<span class="library-search-type">'+esc(item.type)+'</span>'+ 
        '<strong>'+esc(item.title.replace(/\s*\|\s*SOUBEL.*$/i,''))+'</strong>'+ 
        '<p>'+esc(snippet(item,words))+'</p>'+ 
        '<span class="library-search-path">'+esc(item.url)+'</span>'+ 
      '</a>'
    ).join('');
  }

  let timer;
  input.addEventListener('input',()=>{ clearTimeout(timer); timer=setTimeout(()=>render(input.value),120); });
  form.addEventListener('submit',e=>{ e.preventDefault(); clearTimeout(timer); render(input.value); });
  input.addEventListener('keydown',e=>{
    if(e.key==='Escape'){input.value='';render('');input.focus();}
  });
})();
