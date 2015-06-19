function resaleCheck() {
    $("#id_is_resale_1").click(function () {

        $('#div_id_name_of_seller').show();
        $('#div_id_contact_number_seller').show();
        $('#div_id_email_seller').show();
    });

    $("#id_is_resale_2").click(function () {

        $('#div_id_name_of_seller').hide();
        $('#div_id_contact_number_seller').hide();
        $('#div_id_email_seller').hide();
    });

    if ($('#id_is_resale_1').is(":checked")) {
        $('#div_id_name_of_seller').show();
        $('#div_id_contact_number_seller').show();
        $('#div_id_email_seller').show();
    }

    if ($('#id_is_resale_2').is(":checked")) {
        $('#div_id_name_of_seller').hide();
        $('#div_id_contact_number_seller').hide();
        $('#div_id_email_seller').hide();
    }

}