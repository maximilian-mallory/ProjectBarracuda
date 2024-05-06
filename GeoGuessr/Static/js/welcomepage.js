//simple nav
document.getElementById("leaderBtn").addEventListener("click", function() {
    window.location.href= 'http://localhost:8000/leaderboard/';
    //Here is the link I used to store the variables
    //abc123
    //https://stackoverflow.com/questions/27765666/passing-variable-through-javascript-from-one-html-page-to-another-page
});
//more nav
document.getElementById("casualBtn").addEventListener("click", function() {
    localStorage.setItem("isRanked",false);
    window.location.href= 'http://localhost:8000/gamepage/';
});

//this is attached to the ranked button
function tryRanked()
{
    if(username != 'null') //if there is a user logged in, they can play ranked
    {
            window.location.href= 'http://localhost:8000/gamepage/';
    }
    else 
    {   //otherwised they will be asked to log in to continue
        var choice = confirm("You need to login to play ranked. Would you like to login and play ranked?");

        if (choice) 
        {
            //If user chooses to login and play ranked
            window.location.href = 'http://localhost:8000/login/';
        }        
    }
}

rankedBtn.onclick = tryRanked;

//this will change the functionality and text value of the login/logout button
function toggleLoginLogout () 
{
    if(username != 'null') //if someone is logged in, we want to let them to be able to logout
    {
        loginBtn.textContent = 'Logout';
        loginBtn.onclick = function () 
        {
            fetch('/logout/', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'X-CSRFToken': csrfToken
            },
            credentials: 'same-origin', 
        })
        .then(response => {
            if (!response.ok) {
                throw new Error('Logout failed');
            }
            return response.json();
        })
        .then(data => {
            window.location.reload();
        })
        .catch(error => {
            console.error('Logout error:', error);
        });
        }
    }
    else //otherwise they will get redirected to the login page
    {
        loginBtn.textContent = 'Login';
        loginBtn.onclick = function () {
            window.location.href = 'http://localhost:8000/login/';
        };
    }

}

window.addEventListener('load', toggleLoginLogout);