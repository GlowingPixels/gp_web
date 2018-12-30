//code for on click zoom function

var card =  document.querySelector(".stuffEnlarge");

for(var i=0; i<6; i++)  {
    card.addEventListener("click", function(){
        this.classList.add('showZoom');
    });
}

