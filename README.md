# SongForHue

# Instructions to Try:
## 1. Getting access to the cool stuff
Create an OpenAI account and get a secret key here https://openai.com/api/

## 2. Set up virtual environment

### Creating virtual environment:
`python3 -m venv venv`

### Activating virtual environment:
`source venv/bin/activate`

### Deactivating virtual environment:
`deactivate`

## 3. Dependencies
`pip install flask`

`python -m pip install python-dotenv`

`pip install openai`

`pip install requests`

The following command can confirm installation of flask:
`python -c "import flask; print(flask.__version__)"`
should output something like
`2.2.2`

## 4. Running Flask Web App
`export FLASK_APP=home && export FLASK_DEBUG=True && flask run`
If everything goes well, you should have a localhost running with a message like "* Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)," where you can view your current project.
