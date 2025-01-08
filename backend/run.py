# run.py
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from backend.app import create_app
from backend.app import ngrok

app = create_app()

if __name__ == "__main__":
    print("NGROK_AUTH_TOKEN:", os.getenv("NGROK_AUTH_TOKEN"))
    public_url = ngrok.connect(5000)
    print(f"ngrok URL: {public_url}")
    app.run(port=5000)
