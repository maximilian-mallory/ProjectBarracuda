//nav function
toWelcome.onclick = function() {
    window.location.href = "http://localhost:8000/welcome/"; // Change this to your desired URL
};

//check that the both passwords entered by the user are identical
function validatePassword(password, confirmpassword)
{
  if( password !== confirmpassword )
  {

    return false;
  }
  else
  {

    return true;
  }
}

var message = document.getElementById('message');


document.addEventListener('DOMContentLoaded', function() {
const form = document.querySelector('form');

  form.addEventListener('submit', function(event) {
    event.preventDefault();

    //access form data and hash passwords
    const username = document.querySelector('#username').value.trim();
    const password = CryptoJS.SHA1(document.querySelector('#password').value.trim()).toString();
    const confirmpassword = CryptoJS.SHA1(document.querySelector('#confirmpassword').value.trim()).toString();

    //if the hash values do not match, make the inputs red and alert the user
    if( validatePassword(password, confirmpassword) == false )
    {
      message.textContent = "Passwords do not match";
      document.querySelector('#password').style.border = "1px solid red";
      document.querySelector('#confirmpassword').style.border = "1px solid red";
    }  
    else //otherwise create the user 
    {
      const data = {
        username: username,
        password: password
      };

      fetch('/sign-up-verify/', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
          'X-CSRFToken': csrfToken //this is mad idk why
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