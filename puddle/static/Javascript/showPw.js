document.addEventListener('DOMContentLoaded', function() {
    const showPasswordToggles = document.querySelectorAll('.show-password-toggle-checkbox');
    const passwordFields = document.querySelectorAll('.password-field input[type="password"]');

    showPasswordToggles.forEach((toggle, index) => {
        toggle.addEventListener('change', function() {
            passwordFields[index].type = toggle.checked ? 'text' : 'password';
        });
    });
});
