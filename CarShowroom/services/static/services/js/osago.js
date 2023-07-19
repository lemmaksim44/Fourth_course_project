if (document.getElementById('input_name_id').value != '' || document.getElementById('input_phone_id').value != '') {
    document.getElementById('form_question').style.display = 'block';
};


function view_form_question() {
    document.getElementById('form_question').style.display = 'block';
};


function view_kbm_question() {
    document.getElementById('kbm_question').style.display = 'block';
};


function view_site() {
    document.getElementById('form_question').style.display = 'none';
    document.getElementById('kbm_question').style.display = 'none';
};



document.getElementById('input_name_service_id').value = 'Страхование';


function send() {
    document.getElementById('input_name_id_2').value = document.getElementById('input_name_id').value;
    document.getElementById('input_phone_id_2').value = document.getElementById('input_phone_id').value;
    document.getElementById('input_comment_id').value = document.getElementById('selected_insurance').value;
    document.getElementById('input_checkbox_id').value = False;
};


document.getElementById('selected_region').value = 33;
document.getElementById('33').style.display = 'block';

function double_select() {

    let element = document.getElementById('selected_region').value;

    if (element == 'clean_select') {

        let html_class = document.getElementsByClassName('calculator_select_hide');
        for (var i = 0; i < html_class.length; i++) {
            html_class[i].style.display = 'none';
            html_class[i].value = '';
        }

    }
    else {

        let html_class = document.getElementsByClassName('calculator_select_hide');
        for (var i = 0; i < html_class.length; i++) {
            html_class[i].style.display = 'none';
            html_class[i].value = '';
        }

        document.getElementById(element).style.display = 'block';
    }
};


function calculator() {

    document.getElementById('min_answer').innerHTML = '';
    document.getElementById('max_answer').innerHTML = '';
    document.getElementById('error').innerHTML = '';

    let region = document.getElementById('selected_region').value;
    let city = document.getElementById(region).value;
    let age = document.getElementById('age').value;
    let experience = document.getElementById('experience').value;
    let kbm = document.getElementById('KBM').value;
    let power = document.getElementById('power').value;
    let term = document.getElementById('term').value;
    let restrictions = document.getElementById('restrictions').value;

    if ((city == 0 || age == '' || experience == '' || kbm == '' || power == '' || term == '' || restrictions == '') || (age >= 120 || experience > age - 16 || power >= 1000)) {
        document.getElementById('error').innerHTML = 'Ошибка данных!';
    }
    else {

        let KVS;
        if (16 <= age && age <= 21) {
            let list = [2.27, 1.92, 1.84, 1.65, 1.65, 1.62, 1.62];
            KVS = list[experience];
        }
        if (22 <= age && age <= 24) {
            let list = [1.88, 1.72, 1.71, 1.13, 1.13, 1.10, 1.10, 1.09, 1.09, 1.09];
            KVS = list[experience];
        }
        if (25 <= age && age <= 29) {
            let list = [1.72, 1.60, 1.54, 1.09, 1.09, 1.08, 1.08, 1.07, 1.07, 1.07, 1.02, 1.02, 1.02, 1.02, 1.02];
            KVS = list[experience];
        }
        if (30 <= age && age <= 34) {
            let list = [1.56, 1.50, 1.48, 1.05, 1.05, 1.04, 1.04, 1.01, 1.01, 1.01, 0.97, 0.97, 0.97, 0.97, 0.97, 0.95];
            if (experience > 14) { experience = 15; }
            KVS = list[experience];
        }
        if (35 <= age && age <= 39) {
            let list = [1.54, 1.47, 1.46, 1.00, 1.00, 0.97, 0.97, 0.95, 0.95, 0.95, 0.94, 0.94, 0.94, 0.94, 0.94, 0.93];
            if (experience > 14) { experience = 15; }
            KVS = list[experience];
        }
        if (40 <= age && age <= 49) {
            let list = [1.50, 1.44, 1.43, 0.96, 0.96, 0.95, 0.95, 0.94, 0.94, 0.94, 0.93, 0.93, 0.93, 0.93, 0.93, 0.91];
            if (experience > 14) { experience = 15; }
            KVS = list[experience];
        }
        if (50 <= age && age <= 59) {
            let list = [1.46, 1.40, 1.39, 0.93, 0.93, 0.92, 0.92, 0.91, 0.91, 0.91, 0.90, 0.90, 0.90, 0.90, 0.90, 0.86];
            if (experience > 14) { experience = 15; }
            KVS = list[experience];
        }
        if (59 < age) {
            let list = [1.43, 1.36, 1.35, 0.91, 0.91, 0.90, 0.90, 0.89, 0.89, 0.89, 0.88, 0.88, 0.88, 0.88, 0.88, 0.83];
            if (experience > 14) { experience = 15; }
            KVS = list[experience];
        }
        
        let KM;
        if (power <= 50) {
            KM = 0.6;
        }
        if (power > 50 && power <= 70) {
            KM = 1;
        }
        if (power > 70 && power <= 100) {
            KM = 1.1;
        }
        if (power > 100 && power <= 120) {
            KM = 1.2;
        }
        if (power > 120 && power <= 150) {
            KM = 1.4;
        }
        if (power > 150) {
            KM = 1.6;
        }

        let min = parseFloat(5000) * parseFloat(city.replace(",", ".")) * parseFloat(kbm) * KVS * parseFloat(restrictions) * parseFloat(term) * KM;
        let max = parseFloat(7535) * parseFloat(city.replace(",", ".")) * parseFloat(kbm) * KVS * parseFloat(restrictions) * parseFloat(term) * KM;

        min = min.toFixed(2);
        max = max.toFixed(2);

        console.log(min, max);

        min = min.substring(0, min.length - 6) + " " + min.substring(min.length - 6);
        max = max.substring(0, max.length - 6) + " " + max.substring(max.length - 6);

        document.getElementById('min_answer').innerHTML = min + ' ₽';
        document.getElementById('max_answer').innerHTML = max + ' ₽';
    
    }
   
}


function calculator_scroll() {
    window.scrollTo(0, 1000);
}