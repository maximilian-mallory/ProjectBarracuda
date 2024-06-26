//simple nav function
toWelcome.onclick = function() {
    window.location.href = "http://localhost:8000/welcome/"; // Change this to your desired URL
};
//originally wanted to track the date and time the user played matches at but left it out
function formatTime(seconds) {
    const date = new Date(seconds * 1000);
    return date.toLocaleTimeString('en-US', { minute: '2-digit', second: '2-digit' });
}

//this will query all the data one time and filter it later
function loadAllScores() {
    //the page loads with all scores displayed and is attached to a button
    const leaderboardBody = document.getElementById("leaderboardBody");
    leaderboardBody.innerHTML = "";
    let i = 0;
    allScores.forEach(entry => {
        const row = document.createElement("tr");
        row.innerHTML = `
            <td>${++i}</td>
            <td>${entry.fields.username}</td>
            <td>${entry.fields.score}</td>
            <td>${formatTime(Math.abs(entry.fields.finalTime - 300))}</td>
        `;
        leaderboardBody.appendChild(row);
    });
}

//this will activate on click if there is a user logged in, otherwise they are asked to login and redirected
function loadUserScores() {
    if(username !== 'null')
    {
        const leaderboardBody = document.getElementById("leaderboardBody");
        leaderboardBody.innerHTML = "";

        let i = 0;
        allScores.forEach(entry => {
            if(entry.fields.username == username)
            {
                const row = document.createElement("tr");
                row.innerHTML = `
                    <td>${++i}</td>
                    <td>${entry.fields.username}</td>
                    <td>${entry.fields.score}</td>
                    <td>${formatTime(Math.abs(entry.fields.finalTime - 300))}</td>
                `;
                leaderboardBody.appendChild(row);
            }
        });
    }
    else
    {
        var choice = confirm("You must be logged in to view your scores\nWould you like to login?");
            
        if (choice) 
        {
            window.location.href= 'http://localhost:8000/login/';
        }  
    }
}

//attach functions to elements at loadtime
document.addEventListener("DOMContentLoaded", function() {

    allScoresButton.onclick = loadAllScores;
    userScoresButton.onclick = loadUserScores;
    window.onload = loadAllScores;

});