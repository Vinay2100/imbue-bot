import os

os.system('python -m rasa_core.run -d models/dialogue -u models/nlu/current --port 5002 --connector facebook --credentials fb_credentials.yml')

