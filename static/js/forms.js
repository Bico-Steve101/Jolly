// static/js/forms.js

document.addEventListener('DOMContentLoaded', function () {
    // Smooth scroll effect for anchor links
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function (e) {
            e.preventDefault();

            document.querySelector(this.getAttribute('href')).scrollIntoView({
                behavior: 'smooth'
            });
        });
    });

    // Validate password and confirmation password match on registration form
    const registerForm = document.getElementById('register-form');

    if (registerForm) {
        registerForm.addEventListener('submit', function (e) {
            const password = document.getElementById('id_password').value;
            const confirmPassword = document.getElementById('id_confirm_password').value;

            if (password !== confirmPassword) {
                e.preventDefault();
                alert('Passwords do not match. Please re-enter.');
                // You can also provide more user-friendly feedback, like updating a div element with an error message.
            }
        });
    }
});
