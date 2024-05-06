//simple nav function
toWelcome.onclick = function() {
    window.location.href = "http://localhost:8000/welcome/"; // Change this to your desired URL
};
//when the page is loaded, we can add an event listener to our form
document.addEventListener('DOMContentLoaded', function() {
  const form = document.querySelector('form');

  form.addEventListener('submit', function(event) {
    event.preventDefault();

    //immediately hash password
    const username = document.querySelector('#username').value.trim();
    const password = CryptoJS.SHA1(document.querySelector('#password').value.trim()).toString();

    const data = {
      username: username,
      password: password
    };

    fetch('/login-verify/', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        'X-CSRFToken': csrfToken
      },
      body: JSON.stringify(data)
    })
    .then(response => {
      if( response.ok )
      {
        console.log(response);
        window.location.href = '/welcome/';
      } 
      else 
      {
        return response.json();
      }
    })
    .then(data => {
      //if we make it here, it means the passwords did not match and an error was thrown on the backen
      window.alert(data.error);
    })
    .catch(error => {
      console.error('Error:', error);
    });

  });

});

document.getElementById("signupBtn").addEventListener("click", function() {
    window.location.href= 'http://localhost:8000/signup/';
});