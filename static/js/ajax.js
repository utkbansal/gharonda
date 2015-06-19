$(document).ready(function () {
    var propertyDetailsForm = $('#property-details');
    var button = $('#submit-property-details');
    button.click(function () {
        var post = $(this).attr("name") + "=" + $(this).val();
        var form_data = $(propertyDetailsForm).serialize() + "&" + post;
        console.log(form_data);

        $.ajax({
            data: form_data,
            type: 'POST',
            //headers: { "X-CSRFToken": getCookie("csrftoken") },
            url: $(this).attr('action'),
            success: function (data) {
                //var json_response = JSON.parse(data);
                console.log(data);
                if ((data['success'] == 'false')) {
                    alert('here');
                    // Here we replace the form, for the
                    $('#property-details').replaceWith(data['form_html']);
                }
                else {
                    // Here you can show the user a success message or do whatever you need
                    alert('works!');
                }
            }
        });
        return false;
    });
});


$(document).ready(function () {
    var ownerDetailsForm = $('#owner-details');
    var button = $('#submit-owner-details');
    button.click(function () {
        var post = $(this).attr("name") + "=" + $(this).val();
        var form_data = $(ownerDetailsForm).serialize() + "&" + post;
        console.log(form_data);

        $.ajax({
            data: form_data,
            type: 'POST',
            url: $(this).attr('action'),
            success: function (data) {
                //var json_response = JSON.parse(data);
                console.log(data);
                if ((data['success'] == 'false')) {
                    alert('here');
                    // Here we replace the form, for the
                    $('#owner-details').replaceWith(data['form_html']);
                }
                else {
                    // Here you can show the user a success message or do whatever you need
                    alert('works!');
                }
            }
        });
        return false;
    });
});


$(document).ready(function () {
    var projectDetailsForm = $('#project-details');
    var button = $('#submit-project-details');
    button.click(function () {
        var post = $(this).attr("name") + "=" + $(this).val();
        var form_data = $(projectDetailsForm).serialize() + "&" + post;
        console.log(form_data);

        $.ajax({
            data: form_data,
            type: 'POST',
            url: $(this).attr('action'),
            success: function (data) {
                //var json_response = JSON.parse(data);
                console.log(data);
                if ((data['success'] == 'false')) {
                    alert('here');
                    // Here we replace the form, for the
                    $('#project-details').replaceWith(data['form_html']);
                }
                else {
                    // Here you can show the user a success message or do whatever you need
                    alert('works!');
                }
            }
        });
        return false;
    });
});




$(document).ready(function () {
    var otherDetailsForm = $('#other-details');
    var button = $('#submit-other-details');
    button.click(function () {
        var post = $(this).attr("name") + "=" + $(this).val();
        var form_data = $(otherDetailsForm).serialize() + "&" + post;
        console.log(form_data);

        $.ajax({
            data: form_data,
            type: 'POST',
            url: $(this).attr('action'),
            success: function (data) {
                //var json_response = JSON.parse(data);
                console.log(data);
                if ((data['success'] == 'false')) {
                    alert('here');
                    // Here we replace the form, for the
                    $('#other-details').replaceWith(data['form_html']);
                }
                else {
                    // Here you can show the user a success message or do whatever you need
                    alert('works!');
                }
            }
        });
        return false;
    });
});
