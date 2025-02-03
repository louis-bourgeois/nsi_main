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
      html += `<td class="wrong black" onClick="tentative(${cpt})" id="${cpt}">${cpt}</td>`;
      cpt++;
    }
    html += "</tr>";
  }
  table.innerHTML = html;

  // Affichage en console pour tester
  console.log("Nombre mystère :", numMystere);
}

function tentative(numCell) {
  let cell = document.getElementById(numCell);
  console.log(numCell)
  if (parseInt(cell.innerHTML) === numMystere) {
    cell.classList.add("right");
  } else {
    cell.classList.add("wrong");
  }
}
