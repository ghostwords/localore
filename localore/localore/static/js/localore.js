$(function() {

  // jQuery.easing['jswing'] = jQuery.easing['swing'];

  jQuery.extend( jQuery.easing,
  {
      easeOutCirc: function (x, t, b, c, d) {
          return c * Math.sqrt(1 - (t=t/d-1)*t) + b;
      }
  });

  $(".view-more").click(function() {
    $('html, body').animate({
        scrollTop: $("#livefeed").offset().top
    }, 600, 'easeOutCirc');
  });


});
