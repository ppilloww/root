// Icon byUsername
var user = {
    tag: 'hr' // this could be 'admin', 'hr', 'ma'
};

// droptown by ID
var dropdownItem = document.getElementById('user');

// Create an icon element
var icon = document.createElement('i');
icon.style.marginRight = '5px'; // Add some space between the icon and the text

// logic
if (user.tag === 'admin') {
    icon.className = 'fa-solid fa-user-plus';
} else if (user.tag === 'hr') {
    icon.className = 'fa-solid fa-user-tie';
} else if (user.tag === 'ma') {
    icon.className = 'fa-solid fa-user';
}

// Add icon to dropdown item
dropdownItem.prepend(icon);
