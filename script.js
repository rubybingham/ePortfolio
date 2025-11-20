// Small helper: if local video is not available, show a notice in console and keep YouTube visible.
(function(){
  const vid = document.getElementById('localVideo');
  if(!vid) return;
  // check if source is reachable (basic): load metadata and catch error
  vid.addEventListener('error', function(e){
    console.warn('Local video failed to load. Make sure you put your video at assets/video.mp4 or update the <source> in index.html.');
  });

  // keyboard shortcut: press 'k' to play/pause focused video
  window.addEventListener('keydown', function(e){
    if(e.key === 'k' || e.key === 'K'){
      if(document.activeElement === vid || vid.contains(document.activeElement)){
        if(vid.paused) vid.play(); else vid.pause();
      }
    }
  });
})();