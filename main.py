import os
import openai
import flask
from dotenv import load_dotenv

load_dotenv()

openai.api_key = os.getenv('OPENAI_API_KEY')

# response = openai.Completion.create(
#   model="text-davinci-003",
#   prompt="The CSS code for a color of sad, depression, and dogs:\n\nbackground-color: #6A5ACD",
#   temperature=0,
#   max_tokens=256,
#   top_p=1,
#   frequency_penalty=0,
#   presence_penalty=0,
#   stop=[";"]
# )