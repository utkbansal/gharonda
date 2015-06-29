$("#id_type_1").click(function () {

    $('#common-data').show();
    $('#broker-only-data').show();
});

$("#id_type_2").click(function () {

    $('#common-data').show();
    $('#broker-only-data').hide();
});

if ($('#id_type_1').is(":checked")) {
    $('#common-data').show();
    $('#broker-only-data').show();
}

if ($('#id_type_2').is(":checked")) {
    $('#common-data').show();
    $('#broker-only-data').hide();
}
