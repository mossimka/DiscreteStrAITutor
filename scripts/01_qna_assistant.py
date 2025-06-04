import openai
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()
client = openai.OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# 1. Create a vector store
vector_store = client.vector_stores.create(name="My Vector Store")
print("📦 Vector Store created. ID:", vector_store.id)

# 2. Upload the PDF and attach to the vector store
file = client.files.create(
    file=open("data/ChineseRemainderTheorem.pdf", "rb"),
    purpose="assistants"
)
client.vector_stores.files.create(
    vector_store_id=vector_store.id,
    file_id=file.id
)
print("📄 File uploaded and attached to vector store.")

# 3. Query using the Responses API with file_search
response = client.responses.create(
    input="Explain the Chinese Remainder Theorem",
    model="gpt-4o",  # or "gpt-4o-mini"
    tools=[{
        "type": "file_search",
        "vector_store_ids": [vector_store.id],
    }]
)

print("\n📘 Response:")
print(response.output[1].content[0].text) 