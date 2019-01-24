console.log("profile.js connected");

// settings hover effects
$(".fa-cog").hover(
    ()=>{
        $(".fa-cog").css('transform', 'rotate(90deg)');
    },()=>{
        $(".fa-cog").css('transform', 'rotate(0deg)');
    }
);

$(".fa-pencil-alt").click(function () {
    $(".picEdit").fadeToggle();
});

//code for color changing with time interval
setInterval(function(){
    var randcolor = randomcolor();
    $(".fa-plus").css("color", String(randcolor));
    $(".contributeArea").css("box-shadow", "0 0 1px " +  String(randcolor));
}, 3000);

// random color generator
function randomcolor()  {
    var r = Math.floor(Math.random() * 256);
    var g = Math.floor(Math.random() * 256);
    var b = Math.floor(Math.random() * 256);
    return "rgba("+r+", "+g+", "+b+")"
}
