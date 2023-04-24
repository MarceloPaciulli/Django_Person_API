$(document).ready( function () {
    $('#personas').DataTable();
} );

var csrftoken = $("[name=csrfmiddlewaretoken]").val();

$.ajaxSetup({
    beforeSend: function(xhr, settings) {
        xhr.setRequestHeader("X-CSRFToken", csrftoken);
    }
});






