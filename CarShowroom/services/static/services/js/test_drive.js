if (document.getElementById('input_name_id').value != '' || document.getElementById('input_phone_id').value != '') {
    document.getElementById('form_question').style.display = 'block';
};


function view_form_question() {
    document.getElementById('form_question').style.display = 'block';
};


function view_site() {
    document.getElementById('form_question').style.display = 'none';
};



document.getElementById('input_name_service_id').value = 'Тест-драйв';

document.getElementById('first_select').style.display = 'inline-block';
document.getElementById('first_select$').style.display = 'inline-block';


function double_select() {

    let element = document.getElementById('selected_brand').value;

    if (element == 'clean_select') {

        let html_class = document.getElementsByClassName('service_form_select_hide');
        for (var i = 0; i < html_class.length; i++) {
            html_class[i].style.display = 'none';
            html_class[i].value = '';
        }

        let html_class_star = document.getElementsByClassName('service_form_select_hide_dop');
        for (var i = 0; i < html_class_star.length; i++) {
            html_class_star[i].style.display = 'none';
        }

        document.getElementById('first_select').style.display = 'inline-block';
        document.getElementById('first_select$').style.display = 'inline-block';

    }
    else {

        let html_class = document.getElementsByClassName('service_form_select_hide');
        for (var i = 0; i < html_class.length; i++) {
            html_class[i].style.display = 'none';
            html_class[i].value = '';
        }

        let html_class_star = document.getElementsByClassName('service_form_select_hide_dop');
        for (var i = 0; i < html_class_star.length; i++) {
            html_class_star[i].style.display = 'none';
        }

        document.getElementById(element).style.display = 'inline-block';
        document.getElementById(element + '$').style.display = 'inline-block';
    }
};


function send() {

    document.getElementById('input_comment_id').value = document.getElementById('selected_brand').value + " ";
    let html_class = document.getElementsByClassName('service_form_select_hide');
    for (var i = 0; i < html_class.length; i++) {
        document.getElementById('input_comment_id').value += html_class[i].value + ' ';
    }

    document.getElementById('input_name_id_2').value = document.getElementById('input_name_id').value;
    document.getElementById('input_phone_id_2').value = document.getElementById('input_phone_id').value;
    document.getElementById('input_checkbox_id').value = False;
};