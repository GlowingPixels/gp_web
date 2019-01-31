console.log("homepage.js connected");

// code for search area border and dropdown----------------------------
$(".search_bar").children("input").focus(function(){
    $(this).parent(".search_bar").css("border", "2px solid rgb(10, 177, 177)");
});
$(".search_bar").children("input").blur(function(){
    $(this).parent(".search_bar").css("border", "2px solid rgb(129, 129, 129)");
});

// code for img block ---------------------------------------------------
//code that will run only on page reload
// var categoryBlockWidth = $(".category_block_col").width();
// console.log(categoryBlockWidth);
// $(".category_block_col").css("height", String(categoryBlockWidth));
// // code that will run on page resize
// $(window).on('resize', function(){
//     var categoryBlockWidth = $(".category_block_col").width();
//     console.log(categoryBlockWidth);
//     $(".category_block_col").css("height", String(categoryBlockWidth));    
// });