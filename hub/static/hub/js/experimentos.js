$(document).ready(function(){
    $(".controle-overflow").css("height", $(".conteudo").css("height"))

    var globalScrollTop = 0
    $(".seletor").scroll(function(){
        $("#scroll").scrollTop($(".seletor").scrollTop())
    })
    $("#scroll").scroll(function(){
        // $(".seletor").scrollTop($("#scroll").scrollTop())
        $("#scroll").scrollTop($(".seletor").scrollTop())
    })
})
