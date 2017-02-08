$(".item-carousel").each(function(i){
	$(this).css("position","absolute")
	$(this).css("left",i * 300)
})


var pos = 0;
var pos_max = $(".item-carousel").length - 1;
var pos_min = 0;
$(".left-arrow").click(function(){
    if (pos > pos_min){
        pos--;
    }
    else {
        $(this).addClass("buzz")
        updateAnimationListeners()
    }
        coordenada = pos * 300;
        $(".carousel div").css("-webkit-transform", `translateX(${coordenada}px)`)
})
$(".right-arrow").click(function(){
    if (pos < pos_max){
        pos++;
    }
    else{
        $(this).addClass("buzz")
        updateAnimationListeners()
    }
        coordenada = pos * 300 * -1;
        $(".carousel div").css("-webkit-transform", `translateX(${coordenada}px)`)
})

var updateAnimationListeners = function(){
    // Atualiza o sensor de fim de animação para todos os elemetos atualmente na classe buzz
    $('.buzz').bind('webkitAnimationEnd', function(){
        $(this).removeClass("buzz")
        console.log("Atualizou!")
    });
};
