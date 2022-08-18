var fs = require("fs");

//read in a file
var file = fs.readFileSync("addFIPS/2004_numbers.csv", "utf8");
var map = fs.readFileSync("counties.svg", "utf8");
//console.log(file)

let listOfFIPS = {};
let count = 0;

fs.readFile("smokingTobaccoData/2012.csv", "utf8", (error, textContent) => {
  if (error) {
    throw error;
  }

  for (let row of textContent.split("\n")) {
    const rowItems = row.split(",");

    if (rowItems[0].length < 5) {
      rowItems[0] = "0" + rowItems[0];
    }
    listOfFIPS[rowItems[0]] = rowItems[5];
    count++;
  }

  fs.readFile("counties.svg", "utf8", (error, mapContent) => {
    if (error) {
      throw error;
    }
    for (let row of mapContent.split("<path")) {
      const rowItems = row.split(" ");
      let currentCounty = rowItems[1]
        .replace("FIPS_", "")
        .replace('id="', "")
        .replace('"', "");
      //currentCounty = currentCounty.replace('id="', '')
      let currentValue = listOfFIPS[currentCounty];

      if (currentValue > 40) {
        console.log(
          '<path fill="#CE1522" data-smokingLevels="' +
            currentValue +
            '"' +
            row.replace("\n", "")
        );
      } else if (currentValue > 30) {
        console.log(
          '<path fill="#FB8C68" data-smokingLevels="' +
            currentValue +
            '"' +
            row.replace("\n", "")
        );
      } else if (currentValue > 20) {
        console.log(
          '<path fill="#E6E0C2" data-smokingLevels="' +
            currentValue +
            '"' +
            row.replace("\n", "")
        );
      } else if (currentValue > 10) {
        console.log(
          '<path fill="#68C2AF" data-smokingLevels="' +
            currentValue +
            '"' +
            row.replace("\n", "")
        );
      } else {
        console.log(
          '<path fill="#ddd" data-smokingLevels="' +
            currentValue +
            '"' +
            row.replace("\n", "")
        );
      }
    }
  });
});

//create a new file and write the new calculations to that file

/*
fs.openSync('test/encrypted.txt', 'w');
fs.writeFileSync('test/encrypted.txt', encrypted, 'utf8');
*/
