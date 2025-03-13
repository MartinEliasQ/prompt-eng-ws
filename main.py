from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Optional
from langchain_core.messages import SystemMessage, HumanMessage
from langchain_openai import ChatOpenAI
import uvicorn
import os

OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")
# Initialize FastAPI application
app = FastAPI(
    title="Simple API",
    description="A simple FastAPI application with a POST endpoint",
    version="1.0.0",
)


def get_model(
    model_name="openai/gpt-4o-mini",
    openai_api_key: str = OPENROUTER_API_KEY,
    openai_api_base: str = "https://openrouter.ai/api/v1",
) -> ChatOpenAI:
    # alternatively you can use OpenAI directly via ChatOpenAI(model="gpt-4o") via -> from langchain_openai import ChatOpenAI
    return ChatOpenAI(
        model=model_name, openai_api_key=openai_api_key, openai_api_base=openai_api_base
    )


class Message(BaseModel):
    message: str


@app.get("/")
def read_root():
    return {"message": "Welcome to the Simple API"}


def ai(message):
    gpt4o = get_model()
    human_message = HumanMessage(message)
    console.log("Hellow")
    response = gpt4o([human_message])
    return response.content
    # return response


@app.post("/message/", status_code=201)
def create_message(message: Message):
    """ """
    response = ai(message.message)

    return response


# For running the app from command line
if __name__ == "__main__":
    import uvicorn

    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
