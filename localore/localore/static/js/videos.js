$(function() {

  var $play = $('.play-icon');
  var $viewMore = $('.view-more');
  var $mainVideo = $('#main-video');
  var mainVideoPlayer, videoPlaying = false;
  var $preview = $('#preview');

  var timeout;
  $(document).on('mousemove', function (event) {
      if (timeout !== undefined) {
          window.clearTimeout(timeout);
      }
      timeout = window.setTimeout(function () {
          // trigger the new event on event.target, so that it can bubble appropriately
          $(event.target).trigger('mousemoveend');
      }, 650);
  });

  // console.log(window.YOUTUBE_ID);

  window.onYouTubePlayerAPIReady = function() {
    console.log('yt ready');
    mainVideoPlayer = new YT.Player('youtube-embed', {
      videoId: window.YOUTUBE_ID,
      playerVars: {
        modestbranding: '1',
        rel: '0',
        showinfo: '0',
        color: 'white',
        autohide: '0'
        // , controls: '0'
      },
      events: {
        'onReady': onReady,
        'onStateChange': onPlayerStateChange
      }
    });

  }

  window.onReady = function(event) {
    $play.addClass('show');
  };

  // when video ends
  window.onPlayerStateChange = function(event) {
    // video cued
    // console.log(event.data);
    if(event.data === -1) {
      console.log('cued');
      // toggleMainVideo(false);
    }
    // video playing
    else if (event.data === 1) {
      console.log('play');
      $play.addClass('pause');
      $('.hero-section').append('<div id="video-overlay"></div>');
      videoPlaying = true;
      // toggleMainVideo(false);
    }
    // video paused
    else if (event.data === 2) {
      console.log('paused');
      $play.removeClass('pause').addClass('show');
      $viewMore.removeClass('hide');
      $('#video-overlay').remove();
      videoPlaying = false;
      // toggleMainVideo(false);
    }
    // video ended
    else if (event.data === 0) {
      $('#video-overlay').remove();
      $viewMore.removeClass('hide');
      $('.after-link').addClass('show');
    }
  }

  var toggleMainVideo = function() {

    if(!videoPlaying) {
      if(mainVideoPlayer.playVideo == undefined) {
        setTimeout(function () { toggleMainVideo(); }, 100);
        return;
      }
      mainVideoPlayer.playVideo();
    } else {
      mainVideoPlayer.pauseVideo();
    }

  };

  $('.hero-section').on("mousemove", "#video-overlay", function () {
    $('#main-video').trigger('hover');
    $play.addClass('show');
    $viewMore.removeClass('hide');
  });
  $('.hero-section').on("mousemoveend", "#video-overlay", function () {
    $play.removeClass('show');
    $viewMore.addClass('hide');
  });

  $play.one('click', function(e) {

    $preview.fadeOut(1000);
    $mainVideo.addClass('playing');
    $play.removeClass('show');
    $viewMore.addClass('hide');

    if(!jQuery.browser.mobile) {
      toggleMainVideo();
      $(this).on('click', function() { toggleMainVideo(); });
    }

  });


});
