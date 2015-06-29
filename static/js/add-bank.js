function addBankCheck() {
    if ($('#id_add_bank').is(":checked")) {
        $('#div_id_new_bank').show();
    }
    else
        $('#div_id_new_bank').hide();

    $("#id_add_bank").click(function () {

        if ($('#id_add_bank').is(":checked")) {
            $('#div_id_new_bank').show(500);
        }
        else
            $('#div_id_new_bank').hide(500);

    });
}