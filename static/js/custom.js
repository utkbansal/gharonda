function fieldVisiblityCheck() {

    // If Broker
    if (document.getElementById('id_type_1').checked) {
        document.getElementById('common-data').style.display = 'block';
        document.getElementById('broker-only-data').style.display = 'block';
    }
    // If Normal User
    if (document.getElementById('id_type_2').checked) {
        document.getElementById('common-data').style.display = 'block';
        document.getElementById('broker-only-data').style.display = 'none';
    }
}
e1 = document.getElementById('id_type_1');
e2 = document.getElementById('id_type_2');
e1.addEventListener('click', fieldVisiblityCheck);
e2.addEventListener('click', fieldVisiblityCheck);

fieldVisiblityCheck();