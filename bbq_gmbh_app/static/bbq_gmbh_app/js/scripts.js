/*!
* Start Bootstrap - Grayscale v7.0.6 (https://startbootstrap.com/theme/grayscale)
* Copyright 2013-2023 Start Bootstrap
* Licensed under MIT (https://github.com/StartBootstrap/startbootstrap-grayscale/blob/master/LICENSE)
*/
//
// Scripts
// 

window.addEventListener('DOMContentLoaded', event => {

    // Navbar shrink function
    var navbarShrink = function () {
        const navbarCollapsible = document.body.querySelector('#mainNav');
        if (!navbarCollapsible) {
            return;
        }
        if (window.scrollY === 0) {
            navbarCollapsible.classList.remove('navbar-shrink')
        } else {
            navbarCollapsible.classList.add('navbar-shrink')
        }

    };

    // Shrink the navbar 
    navbarShrink();

    // Shrink the navbar when page is scrolled
    document.addEventListener('scroll', navbarShrink);

    // Activate Bootstrap scrollspy on the main nav element
    const mainNav = document.body.querySelector('#mainNav');
    if (mainNav) {
        new bootstrap.ScrollSpy(document.body, {
            target: '#mainNav',
            rootMargin: '0px 0px -40%',
        });
    };

    // Collapse responsive navbar when toggler is visible
    const navbarToggler = document.body.querySelector('.navbar-toggler');
    const responsiveNavItems = [].slice.call(
        document.querySelectorAll('#navbarResponsive .nav-link')
    );
    // responsiveNavItems.map(function (responsiveNavItem) {
    //     responsiveNavItem.addEventListener('click', () => {
    //         if (window.getComputedStyle(navbarToggler).display !== 'none') {
    //             navbarToggler.click();
    //         }
    //     });
    // });

});


// // Icon byUsername
// var user = {
//     tag: 'hr' // this could be 'admin', 'hr', 'ma'
// };

// // droptown by ID
// var dropdownItem = document.getElementById('user');

// // Create an icon element
// var icon = document.createElement('i');
// icon.style.marginRight = '5px'; // Add some space between the icon and the text

// // logic
// if (user.tag === 'admin') {
//     icon.className = 'fa-solid fa-user-plus';
// } else if (user.tag === 'hr') {
//     icon.className = 'fa-solid fa-user-tie';
// } else if (user.tag === 'ma') {
//     icon.className = 'fa-solid fa-user';
// }

// // Add icon to dropdown item
// dropdownItem.prepend(icon);


// //Password Change and alerts
// document.querySelector('form').addEventListener('submit', function(event) {
//     event.preventDefault(); // Prevent the form from submitting

//     var correctPassword = '12345';

//     var currentPassword = document.getElementById('currentPassword').value;
//     var newPassword = document.getElementById('newPassword').value;
//     var confirmNewPassword = document.getElementById('confirmNewPassword').value;
    
//     if (!currentPassword || !newPassword || !confirmNewPassword) {
//         document.getElementById('message').textContent = 'All fields must be filled out.';
//         document.querySelector('.card').style.display = 'block'; // Show the card
//     } else if (currentPassword !== correctPassword) {
//         document.getElementById('message').textContent = 'Current password is incorrect.';
//         document.querySelector('.card').style.display = 'block'; // Show the card
//     } else if (newPassword.length < 8) {
//         document.getElementById('message').textContent = 'New password must be at least 8 characters long.';
//         document.querySelector('.card').style.display = 'block'; // Show the card
//     } else if (newPassword !== confirmNewPassword) {
//         document.getElementById('message').textContent = 'New password does not match the confirmed password.';
//         document.querySelector('.card').style.display = 'block'; // Show the card
//     } else {
//         document.getElementById('message').textContent = 'Password changed successfully.';
//         var card = document.querySelector('.card');
//         card.style.display = 'block'; // Show the card and store it in a variable
//         card.classList.add('bg-success'); // Add the 'bg-success' class to the card
//         // Here you can add the code to actually change the password
//     }
// });


// altomaticly scroll element into view
window.onload = function() {
    var element = document.getElementById('myElement');
    element.scrollIntoView({behavior: "smooth", block: "center"});
}


// Navicon

function executeMyCode(user) {
    var navbar = document.querySelector('.navbar-nav.ms-auto');

    if (user.tag === "admin" || user.tag === "hr") {
        // Create new nav item and link
        var employeeManagementUrl = document.body.dataset.employeeManagementUrl;
        var newItem = document.createElement('li');
        newItem.className = 'nav-item';

        var newLink = document.createElement('a');
        newLink.className = 'nav-link';
        newLink.href = employeeManagementUrl;
        newLink.textContent = 'Employee management';

        // Append new link to new item
        newItem.appendChild(newLink);

        // Find the position where the new item should be inserted
        var refItem = document.querySelector('.navbar-nav.ms-auto .nav-item:nth-last-child(2)');

        // Insert the new item before the reference item
        navbar.insertBefore(newItem, refItem);
    }
}

// fetch user tag
fetch('/get_user_role/')
.then(response => response.json())
.then(data => {
    if (data.user_role) {

        // Icon byUsername
        var user = {
            tag: data.user_role // this could be 'admin', 'hr', 'ma'
        };

        // droptown by ID
        var dropdownItem = document.getElementById('user');

        // Create an icon element
        var icon = document.createElement('i');
        icon.style.marginRight = '5px'; // Add some space between the icon and the text

        // logic
        if (user.tag === 'admin') {
            icon.className = 'fa-solid fa-user-plus text-danger';
        } else if (user.tag === 'hr') {
            icon.className = 'fa-solid fa-user-tie text-warning';
        } else {
            icon.className = 'fa-solid fa-user text-primary';
        }

        // Add icon to dropdown item
        dropdownItem.prepend(icon);

        // Execute the function with the user object
        executeMyCode(user);
    }
})
.catch(error => console.error('Error:', error));