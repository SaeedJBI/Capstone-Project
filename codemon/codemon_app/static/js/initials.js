document.addEventListener('DOMContentLoaded', function() {
    const userDropdown = document.querySelector('.desktop-user-dropdown');
    const userButton = document.querySelector('.user-initials-btn');
    const dropdownMenu = document.querySelector('.desktop-dropdown-menu');
    
    if (userButton && dropdownMenu) {
        // Toggle dropdown on click
        userButton.addEventListener('click', function(e) {
            e.stopPropagation();
            dropdownMenu.classList.toggle('show');
        });
        
        // Close dropdown when clicking outside
        document.addEventListener('click', function() {
            dropdownMenu.classList.remove('show');
        });
        
        // Prevent dropdown close when clicking inside dropdown
        dropdownMenu.addEventListener('click', function(e) {
            e.stopPropagation();
        });
    }
});