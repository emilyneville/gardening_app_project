// INTIIAL SET UP
//initial data array for gantt
let gantt_counter = 0;

let DATA_ARRAY = [
  // [
  //   "Plant Gantt ID",
  //   "Plant Name",
  //   "Plant SubCategory",
  //   new Date(2022, 4, 1),
  //   new Date(2022, 7, 1),
  //   null,
  //   null,
  //   null,
  // ],
];

const OPTIONS = {
  height: 400,
  gantt: {
    trackHeight: 30,
    labelStyle: {
      fontName: "Arial",
    },
    palette: [
      {
        color: "#5b618aff",
        dark: "#5b618aff",
        light: "#5b618aff",
      },
      {
        color: "#4a442dff",
        dark: "#4a442dff",
        light: "#4a442dff",
      },
      {
        color: "#7ca982ff",
        dark: "#7ca982ff",
        light: "#7ca982ff",
      },
      {
        color: "#93032eff",
        dark: "#93032eff",
        light: "#93032eff",
      },
      {
        color: "#c2a83eff",
        dark: "#c2a83eff",
        light: "#c2a83eff",
      },
      {
        color: "#a47b73",
        dark: "#a47b73",
        light: "#a47b73",
      },
      {
        color: "#5a4a29",
        dark: "#5a4a29",
        light: "#5a4a29",
      },
      {
        color: "#623918",
        dark: "#623918",
        light: "#623918",
      },
      {
        color: "#737b20",
        dark: "#737b20",
        light: "#737b20",
      },
      {
        color: "#736262",
        dark: "#736262",
        light: "#736262",
      },
      {
        color: "#bdb46a",
        dark: "#bdb46a",
        light: "#bdb46a",
      },
    ],
  },
  tooltip: {
    isHtml: true,
    textStyle: {
      fontName: "Arial",
    },
  },
};

function drawChart() {
  const data = new google.visualization.DataTable();
  data.addColumn("string", "Task ID");
  data.addColumn("string", "Task Name");
  data.addColumn("string", "Resource");
  data.addColumn("date", "Start Date");
  data.addColumn("date", "End Date");
  data.addColumn("number", "Duration");
  data.addColumn("number", "Percent Complete");
  data.addColumn("string", "Dependencies");

  data.addRows(DATA_ARRAY);

  const chart = new google.visualization.Gantt(
    document.getElementById("chart_div")
  );

  chart.draw(data, OPTIONS);
}

// Get previously stored data from gantt //
// let gantt_id = document.querySelector("h1").id;
const gantt_id = $("#chart_div").data("gantt-id");
console.log(`my gantt id is ${gantt_id}`);

let currentGanttData;

fetch(`/api/gantt/${gantt_id}.json`)
  .then((response) => response.json())
  .then((data) => (currentGanttData = data))
  .then(() => {
    // console.log(currentGanttData);
    for (const [key, value] of Object.entries(currentGanttData)) {
      // console.log(`${key}`);
      const a = document.getElementById("list");
      let string_to_add = currentGanttData[key]["name"].concat(
        " | ",
        currentGanttData[key]["category"] ?? "N/A",
        " | ",
        currentGanttData[key]["days_to_maturity"] ?? "N/A",
        " | ",
        dayjs(currentGanttData[key]["start_date"])
          .add(7, "hour")
          .format("YYYY-MM-DD"),
        " | ",
        dayjs(currentGanttData[key]["end_date"])
          .add(7, "hour")
          .format("YYYY-MM-DD")
      );
      const li = document.createElement("li");
      li.setAttribute("class", "gantt-item");
      li.setAttribute("id", currentGanttData[key]["name"]);
      li.appendChild(document.createTextNode(string_to_add));
      a.appendChild(li);
      document
        .getElementById(currentGanttData[key]["name"])
        .insertAdjacentHTML(
          "beforeend",
          `&nbsp; <button id='remove-item ${gantt_counter.toString()}' class='remove-item btn btn-outline-danger btn-xs'> X </button>`
        );
    }
    console.log("loaded data from chart");
    loadExistingGantt();
  });

// function loadExistingGantt(ganttItems) {
function loadExistingGantt() {
  DATA_ARRAY = [];
  console.log("loading exiting gantt chart....");
  let ganttItems = document.querySelectorAll(".gantt-item");
  for (const item of ganttItems) {
    // kill these lines since we have a json object fed int
    plant_string = item.textContent.replace(" X ", "");
    console.log(item.textContent.replace(" X ", ""));
    let plant_name = plant_string.split(" | ")[0];
    let start_date = plant_string.split(" | ")[3];
    let end_date = plant_string.split(" | ")[4];
    //need to conver the json string date to a js date (dayjs)
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
    DATA_ARRAY.push(data_to_add);
  }
  drawChart;
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
  DATA_ARRAY.push(data_to_add);
  console.log(DATA_ARRAY);
  drawChart();
  a.appendChild(li);
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
  DATA_ARRAY = DATA_ARRAY.filter(
    (plant) => plant[0] !== btnClicked.parentElement.id
  );
  btnClicked.parentElement.remove();
  drawChart();
});

// SAVE CHANGES

// make it listen to the "save changes" button
const saveBtn = document.getElementById("save changes");
saveBtn.addEventListener("click", (evt) => {
  console.log("SAVE MY CHANGES!!!");
  console.log(DATA_ARRAY);
  console.log(`my gantt id is ${gantt_id}`);
  const data_export = { gantt_id: gantt_id, line_items: DATA_ARRAY };

  fetch("/submit-gantt-change", {
    method: "POST",
    body: JSON.stringify(data_export),
    headers: {
      "Content-Type": "application/json",
    },
  })
    .then((response) => response.json())
    .then((responseJson) => {
      alert(responseJson.status);
    });
});
