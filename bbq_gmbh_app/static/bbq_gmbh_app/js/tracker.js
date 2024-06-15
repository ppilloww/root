// logic for checkin with message and database
// Check-in button
// this is handling holidays, messages and the checkin time
var cardRemove = document.querySelector('.alert');

document.getElementById('checkin').addEventListener('click', function(event) {
    event.preventDefault();


    fetch('/checkHolidays/')
    .then(response => response.json())
    .then(data => {
        cardRemove.classList.remove('bg-danger'); // this is to refresh the card
        cardRemove.classList.remove('bg-warning');
        cardRemove.classList.remove('bg-success');

        if (data.non_working_day) {
            
            document.getElementById('message').textContent = 'Check-in is not allowed on public holidays or Sundays. Enjoy your day off!';
            var card = document.querySelector('.alert');
            card.style.display = 'block'; // Show the card and store it in a variable
            card.classList.add('bg-danger'); // Add the 'bg-danger' class to the card   
        } else if (!data.allowedWorkingHours) {
            
            document.getElementById('message').textContent = 'A healthy sleep is important. Check-in is not allowed between 22:00h and 6:00h. Go to sleep!';
            var card = document.querySelector('.alert');
            card.style.display = 'block'; // Show the card and store it in a variable
            card.classList.add('bg-danger'); // Add the 'bg-danger' class to the card  

        } else if (data.checkOutStatus) {
            
            fetch('/checkIn/', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/x-www-form-urlencoded',
                    'X-CSRFToken': document.getElementById('csrfToken').value,
                },
                body: new URLSearchParams({
                    'status': 'True',
                }),
            })
            .then(response => {
                
                if (!response.ok) {
                    document.getElementById('message').textContent = 'Network response was not ok';
                    var card = document.querySelector('.alert');
                    card.style.display = 'block'; // Show the card and store it in a variable
                    card.classList.add('bg-warning');
                    throw new Error('Network response was not ok');
                } else {
                    document.getElementById('message').textContent = 'Have a nice day at work. ';
                    var card = document.querySelector('.alert');
                    card.style.display = 'block'; // Show the card and store it in a variable
                    card.classList.add('bg-success');

                    // refresh the table after check-in
                    fetch('/arbeitsstunden/')  // replace with the path to your Django view
                    .then(response => response.text())
                    .then(html => {
                        document.getElementById('table_body').innerHTML = html;
                    });
                    // refresh infobox
                    fetch('/infoBox/')  // replace with the path to your Django view
                    .then(response => response.text())
                    .then(html => {
                        document.getElementById('infobox').innerHTML = html;
                    });
                }

            })
            .catch(error => {
                document.getElementById('message').textContent = 'There has been a problem with your fetch checkin operation', error;
                var card = document.querySelector('.alert');
                card.style.display = 'block'; // Show the card and store it in a variable
                card.classList.add('bg-warning'); // Add the 'bg-warning' class to the card
                console.error('There has been a problem with your fetch checkin operation:', error);
            });                
        } else {
            document.getElementById('message').textContent = 'You are already checked in!';
            var card = document.querySelector('.alert');
            card.style.display = 'block'; // Show the card and store it in a variable
            card.classList.add('bg-warning'); // Add the 'bg-warning' class to the card
        }
    })
    .catch(error => { // Removed semicolon before this line
        document.getElementById('message').textContent = 'There has been a problem with your fetch holiday checkin operation', error;
        var card = document.querySelector('.alert');
        card.style.display = 'block'; // Show the card and store it in a variable
        card.classList.add('bg-warning'); // Add the 'bg-warning' class to the card
        console.error('There has been a problem with your fetch holiday operation:', error);
    });
});

// this is handling the checkout time
document.getElementById('checkout').addEventListener('click', function(event) {
    event.preventDefault();

    fetch('/checkHolidays/')
    .then(response => response.json())
    .then(data => {
        cardRemove.classList.remove('bg-danger'); // this is to refresh the card
        cardRemove.classList.remove('bg-warning');
        cardRemove.classList.remove('bg-success');
        // if (data.non_working_day) {
        //     document.getElementById('message').textContent = 'Check-in is not allowed on public holidays. Enjoy your day off!';
        //     var card = document.querySelector('.alert');
        //     card.style.display = 'block'; // Show the card and store it in a variable
        //     card.classList.add('bg-danger'); // Add the 'bg-danger' class to the card 
        // } else 
        if (data.checkInStatus){

            fetch('/checkOut/', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/x-www-form-urlencoded',
                    'X-CSRFToken': document.getElementById('csrfToken').value,
                },
                body: new URLSearchParams({
                    'status': 'False',
                }),
            })
            .then(response => {
                
                if (!response.ok) {
                    document.getElementById('message').textContent = 'Network response was not ok';
                    var card = document.querySelector('.alert');
                    card.style.display = 'block'; // Show the card and store it in a variable
                    card.classList.add('bg-warning');
                    throw new Error('Network response was not ok');
                } else{
                    document.getElementById('message').textContent = 'Have a great evening. ';
                    var card = document.querySelector('.alert');
                    card.style.display = 'block'; // Show the card and store it in a variable
                    card.classList.add('bg-danger');

                    // refresh the table after check-in
                    fetch('/arbeitsstunden/')  // replace with the path to your Django view
                    .then(response => response.text())
                    .then(html => {
                        document.getElementById('table_body').innerHTML = html;
                    });
                    // refresh infobox
                    fetch('/infoBox/')  // replace with the path to your Django view
                    .then(response => response.text())
                    .then(html => {
                        document.getElementById('infobox').innerHTML = html;
                    });
                }

            })
            .catch(error => {
                document.getElementById('message').textContent = 'There has been a problem with your fetch checkout operation', error;
                var card = document.querySelector('.alert');
                card.style.display = 'block'; // Show the card and store it in a variable
                card.classList.add('bg-warning'); // Add the 'bg-warning' class to the card
                console.error('There has been a problem with your fetch checkin operation:', error);
            });
        } else {
            document.getElementById('message').textContent = 'You are not checked in!';
            var card = document.querySelector('.alert');
            card.style.display = 'block'; // Show the card and store it in a variable
            card.classList.add('bg-warning'); // Add the 'bg-warning' class to the card
        }
    })
    .catch(error => { // Removed semicolon before this line
        document.getElementById('message').textContent = 'There has been a problem with your fetch holiday checkout operation', error;
        var card = document.querySelector('.alert');
        card.style.display = 'block'; // Show the card and store it in a variable
        card.classList.add('bg-warning'); // Add the 'bg-warning' class to the card
        console.error('There has been a problem with your fetch holiday operation:', error);
    });
});