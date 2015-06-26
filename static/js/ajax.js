hideAllForms();
$('#property-details-form').show(500);

function propertyAjax() {
    var propertyDetailsForm = $('#property-details');
    var post = $(this).attr("name") + "=" + $(this).val();
    var form_data = $(propertyDetailsForm).serialize() + "&" + post;
    console.log(form_data);

    $.ajax({
        data: form_data,
        type: 'POST',
        url: $(this).attr('action'),
        success: function (data) {
            console.log(data);
            $('#property-details').replaceWith(data['form_html']);
            $('#submit-property-details').click(propertyAjax);
            all();

            if ((data['success'] == 'true')) {
                hideAllForms();
                $('#owner-details-form').show(500);
            }
        }
    });
    return false;
}

$('#submit-property-details').click(propertyAjax);


function ownerAjax() {
    var ownerDetailsForm = $('#owner-details');
    var post = $(this).attr("name") + "=" + $(this).val();
    var form_data = $(ownerDetailsForm).serialize() + "&" + post;
    console.log(form_data);

    $.ajax({
        data: form_data,
        type: 'POST',
        url: $(this).attr('action'),
        success: function (data) {
            console.log(data);
            $('#owner-details').html(data['form_html']);
            $('#submit-owner-details').click(propertyAjax);
            all();

            if ((data['success'] == 'true')) {
                hideAllForms();
                $('#project-details-form').show(500);
            }
        }
    });
    return false;
}

$('#submit-owner-details').click(ownerAjax);


function projectAjax() {
    var projectDetailsForm = $('#project-details');
    var post = $(this).attr("name") + "=" + $(this).val();
    var form_data = $(projectDetailsForm).serialize() + "&" + post;
    console.log(form_data);

    $.ajax({
        data: form_data,
        type: 'POST',
        url: $(this).attr('action'),
        success: function (data) {
            console.log(data);
            $('#project-details').html(data['form_html']);
            $('#submit-project-details').click(projectAjax);
            $('#add-tower').click(addTower);

            all();

            if ((data['success'] == 'true')) {
                hideAllForms();
                $('#builder-details-form').show(500);
            }
        }
    });
    return false;
}

$('#submit-project-details').click(projectAjax);

function addTower() {
    var projectDetailsForm = $('#project-details');
    var post = $(this).attr("name") + "=" + $(this).val();
    var form_data = $(projectDetailsForm).serialize() + "&" + post;
    console.log(form_data);

    $.ajax({
        data: form_data,
        type: 'POST',
        url: $(this).attr('action'),
        success: function (data) {
            console.log(data);
            $('#tower-part-form').html(data['form_html']);
            $('#submit-project-details').click(projectAjax);
            $('#add-tower').click(addTower);
            all();
        }
    });
    return false;
}

$('#add-tower').click(addTower);


function builderAjax() {
    var builderDetailsForm = $('#builder-details');
    var post = $(this).attr("name") + "=" + $(this).val();
    var form_data = $(builderDetailsForm).serialize() + "&" + post;
    console.log(form_data);

    $.ajax({
        data: form_data,
        type: 'POST',
        url: $(this).attr('action'),
        success: function (data) {
            console.log(data);
            $('#builder-details').html(data['form_html']);
            $('#submit-builder-details').click(builderAjax);
            $('#add-project').click(addFormset);
            if ((data['success'] == 'true')) {
                hideAllForms();
                $('#other-details-form').show(500);
            }

            all();
        }
    });
    return false;
}

$('#submit-builder-details').click(builderAjax);

function addFormset() {
    var builderDetailsForm = $('#builder-details');
    var post = $(this).attr("name") + "=" + $(this).val();
    var form_data = $(builderDetailsForm).serialize() + "&" + post;
    console.log(form_data);

    $.ajax({
        data: form_data,
        type: 'POST',
        url: $(this).attr('action'),
        success: function (data) {
            console.log(data);
            $('#builder-details').html(data['form_html']);
            $('#submit-builder-details').click(builderAjax);
            $('#add-project').click(addFormset);
            all();
        }
    });
    return false;
}

$('#add-project').click(addFormset);

function otherAjax() {
    var otherDetailsForm = $('#other-details');
    var post = $(this).attr("name") + "=" + $(this).val();
    var form_data = $(otherDetailsForm).serialize() + "&" + post;
    console.log(form_data);

    $.ajax({
        data: form_data,
        type: 'POST',
        url: $(this).attr('action'),
        success: function (data) {
            console.log(data);
            $('#other-details').html(data['form_html']);
            $('#submit-other-details').click(otherAjax);
            all();
        }
    });
    return false;
}

$('#submit-other-details').click(otherAjax);
