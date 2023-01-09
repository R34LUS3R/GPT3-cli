# GPT-3 CLI
A command-line interface for interacting with the OpenAI GPT-3 API.

## Requirements:
1. Python 3.5 or later
1. The requests library (install with `pip3 install requests`)
1. The pygments library (install with `pip3 install pygments`)
1. An OpenAI API key (sign up for a free API key at https://beta.openai.com/ and after login head towards https://beta.openai.com/account/api-keys for API key"

## Usage:

```gpt.py [-h] [-k API_KEY] [prompt]```
<br />
<br />

## optional arguments:

  `-h`, `--help` show this help message and exit
  
  `-k API_KEY`, `--api-key API_KEY` OpenAI API key

You can specify the OpenAI API key either as a command-line argument (-k or --api-key) or as an environment variable called OPENAI_API_KEY. If you do not specify the API key, the script will look for the OPENAI_API_KEY environment variable.
<br />
<br />

## To setup the environment variable: 

```export OPENAI_API_KEY=sk-ny0KrxyJrYMAqPuq+EpKiGmlkfUfrTvberror``` // demo key

Its recommended to add this into `.bashrc`, `.zshrc` or `.profile` in your home root directory as this way you wouldn't have to set it up or declare each time:

```echo "export OPENAI_API_KEY=sk-ny0KrxyJrYMAqPuq+EpKiGmlkfUfrTvberror" >> ~/.bashrc```
<br />
<br />

## To run the script, enter the following command:

```pip3 install -r requirements.txt```

```chmod +x gpt.py```

```./gpt.py` or `python3 gpt.py "give me script for scraping a website"```

You can also make the script executable and move it to a directory in your PATH (e.g. `/usr/local/bin`):

```cp gpt.py /usr/local/bin/g3```

Then you can run the script from any directory by simply typing `g3` from anywhere.

```g3 "how do I convrt pdf to docx from cli?"```

<br />
<br /> 

## Configuration:
The default values for the script's arguments are hardcoded at the top of the script. You can modify these values to change the behavior of the script.

`MODEL`: Specifies the model to use (default: `text-davinci-003`)

`TOKEN_COUNT`: Specifies the number of tokens to generate (default: `300`)

`TEMPERATURE`: Specifies the temperature (default: `0.4`)

`TOP_P`: Specifies the top_p value (default: `1`)

`FREQUENCY`: Specifies the frequency penalty (default: `0.5`)

`PRESENCE`: Specifies the presence penalty (default: `0.5`)
