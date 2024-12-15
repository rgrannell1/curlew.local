function attachPauseOtherVideosListener() {
  const videos = document.querySelectorAll('video');

  videos.forEach(video => {
      video.addEventListener('play', () => {
      videos.forEach(otherVideo => {
          if (otherVideo !== video) {
              otherVideo.pause();
          }
      });
      });
  });
}

attachPauseOtherVideosListener();
