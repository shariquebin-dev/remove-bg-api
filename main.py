from fastapi import FastAPI, UploadFile, File
from fastapi.responses import Response
from rembg import remove, new_session

app = FastAPI()

# Model loads lazily on first request, not at startup,
# so the server can open its port immediately.
session = None

def get_session():
    global session
    if session is None:
        session = new_session("u2netp")
    return session

@app.get("/")
def health_check():
    return {"status": "running"}

@app.post("/remove-background")
async def remove_background(file: UploadFile = File(...)):
    input_bytes = await file.read()
    output_bytes = remove(input_bytes, session=get_session())
    return Response(content=output_bytes, media_type="image/png")
