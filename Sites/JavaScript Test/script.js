const pi = 3.14159265359;
var clicked = false;

console.log(pi);
console.log("no more hello world, just pi.");

document.write("why yes potato man");

function toggleClicked() {
    clicked = !clicked;
};

var button = document.createElement("button");
button.innerHTML = "Click Me, for seizures.";
button.addEventListener("click", function() {
    toggleClicked();
});

document.body.appendChild(button);

while (clicked) {
    console.log("Clicked");
};