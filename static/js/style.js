document.addEventListener('DOMContentLoaded', () => {
    const showLogin = document.getElementById('showLogin');
    const loginOverlay = document.getElementById('loginOverlay');
    const closeLogin = document.getElementById('closeLogin');

    showLogin.addEventListener('click', () => {
        loginOverlay.classList.remove('hidden');
        loginOverlay.classList.add('flex'); 
    });

    closeLogin.addEventListener('click', () => {
        loginOverlay.classList.remove('flex'); 
        loginOverlay.classList.add('hidden');
    });
});