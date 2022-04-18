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
      listOfFIPS[rowItems[0]] = rowItems[3]
      count++
    }
    console.log(listOfFIPS)
    console.log(typeof listOfFIPS)
  })
//console.log(listOfFIPS)

  
fs.readFile("counties.svg", "utf8", (error, mapContent) => {
  if(error){ throw error; }
  for(let row of mapContent.split("<path")){
    const rowItems = row.split(" ");
    console.log(row)
    let currentCounty = rowItems[1].replace('FIPS_', '').replace('id="', '').replace('"', '')
    //currentCounty = currentCounty.replace('id="', '')
    console.log('///////////')
    console.log(currentCounty)
    console.log(listOfFIPS[currentCounty])
    console.log('///////////')
  }
})


//create a new file and write the new calculations to that file

/*
fs.openSync('test/encrypted.txt', 'w');
fs.writeFileSync('test/encrypted.txt', encrypted, 'utf8');
*/