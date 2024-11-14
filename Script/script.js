const dropdowns = document.querySelectorAll('.dropdown-2, .dropdown, .sidebar-socialmedia');
dropdowns.forEach(dropdown => {
    dropdown.addEventListener('click', () => { 
        dropdown.classList.toggle('active'); 
    });
});
