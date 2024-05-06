toWelcome.onclick = function() {
    window.location.href = "http://localhost:8000/welcome/"; // Change this to your desired URL
};

function validatePassword(password, confirmpassword)
{
  if( password !== confirmpassword )
  {
    console.log("passwords don't match");
    return false;
  }
  else
  {
    console.log("passwords match");
    return true;
  }
}

var message = document.getElementById('message');

document.addEventListener('DOMContentLoaded', function() {
const form = document.querySelector('form');

  form.addEventListener('submit', function(event) {
    event.preventDefault();

    const username = document.querySelector('#username').value.trim();
    const password = CryptoJS.SHA1(document.querySelector('#password').value.trim()).toString();
    const confirmpassword = CryptoJS.SHA1(document.querySelector('#confirmpassword').value.trim()).toString();
    console.log(password);
    console.log(confirmpassword);

    if( validatePassword(password, confirmpassword) == false )
    {
      message.textContent = "Passwords do not match";
      document.querySelector('#password').style.border = "1px solid red";
      document.querySelector('#confirmpassword').style.border = "1px solid red";
    }  
    else
    {
      const data = {
        username: username,
        password: password
      };
      console.log(data);

      fetch('/sign-up-verify/', {
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
        }
        )
        .catch(error => {
          console.error('Error:', error);
        });
    }
  });
});