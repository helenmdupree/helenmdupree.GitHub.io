(()=>{
  const root=document.querySelector('[data-iccp-cinematic]');
  if(!root) return;

  const video=root.querySelector('video');
  const play=root.querySelector('[data-film-play]');
  const reset=root.querySelector('[data-film-reset]');
  const overlay=root.querySelector('[data-film-overlay-play]');
  const progress=root.querySelector('[data-film-progress]');
  const status=root.querySelector('[data-film-status]');
  const title=root.querySelector('[data-film-title]');
  const body=root.querySelector('[data-film-body]');
  const buttons=[...root.querySelectorAll('[data-film-stage]')];

  const stages=buttons.map((button,index)=>({
    button,
    index,
    start:Number(button.dataset.start),
    end:Number(button.dataset.end),
    title:button.dataset.title,
    body:button.dataset.body
  }));

  let segmentEnd=null;
  let fullSequence=false;
  function stageForTime(time){
    let found=stages[0];
    for(const stage of stages){
      if(time>=stage.start) found=stage;
    }
    return found;
  }

  function setActive(stage){
    buttons.forEach(button=>button.classList.toggle('is-active',button===stage.button));
    title.textContent=stage.title;
    body.textContent=stage.body;
    status.textContent=`Stage ${stage.index+1} of ${stages.length}`;
  }

  function setPlayingUI(){
    const playing=!video.paused&&!video.ended;
    play.textContent=playing?'Pause':'Play sequence';
    overlay.classList.toggle('is-hidden',playing||video.currentTime>0.05);
  }

  function playFull(){
    segmentEnd=null;
    fullSequence=true;
    if(video.ended||video.currentTime>=video.duration-.15) video.currentTime=0;
    video.play();
  }

  function togglePlay(){
    if(video.paused||video.ended) playFull();
    else video.pause();
  }
  buttons.forEach((button,index)=>{
    button.addEventListener('click',()=>{
      const stage=stages[index];
      fullSequence=false;
      segmentEnd=stage.end;
      video.currentTime=stage.start;
      setActive(stage);
      video.play();
    });
  });

  play.addEventListener('click',togglePlay);
  overlay.addEventListener('click',playFull);
  reset.addEventListener('click',()=>{
    video.pause();
    video.currentTime=0;
    fullSequence=false;
    segmentEnd=null;
    setActive(stages[0]);
    setPlayingUI();
  });

  video.addEventListener('click',togglePlay);
  video.addEventListener('keydown',event=>{
    if(event.key==='Enter'||event.key===' '){
      event.preventDefault();
      togglePlay();
    }
  });

  video.addEventListener('timeupdate',()=>{
    const duration=video.duration||26;
    progress.style.width=`${Math.min(100,(video.currentTime/duration)*100)}%`;
    setActive(stageForTime(video.currentTime));
    if(segmentEnd!==null&&video.currentTime>=segmentEnd-.06){
      video.pause();
      video.currentTime=Math.max(0,segmentEnd-.08);
      segmentEnd=null;
    }
  });
  video.addEventListener('play',setPlayingUI);
  video.addEventListener('pause',setPlayingUI);
  video.addEventListener('ended',()=>{
    fullSequence=false;
    segmentEnd=null;
    play.textContent='Replay sequence';
    status.textContent='Sequence complete';
    overlay.classList.remove('is-hidden');
  });
  video.addEventListener('loadedmetadata',()=>{
    setActive(stages[0]);
    progress.style.width='0%';
    setPlayingUI();
  });

  setActive(stages[0]);
  setPlayingUI();
})();
