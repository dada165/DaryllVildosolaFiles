// Add your code here
//Answer for the task
let myArray = ["Orange","Apple","Lemon"];
console.log(myArray);
myArray[0] = "Grapes";
console.log(myArray);
myArray[1] = "Melon";
console.log(myArray);
myArray.unshift("Pineapple");
console.log(myArray);
// Don't edit the code below here!section.innerHTML = ' ';
let para1 = document.createElement('p');
para1.textContent = `Array: ${ myArray }`;
section.appendChild(para1);