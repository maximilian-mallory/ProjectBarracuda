document.getElementById("leaderBtn").addEventListener("click", function() {
    window.location.href= 'http://localhost:8000/leaderboard/';
    //Here is the link I used to store the variables
    //abc123
    //https://stackoverflow.com/questions/27765666/passing-variable-through-javascript-from-one-html-page-to-another-page
});

document.getElementById("casualBtn").addEventListener("click", function() {
    localStorage.setItem("isRanked",false);
    window.location.href= 'http://localhost:8000/gamepage/';
});



function tryRanked()
{
    if(username != 'null')
    {
            window.location.href= 'http://localhost:8000/gamepage/';
    }
    else 
    {
        var choice = confirm("You need to login to play ranked. Would you like to login and play ranked?");

        if (choice) 
        {
            //If user chooses to login and play ranked
            window.location.href = 'http://localhost:8000/login/';
        }        
    }
}

rankedBtn.onclick = tryRanked;



function toggleLoginLogout () 
{
    if(username != 'null')
    {
        loginBtn.textContent = 'Logout';
        loginBtn.onclick = function () 
        {
            fetch('/logout/', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
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
            console.log(data.message);
            window.location.reload();
        })
        .catch(error => {
            // Handle error
            console.error('Logout error:', error);
        });
        }
    }
    else 
    {
        loginBtn.textContent = 'Login';
        loginBtn.onclick = function () {
            window.location.href = 'http://localhost:8000/login/';
        };
    }

}

window.addEventListener('load', toggleLoginLogout);