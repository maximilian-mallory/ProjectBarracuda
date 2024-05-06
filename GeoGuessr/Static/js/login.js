toWelcome.onclick = function() {
    window.location.href = "http://localhost:8000/welcome/"; // Change this to your desired URL
};

document.addEventListener('DOMContentLoaded', function() {
const form = document.querySelector('form');

form.addEventListener('submit', function(event) {
  event.preventDefault();

  const username = document.querySelector('#username').value.trim();
  const password = CryptoJS.SHA1(document.querySelector('#password').value.trim()).toString();

  const data = {
    username: username,
    password: password
  };
  console.log(data);

  fetch('/login-verify/', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify(data)
    })
    .then(response => {
      if( response.ok )
      {
        window.location.href = '/welcome/';
      } 
    })
    .catch(error => {
      console.error('Error:', error);
    });
});
});

document.getElementById("signupBtn").addEventListener("click", function() {
    window.location.href= 'http://localhost:8000/signup/';
});