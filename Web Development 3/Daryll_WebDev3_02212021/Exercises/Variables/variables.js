//Variables Exercise #1
var myName
myName = " I am Daryll G. Vildosola"
var myAge = "I am 19 years of age"
var section = document.getElementById("section");
// Don't edit the code below here!
section.innerHTML = ' ';
let para1 = document.createElement('p');
para1.textContent = myName;
let para2 = document.createElement('p');
para2.textContent = myAge;
section.appendChild(para1);
section.appendChild(para2);