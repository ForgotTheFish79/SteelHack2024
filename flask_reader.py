from flask import Flask, request, render_template

app = Flask(__name__)

# Route for the home page
@app.route('/')
def home():
    return render_template('index.html')  # Render the HTML form

# Route to handle form submissions
@app.route('/submit', methods=['POST'])
def submit():
    # Retrieve form data
    username = request.form.get('username')
    email = request.form.get('email')
    major = request.form.get('major')
    year = request.form.get('year')
    
    # Log the received data
    print(f'Received: {username}, {email}, {major}, {year}')
    
    # Respond to the user
    return f'Data received: {username}, {email}, {major}, {year}'

if __name__ == '__main__':
    app.run(debug=True)  # Start the Flask application