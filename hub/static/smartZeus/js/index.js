$("#chamar_ajax").click(function () {
  var corpo_texto = $("#id_corpo_texto").val();
  var formulario = $("#id_corpo_texto").closest("form");
  $.ajax({
    url: formulario.attr("data-ajax-url"),
    data:  formulario.serialize(),
    dataType: 'json',
    success: function (data) {
      console.log(data.corpo_texto)
    }
  });

});
