from config import client
from utils.logger import Logger

class Moderation:

  @staticmethod
  def is_safe(transcript_txt : str , threshold : float = 0.8)-> bool:

    Logger.log("Checking moderation...")
    # Send the moderation request
    response = client.moderations.create(
           model="text-moderation-latest",
           input = transcript_txt
     )
    # Extract scores and convert to dictionary
    scores = response.results[0].category_scores.model_dump()
    safe = True
    if any(score is not None and score > threshold for score in scores.values()):
       safe = False       
    else:
       safe = True

    Logger.log("Safe ✅" if safe else "Unsafe ❌")
    return safe