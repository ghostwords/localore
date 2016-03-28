$(function() {

  var $play = $('.play-icon');
  var $viewMore = $('.view-more');
  var $mainVideo = $('#main-video');
  var $previewVideo = $('#preview-video');
  var previewVideoPlayer = $('#preview-video').data('vide').getVideoObject();
  var mainVideoPlayer, videoPlaying = false;

  var timeout;
  $(document).on('mousemove', function (event) {
      if (timeout !== undefined) {
          window.clearTimeout(timeout);
      }
      timeout = window.setTimeout(function () {
          // trigger the new event on event.target, so that it can bubble appropriately
          $(event.target).trigger('mousemoveend');
      }, 1000);
  });
  // $.fn.mousemoveend = function (cb) {
  //     return this.on('mousemoveend', cb);
  // });

  window.onYouTubePlayerAPIReady = function() {
    mainVideoPlayer = new YT.Player('youtube-embed', {
      videoId: 'j6IIjLK-8fU',
      playerVars: {
        modestbranding: '1',
        rel: '0',
        showinfo: '0',
        color: 'white',
        controls: '0'
      },
      events: {
        'onStateChange': onPlayerStateChange
      }
    });
    $play.addClass('show');
  }

  // when video ends
  window.onPlayerStateChange = function(event) {
    if(event.data === 0) {
      // $mainVideo.modal('hide');
    }
  }

  var toggleMainVideo = function() {
    console.log('toggle', videoPlaying);
    if(!videoPlaying) {
      mainVideoPlayer.playVideo();
      $play.addClass('pause');
    } else {
      mainVideoPlayer.pauseVideo();
      $play.removeClass('pause');
    }
    videoPlaying = !videoPlaying;
  };

  $('.hero-section').on("mousemove", "#video-overlay", function () {
    $play.addClass('show');
    $viewMore.removeClass('hide');
  });
  $('.hero-section').on("mousemoveend", "#video-overlay", function () {
    $play.removeClass('show');
    $viewMore.addClass('hide');
  });


  $play.one('click', function(e) {
    $previewVideo.fadeOut(1000);
    $mainVideo.addClass('playing');
    toggleMainVideo();
    $play.removeClass('show');
    $viewMore.addClass('hide');
    $('.hero-section').append('<div id="video-overlay"></div>');
    // $('#video-overlay').mouseover(function () {
    //   console.log('fuck');
    // });
    //console.log(e);

    // $(document).on('mousemove', function () {
    //   console.log('hello');
    // });

    $(this).on('click', function() {
      toggleMainVideo();
    });

  });
  //
  // $homeVideo.on('show.bs.modal', function (e) {
  //   player.playVideo();
  //   vide.pause();
  // });
  //
  // $homeVideo.on('hide.bs.modal', function (e) {
  //   player.pauseVideo();
  //   vide.play();
  // });


});
