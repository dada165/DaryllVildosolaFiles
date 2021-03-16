// Final result should be 10.42
// Add/update your code here
//Answer for #1
let result = (7 + 13) / (9 + 7); //Answer for #4
console.log(result);
result2 = 100 / (2 * 6);//Answer for #4
result = result * result2;
console.log(result);
//Asnwer for #2
finalResult = result.toFixed(2);
console.log(finalResult);
//Answer for #3
console.log(typeof(finalResult));
let finalNumber = Number(finalResult);
console.log(typeof(finalNumber));
console.log(finalNumber);
//Answer for #4

// Don't edit the code below here!
section.innerHTML = ' ';
let para1 = document.createElement('p');
para1.textContent = `Your finalResult is ${ finalResult }`;
let para2 = document.createElement('p');
let finalNumberCheck = isNaN(finalNumber) === false ? 'finalNumber is a number type. Well done!' : 
`Ooops! finalNumber is not a number.`;
para2.textContent = finalNumberCheck;
section.appendChild(para1);
section.appendChild(para2);