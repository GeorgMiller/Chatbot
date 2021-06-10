# Chatbot

Setup: install rasa==2.6.1

Download the two models and put the first one in the rasa folder, and the second one in the rasa/tts_model

deepspeech-0.9.3-models.pbmm

checkpoint_130000.pth.tar

cd in rasa and run

pip install -r requirements.txt

Then run in a terminal in the rasa folder  

rasa run -m models --enable-api --cors “*” --debug

When errors occur just pip install the modules. Didnt keep track

then cd in the server folder and run the 

python3 client.py

or 

node app

to run the server.

I modified the socketio_connector.py and the deepspeech_connector.py

Only two functions in the socketio_connector.py are actually important. I marked them with a lot of hashtagsc



