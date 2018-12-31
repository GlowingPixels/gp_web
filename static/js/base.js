// code for scrooling effect

$(function(){
	var navbar = $('.navbar');
	
	$(window).scroll(function(){
		if($(window).scrollTop() <= 100){
			navbar.removeClass('navbar-scroll');
		} else {
			navbar.addClass('navbar-scroll');
		}
	});
});

// code for changing color for each letter of navbar-brand

//var brandname = $("#colorchange").text();
// $(".navbar-brand").hover(()=>{
// 	for(var i=1; i<=13; i++){
// 		var id = "#let" + String(i);
// 		var randcolor = randomcolor();
// 		$(id).css('color', String(randcolor));
// 		// $(id).css({textShadow: String(randcolor) + " 0 0 3px"});
// 		console.log("count");
// 	}
// });

// Code for changing color of hole navbar-brand
$(".navbar-brand").hover(()=>{
	var randcolor = randomcolor();
	$(".navbar-brand").css('color', String(randcolor));
});



// random color generator
function randomcolor()  {
    var r = Math.floor(Math.random() * 256);
    var g = Math.floor(Math.random() * 256);
    var b = Math.floor(Math.random() * 256);
    return "rgb("+r+", "+g+", "+b+")"
}