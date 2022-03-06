// INTIIAL SET UP
//initial data array for gantt
let gantt_counter = 0;

let data_array = [
  [
    "Plant Gantt ID",
    "Plant Name",
    "Plant SubCategory",
    new Date(2022, 4, 1),
    new Date(2022, 7, 1),
    null,
    null,
    null,
  ],
];

function drawChart() {
  var data = new google.visualization.DataTable();
  data.addColumn("string", "Task ID");
  data.addColumn("string", "Task Name");
  data.addColumn("string", "Resource");
  data.addColumn("date", "Start Date");
  data.addColumn("date", "End Date");
  data.addColumn("number", "Duration");
  data.addColumn("number", "Percent Complete");
  data.addColumn("string", "Dependencies");

  data.addRows(data_array);

  var options = {
    height: 400,
    gantt: {
      trackHeight: 30,
      labelStyle: {
        fontName: "Arial",
      },
    },
    tooltip: {
      isHtml: true,
      textStyle: {
        fontName: "Arial",
      },
    },
  };

  var chart = new google.visualization.Gantt(
    document.getElementById("chart_div")
  );

  chart.draw(data, options);
}

// Get previously stored data from gantt //
let gantt_id = document.querySelector("h1").id;
console.log(`my gantt id is ${gantt_id}`);

let current_gantt_data;

fetch(`/api/gantt/${gantt_id}.json`)
  .then((response) => response.json())
  .then((data) => (current_gantt_data = data))
  .then(() => {
    // console.log(current_gantt_data);
    let data_array = [];
    for (const [key, value] of Object.entries(current_gantt_data)) {
      // console.log(`${key}`);
      const a = document.getElementById("list");
      let string_to_add = current_gantt_data[key]["name"].concat(
        // " | ",
        // current_gantt_data[key]["category"] ?? "N/A",
        // " | ",
        // current_gantt_data[key]["days_to_maturity"] ?? "N/A",
        " | ",
        "2022-05-01",
        " | ",
        "2022-07-01"
      );
      // console.log(string_to_add);
      const li = document.createElement("li");
      li.setAttribute("class", "gantt-item");
      li.setAttribute("id", current_gantt_data[key]["name"]);
      li.appendChild(document.createTextNode(string_to_add));
      a.appendChild(li);
      document
        .getElementById(current_gantt_data[key]["name"])
        .insertAdjacentHTML(
          "beforeend",
          `&nbsp; <button id='remove-item ${gantt_counter.toString()}' class='remove-item btn btn-outline-danger btn-xs'> X </button>`
        );
      
    }
  loadExistingGantt();
  });

function loadExistingGantt() {
  data_array = [];
  console.log("loading exiting gantt chart....");
  let ganttItems = document.querySelectorAll(".gantt-item");
  for (const item of ganttItems) {
    plant_string = item.textContent.replace(" X ", "") ;
    // console.log(plant_string.split(" | ")[2]);
    console.log(item.textContent.replace(" X ", ""))
    let plant_name = plant_string.split(" | ")[0];
    let start_date = plant_string.split(" | ")[1];
    let end_date =  plant_string.split(" | ")[2];
    let data_to_add = [
      plant_name,
      plant_name,
      plant_name,
      new Date(
        parseInt(start_date.split("-")[0]),
        parseInt(start_date.split("-")[1]) - 1,
        parseInt(start_date.split("-")[2])
      ),
      new Date(
        parseInt(end_date.split("-")[0]),
        parseInt(end_date.split("-")[1]) - 1,
        parseInt(end_date.split("-")[2])
      ),
      null,
      0,
      null,
    ];
    data_array.push(data_to_add);
  }
}


//Google chart
google.charts.load("current", { packages: ["gantt"] });
google.charts.setOnLoadCallback(drawChart);

///////// INTERACTIONS /////////

// ADDING ITEM //
//counter for add item - ensuring all unique IDs
//ToDo - make unique to specific plants

function addItem() {
  gantt_counter += 1;
  const a = document.getElementById("list");
  const plant_name = document.getElementById("plant-names");
  const start_date = document.getElementById("start-date");
  const end_date = document.getElementById("end-date");
  let string_to_add = plant_name.value.concat(
    " | ",
    start_date.value,
    " | ",
    end_date.value
  );
  const li = document.createElement("li");
  li.setAttribute("class", "gantt-item");
  li.setAttribute("id", plant_name.value);
  li.appendChild(document.createTextNode(string_to_add));
  let data_to_add = [
    plant_name.value,
    plant_name.value,
    "subcategory " + gantt_counter.toString(),
    new Date(
      parseInt(start_date.value.split("-")[0]),
      parseInt(start_date.value.split("-")[1]) - 1,
      parseInt(start_date.value.split("-")[2])
    ),
    new Date(
      parseInt(end_date.value.split("-")[0]),
      parseInt(end_date.value.split("-")[1]) - 1,
      parseInt(end_date.value.split("-")[2])
    ),
    null,
    0,
    null,
  ];
  data_array.push(data_to_add);
  console.log(data_array);
  drawChart();
  a.appendChild(li);
  // document.getElementById(plant_name.value + gantt_counter.toString()).insertAdjacentHTML("beforeend", `&nbsp; <img id='remove-item ${gantt_counter.toString()}' src='/static/img/x-square.svg'/>`);
  document
    .getElementById(plant_name.value)
    .insertAdjacentHTML(
      "beforeend",
      `&nbsp; <button id='remove-item ${gantt_counter.toString()}' class='remove-item btn btn-outline-danger btn-xs'> X </button>`
    );
}

// REMOVE ITEM
const btnWrapper = document.getElementById("wrapper");
wrapper.addEventListener("click", (evt) => {
  const isButton = evt.target.nodeName === "BUTTON";
  if (!isButton) {
    return;
  }
  // evt.target.id is the ID of the object
  let btnClicked = evt.target;
  console.log(btnClicked.parentElement);
  console.log(btnClicked.parentElement.id);
  data_array = data_array.filter(
    (plant) => plant[0] !== btnClicked.parentElement.id
  );
  btnClicked.parentElement.remove();
  drawChart();
});

// function geekConfirm() {
//   var x;
//   if (confirm("Would you like to save this schedule?") == true) {
//     window.location.replace("http://localhost:5000/user_gantt_details");
//   }
// }
