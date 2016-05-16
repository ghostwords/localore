$(function() {

  var $modal = $('#dispatch');
  var $modalBody = $modal.find('.modal-media-embed');
  var $prev = $modal.find('.dispatch-prev');
  var $next = $modal.find('.dispatch-next');
  var isLoadingDispatch = false;

  window.loadDispatch = function(data, item) {

    // clear prev/next arrows and apply new hrefs
    $next.removeClass('show');
    $prev.removeClass('show');
    if(data.prev_url) $prev.addClass('show').attr("href", data.prev_url);
    if(data.next_url) $next.addClass('show').attr("href", data.next_url);

    // set keydown events
    $(document).on("keydown.dispatch", function(evt) {
      evt = evt || window.event;
      switch (evt.keyCode) {
          case 37:
              if($prev.hasClass('show')) $prev.click();
              break;
          case 39:
              if($next.hasClass('show')) $next.click();
              break;
      }
    });

    // embed new content
    $modalBody.html(data.embed_html);

    // show the modal
    $modal.modal('show');
  };

  $('.post-item-link, .dispatch-arrow').on('click', function() {
    var item = $(this).attr("href");

    if(!isLoadingDispatch) {

      isLoadingDispatch = true;

      // TODO cache
      $.getJSON(item + "?json", function(data) {
        // update URL to dispatch page
        window.history.pushState("", data.title, item);
        loadDispatch(data, item);
        isLoadingDispatch = false;
      });
    }

    return false;
  });

  $modal.on('hide.bs.modal', function (e) {
    // update URL to dispatches index
    if (document.location.pathname != INDEX_PAGE.path) {
      window.history.pushState("", INDEX_PAGE.title, INDEX_PAGE.path);
    }

    $(document).off("keydown.dispatch");
    $modalBody.empty();
  });

  // handle browser back/forward navigation
  window.onpopstate = function (ev) {
    // if browser-initiated navigation
    if (!ev.state) {
      var path = document.location.pathname;

      // dispatches index
      if (path == INDEX_PAGE.path) {
        $modal.modal('hide');

      // dispatch
      } else {
        // TODO cache
        $.getJSON(path + "?json", function (data) {
          loadDispatch(data, path);
        });
      }
    }
  };

});
