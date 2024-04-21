window.addEventListener('load', function() {
    // Überprüfe, ob die CSS-Datei geladen wurde
    var linkElement = document.querySelector('link[href="#"]');
    
    if (linkElement) {
        console.log('Die CSS-Datei wurde erfolgreich geladen!');
    } else {
        console.error('Fehler beim Laden der CSS-Datei!');
    }
});
