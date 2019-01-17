console.log("homepage.js connected");

// thumbanils hover effects
$(".col-u").hover(
    function() {
      $(this).children('img').css("filter", "brightness(70%)");
      $(this).children('.enlarge').children('.backLay').fadeIn();
      $(this).css("bottom", "2px");
    }, function() {
      $(this).children('img').css("filter", "brightness(100%)");
      $(this).children('.enlarge').children('.backLay').fadeOut();
      $(this).css("bottom", "0");
    }
  );

  // img zoom in-out code
  $(".backLay").click(function() {
      var src = $( this ).parent('.enlarge').siblings(".imgThumbnails").attr('src_full');
      var byName = $(this).parent('.enlarge').siblings('.postBy').children('a').children('span').html();
      $('.zoomImg').children('img').attr('src', src);
      $('.zoomImg').children('.afterZoomName').children('a').children('span').html(byName);
      $('.zoomImg').fadeIn();
      $(".overlay").fadeIn();
      $('body').css('overflow', 'hidden');
      console.log("clicked");
      console.log(byName);
  });

  $(".overlay").click(()=>{
      $(".overlay").fadeOut();
      $('.zoomImg').fadeOut();
      $('body').css('overflow', 'visible');
  });

  //for phones  
  if (window.matchMedia("(min-resolution: 192dpi)").matches) {
    $(".col-u").each(()=>{
      var fullsrc = $(this).children('.imgThumbnails').attr('src_full');
      console.log(fullsrc);
      $(this).children('.imgThumbnails').attr('src', fullsrc);
    });  
  }
