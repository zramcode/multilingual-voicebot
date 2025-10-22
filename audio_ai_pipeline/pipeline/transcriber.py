from config import client
from utils.logger import Logger

class Transcriber:

  @staticmethod
  def transcribe(audio_path : str)-> str:
    Logger.log("Transcribing audio...")
    with open(audio_path,"rb") as audio_file:
         response = client.audio.transcriptions.create(
            model = "gpt-4o-transcribe",
            file = audio_file
            )
    transcript = response.text.strip()
    Logger.log("Transcribtion compelet.")
    return transcript
