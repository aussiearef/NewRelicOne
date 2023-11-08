# Run this code with:
# NEW_RELIC_CONFIG_FILE=./newrelic.ini newrelic-admin run-program uvicorn main:app --host 0.0.0.0 --port 8000


from fastapi import FastAPI
import logging

# Create an instance of the FastAPI app
app = FastAPI()
logging.basicConfig(filename='log.txt', level=logging.WARNING, format='%(asctime)s - %(levelname)s - %(message)s')

# Define a route for the GET request
@app.get("/")
async def get_hello_world():
    logging.warn("Hello World API called.")
    return {"message": "Hello World"}

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)

    logging.shutdown()
