let html_class1 = document.getElementsByClassName('car_equipment_block_text');
for (var i = html_class1.length - 1; i >= html_class1.length - 1; i--) {
    html_class1[i].style.display = 'block';
}

function double_select(val) {

    let html_class = document.getElementsByClassName('car_equipment_block_text');
    for (var i = 0; i < html_class.length; i++) {
        html_class[i].style.display = 'none';
    }
    
    document.getElementById(val).style.display = 'block';
   
};


document.querySelector('#arrow_button_left1').addEventListener('click', () => {
    document.getElementById('container1').scrollBy({ left: -300, behavior: 'smooth' });
});

document.querySelector('#arrow_button_right1').addEventListener('click', () => {
    document.getElementById('container1').scrollBy({ left: 300, behavior: 'smooth' });
});


document.querySelector('#arrow_button_left2').addEventListener('click', () => {
    document.getElementById('container2').scrollBy({ left: -300, behavior: 'smooth' });
});

document.querySelector('#arrow_button_right2').addEventListener('click', () => {
    document.getElementById('container2').scrollBy({ left: 300, behavior: 'smooth' });
});


const scrollableBlock = document.querySelector('#container1');

scrollableBlock.addEventListener('mouseenter', () => {
  scrollableBlock.addEventListener('wheel', handleScroll);
});

scrollableBlock.addEventListener('mouseleave', () => {
  scrollableBlock.removeEventListener('wheel', handleScroll);
});

function handleScroll(event) {
  event.preventDefault();
  scrollableBlock.scrollLeft += event.deltaY;
}


const scrollableBlock2 = document.querySelector('#container2');

scrollableBlock2.addEventListener('mouseenter', () => {
  scrollableBlock2.addEventListener('wheel', handleScroll2);
});

scrollableBlock2.addEventListener('mouseleave', () => {
  scrollableBlock2.removeEventListener('wheel', handleScroll2);
});

function handleScroll2(event) {
  event.preventDefault();
  scrollableBlock2.scrollLeft += event.deltaY;
}