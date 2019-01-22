console.log("login.js connected");

//code for input focus
$(".form-group").children("input").focus(function() {
    $(this).parent(".form-group").css('border', '2px solid #2196f3');
});
$(".form-group").children("input").blur(function() {
    $(this).parent(".form-group").css('border', '2px solid white');
});

//code for color border on error
$(".signupBtn").click(function(){
    var passNotMatch = $(".password2").children("input").attr("placeholder");
    console.log("click");
});