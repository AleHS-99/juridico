function message_error(obj){
    var html = "<ul>";
    $.each(obj,function(key, value){
        if (Array.isArray(value)) {
            html += '<li>' + key + ': ' + value[0] + '</li>';
        } else if (typeof value === 'object') {
            // Si value es un objeto, accedemos a su primer valor
            var firstValue = Object.values(value)[0];
            html += '<li>' + key + ': ' + firstValue + '</li>';
        } else {
            html += '<li>' + key + ': ' + value + '</li>';
        }
    });
    html+="</ul>";
    Swal.fire({
        title:'Error!',
        html: html,
        icon: 'error'
    });
}