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
    "Each note must be a JSON object with keys: id (int, 1-10), heading (str), summary (str), and page_ref (int or null). "
    "Respond ONLY with a JSON object like: {\"notes\": [{\"id\": 1, \"heading\": \"...\", \"summary\": \"...\", \"page_ref\": 1}, ...]}."
)

response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[{"role": "system", "content": system}],
    response_format={"type": "json_object"},
)

data = json.loads(response.choices[0].message.content)
print(json.dumps(data, indent=2))

notes = []
for i, item in enumerate(data["notes"], 1):
    if isinstance(item, str):
        notes.append(Note(id=i, heading=f"Note {i}", summary=item))
    elif isinstance(item, dict):
        notes.append(Note(**item))


for note in notes:
    print(f"{note.id}. {note.heading} (page {note.page_ref})\n  {note.summary}\n")
