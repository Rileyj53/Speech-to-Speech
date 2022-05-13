import json
from os.path import join, dirname
from ibm_watson import SpeechToTextV1
from ibm_watson.websocket import RecognizeCallback, AudioSource
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from ibm_watson import LanguageTranslatorV3
from ibm_watson import TextToSpeechV1


auth1 = '' # IBM Watson api key 
url1 = '' # IBM Watson api URL 

auth2 = '' # IBM Watson api key 
url2 = '' # IBM Watson api URL 

auth3 = '' # IBM Watson api key 
url3 = '' # IBM Watson api URL 

authenticator = IAMAuthenticator(auth1)
speech_to_text = SpeechToTextV1(
    authenticator=authenticator
)

# Translate an english audio file to text 

speech_to_text.set_service_url(url1)

with open(join(dirname('C:\\Users\\'), '', 'audio-file2.flac'),
               'rb') as audio_file:
      speech_recognition_results = speech_to_text.recognize(
        audio=audio_file,
        content_type='audio/flac',
        word_alternatives_threshold=0.9,

    ).get_result()

      # Recognize original files language

text_res= speech_recognition_results['results'][0]['alternatives'][0]['transcript']

authenticator = IAMAuthenticator(auth2)
language_translator = LanguageTranslatorV3(
    version='2018-05-01',
    authenticator=authenticator
)

# Translate original transcript to specific language (Spanish)

language_translator.set_service_url(url2)

translation = language_translator.translate(
    text = text_res,
    model_id='en-es').get_result()
text_tran = translation['translations'][0]['translation']
    
authenticator = IAMAuthenticator(auth3)
text_to_speech = TextToSpeechV1(
    authenticator=authenticator
)

# Narrate translated text. The result is in spanish

text_to_speech.set_service_url(url3)

with open('Final_Project.wav', 'wb') as audio_file:
    audio_file.write(
        text_to_speech.synthesize(
            text_tran,
            voice='es-US_SofiaV3Voice',
            accept='audio/wav'        
        ).get_result().content)