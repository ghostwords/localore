$(function() {



  // function _testCSS(prop) {
  //     return prop in document.documentElement.style;
  // }

  /**
   * jQuery.browser.mobile (http://detectmobilebrowser.com/)
   *
   * jQuery.browser.mobile will be true if the browser is a mobile device
   *
   **/
  (function(a){(jQuery.browser=jQuery.browser||{}).mobile=/(android|bb\d+|meego).+mobile|avantgo|bada\/|blackberry|blazer|compal|elaine|fennec|hiptop|iemobile|ip(hone|od)|iris|kindle|lge |maemo|midp|mmp|mobile.+firefox|netfront|opera m(ob|in)i|palm( os)?|phone|p(ixi|re)\/|plucker|pocket|psp|series(4|6)0|symbian|treo|up\.(browser|link)|vodafone|wap|windows ce|xda|xiino/i.test(a)||/1207|6310|6590|3gso|4thp|50[1-6]i|770s|802s|a wa|abac|ac(er|oo|s\-)|ai(ko|rn)|al(av|ca|co)|amoi|an(ex|ny|yw)|aptu|ar(ch|go)|as(te|us)|attw|au(di|\-m|r |s )|avan|be(ck|ll|nq)|bi(lb|rd)|bl(ac|az)|br(e|v)w|bumb|bw\-(n|u)|c55\/|capi|ccwa|cdm\-|cell|chtm|cldc|cmd\-|co(mp|nd)|craw|da(it|ll|ng)|dbte|dc\-s|devi|dica|dmob|do(c|p)o|ds(12|\-d)|el(49|ai)|em(l2|ul)|er(ic|k0)|esl8|ez([4-7]0|os|wa|ze)|fetc|fly(\-|_)|g1 u|g560|gene|gf\-5|g\-mo|go(\.w|od)|gr(ad|un)|haie|hcit|hd\-(m|p|t)|hei\-|hi(pt|ta)|hp( i|ip)|hs\-c|ht(c(\-| |_|a|g|p|s|t)|tp)|hu(aw|tc)|i\-(20|go|ma)|i230|iac( |\-|\/)|ibro|idea|ig01|ikom|im1k|inno|ipaq|iris|ja(t|v)a|jbro|jemu|jigs|kddi|keji|kgt( |\/)|klon|kpt |kwc\-|kyo(c|k)|le(no|xi)|lg( g|\/(k|l|u)|50|54|\-[a-w])|libw|lynx|m1\-w|m3ga|m50\/|ma(te|ui|xo)|mc(01|21|ca)|m\-cr|me(rc|ri)|mi(o8|oa|ts)|mmef|mo(01|02|bi|de|do|t(\-| |o|v)|zz)|mt(50|p1|v )|mwbp|mywa|n10[0-2]|n20[2-3]|n30(0|2)|n50(0|2|5)|n7(0(0|1)|10)|ne((c|m)\-|on|tf|wf|wg|wt)|nok(6|i)|nzph|o2im|op(ti|wv)|oran|owg1|p800|pan(a|d|t)|pdxg|pg(13|\-([1-8]|c))|phil|pire|pl(ay|uc)|pn\-2|po(ck|rt|se)|prox|psio|pt\-g|qa\-a|qc(07|12|21|32|60|\-[2-7]|i\-)|qtek|r380|r600|raks|rim9|ro(ve|zo)|s55\/|sa(ge|ma|mm|ms|ny|va)|sc(01|h\-|oo|p\-)|sdk\/|se(c(\-|0|1)|47|mc|nd|ri)|sgh\-|shar|sie(\-|m)|sk\-0|sl(45|id)|sm(al|ar|b3|it|t5)|so(ft|ny)|sp(01|h\-|v\-|v )|sy(01|mb)|t2(18|50)|t6(00|10|18)|ta(gt|lk)|tcl\-|tdg\-|tel(i|m)|tim\-|t\-mo|to(pl|sh)|ts(70|m\-|m3|m5)|tx\-9|up(\.b|g1|si)|utst|v400|v750|veri|vi(rg|te)|vk(40|5[0-3]|\-v)|vm40|voda|vulc|vx(52|53|60|61|70|80|81|83|85|98)|w3c(\-| )|webc|whit|wi(g |nc|nw)|wmlb|wonu|x700|yas\-|your|zeto|zte\-/i.test(a.substr(0,4))})(navigator.userAgent||navigator.vendor||window.opera);

  // window.browser = { isOpera : false, isFirefox : false, isSafari : false, isChrome : false, isIE : false };
  // jQuery.browser.isOpera = !!(window.opera && window.opera.version);  // Opera 8.0+
  // jQuery.browser.isFirefox = _testCSS('MozBoxSizing');                 // FF 0.8+
  // jQuery.browser.isSafari = Object.prototype.toString.call(window.HTMLElement).indexOf('Constructor') > 0;
  // jQuery.browser.isChrome = !this.browser.isSafari && _testCSS('WebkitTransform');  // Chrome 1+
  // jQuery.browser.isIE = /*@cc_on!@*/false || _testCSS('msTransform');  // At least IE6


  /**
   *    UTIL
   **/

  jQuery.extend( jQuery.easing,
  {
      easeOutCirc: function (x, t, b, c, d) {
          return c * Math.sqrt(1 - (t=t/d-1)*t) + b;
      }
  });

  FastClick.attach(document.body);

  $(document).on('focus', '.accessible',function(){
    var $this = $(this);
    $(document).on('keyup.access', function(e){
        if(e.which==13 || e.which==32) {  $this.click(); }
    });
  });
  $(document).on('focusout', '.accessible',function(){
    $(document).off('keyup.access');
  });

  $(document).on('click', '.accessible',function(){
    $(this).addClass('clicked');
  });

  var lastScrollTop = window.pageYOffset || document.documentElement.scrollTop;
  var hasShrunkHeader = false;
  var isScrollingUp = false;
  var scrollUpStart, scrollUpDist;
  var scrollUpThreshold = 1500;
  var threshold = 125;
  var windowWidth;
  var $title = $('.title-about');
  var $header = $('header').not('.template-homepage header');

  $(window).resize(function() { windowWidth = $(this).width(); }).trigger('resize');

  $(window).scroll(function() {
     var st = window.pageYOffset || document.documentElement.scrollTop; // Credits: "https://github.com/qeremy/so/blob/master/so.dom.js#L426"

     if(st > lastScrollTop) {
       isScrollingUp = false;
       scrollUpStart = scrollUpDist = 0;
     } else if(!isScrollingUp) {
       isScrollingUp = true;
       scrollUpStart = st;
     } else {
       scrollUpDist = scrollUpStart - st;
     }


     if(st > lastScrollTop && st > threshold && windowWidth >= 925 && !hasShrunkHeader) {
       $title.addClass('scrolled');
       $header.addClass('scrolled');
       hasShrunkHeader = true;
     } else if((st < lastScrollTop && hasShrunkHeader && scrollUpDist > scrollUpThreshold) || st == 0) {
       $title.removeClass('scrolled');
       $header.removeClass('scrolled');
       hasShrunkHeader = false;
     }

     lastScrollTop = st;
  });

  /**
   *    INTRO
   **/
  function setCookie(c_name, value, exdays) {
    var exdate = new Date();
    exdate.setDate(exdate.getDate() + exdays);
    var c_value = escape(value) + ((exdays == null) ? "" : "; expires=" + exdate.toUTCString());
    document.cookie = c_name + "=" + c_value;
  }

  function getCookie(c_name) {
    var i, x, y, ARRcookies = document.cookie.split(";");
    for (i = 0; i < ARRcookies.length; i++) {
      x = ARRcookies[i].substr(0, ARRcookies[i].indexOf("="));
      y = ARRcookies[i].substr(ARRcookies[i].indexOf("=") + 1);
      x = x.replace(/^\s+|\s+$/g, "");
      if (x == c_name) {
        return unescape(y);
      }
    }
  }

  // console.log(window.location.pathname);
  if(!getCookie('has_visited') && window.location.pathname == '/') {
    setCookie('has_visited', 'true', 30);
    $('body').addClass('intro');
    $('#intro').css("display", "block");
    $('.intro-section').addClass('show');
  }

  $('#intro, .intro-enter-btn').click(function () {
    $('.intro-section').removeClass('show');
    setTimeout(function(){
      $('body').removeClass('intro');
      $('#intro').css("display", "none");
    }, 750);
  });

  $('.intro-section').click(function (e) {
    e.stopPropagation();
  });



  /**
   *    HOMEPAGE
   **/

  $(".view-more").click(function() {
    $('html, body').animate({
        scrollTop: $(window).height()
    }, 600, 'easeOutCirc');
    $(this).blur();
  });

  window.checkViewHeight = function() {
    // console.log('juicer loaded');
    if(window.location.hash.substr(1) === "livefeed") $(".view-more").click();
  };




  /**
   *    SITE SEARCH
   **/

  $('#search').on('shown.bs.modal', function (e) {
    $( "#site-search-text" ).focus();
  });

  $('#site-search').submit(function (e) {

    var query = $('#site-search-text').val();
    var $results = $('.search-results');

    // $.getJSON('https://demo.finding-america.com/search/?query=' + query + '&json=true', function(data) {
    $.getJSON('/search/?query=' + query + '&json=true', function(data) {

      if(data.search_results.length) {
        console.log(data);
        $results.empty();
        $.each(data.search_results, function (i, v) {
          $results.append('<div class="search-results-item"><span>' + v.content_type + '</span><a href="' + v.url + '"><h5>' + v.title + '</h5></a></div>');
        });
      } else {
        $results.html('<p>Nothing found, apologies!</p>');
      }
    });

    return false;
  });




  /**
   *    PRODUCTION DETAILS
   **/

  //  $(window).load(function () {
  //   $(window).resize(function() { $('.prod-description').css("margin-bottom", $('.prod-team').height()); }).trigger('resize');
  //  });

   setTimeout(function () {
     $(window).resize(function() { $('.prod-description').css("margin-bottom", $('.prod-team').height()); }).trigger('resize');
   }, 10);



  /**
   *    ABOUT - TEAM
   **/

   if(jQuery.browser.mobile) {
     $('.about-team-member').collapse('hide');
   }





});
