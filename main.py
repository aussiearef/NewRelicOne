from fastapi import FastAPI

# Create an instance of the FastAPI app
app = FastAPI()

# Define a route for the GET request
@app.get("/")
async def get_hello_world():
    return {"message": "Hello World"}

if __name__ == "__main__":
    import uvicorn

    # Run the FastAPI app using Uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
