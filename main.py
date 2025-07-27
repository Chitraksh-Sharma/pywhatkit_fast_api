import pywhatkit
import time
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import datetime
import logging
from typing import Optional
# Set up logging

logger = logging.getLogger(__name__)

app = FastAPI(title="WhatsApp API", description="Send WhatsApp messages via API")

class MessageRequest(BaseModel):
    phone: str  # Include country code, e.g., "+917014451730"
    message: str

class MessageRequestImage(BaseModel):
    phone: str  # Include country code, e.g., "+917014451730"
    img_path: str
    caption: Optional[str] = None

@app.post("/send-whatsapp-text", summary="Send WhatsApp Message")
async def send_whatsapp_message(request: MessageRequest):
    """
    Send a WhatsApp message to the specified phone number.
    
    - **phone**: Phone number with country code (e.g., "+917014451730")
    - **message**: The message text to send
    """
    try:
        logger.info(f"Sending message to {request.phone}: {request.message}")
        
        # Send message instantly using PyWhatKit
        pywhatkit.sendwhatmsg_instantly(
            phone_no=request.phone,
            message=request.message,
            wait_time=20,  # Wait 20 seconds for WhatsApp web to load
            tab_close=True,  # Close tab after sending
            close_time=5  # Close browser after 5 seconds
        )
        
        logger.info("Message sent successfully")
        return {
            "status": "success",
            "message": "Message sent successfully",
            "phone": request.phone,
            "timestamp": datetime.datetime.now().isoformat()
        }
        
    except Exception as e:
        error_msg = f"Failed to send message: {str(e)}"
        logger.error(error_msg)
        raise HTTPException(status_code=500, detail=error_msg)


@app.post("/send-whatsapp-img", summary="Send WhatsApp Image")
async def send_whatsapp_message(request: MessageRequestImage):
    """
    Send a WhatsApp message to the specified phone number.
    
    - **phone**: Phone number with country code (e.g., "+917014451730")
    - **message**: The message text to send
    """
    try:
        logger.info(f"Sending message to {request.phone}: {request.img_path}")
        valid_extensions = ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.webp']
        # Send message instantly using PyWhatKit
        pywhatkit.sendwhats_image(
            receiver=request.phone,
            img_path=request.img_path,
            wait_time=20,  # Wait 20 seconds for WhatsApp web to load
            caption=request.caption or "",
            tab_close=True,  # Close tab after sending
            close_time=5  # Close browser after 5 seconds
        )
        
        logger.info("Image sent successfully")
        return {
            "status": "success",
            "message": "Image sent successfully",
            "phone": request.phone,
            "timestamp": datetime.datetime.now().isoformat()
        }
        
    except Exception as e:
        error_msg = f"Failed to send Image: {str(e)}"
        logger.error(error_msg)
        raise HTTPException(status_code=500, detail=error_msg)


@app.get("/", summary="API Health Check")
async def root():
    return {
        "message": "WhatsApp API is running!", 
        "instructions": "Use POST /send-whatsapp to send messages",
        "example_request": {
            "phone": "+917014451730",
            "message": "Hello from FastAPI!"
        }
    }

@app.get("/health", summary="Health Status")
async def health_check():
    return {"status": "healthy", "timestamp": datetime.datetime.now().isoformat()}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)