console.log("signup.js connected");

// input border on focus
$(".row").children("input").focus(function() {
    $(this).parent(".row").css('border', '2px solid #2196f3');
});
$(".row").children("input").blur(function() {
    $(this).parent(".row").css('border', '2px solid white');
});