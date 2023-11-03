# To run this program use:
# NEW_RELIC_CONFIG_FILE=newrelic.ini newrelic-admin run-program uvicorn app:app --host 0.0.0.0 --port 8000

# Make sure below libraries are installed:
# pip install fastapi
# pip install uvicorn
# pip install pyodbc
# pip install newrelic

# Follow these instructions to install SQL Server Driver:
# https://learn.microsoft.com/en-us/sql/connect/odbc/linux-mac/install-microsoft-odbc-driver-sql-server-macos?view=sql-server-ver15#17
# Or use a different database server and change the connection string accordingly.

# Run this code with:
# NEW_RELIC_CONFIG_FILE=./newrelic.ini newrelic-admin run-program uvicorn db:app --host 0.0.0.0 --port 5217
from fastapi import FastAPI
import pyodbc
import random
import time

app = FastAPI()

@app.get("/")
async def read_root():
    DbConnectionStringBuilder = "Driver={ODBC Driver 17 for SQL Server};Server=localhost,1433;Database=NewRelic;Uid=sa;Pwd=Asd123)_"
    
    con = pyodbc.connect(DbConnectionStringBuilder)
    cmd = con.cursor()
    cmd.execute("select * from testdata")

    while True:
        row = cmd.fetchone()
        if not row:
            break

        rnd = random.randint(0, 9)
        print(f"Waiting for {10 * rnd} milli-seconds")
        time.sleep(0.01 * rnd)
    
    con.close()

    print("API execution ended.")
    return {"message": "API execution ended."}
