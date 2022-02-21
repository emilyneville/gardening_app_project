let gantt_counter = 1;

function addItem() {
  gantt_counter += 1;
  const a = document.getElementById("list");
  const plant_name = document.getElementById("plant-names");
  const start_date = document.getElementById("start-date");
  const end_date = document.getElementById("end-date");
  let string_to_add = plant_name.value.concat(
    " | ",
    start_date.value,
    " -- ",
    end_date.value
  );
  const li = document.createElement("li");
  li.setAttribute("class", "gantt-item");
  li.setAttribute("id", plant_name.value + " " + gantt_counter.toString());
  li.appendChild(document.createTextNode(string_to_add));
  a.appendChild(li);
  // document.getElementById(plant_name.value + gantt_counter.toString()).insertAdjacentHTML("beforeend", `&nbsp; <img id='remove-item ${gantt_counter.toString()}' src='/static/img/x-square.svg'/>`);
  document
    .getElementById(plant_name.value + " " + gantt_counter.toString())
    .insertAdjacentHTML(
      "beforeend",
      `&nbsp; <button id='remove-item ${gantt_counter.toString()}' class='remove-item btn btn-outline-danger btn-xs'> X </button>`
    );
}

const btnWrapper = document.getElementById('wrapper');

wrapper.addEventListener('click', (evt) => {
    const isButton = evt.target.nodeName === 'BUTTON';
    if (!isButton) {
      return;
    }
    // evt.target.id is the ID of the object
    let btnClicked = evt.target; 
    console.log(btnClicked.parentElement);
    btnClicked.parentElement.remove();

    
  })