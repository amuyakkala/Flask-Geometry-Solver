# Python service using Flask that acts as a geometry engine. 
##  Instructions to Run the Service Locally
### Clone the Repository: 
#### Clone the repository containing the Flask application to your local machine. Here Just extract the zip file and get inside the assignment-1 folder.
#### Navigate to the Directory: Open your terminal or command prompt and navigate to the directory (assignment-1) where the Flask application is located.
### Set Up Virtual Environment: If you haven't already set up a virtual environment, create one using virtualenv or venv:
#### virtualenv venv  or
#### python -m venv venv
### Activate the Virtual Environment: Activate the virtual environment:
#### On Windows:
#### venv\Scripts\activate
#### On macOS and Linux:
#### source venv/bin/activate
### Install Dependencies: Install Flask if you haven't already installed it:
#### pip install -r requirements.txt
### Run the Flask Application: Run the Flask application:
#### python app.py
### Access the Endpoints: Once the Flask application is running, you can access the endpoints using tools like Postman or by sending HTTP requests programmatically.

### To run the application if everything has been setup (running locally):
#### In one terminal activate the virtual environment and run the geometry.py file as a simple python file. `python geometry.py`. This will start the flask server at localhost on port 5000(default).
#### In another terminal, while the geometry file is running, run the test_endpoints.py file to run the 4 tests.
#### If you want to check the output separately, try the POSTMAN application or cmd itself to send the post method to the endpoints and get the output for your input.
### To run the Docker container, Just run the following commands inside the directory
#### `docker build -t flask-app .`
#### `docker run -p 5000:5000 flask-app`
 Python service using Flask that acts as a geometry engine. 
