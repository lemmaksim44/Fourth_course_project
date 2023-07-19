document.querySelector('#arrow_button_up').addEventListener('click', () => {
    document.getElementById('container').scrollTop += -150;
});

document.querySelector('#arrow_button_down').addEventListener('click', () => {
    document.getElementById('container').scrollTop += 150;
});