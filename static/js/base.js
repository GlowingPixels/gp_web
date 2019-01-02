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

$(".navbar-brand").hover(()=>{
	var randcolor = randomcolor();
	var time = 0;
	for(var i=1; i<=13; i++){
		var id = "#let" + String(i);
		time = time +170;
		$(id).css('transition',String(time) + "ms");
		$(id).css('color', String(randcolor));
		// $(id).css({textShadow: String(randcolor) + " 0 0 3px"});
	}
});

// Code for changing color of whole navbar-brand

// $(".navbar-brand").hover(()=>{
// 	var randcolor = randomcolor();
// 	$(".navbar-brand").css('color', String(randcolor));
// });

// code for changing color of catagory

// $(".dropdown").hover(()=>{
// 	var randcolor2 = randomcolor();
// 	$("#cato").css('color', String(randcolor2));
// 	$("#underln").css('border-bottom',"3px solid " + String(randcolor2));
// },()=>{
// 	$("#cato").css('color', "black");
// 	$("#underln").css('border-bottom',"3px solid black");
// });



// random color generator
function randomcolor()  {
    var r = Math.floor(Math.random() * 256);
    var g = Math.floor(Math.random() * 256);
    var b = Math.floor(Math.random() * 256);
    return "rgb("+r+", "+g+", "+b+")"
}