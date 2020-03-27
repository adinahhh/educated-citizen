"use strict";

// Trying out an event listener
// const button = document.querySelector('#contactLegis');

// button.addEventListener('click', () => {
//     alert('Great work!');
// });



// const button = document.querySelector('#bills');

// const showAlert = () => {
//     alert('Great work!');
// }

// button.addEventListener('click', showAlert);

// event listener using jQuery

// $('#bills').on('click', () => {
//     alert('Great work!');
// });

// const button = document.querySelector('#bills');

// button.addEventListener('click', (evt) => {
//     evt.preventDefault();
//     alert('Great work!');
// });

// from homepage.html form
// make sure user zipcode is at least 5 chars
// const userZipcode = document.querySelector('form');

// userZipcode.addEventListener('submit', (evt) => {
//     const zipcodeInput = document.querySelector('input[name="zipcode"]');

//     if (zipcodeInput.value.length < 5) {
//         evt.preventDefault();
//     }
// });

// #### Trying to show successAlert id in voting_results.html
// unclear how to use show method 

// function replaceFortune(results) {
//     $("#successAlert").html(results);
// }
/////////////
// $('#contactLegis').on('click', (evt) => {
//     evt.preventDefault();

//     $.get('/using-ajax', (res) => {
//     //$('#successAlert').text(res).show();
//     alert(res);
//     });
// });


// function showParty(evt) {
//     evt.preventDefault();

//     let url = "/using-ajax";
//     let formData = 
// }

/////////////
// $(document).ready(function(){
//     /* get the phone number for legislator */
//     $('#form').on('submit', function(event) {
//         event.preventDefault();

//         $.ajax({
//             data: {
//                 phone: $('#hidden').val()
//             }
//             type: 'GET',
//             url: '/using-ajax'
//         })
//             .done(function(data){
//                 $('#phone').text(data.phone).show();
//             });
//             }
// })

function show(elementId) { 
    document.getElementById("phone").style.display="none";
    document.getElementById("website").style.display="none";
    document.getElementById(elementId).style.display="block";
}











