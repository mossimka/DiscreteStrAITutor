import openai
from dotenv import load_dotenv
import os
import json
from pydantic import BaseModel, Field

load_dotenv()
client = openai.OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

class Note(BaseModel):
    id: int = Field(..., ge=1, le=10)
    heading: str
    summary: str
    page_ref: int | None = None

system = (
    "You are a study summarizer. "
    "Return exactly 10 unique notes that will help prepare for the exam. "
    "Respond *only* with a JSON object like: {\"notes\": Note[]}."
)

response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[{"role": "system", "content": system}],
    response_format={"type": "json_object"},
)

data = response.choices[0].message.content
notes = [Note(**item) for item in data["notes"]]

for note in notes:
    print(f"{note.id}. {note.heading} (page {note.page_ref})\n  {note.summary}\n")
