// fetch user tag
fetch('/login_view/', {
    method: 'POST',
    body: JSON.stringify({
        email: emailInput.value,
        password: passwordInput.value
    })
})
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

        // show only link by userId
        document.addEventListener('DOMContentLoaded', function() {
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
                var refItem = document.querySelector('.navbar-nav.ms-auto .nav-item:nth-child(2)');

                // Insert the new item before the reference item
                navbar.insertBefore(newItem, refItem);
            }
        });
        
    }
});