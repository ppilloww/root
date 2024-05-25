// The form will only submit if there are no errors.
// This script is used in the extra_js_bottom block of the templates.


let errors = JSON.parse('{{ form.errors|escapejs|safe }}');
document.querySelector('form').addEventListener('submit', function(event) {
event.preventDefault(); // Prevent the form from submitting

if (Object.keys(errors).length > 0) {
    document.querySelector('.card').style.display = 'block';
    
    let message = '';
    for (let field in errors) {
    message += field + ': ' + errors[field].join(', ') + '<br>';
    }
    document.getElementById('message').innerHTML = message;
} else {
    document.querySelector('form').submit();
}
});
