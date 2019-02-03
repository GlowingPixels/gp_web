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

// code for color toggle on clicking list_items
$(".list_items").click(function(){
    $(this).children("span").toggleClass("change_color");
});

// code for showing and unshowing sub-category
$(".list_items").click(function(){
    $(this).children(".sub_category").slideToggle();
});

// code for footer
$(".details_sections_col").children("ul").children("li").children("a").hover(function(){
    $(this).children("i").css("opacity", "1");
},function(){
    $(this).children("i").css("opacity", "0");
});

