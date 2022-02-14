
function addItem() {
    const a = document.getElementById("list");
    const plant_name = document.getElementById("plant-names");
    const start_date = document.getElementById("start-date");
    const end_date = document.getElementById("end-date");
    let string_to_add = plant_name.value.concat(" | ", start_date.value, " -- ", end_date.value  )
    const li = document.createElement("li");
    li.setAttribute('id', plant_name.value);
    var counter = counter + 1;
    li.appendChild(document.createTextNode(string_to_add));
    a.appendChild(li);
    document.getElementById(plant_name.value).insertAdjacentHTML("beforeend", "&nbsp;<img src='/static/x-square.svg'/>");
}

// Creating a function to remove item from list
function removeItem() {

    // Declaring a variable to get select element
    var a = document.getElementById("list");
    var plant_name = document.getElementById("plant-names");
    var item = document.getElementById(plant_name.value);
    a.removeChild(item);
}