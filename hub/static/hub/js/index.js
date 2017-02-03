$(document).ready(function(){
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
            coordenada = pos * 300;
            $(".carousel div").css("-webkit-transform", `translateX(${coordenada}px)`)
    })
    $(".right-arrow").click(function(){
        if (pos < pos_max){
            pos++;
        }
            coordenada = pos * 300 * -1;
            $(".carousel div").css("-webkit-transform", `translateX(${coordenada}px)`)
    })
})
