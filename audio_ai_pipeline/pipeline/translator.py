from config import client
from utils.logger import Logger

class Translator:

  @staticmethod
  def detect_language(text : str)-> str:

    Logger.log("Detecting language....")
    response = client.chat.completions.create(
     model = "gpt-4o-mini",
     messages = [{"role" : "user" ,"content": f"""Detect the language of the following message and return ONLY its ISO 639-1 language code (like en, fr, de, es, etc.).
        Message: {text}""" }]
      )
    language_code = response.choices[0].message.content.strip()
    Logger.log(f"Detected language{language_code}")

    return language_code
  
  def translate(transcription_txt : str , source_language : str ,  target_language : str = "en")-> str:
   
   if source_language == target_language: 
      return transcription_txt
   
   Logger.log(f"Translating text from {source_language} to {target_language}...")

   # Translate the transcript into English
   response = client.chat.completions.create(
     model = "gpt-4o-mini",
     messages = [{"role":"user" ,
                 "content":f"Translate this text from {source_language} to {target_language}:\n{transcription_txt}"}
                 ])

   # Extract the translated transcript text
   en_translated = response.choices[0].message.content.strip()
   Logger.log("Translation completed.")
   return en_translated  