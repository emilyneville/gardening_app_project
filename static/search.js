'use strict';

document.querySelector('#search-form').addEventListener('submit', evt => {
  evt.preventDefault();

  // Get user input from a form
  const formData = {
    keyword: document.querySelector('#keyword-field').value
  };
  alert(`You have entered ${keyword}`);
  // construct query string – will be in the format of 'city=CITY_VAL&address=ADDRESS_VAL'
  const queryString = new URLSearchParams(formData).toString();

//   fetch(`/delivery-info.json?${queryString}`)
//     .then(response => response.json())
//     .then(responseJson => {
//       // Display response from the server
//       alert(`This will cost $${responseJson.cost} and arrive in ${responseJson.days} day(s)`);
//     });
});
