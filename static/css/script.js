document.getElementById('predictForm').addEventListener('submit', function(event) {
    event.preventDefault();
    
    const formData = new FormData(event.target);
    const data = Object.fromEntries(formData.entries());
    
    fetch('/predict', {
        method: 'POST',
        body: new URLSearchParams(data) // Use URLSearchParams to send form data as `application/x-www-form-urlencoded`
    })
    .then(response => response.json())
    .then(result => {
        if (result.error) {
            document.getElementById('result').innerText = 'Error: ' + result.error;
        } else {
            document.getElementById('result').innerText = 'Prediction: ' + result.CourseCompletion;
        }
    })
    .catch(error => {
        console.error('Error:', error);
        document.getElementById('result').innerText = 'Error occurred';
    });
});
