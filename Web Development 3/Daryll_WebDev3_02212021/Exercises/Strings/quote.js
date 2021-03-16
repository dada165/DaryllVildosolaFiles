let quote = 'I dO nOT lIke gREen eGgS anD HAM';
// Add your code here
//Answer for #1
let lowerCases = quote.toLowerCase();
let fixedQuote = lowerCases[0].toUpperCase()+lowerCases.substring(1);
console.log(fixedQuote);
//Answer for #2 and #3
let finalQuote = fixedQuote.replace(fixedQuote,"I do not like ladies finger");  
console.log(finalQuote);  
// Don't edit the code below here!
section.innerHTML = ' ';
let para1 = document.createElement('p');
para1.textContent = fixedQuote;
let para2 = document.createElement('p');
para2.textContent = finalQuote;
section.appendChild(para1);
section.appendChild(para2);