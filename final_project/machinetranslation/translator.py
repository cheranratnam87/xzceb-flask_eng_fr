import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']

authenticator = IAMAuthenticator('F3Ghtgt5f3zKM6rRWibE3rO4cgSKm4F2MX83OoZVjlic')
language_translator = LanguageTranslatorV3(
    version='2018-05-01',
    authenticator=authenticator
)

language_translator.set_service_url(
'https://api.au-syd.language-translator.watson.cloud.ibm.com/instances/a0e1a428-0be1-49eb-ba8e-36f6bdebb6e8')

def english_to_french(english_text):
    """
    This function returns text in french that was converted from english
    """
    french_text = language_translator.translate(english_text, model_id='en-fr').get_result()
    return french_text.get("translations")[0].get("translation")

def french_to_english(french_text):
    """
    This function returns text in english that was converted from french
    """
    english_text = language_translator.translate(french_text, model_id='fr-en').get_result()
    return english_text.get("translations")[0].get("translation")