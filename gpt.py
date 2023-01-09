#!/usr/bin/env python3

import argparse
import json
import os
import requests
from pygments import highlight
from pygments.lexers import JsonLexer
from pygments.formatters import TerminalFormatter

# Set default values for command-line arguments
MODEL = "text-davinci-003"  # model to use
TOKEN_COUNT = 300  # number of tokens to generate
TEMPERATURE = 0.4  # temperature
TOP_P = 1  # top_p value
FREQUENCY = 0.5  # frequency penalty
PRESENCE = 0.5  # presence penalty

def main():
  """Main entry point."""
  # Parse command-line arguments
  parser = argparse.ArgumentParser()
  parser.add_argument("prompt", nargs="?", default="",
                      help="prompt to use as input for the GPT-3 model")
  parser.add_argument("-k", "--api-key",
                      help="OpenAI API key")
  args = parser.parse_args()

  # Get the OpenAI API key
  api_key = args.api_key or os.environ.get("OPENAI_API_KEY")
  if not api_key:
    print("Error: OPENAI_API_KEY is not set.")
    return

  # Set up the API request
  url = "https://api.openai.com/v1/completions"
  headers = {
    "Authorization": f"Bearer {api_key}",
    "Content-Type": "application/json",
  }
  data = {
    "model": MODEL,
    "prompt": args.prompt,
    "temperature": TEMPERATURE,
    "top_p": TOP_P,
    "frequency_penalty": FREQUENCY,
    "presence_penalty": PRESENCE,
    "max_tokens": TOKEN_COUNT,
  }

  # Send the API request
  response = requests.post(url, headers=headers, json=data)

  # Check for errors in the API response
  if response.status_code != 200:
    print("Error:", response.json()["error"])
    return

  # Extract the text from the response
  text = response.json()["choices"][0]["text"]

  # Print the output
  print(text)

if __name__ == "__main__":
  main()
