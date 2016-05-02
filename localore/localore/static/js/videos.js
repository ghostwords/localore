$(function() {

  var $play = $('.play-icon');
  var $viewMore = $('.view-more');
  var $mainVideo = $('#main-video');
  var mainVideoPlayer, videoPlaying = false;
  var $preview = $('#preview');
  var $title = $('#title');
  var $header = $('header');

  var timeout;
  $(document).on('mousemove', function (event) {
      if (timeout !== undefined) {
          window.clearTimeout(timeout);
      }
      timeout = window.setTimeout(function () {
          // trigger the new event on event.target, so that it can bubble appropriately
          $(event.target).trigger('mousemoveend');
      }, 2000);
  });

  window.onYouTubePlayerAPIReady = function() {
    console.log('yt ready 1');
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
    console.log('yt ready 2');
    $play.addClass('show');
  };

  window.onPlayerStateChange = function(event) {
    // video cued
    if(event.data === -1) {
      // console.log('cued');
    }
    // video playing
    else if (event.data === 1) {
      // console.log('play');
      $play.addClass('pause');
      if(!window.IS_360_VIDEO) $('.hero-section').append('<div id="video-overlay"></div>');
      else {
        $play.removeClass('show');
        $viewMore.addClass('hide');
        $title.fadeOut(600);
        $header.fadeOut(600);
      }
      videoPlaying = true;
    }
    // video paused
    else if (event.data === 2) {
      // console.log('paused');
      $play.removeClass('pause').addClass('show');
      $viewMore.removeClass('hide');
      if(!window.IS_360_VIDEO) $('#video-overlay').remove();
      else {
        $play.addClass('show');
        $viewMore.removeClass('hide');
        $title.fadeIn(600);
        $header.fadeIn(600);
      }
      videoPlaying = false;
    }
    // video ended
    else if (event.data === 0) {
      if(!window.IS_360_VIDEO) $('#video-overlay').remove();
      $viewMore.removeClass('hide');
      $title.fadeIn(600);
      $header.fadeIn(600);
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
    $title.fadeIn(600);
    $header.fadeIn(600);
  });
  $('.hero-section').on("mousemoveend", "#video-overlay", function () {
    $play.removeClass('show');
    $viewMore.addClass('hide');
    $title.fadeOut(600);
    $header.fadeOut(600);
  });

  $play.one('click', function(e) {

    $preview.fadeOut(1000);
    $mainVideo.addClass('playing');
    $play.removeClass('show');
    $viewMore.addClass('hide');

    if(!jQuery.browser.mobile) {
      $title.fadeOut(600);
      $header.fadeOut(600);
      toggleMainVideo();
      $(this).on('click', function() { toggleMainVideo(); });
    }

  });


});
