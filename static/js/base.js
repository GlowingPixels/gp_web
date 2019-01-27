console.log("homepage.js connected");

// code for category slide in/out
$(".burger_icon").click(function(){
    $(".category_container").css("display", "block");
});
$(".screen_side").click(function(){
    $(".category_container").css("display", "none");
});
