console.log("homepage.js connected");

// code for search area border and dropdown------------------------------------
$(".search_bar").children("input").focus(function(){
    $(this).siblings(".search_result").slideDown();
});
$(".search_bar").children("input").blur(function(){
    $(this).siblings(".search_result").slideUp();
});

// code for hover effect on category block -------------------------------------
$(".category_block_col").hover(function(){
    $(this).children("a").children(".category_name").addClass("block_visiblity");
}, function(){
    $(this).children("a").children(".category_name").removeClass("block_visiblity");
});

// code to disable dowload-------------------------------------------------------
$(document).ready(function() {
    $(".category_block_col").bind('cut copy paste', function (e) {
     e.preventDefault();
    });
 });