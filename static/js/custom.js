$("#id_type_1").click(function () {

    $('#common-data').show(500);
    $('#broker-only-data').show(500);
});

$("#id_type_2").click(function () {

    $('#common-data').show(500);
    $('#broker-only-data').hide(500);
});

if ($('#id_type_1').is(":checked")) {
    $('#common-data').show(500);
    $('#broker-only-data').show(500);
}

if ($('#id_type_2').is(":checked")) {
    $('#common-data').show(500);
    $('#broker-only-data').hide();
}
