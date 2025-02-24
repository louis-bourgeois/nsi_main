function getRandomInt(max) {
  return Math.floor(Math.random() * Math.floor(max)) + 1;
}

const difficultiesdict = {
  "easy" : 50,
  "medium" :100, 
  "hard" : 150
}

let currentDifficulty = "medium"
let MAX = difficultiesdict[currentDifficulty];
let essais;
let numMystere;
let essaisSpan = document.getElementById("nbEssais");

function play() {
  let table = document.getElementById("tableau");
  
  let html = "";
  essais = 0;
  essaisSpan.innerHTML="0"
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
  let cell = document.getElementById(numCell.toString()); // Je l'avais
  let gridSize = MAX / 10; // Je l'avais

  // Coordonnées allant 0 à 9 | Je l'avais
  let clickedRow = Math.floor((numCell - 1) / gridSize); 
  let clickedCol = (numCell - 1) % gridSize;

  // Coordonnées allant 0 à 9 du nombre à trouver | Je l'avais
  let mysteryRow = Math.floor((numMystere - 1) / gridSize);
  let mysteryCol = (numMystere - 1) % gridSize;

  let distance = Math.sqrt(
    Math.pow(clickedRow - mysteryRow, 2) + Math.pow(clickedCol - mysteryCol, 2)
  ); // Je l'avais, juste math.pow : c'est élever à une racine


  // Ici on calcule les distances maximales aux 4 coins tu tableaux : 
  let d1 = Math.sqrt(Math.pow(mysteryRow - 0, 2) + Math.pow(mysteryCol - 0, 2));
  let d2 = Math.sqrt(
    Math.pow(mysteryRow - 0, 2) + Math.pow(mysteryCol - (gridSize - 1), 2)
  );
  let d3 = Math.sqrt(
    Math.pow(mysteryRow - (gridSize - 1), 2) + Math.pow(mysteryCol - 0, 2)
  );
  let d4 = Math.sqrt(
    Math.pow(mysteryRow - (gridSize - 1), 2) + Math.pow(mysteryCol - (gridSize - 1), 2)
  );
  let maxDistance = Math.max(d1, d2, d3, d4);

  if (numCell === numMystere) {
    cell.classList.remove("wrong");
    cell.classList.add("right");
    cell.style.backgroundColor = "green";
  } else {
    essais++;
    essaisSpan.innerHTML = essais.toString();

    let intensity = Math.floor(255 - (distance / maxDistance) * 255);
    intensity = 255-Math.max(0, Math.min(255, intensity));

    cell.style.backgroundColor = `rgb(255, ${intensity*4}, ${intensity/2})`;
  }
}


document.querySelectorAll('.difficulties_libelle').forEach(button => {
  button.addEventListener('click', event => {
    document.querySelectorAll('.difficulties_libelle').forEach(btn => btn.classList.remove('active'));
    event.currentTarget.classList.add('active');
    const difficulty = event.currentTarget.dataset.difficulty;
    selectDifficulty(difficulty);
  });
});

function selectDifficulty(difficulty) {
  currentDifficulty = difficulty;
  MAX = difficultiesdict[difficulty];
  console.log("Difficulté sélectionnée :", difficulty);
}
 

// 