from fastapi import FastAPI, UploadFile, File
from fastapi.responses import Response
from rembg import remove, new_session

app = FastAPI()

# u2netp is the lightweight model, better suited to Render's free tier (512MB RAM)
session = new_session("u2netp")

@app.get("/")
def health_check():
    return {"status": "running"}

@app.post("/remove-background")
async def remove_background(file: UploadFile = File(...)):
    input_bytes = await file.read()
    output_bytes = remove(input_bytes, session=session)
    return Response(content=output_bytes, media_type="image/png")
