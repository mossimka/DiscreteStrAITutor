import openai
from dotenv import load_dotenv
import os
import time

# Load environment variables
load_dotenv()
client = openai.OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# 1. Upload the file
file = client.files.create(
    file=open("data/ChineseRemainderTheorem.pdf", "rb"),
    purpose="assistants"
)
print("📄 File uploaded. File ID:", file.id)

# 3. Create a Thread
thread = client.beta.threads.create()

# 4. Add a Message to the Thread
client.beta.threads.messages.create(
    thread_id=thread.id,
    role="user",
    content="Explain the Chinese Remainder Theorem"
)

# 5. Run the Assistant on the Thread
run = client.beta.threads.runs.create(
    thread_id=thread.id,
    assistant_id=os.getenv("ASSISTANT_ID")
)

# 6. Poll for the Run to complete
print("⏳ Waiting for response...")
while run.status not in ["completed", "failed"]:
    time.sleep(1)
    run = client.beta.threads.runs.retrieve(
        thread_id=thread.id,
        run_id=run.id
    )

# 7. Read the Assistant's response
print("\n📘 Response:")
messages = client.beta.threads.messages.list(thread_id=thread.id)
for msg in messages.data:
    if msg.role == "assistant":
        print(msg.content[0].text.value) 