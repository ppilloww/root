// Systemdatum
let day = document.getElementById("day");
let weekday = document.getElementById("weekday");
let month = document.getElementById("month");
let year = document.getElementById("year");
// Systemuhrzeit
let hrs = document.getElementById("hrs");
let min = document.getElementById("min");
let sec = document.getElementById("sec");
let currentDate
let currentTime


// setInterval(() => {
currentDate = new Date();

let dayOfMonth = currentDate.getDate();
let dayNames = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"];
let dayOfWeek = dayNames[currentDate.getDay()]; 
let currentMonth = currentDate.getMonth() + 1;
let currentYear = currentDate.getFullYear();

// logic for numbers smaller 10
dayOfMonth = (dayOfMonth < 10) ? '0' + dayOfMonth : dayOfMonth;
currentMonth = (currentMonth < 10) ? '0' + currentMonth : currentMonth;

day.innerHTML = dayOfMonth;
weekday.innerHTML = dayOfWeek;
month.innerHTML = currentMonth;
year.innerHTML = currentYear;

// }, 1000);



setInterval(()=>{
    currentTime = new Date();

    let hours = currentTime.getHours(); 
    let minutes = currentTime.getMinutes();
    let seconds = currentTime.getSeconds();

    // logic numbers smaller 10
    hours = (hours < 10) ? '0' + hours : hours;
    minutes = (minutes < 10) ? '0' + minutes : minutes;
    seconds = (seconds < 10) ? '0' + seconds : seconds;

    hrs.innerHTML = hours;
    min.innerHTML = minutes;
    sec.innerHTML = seconds;

},1000)