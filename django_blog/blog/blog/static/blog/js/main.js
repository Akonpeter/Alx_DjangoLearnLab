// // Basic example script to demonstrate dynamic behavior
// document.addEventListener('DOMContentLoaded', function() {
//     console.log('Blog page loaded');
// });

// blog/static/blog/js/main.js

document.addEventListener('DOMContentLoaded', function() {
    console.log('Authentication system JavaScript loaded');
    
    // Form validation enhancements
    const forms = document.querySelectorAll('form');
    forms.forEach(form => {
        form.addEventListener('submit', function(e) {
            const requiredFields = form.querySelectorAll('[required]');
            let isValid = true;
            
            requiredFields.forEach(field => {
                if (!field.value.trim()) {
                    isValid = false;
                    field.style.borderColor = '#dc3545';
                }
            });
            
            if (!isValid) {
                e.preventDefault();
                alert('Please fill in all required fields.');
            }
        });
    });
    
    // Password strength indicator for registration
    const passwordInput = document.querySelector('input[name="password1"]');
    if (passwordInput) {
        passwordInput.addEventListener('input', function() {
            const password = this.value;
            const strengthIndicator = document.createElement('div');
            strengthIndicator.className = 'password-strength';
            
            let strength = 0;
            if (password.length >= 8) strength++;
            if (/[A-Z]/.test(password)) strength++;
            if (/[0-9]/.test(password)) strength++;
            if (/[^A-Za-z0-9]/.test(password)) strength++;
            
            const parent = this.parentElement;
            const existingIndicator = parent.querySelector('.password-strength');
            if (existingIndicator) existingIndicator.remove();
            
            if (password) {
                strengthIndicator.innerHTML = `Password strength: ${'★'.repeat(strength)}${'☆'.repeat(4-strength)}`;
                strengthIndicator.style.color = strength >= 3 ? 'green' : strength >= 2 ? 'orange' : 'red';
                parent.appendChild(strengthIndicator);
            }
        });
    }
    
    // Real-time form validation
    const inputs = document.querySelectorAll('input');
    inputs.forEach(input => {
        input.addEventListener('blur', function() {
            if (this.value.trim() && this.checkValidity()) {
                this.style.borderColor = '#28a745';
            }
        });
        
        input.addEventListener('input', function() {
            this.style.borderColor = '#ddd';
        });
    });
});