//this function is used to access the google api with a lat long combo
function initialize ()
{
  const location = { lat: latitude, lng: longitude };
 
  const panorama = new google.maps.StreetViewPanorama(
    document.getElementById("pano"),
    {
      position: location,
      pov: {
        heading: 34,
        pitch: 10,
      },
      
      linksControl: true,
      panControl: false,
      enableCloseButton: false,
      addressControl: false,
      showRoadLabels: false,
      motionTracking: false,
    },           
  );
}

//this is the function used to start the timer
function startTimer(duration, display) 
{
    var timer = duration;
    var interval = setInterval(function () {
        var minutes = parseInt(timer / 60, 10);
        var seconds = parseInt(timer % 60, 10);

        seconds = seconds < 10 ? "0" + seconds : seconds;

        display.textContent = minutes + ":" + seconds;

        //when the user is out of time, let them know
        if (--timer < 0) 
        {
            clearInterval(interval);
            display.textContent = "Time Bonus Gone!";
            return; //return or else it will run again
        } 
        //first set of values is green for good
        else if (timer > 180) 
        {
            display.style.color = "green";
        } 
        //been playing for a while
        else if (timer < 180 && timer >= 60) 
        {
            display.style.color = "orange";
        } 
        //closing in
        else if (timer < 60 && timer >= 30)
        {
            display.style.color = "red";
        } 
        //oh shoot hurrt up
        else if (timer < 30 && timer % 2 == 1) 
        {
            display.style.color = "red";
            display.style.backgroundColor = "black";
        } 
        //flash timer when under 30 seconds
        else if (timer < 30 && timer % 2 == 0)
        {
            display.style.color = "red";
            display.style.backgroundColor = "white";
        }

        remainingTime = timer;
    }, 1000);

    remainingTime = timer;

}

//this will query all scores and only display the first ten
function loadAllScores() 
{
    const leaderboardBody = document.getElementById("leaderboardBody");
    leaderboardBody.innerHTML = "";
    let i = 0;
    allScores.forEach(entry => {
        if (i >= 10) return; //stop when we reach ten scores
        const row = document.createElement("tr");
        row.innerHTML = `
            <td>${++i}</td>
            <td>${entry.fields.username}</td>
            <td>${entry.fields.score}</td>
        `;
        leaderboardBody.appendChild(row);
    });
}

//this is the logic for checking the users guess
function checkGuess() 
{
  ++numGuesses; //always increment the number of guesses taken
  
  guess = userGuess.value;

  if( guess.toLowerCase() == city_name ) //if the input matches the context value
  {
    clearInterval(interval);
    
    var data = {
    timeLeft: remainingTime.toString(),
    numGuesses: numGuesses.toString(),
    hintOne: hintOne,
    hintTwo: hintTwo
    };

    //send data to the python backend with ajax
    fetch('/save_score/', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': csrfToken
        },
        body: JSON.stringify(data)
    }) //our python code returns an ajax response
    .then(response => {
        if (!response.ok) {
            throw new Error('Error saving guess');
        }
        return response.json();
    }) //if the response is good we have access to some json sent by the response
    .then(data => {

      var score = data.gamescore
      var choice = confirm(`Correct! Your score was ${score}\nWould you like to play again?`);
        
      if (choice) 
      {
        window.location.reload();
      }  
      else
      {
        window.location.href= 'http://localhost:8000/welcome/';
      }
    })
    .catch(error => {
        console.error('Error saving guess:', error);
        alert("Error saving guess");
    });
  }
  else
  {
    alert("Wrong");
  }
  
}

//this will simply get the matching key value pair from the stored map of state flowers
hint2btn.onclick = function() 
{
    var data = {
      city: city_name,
    }
  
    fetch('/getbird/', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        'X-CSRFToken': csrfToken
      },
      body: JSON.stringify(data)
    })
    .then(response => {
      if (!response.ok) {
              throw new Error('Error retrieving data');
          }
      return response.text();
    })
    .then(jsonString => {
      
      var jsonData = JSON.parse(jsonString);
      
      let flower = jsonData.flower;
      
      hint2content.value = `The state flower is the ${flower}`;
  
      hintsUsed++;
      hintTwo = true;
    })
    .catch(error => {
      console.error('Error:', error);
    });
  
}
  
//this will simply hit the server and ask it to grab the weather from the NWS API
hint1btn.onclick = function() 
{
    var data = {
      latitude: latitude,
      longitude: longitude
    }
  
    fetch('/getweather/', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        'X-CSRFToken': csrfToken
      },
      body: JSON.stringify(data)
    })
    .then(response => {
      if (!response.ok) {
              throw new Error('Error retrieving data');
          }
      return response.text();
    })
    .then(jsonString => {
      
      var jsonData = JSON.parse(jsonString);
      
      let temperature = jsonData.temperature;
  
      hint1content.value = `The current temperature is ${temperature}°F`;
  
      hintsUsed++;
      hintOne = true;
      
    })
    .catch(error => {
      console.error('Error:', error);
    });
  
};

//when we load the page we need to run some functions
window.onload = function () 
{
    var fiveMinutes = 300,
        display = document.querySelector('#timerDiv');
    interval = startTimer(fiveMinutes, display);
    loadAllScores();
    initialize();
};

