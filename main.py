import os
import openai
import flask

# openai.api_key = "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"

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