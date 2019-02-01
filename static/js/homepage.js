console.log("homepage.js connected");

// code for search area border and dropdown----------------------------
$(".search_bar").children("input").focus(function(){
    $(this).parent(".search_bar").css("border", "2px solid rgb(10, 177, 177)");
});
$(".search_bar").children("input").blur(function(){
    $(this).parent(".search_bar").css("border", "2px solid rgb(129, 129, 129)");
});

// code for hover effect on category block -------------------------------------
$(".category_block_col").hover(function(){
    $(this).children("a").children(".category_name").addClass("block_visiblity");
}, function(){
    $(this).children("a").children(".category_name").removeClass("block_visiblity");
});