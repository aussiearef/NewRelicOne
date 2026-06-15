# 1. Export authentication details
#export NEW_RELIC_LICENSE_KEY="your_actual_license_key"

# 2. Configure APM behavior rules globally
#export NEW_RELIC_APP_NAME="FastAPI-OpenAI-Service"
#export NEW_RELIC_AI_MONITORING_ENABLED="true"
#export NEW_RELIC_CUSTOM_INSIGHTS_EVENTS_MAX_ATTRIBUTE_VALUE=4095

# 3. Launch Uvicorn wrapped inside the New Relic admin manager
#newrelic-admin run-program uvicorn aidemo:app --host 127.0.0.1 --port 8000 --reload

import os
from fastapi import FastAPI
from openai import OpenAI

app = FastAPI(title="New Relic AI Monitoring Demo")

@app.get("/chat")
def run_openai_demo(prompt: str = "Explain metrics, logs, and traces in one sentence."):
    print(f"Received request with prompt: {prompt}")
    
    # Initialize standard client inside the endpoint logic
    client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))
    
    # New Relic will automatically intercept this out-bound call 
    # and link it to the parent FastAPI inbound web transaction
    response = client.chat.completions.create(
        model="gpt-5.4-nano",
        messages=[{"role": "user", "content": prompt}],
        # max_tokens=150,
        max_completion_tokens=150, # GPT 5.x and above
        temperature=0.7
    )
    
    return {
        "status": "success",
        "model": "gpt-4o",
        "response": response.choices[0].message.content.strip()
    }