$(document).ready(function(){
    var pos = 0;
    var pos_max = 1;
    var pos_min = 0;
    $(".left-arrow").click(function(){
        if (pos > pos_min){
            pos--;
        }
            coordenada = pos * 120;
            $(".carousel div").css("-webkit-transform", `translateX(${coordenada}px)`)
    })
    $(".right-arrow").click(function(){
        if (pos < pos_max){
            pos++;
        }
            coordenada = pos * 120 * -1;
            $(".carousel div").css("-webkit-transform", `translateX(${coordenada}px)`)
    })
})
