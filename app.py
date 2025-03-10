from flask import Flask
from apscheduler.schedulers.background import BackgroundScheduler
import requests

app = Flask(__name__)

# Function to call your Vercel API
def send_scheduled_email():
    try:
        response = requests.post("https://your-vercel-app-url/api/send-scheduled-emails")
        print("Scheduler Response:", response.text)
    except Exception as e:
        print("Error:", str(e))

# Setup APScheduler
scheduler = BackgroundScheduler()
scheduler.add_job(send_scheduled_email, 'interval', minutes=10)  # Runs every 10 minutes
scheduler.start()

@app.route('/')
def home():
    return "Flask Scheduler Running on Render"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
