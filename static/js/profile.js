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