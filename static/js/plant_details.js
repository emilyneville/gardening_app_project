"use strict";

document.querySelector("#favorite-button").addEventListener("click", (evt) => {
  const loginBtn = evt.target;

  if (loginBtn.innerHTML === "Favorite This Plant!") {
    const formInputs = {
      plantId: document.querySelector("title").innerHTML,
    };

    fetch("/add-favorite", {
      method: "POST",
      body: JSON.stringify(formInputs),
      headers: {
        "Content-Type": "application/json",
      },
    })
      .then((response) => response.json())
      .then((responseJson) => {
        if (responseJson.success === "false") {
          alert("You must log in to favorite a plant");
        } else {
          alert("You have added this plant to favorites!");
          document.getElementById("favorite-button").classList.remove('btn-primary');
          document.getElementById("favorite-button").classList.add('btn-outline-danger');
          loginBtn.innerHTML = "Remove Plant From Favorites";
          
        }
      });
  } else {

    const formInputs = {
      plantId: document.querySelector("title").innerHTML,
    };
    fetch("/remove-favorite", {
      method: "POST",
      body: JSON.stringify(formInputs),
      headers: {
        "Content-Type": "application/json",
      },
    })
      .then((response) => response.json())
      .then((responseJson) => {
        if (responseJson.success === "false") {
          alert("You must log in to unfavorite a plant");
        } else {
          alert("You have removed this plant from favorites </3 ");
          document.getElementById("favorite-button").classList.remove('btn-outline-danger');
          document.getElementById("favorite-button").classList.add('btn-primary');
          loginBtn.innerHTML = "Favorite This Plant!";
          
        }
      });
    
  }
});
