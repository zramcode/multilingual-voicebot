from config import client
from utils.logger import Logger

class TextToSpeech:

  @staticmethod
  def synthesize(user_text : str ,output_path: str = "output.mp3")-> str:

    Logger.log("converting text to speech...")
    # Create the text-to-speech request
    response = client.audio.speech.create(
    model = "gpt-4o-mini-tts",
    voice= "onyx",
    input = user_text
   )

    # Stream the response to an MP3 file
    response.stream_to_file(output_path)
    Logger.log(f"Audio saved at {output_path}")

    return output_path