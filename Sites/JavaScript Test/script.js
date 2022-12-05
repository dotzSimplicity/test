const pi = 3.14159265359
let clicked = false

console.log(pi);
alert("Hello World!");

document.write("why yes potato man");


var button = document.createElement("button");
button.innerHTML = "Click Me";
button.addEventListener("click", function() {
    if (clicked == false) {
    clicked = true;
    else if (clicked == true)
    clicked == false;
    }
    });

document.body.appendChild(button);

while(clicked == true)
{
    console.log("Clicked");
};