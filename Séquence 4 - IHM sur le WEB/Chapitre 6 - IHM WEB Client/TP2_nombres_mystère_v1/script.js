function getRandomInt(max) {
  return Math.floor(Math.random() * Math.floor(max)) + 1;
}

const MAX = 100;
let essais;
let numMystere;

function play() {
  let table = document.getElementById("tableau");
  let html = "";
  essais = 0;
  let cpt = 1;

  numMystere = getRandomInt(MAX);

  for (let i = 0; i < MAX / 10; i++) {
    html += "<tr>";
    for (let j = 0; j < MAX / 10; j++) {
      html += `<td class="" onClick="tentative(${cpt})" id="${cpt}">${cpt}</td>`;
      cpt++;
    }
    html += "</tr>";
  }
  table.innerHTML = html;

  console.log("Nombre mystère :", numMystere);
}

function tentative(numCell) {
  let cell = document.getElementById(numCell.toString());
  let diff = Math.abs(numCell - numMystere);
  let maxDiff = MAX;   
  if (numCell === numMystere) {
    cell.classList.remove("wrong");
    cell.classList.add("right");
    cell.style.backgroundColor = "green";
  } else {
    let intensity = Math.floor(255 - (diff / maxDiff) * 255);
    cell.style.backgroundColor = `rgb(255, ${intensity}, ${intensity})`;
  }
}
