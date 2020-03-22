# Corvid19 Whatsapp Bot
This project is to create a whatsapp bot that can give latest information about COVID-19 situation in Sri Lanka

This app was created by following the base tutorial: https://www.twilio.com/blog/build-a-whatsapp-chatbot-with-python-flask-and-twilio

## Prereqisites
* [Python 3.6](https://www.python.org/downloads/) or newer
* Virtual environment python plugin (Installation steps are given below).
* [Flask](https://palletsprojects.com/p/flask/) web application framework for Python
* A smartphone with an active phone number and WhatsApp installed.
* A [Twilio](https://www.twilio.com/) account

## Developer Guide
1. Create a Fork of this repository and clone it to your developer machine.
2. Install [Python 3.6](https://www.python.org/downloads/) or newer.
3. Install Python package VirtualEnv. using `pip3 install virtualenv`. 
4. Activate virtual environment and install dependencies. Windows (Powershell) -> `virtualenv .env; .\.env\Scripts\activate; pip install -r requirements.txt`, Mac/Unix -> `virtualenv .env && source .env/bin/activate && pip install -r requirements.txt`
4. Run [Flask Application](https://flask.palletsprojects.com/en/1.1.x/cli/). Windows (Powershell) -> `$env:FLASK_APP = "bot.py"; flask run`, Mac/Unix -> `export FLASK_APP=bot.py && flask run`
5. Use the steps 'Testing the Chat bot' in the [article](https://www.twilio.com/blog/build-a-whatsapp-chatbot-with-python-flask-and-twilio) to setup ngrok tunnel and related Twilio configurations.

Note: Follow the cofiguration steps given in the [article](https://www.twilio.com/blog/build-a-whatsapp-chatbot-with-python-flask-and-twilio) for more information regarding how it works. If you need to install new python packages make sure you export them to requirements.txt by using `pip freeze > requirements.txt`

## Testing Locally
You can install Postman and send a POST request to http://127.0.0.1:5000/bot with raw body having number 1, 2 & etc. as input.

## Deployment
We are using AWS ElasticBeanstalk for the deployment and you can find more details in [Deploying a flask application to Elastic Beanstalk](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/create-deploy-python-flask.html)
