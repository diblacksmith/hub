$("#id_corpo_texto").on('input', function() {
    $("#text_container").text($("#id_corpo_texto").val()).trigger("change");
});

var receber_sugestoes = function(){
    $.ajax({
      url: "/apps_python/autoclado/buscar_sugestoes",
      data:  {"texto_completo":$("#text_container").text()},
      dataType: 'json',
      success: function (data) {
          $(".wrapper").empty();
          data.resultado.forEach(function(i){
              $(".wrapper").append(`<div class="item-selecionavel">${i[0]}</div>`);
          })
    },
        error : function(xhr,errmsg,err) {
                console.log(errmsg);
                console.log(xhr);
                console.log(err);
            }
    });

}

$("#text_container").on("change", receber_sugestoes);

$(".botao-grande").click(function(){
    $.ajax({
      url: "/apps_python/autoclado/reconhecer_palavras",
      data:  {"texto_completo":$("#text_container").text()},
      dataType: 'json',
      success: function (data) {
        receber_sugestoes();
    },
        error : function(xhr,errmsg,err) {
                console.log(errmsg);
            }
    });
});
