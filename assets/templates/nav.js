// nav.js

document.addEventListener("DOMContentLoaded", function () {
    // Define the navigation links
    var navLinks = [
        { text: 'Me', href: '/' },
        { text: 'Maths', href: '/mathematics/' },
        { text: 'Data Science', href: '/data_science/' },
        { text: 'Football', href: '/football/' },
        { text: 'Yu-Gi-Oh', href: '/yugioh/' },
        { text: 'Cooking', href: '/cooking/' },
        { text: 'Other Stuff', href: '/misc/' }
    ];

    // Find the navigation container in the current HTML file
    var navContainer = document.getElementById("nav");

    // Create the navigation links and add them to the container
    if (navContainer) {
        var navHtml = navLinks.map(function (link) {
            return '<a href="' + link.href + '">' + link.text + '</a>';
        }).join(' | ');

        navContainer.innerHTML = navHtml;
    }
});