var fs = require('fs');

//read in a file 
var file = fs.readFileSync('county.csv', 'utf8');
var map = fs.readFileSync('counties.svg', 'utf8');
//console.log(file)

let listOfFIPS = {}
let count = 0

fs.readFile("county.csv", "utf8", (error, textContent) => {
    if(error){ throw error; }
    for(let row of textContent.split("\n")){
      const rowItems = row.split(",");

      if(rowItems[0].length < 5) {
        rowItems[0] = '0' + rowItems[0]
      }
      listOfFIPS[rowItems[0]] = rowItems[6]
      count++
    }
  })
//console.log(listOfFIPS)

  
fs.readFile("counties.svg", "utf8", (error, mapContent) => {
  if(error){ throw error; }
  for(let row of mapContent.split("<path")){
    const rowItems = row.split(" ");
    let currentCounty = rowItems[1].replace('FIPS_', '').replace('id="', '').replace('"', '')
    //currentCounty = currentCounty.replace('id="', '')
    let currentValue = listOfFIPS[currentCounty]


    if (currentValue > 28) {
      console.log('<path fill="#CE1522" data-medicalDebtShare="' + currentValue + '"' + row.replace('\n', ''))
    } else if(currentValue > 21) {
      console.log('<path fill="#FB8C68" data-medicalDebtShare="' + currentValue + '"' + row.replace('\n', ''))
    } else if(currentValue > 14) {
      console.log('<path fill="#E6E0C2" data-medicalDebtShare="' + currentValue + '"' + row.replace('\n', ''))
   }  else if(currentValue > 7) {
      console.log('<path fill="#68C2AF" data-medicalDebtShare="' + currentValue + '"' + row.replace('\n', ''))
    } else {
      console.log('<path fill="#49A082" data-medicalDebtShare="' + currentValue + '"' + row.replace('\n', ''))
    }
  }
})


//create a new file and write the new calculations to that file

/*
fs.openSync('test/encrypted.txt', 'w');
fs.writeFileSync('test/encrypted.txt', encrypted, 'utf8');
*/