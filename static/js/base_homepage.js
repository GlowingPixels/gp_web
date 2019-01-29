console.log("base.js connected");

// code for category slide in/out
$(".burger_icon").click(function(){
    $(".screen_side").fadeIn();
    $(".category_side").css("left", "0%");
});
$(".screen_side").click(function(){
    $(".screen_side").fadeOut();
    $(".category_side").css("left", "-80%");
});
