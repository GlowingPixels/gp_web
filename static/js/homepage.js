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
      var id = $( this ).parent('.enlarge').siblings('a').children(".imgThumbnails").attr('id');
      var src = $( this ).parent('.enlarge').siblings('a').children(".imgThumbnails").attr('src_full');
      console.log(id);
      console.log(src);
      $('.zoomImg').children('img').attr('src', src);

  });
