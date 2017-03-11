$("#id_corpo_texto").on('input', function() {
    $("#text_container").text($("#id_corpo_texto").val()).trigger("change");
});

$("#chamar_ajax").click(function () {
  var corpo_texto = $("#id_corpo_texto").val();
  var formulario = $("#id_corpo_texto").closest("form");
  $.ajax({
    url: formulario.attr("data-ajax-url"),
    data:  formulario.serialize(),
    dataType: 'json',
    success: function (data) {
      console.log(`Datas encontradas: ${data.datas}\n\nHoras encontradas: ${data.horas}`)
  },
      error : function(xhr,errmsg,err) {
              console.log(errmsg);
          }
  });

});
$("#text_container").on("change", function(){
    $.ajax({
      url: "/apps_python/autoclado/buscar_sugestoes",
      data:  {"texto_completo":$("#text_container").text()},
      dataType: 'json',
      success: function (data) {
          $(".wrapper").empty();
          console.log(data)
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

});

var chamar = function(){
    $.ajax({
      url: "/apps_python/autoclado/reconhecer_palavras",
      data:  {"texto_completo":$("#text_container").text()},
      dataType: 'json',
      success: function (data) {
        console.log(data)
    },
        error : function(xhr,errmsg,err) {
                console.log(errmsg);
            }
    });
}
