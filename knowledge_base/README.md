# Knowledge base
The directory contains knowledge base data files and utils

## Directory structure:
* `data/` — knowledge base represented as a bunch of json files. Every file has the same name as the bot's command which use it
* `insert_data.py` — python script for uploading the knowledge base (`data/*.json`) to a data storage
* `requirements.txt` — list of python libraries required to run `insert_data.py` script
