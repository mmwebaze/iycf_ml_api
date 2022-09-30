## IYCF ML API

* Introduction 
* Requirements
* Installation
* Testing the API
* Future functionality

### INTRODUCTION
------------
The IYCF image databank...

### REQUIREMENTS
------------

* Python 3 (This api was developed using 3.9.13)
* Tensorflow 2.8.2
* Docker
* Docker-compose

### INSTALLATION
------------
Start by cloning this repository and choose your development setup as below:

### Docker
* Build an image from the included docker file
* Run docker-compose against the included docker-compose file
### Without Docker
* Create a virtual environment
* Run pip3 install -r requirements.txt to satisify local dependencies
* Run python api.py and access the api on localhost:8002

### Testing the API
#### Using the Swagger
* From the docs end-point (http://ec2-54-174-165-232.compute-1.amazonaws.com:8002/docs) one can see the endpoints available for testing. 
* Select the predict classification endpoint
* Select the 'Try it out' button
* Attach an image and execute
* The json response will contain a model-prediction-confidence-score and the model-prediction

#### Using Postman or Thunder Clients
* Send a POST request to the prediction endpoint "/image/classification/prediction"