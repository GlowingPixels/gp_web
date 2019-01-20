console.log("homepage.js connected");

// thumbanils hover effects
if (window.matchMedia("(max-resolution: 192dpi)").matches) {
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
}

// img zoom in-out code
$(".backLay").click(function() {
      var src = $( this ).parent('.enlarge').siblings(".imgThumbnails").attr('src_full');
      // var byName = $(this).parent('.enlarge').siblings('.postBy').children('a').children('span').html();
      $('.zoomImg').children('img').attr('src', src);
      //$('.zoomImg').children('.afterZoomName').children('a').children('span').html(byName);
      $('.zoomImg').fadeIn();
      $(".overlay").fadeIn();
      $('body').css('overflow', 'hidden');
      // console.log("clicked");
      // console.log(byName);
});

$(".overlay").click(()=>{
      $(".overlay").fadeOut();
      $('.zoomImg').fadeOut();
      $('body').css('overflow', 'visible');
});

//code only for phones  
if (window.matchMedia("(min-resolution: 192dpi)").matches) {
    //code for resizing of img in phone mode
    $(".col-u").each(function(index){
      var fullsrc = $(this).children(".imgThumbnails").attr("src_full");
      $(this).children('.imgThumbnails').attr('src', fullsrc);
    });

    // img zoom in-out code
    $(".imgThumbnails").click(function() {
      var src = $( this ).attr('src_full');
      // var byName = $(this).parent('.enlarge').siblings('.postBy').children('a').children('span').html();
      $('.zoomImg').children('img').attr('src', src);
      // $('.zoomImg').children('.afterZoomName').children('a').children('span').html(byName);
      $('.zoomImg').fadeIn();
      $(".overlay").fadeIn();
      $('body').css('overflow', 'hidden');
      //console.log("clicked");
      //console.log(byName);
    });   
    
    //code for dblclick love react
    $(".imgThumbnails").dblclick(()=>{
      console.log("dblclicked");
      $(".lovedBtn").addClass("afterLoved");
    });
}


//AJAX call for the love React Implementation
$(()=>{
  $('.lovedBtn').click(function(){ 
      var id = String($( this ).attr('id'));
      $.ajax({
          type: "GET",
          url: id,
          data: {},
          dataType: "html",
          success: (res,status,xhr)=> {
            $(this).toggleClass("afterLoved");
          }
      });
  });
});

$(()=>{
  $(".lovedBtn").each(function(e){
    var id = String($( this ).attr('id'))+"check/";    
    $.ajax({
      type: "GET",
      url: id,
      data: {},
      dataType: "html",
      success: (res,status,xhr)=> {
        if(res=="True"){
          $(this).addClass("afterLoved");
        }
      }
    });
  });
});