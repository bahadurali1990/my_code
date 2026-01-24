from gtts import gTTS
from fastapi import FastAPI
from fastapi.responses import FileResponse,JSONResponse,StreamingResponse
import io
import os
from fastapi import FastAPI, Form
from fastapi.responses import JSONResponse
import subprocess
from pydantic import BaseModel


app = FastAPI()

@app.get("/")
async def get_chat_page():
    # Serve the HTML file directly
    return FileResponse(os.path.join("templates", "Home.html"))

@app.post("/chat")
async def chat_endpoint(payload: dict):

# Extract the user message from JSON body

    user_message = payload.get("message", "")

# Build prompt for Ollama

    prompt = f"User said: {user_message}. Respond naturally."

# Call Ollama CLI (replace 'llama2' with your model name)

    result = subprocess.run( ["ollama", "run", "llama2", prompt], capture_output=True, text=True )
    ollama_output = result.stdout.strip()
    tts = gTTS(text=ollama_output, lang="en")
    buf = io.BytesIO()
    tts.write_to_fp(buf)
    buf.seek(0)

    return StreamingResponse(buf, media_type="audio/mpeg")

    #return JSONResponse({"reply": ollama_output})
