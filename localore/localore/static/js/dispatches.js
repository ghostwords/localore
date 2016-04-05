$(function() {

  var $modal = $('#dispatch');
  var $modalBody = $modal.find('.modal-body');
  var $prev = $modal.find('.dispatch-prev');
  var $next = $modal.find('.dispatch-next');

  var loadDispatch = function(data, item) {

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

    // change URL
    window.history.pushState("", data.title, item);

    // embed new content
    $modalBody.html(data.embed_html);

    // show the modal
    $modal.modal('show');
  };

  var getUrlParameter = function(sParam) {
      var sPageURL = decodeURIComponent(window.location.search.substring(1)),
          sURLVariables = sPageURL.split('&'),
          sParameterName,
          i;

      for (i = 0; i < sURLVariables.length; i++) {
          sParameterName = sURLVariables[i].split('=');

          if (sParameterName[0] === sParam) {
              return sParameterName[1] === undefined ? true : sParameterName[1];
          }
      }
  };

  var item = getUrlParameter("dispatch");
  if(item) {
    $.getJSON(item + "?json", function(data) { loadDispatch(data, item); });
  }

  $('.post-item-link, .dispatch-arrow').on('click', function() {
    var item = $(this).attr("href");
    $.getJSON(item + "?json", function(data) { loadDispatch(data, item); });
    return false;
  });

  $modal.on('hide.bs.modal', function (e) {
    $(document).off("keydown.dispatch");
    $modalBody.empty();
  });





});
