$(function() {

  var $modal = $('#dispatch');
  var $modalBody = $modal.find('.modal-body');
  var $prev = $modal.find('.dispatch-prev');
  var $next = $modal.find('.dispatch-next');

  var loadDispatch = function(data) {
    $next.removeClass('show');
    $prev.removeClass('show');
    if(data.prev_url) $prev.addClass('show').attr("data-item", data.prev_url);
    if(data.next_url) $next.addClass('show').attr("data-item", data.next_url);
    $modalBody.html(data.embed_html);
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
    $.getJSON(item + "?json", function(data) { loadDispatch(data); });
  }



  $('.post-item-link, .dispatch-arrow').on('click', function() {
    var item = $(this).attr("data-item");
    $.getJSON(item, function(data) { loadDispatch(data); });
  });

  $modal.on('hide.bs.modal', function (e) {
    $modalBody.empty();
  });




});
