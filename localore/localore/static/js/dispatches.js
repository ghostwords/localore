$(function() {

  var $modal = $('#dispatch');
  var $modalBody = $modal.find('.modal-body');

  $('.post-item-link').on('click', function() {
    var $this = $(this);
    var item = $this.data().item;

    $.getJSON(item, function(data) {
      $modalBody.html(data.embed_html);
      $modal.modal('show');
    });

  });

});
