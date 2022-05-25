var fs = require('fs');

//read in a file 
var file = fs.readFileSync('county.csv', 'utf8');
//console.log(file)

let listOfFIPS = {}
let count = 0

let listOfStates = {
  "Alabama": "#dcdcdc",
  "Alaska": "#dcdcdc",
  "Arizona": "#dcdcdc",
  "Arkansas": "#dcdcdc",
  "California": "#dcdcdc",
  "Colorado": "#dcdcdc",
  "Connecticut": "#dcdcdc",
  "Delaware": "#dcdcdc",
  "District Of Columbia": "#dcdcdc",
  "Florida": "#ff4e36",
  "Georgia": "#dcdcdc",
  "Hawaii": "#dcdcdc",
  "Idaho": "#dcdcdc",
  "Illinois": "#dcdcdc",
  "Indiana": "#dcdcdc",
  "Iowa": "#dcdcdc",
  "Kansas": "#dcdcdc",
  "Kentucky": "#dcdcdc",
  "Louisiana": "#dcdcdc",
  "Maine": "#dcdcdc",
  "Maryland": "#dcdcdc",
  "Massachusetts": "#dcdcdc",
  "Michigan": "#dcdcdc",
  "Minnesota": "#dcdcdc",
  "Mississippi": "#dcdcdc",
  "Missouri": "#dcdcdc",
  "Montana": "#dcdcdc",
  "Nebraska": "#dcdcdc",
  "Nevada": "#dcdcdc",
  "New Hampshire": "#dcdcdc",
  "New Jersey": "#dcdcdc",
  "New Mexico": "#dcdcdc",
  "New York": "#dcdcdc",
  "North Carolina": "#dcdcdc",
  "North Dakota": "#dcdcdc",
  "Ohio": "#dcdcdc",
  "Oklahoma": "#dcdcdc",
  "Oregon": "#dcdcdc",
  "Palau": "#dcdcdc",
  "Pennsylvania": "#dcdcdc",
  "Puerto Rico": "#dcdcdc",
  "Rhode Island": "#dcdcdc",
  "South Carolina": "#dcdcdc",
  "South Dakota": "#dcdcdc",
  "Tennessee": "#dcdcdc",
  "Texas": "#dcdcdc",
  "Utah": "#dcdcdc",
  "Vermont": "#dcdcdc",
  "Virgin Islands": "#dcdcdc",
  "Virginia": "#dcdcdc",
  "Washington": "#dcdcdc",
  "West Virginia": "#dcdcdc",
  "Wisconsin": "#dcdcdc",
  "Wyoming": "#dcdcdc"
}

fs.readFile("county.csv", "utf8", (error, textContent) => {
    if(error){ throw error; }
    for(let row of textContent.split("\n")){
      const rowItems = row.split(",");

      if(rowItems[0].length < 5) {
        rowItems[0] = '0' + rowItems[0]
      }
      listOfFIPS[rowItems[0]] = rowItems[6]
      count++

      let currentState = rowItems[2]
 
      let currentStateGrouping = listOfStates[currentState]
      //console.log(currentState)
      rowItems.unshift(currentStateGrouping)
      console.log(rowItems.toString())


    }
  })
//console.log(listOfFIPS)


//create a new file and write the new calculations to that file

/*
fs.openSync('test/encrypted.txt', 'w');
fs.writeFileSync('test/encrypted.txt', encrypted, 'utf8');
*/
