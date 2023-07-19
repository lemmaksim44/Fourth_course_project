if (document.getElementById('input_name_id').value != '' || document.getElementById('input_phone_id').value != '') {
    document.getElementById('form_question').style.display = 'block';
};


function view_form_question() {
    document.getElementById('form_question').style.display = 'block';
};


function view_site() {
    document.getElementById('form_question').style.display = 'none';
};



document.getElementById('input_name_service_id').value = 'Сервис';


function send() {
    document.getElementById('input_name_id_2').value = document.getElementById('input_name_id').value;
    document.getElementById('input_phone_id_2').value = document.getElementById('input_phone_id').value;
    document.getElementById('input_email_id_2').value = document.getElementById('input_email_id').value;
    document.getElementById('input_checkbox_id').value = False;
};