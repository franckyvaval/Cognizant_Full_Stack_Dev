// Gets the default color, height and width
let height = document.querySelector('#inputHeight').value;
let width = document.querySelector('#inputWidth').value;
let color = 'black';

// changes the color when the color picker is used
let new_color = colorPicker.addEventListener('input', function (event) { 
    color = event.srcElement.value});

// Event listener for when submit is clicked, a grid is created
sizePicker.addEventListener('submit', makeGrid);

function makeGrid(event) {
    // prevents default action
    event.preventDefault();

    // removes grid if exist
    if (pixelCanvas.hasChildNodes()) {
        let canvas = document.querySelector('#pixelCanvas');
        let container = document.querySelector('.gridContainer')

        canvas.removeChild(container)
    }

    //sets height and width to values selected
    height = document.querySelector('#inputHeight').value;
    width = document.querySelector('#inputWidth').value;

    //creates a grid
    pixelCanvas.appendChild(document.createElement('div')).className = 'gridContainer';
    const gridContainer = document.querySelector('div');

    //creates the cells based on height and weight
    widthPixel = 'auto '.repeat(width);
    heightPixel = 'auto '.repeat(height);
    gridContainer.setAttribute('style', 'display: grid; grid-template-columns: ' + heightPixel + '; grid-template-rows: ' + widthPixel + ';');

    for (c = 0; c < (width * height); c++) {
      let cell = document.createElement("div");
      gridContainer.appendChild(cell).className = "grid-item";
    };

    // changes the cell color when clicked
    pixelCanvas.addEventListener('click', function (evt) {
        evt.target.style.backgroundColor = color;
})
}