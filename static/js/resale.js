function resaleCheck() {
    $("#id_is_resale_1").click(function () {

        $('#div_id_name_of_seller').show(500);
        $('#div_id_contact_number_seller').show(500);
        $('#div_id_email_seller').show(500);
    });

    $("#id_is_resale_2").click(function () {

        $('#div_id_name_of_seller').hide(500);
        $('#div_id_contact_number_seller').hide(500);
        $('#div_id_email_seller').hide(500);
    });

    if ($('#id_is_resale_1').is(":checked")) {
        $('#div_id_name_of_seller').show(500);
        $('#div_id_contact_number_seller').show(500);
        $('#div_id_email_seller').show(500);
    }

    if ($('#id_is_resale_2').is(":checked")) {
        $('#div_id_name_of_seller').hide(500);
        $('#div_id_contact_number_seller').hide(500);
        $('#div_id_email_seller').hide(500);
    }

}

function loanCheck() {
    if ($('#id_loan_status').is(':checked')) {
        $('#div_id_loan_from').show(500);
    }
    else{
        $('#div_id_loan_from').hide();
    }

    $('#id_loan_status').click(function () {
        if ($('#id_loan_status').is(':checked')) {
            $('#div_id_loan_from').show(500);
        }
        else {
            $('#div_id_loan_from').hide(500);
        }

    })
}