document.getElementById('mode-toggle').addEventListener('click', function () {
    document.body.classList.toggle('dark');
    document.body.classList.toggle('light');
    
    // Change the icon based on the mode
    if (document.body.classList.contains('dark')) {
        this.textContent = '🌙'; // Dark mode
    } else {
        this.textContent = '🌞'; // Light mode
    }
});
