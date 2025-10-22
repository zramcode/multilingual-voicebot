from config import client
from utils.logger import Logger

class Refiner:

  @staticmethod
  def refine(transcript_txt : str)-> str:

    Logger.log("Refining Trsnscript...")
     # Fix the mistake in the transcript
    response = client.chat.completions.create(
       model = "gpt-4o-mini",
       max_completion_tokens = 300,
       messages = [{
         "role":"system", "content":"You are an AI assistant that corrects technical transcription errors, including misheard technology names (e.g., 'Lang chain' → 'LangChain'), and fixes minor grammar issues. Return only the corrected text."},
         {"role": "user", "content": transcript_txt}] 
)

    corrected_text = response.choices[0].message.content.strip()
    Logger.log("Refinement compelet.")
    return corrected_text