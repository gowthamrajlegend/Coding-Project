from flask import Flask

# Create an instance of the Flask class
app = Flask(__name__)

# Define a route and the associated function to handle the request
@app.route('/')
def hello_world():
    return 'Hello, World!'

# Run the Flask application
if __name__ == '__main__':
    app.run()
