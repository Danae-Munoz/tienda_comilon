$(document).ready(function() {

  $.get('https://fakestoreapi.com/products', // API donde se obtienen los datos

    function(registros){

      var premioHTML = $('#premio').prop('outerHTML');
      premioHTML = premioHTML.replace('d-none', '');

      $('#lista').empty();

      $.each(registros, function(i, item) {  // Recorrer los registros devueltos por la API

        // Crear el codigo HTML para agegar un recuadro a la lista de premios
        recuadro = premioHTML;
        recuadro = recuadro.replace('src=""', `src="${item.image}"`);
        recuadro = recuadro.replace('[[nombre]]', item.title);
        recuadro = recuadro.replace('[[precio]]', item.price);
        recuadro = recuadro.replace('[[descripcion]]', item.description);
        
        // Agregar el recuadro a la lista de premios
        $('#lista').append(recuadro);
      
    });

    setTimeout(`
      $('#imagen-de-espera').hide();
      $('#capa-cubre-todo').hide();
      `, 2000);

  });

});