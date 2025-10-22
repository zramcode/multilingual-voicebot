from config import client
from utils.logger import Logger

class Responder:

  @staticmethod
  def generate_reply(faqs: str, content_overview:str , user_text : str)-> str:

    Logger.log("Generating AI response...")
    instruction_prompt = f"""
    #### Role
You are a professional AI support assistant for mywebsite.com. You help with:
- Sales (pricing, plans, billing)
- Content (courses, recommendations, feedback)
- Marketing (partnerships, collaborations)

    #### How to Respond
1. Use the FAQs: {faqs}
2. Use the content overview: {content_overview}
3. Respond clearly and concisely in up to 3 paragraphs.
4. If unsure, direct the user to support@mywebsite.com.
"""

    # Generate AI response
    response = client.chat.completions.create(model="gpt-4o-mini",
          messages =[
                     {"role":"system","content" : instruction_prompt},
                     {"role":"user","content" : user_text}])

    chatbot_reply = response.choices[0].message.content.strip()
    Logger.log("AI reply generated.")
    return chatbot_reply
    