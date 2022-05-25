var fs = require('fs');

//read in a file 
var file = fs.readFileSync('county.csv', 'utf8');
//console.log(file)

let listOfFIPS = {}
let count = 0

let listOfStates = {
  "Alabama": "#D81B60",
  "Alaska": "#1976D2",
  "Arizona": "#388E3C",
  "Arkansas": "#FBC02D",
  "California": "#E64A19",
  "Colorado": "#455A64",
  "Connecticut": "#D81B60",
  "Delaware": "#D81B60",
  "District Of Columbia": "#D81B60",
  "Federated States Of Micronesia": "#D81B60",
  "Florida": "#D81B60",
  "Georgia": "#D81B60",
  "Guam": "#D81B60",
  "Hawaii": "#1976D2",
  "Idaho": "#1976D2",
  "Illinois": "#1976D2",
  "Indiana": "#1976D2",
  "Iowa": "#1976D2",
  "Kansas": "#1976D2",
  "Kentucky": "#1976D2",
  "Louisiana": "#388E3C",
  "Maine": "#388E3C",
  "Marshall Islands": "#388E3C",
  "Maryland": "#388E3C",
  "Massachusetts": "#388E3C",
  "Michigan": "#388E3C",
  "Minnesota": "#388E3C",
  "Mississippi": "#388E3C",
  "Missouri": "#388E3C",
  "Montana": "#388E3C",
  "Nebraska": "#FBC02D",
  "Nevada": "#FBC02D",
  "New Hampshire": "#FBC02D",
  "New Jersey": "#FBC02D",
  "New Mexico": "#FBC02D",
  "New York": "#FBC02D",
  "North Carolina": "#FBC02D",
  "North Dakota": "#FBC02D",
  "Northern Mariana Islands": "#FBC02D",
  "Ohio": "#FBC02D",
  "Oklahoma": "#E64A19",
  "Oregon": "#E64A19",
  "Palau": "#E64A19",
  "Pennsylvania": "#E64A19",
  "Puerto Rico": "#E64A19",
  "Rhode Island": "#E64A19",
  "South Carolina": "#E64A19",
  "South Dakota": "#E64A19",
  "Tennessee": "#E64A19",
  "Texas": "#455A64",
  "Utah": "#455A64",
  "Vermont": "#455A64",
  "Virgin Islands": "#455A64",
  "Virginia": "#455A64",
  "Washington": "#455A64",
  "West Virginia": "#455A64",
  "Wisconsin": "#455A64",
  "Wyoming": "#455A64"
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
