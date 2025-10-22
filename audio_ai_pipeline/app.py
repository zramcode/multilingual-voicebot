from fastapi import FastAPI, File, UploadFile, Form
from fastapi.responses import HTMLResponse, FileResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from starlette.requests import Request
import os

from pipeline.transcriber import Transcriber
from pipeline.translator import Translator
from pipeline.refiner import Refiner
from pipeline.moderation import Moderation
from pipeline.responder import Responder
from pipeline.tts import TextToSpeech
from utils.logger import Logger 


app = FastAPI()
templates = Jinja2Templates(directory="templates")
app.mount("/static", StaticFiles(directory="static"), name="static")

UPLOAD_DIR = "uploads"
os.makedirs(UPLOAD_DIR, exist_ok=True)

@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/process")
async def process_audio(
    request: Request,
    file: UploadFile = File(...),
    faqs: str = Form("Pricing, refunds, course access"),
    content_overview: str = Form("My Website provides online courses in data science and AI.")
):
   file_path = os.path.join(UPLOAD_DIR, file.filename)
   with open(file_path, "wb") as f:
        f.write(await file.read())

   Logger.log("Starting Pipline....")

   #step1 : transcribing
   transcribt = Transcriber.transcribe(file_path)

   #step2 :  Detect and translate to English
   text_language = Translator.detect_language(transcribt)
   english_text = Translator.translate(transcribt, text_language, "en" )

   #step3 : Refine text
   refined_text = Refiner.refine(english_text)

   #step4 : moderate text
   if not Moderation.is_safe(refined_text, 0.8) : 
      Logger.log("Transcript failed moderation. Aborting.")
      return
   #step5 : Generate AI reply
   reply_text = Responder.generate_reply(faqs, content_overview, refined_text)

   #step6 : Ensure reply is safe
   if not Moderation.is_safe(reply_text, 0.8) : 
      reply_text = "I'm sorry, I cannot provide that response. Please contact support@mywebsite.com."

   #step7: Translate back to user language
   final_reply = Translator.translate(reply_text, "en" , text_language)

   #step8 : Convert to Audio
   output_audio_path = TextToSpeech.synthesize(final_reply, f"{UPLOAD_DIR}/response.mp3") 

   Logger.log("Pipline finished successfuly.")

   return FileResponse(output_audio_path, media_type="audio/mpeg", filename="response.mp3")