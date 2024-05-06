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

function startTimer(duration, display) 
{
    var timer = duration;
    var interval = setInterval(function () {
        var minutes = parseInt(timer / 60, 10);
        var seconds = parseInt(timer % 60, 10);

        seconds = seconds < 10 ? "0" + seconds : seconds;

        display.textContent = minutes + ":" + seconds;

        if (--timer < 0) {
            clearInterval(interval);
            display.textContent = "Time Bonus Gone!";
            return;
        } else if (timer > 180) {
            display.style.color = "green";
        } else if (timer < 180 && timer >= 60) {
            display.style.color = "orange";
        } else if (timer < 60 && timer >= 30) {
            display.style.color = "red";
        } else if (timer < 30 && timer % 2 == 1) {
            display.style.color = "red";
            display.style.backgroundColor = "black";
        } else if (timer < 30 && timer % 2 == 0) {
            display.style.color = "red";
            display.style.backgroundColor = "white";
        }

        remainingTime = timer;
    }, 1000);

    remainingTime = timer;

}

function loadAllScores() 
{
    const leaderboardBody = document.getElementById("leaderboardBody");
    leaderboardBody.innerHTML = "";
    let i = 0;
    allScores.forEach(entry => {
        if (i >= 10) return;
        const row = document.createElement("tr");
        row.innerHTML = `
            <td>${++i}</td>
            <td>${entry.fields.username}</td>
            <td>${entry.fields.score}</td>
        `;
        leaderboardBody.appendChild(row);
    });
}

function checkGuess() 
{
  numGuesses++;
  
  guess = userGuess.value;

  if( guess.toLowerCase() == city_name )
  {
    clearInterval(interval);
    
    var data = {
    timeLeft: remainingTime.toString(),
    numGuesses: numGuesses.toString(),
    hintOne: hintOne,
    hintTwo: hintTwo
    };

    fetch('/save_score/', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(data)
    })
    .then(response => {
        if (!response.ok) {
            throw new Error('Error saving guess');
        }
        return response.text();
    })
    .then(data => {

      var choice = confirm("Correct! Would you like to play again??");
        
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

hint2btn.onclick = function() 
{
    var data = {
      city: city_name,
    }
  
    fetch('/getbird/', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'
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
      console.log(hint2content.value);
  
      hintsUsed++;
      hintTwo = true;
    })
    .catch(error => {
      console.error('Error:', error);
    });
  
}
  
hint1btn.onclick = function() 
{
    var data = {
      latitude: latitude,
      longitude: longitude
    }
  
    fetch('/getweather/', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'
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
      console.log(hint1content.value);
      
    })
    .catch(error => {
      console.error('Error:', error);
    });
  
};

window.onload = function () 
{
    var fiveMinutes = 300,
        display = document.querySelector('#timerDiv');
    interval = startTimer(fiveMinutes, display);
    loadAllScores();
    initialize();
};