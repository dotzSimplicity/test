var clicked = false;
var rgb1 = 0;
var rgb2 = 0;
var rgb3 = 0;

function toggleClicked() {
    if (clicked) {
        clicked = false; // not that this works you know, cause of the while loop
    } else {
        clicked = true;
        while (clicked) {
            rgb1++
            rgb2+
            rgb3++
            document.body.style.backgroundColor = "rgb(" + rgb1 + "," + rgb2 + "," + rgb3 + ")"; // or this... cause i dont know ,copilot did this
        };
    }
};

