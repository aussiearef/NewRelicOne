FROM python:3.13-slim

WORKDIR /app

# Install curl, mariadb-server, and dependencies for the database runtimes
RUN apt-get update && apt-get install -y \
    curl \
    mariadb-server \
    && rm -rf /var/lib/apt/lists/*

RUN curl --version

# Install Python application dependencies
RUN pip install --no-cache-dir \
    fastapi \
    uvicorn \
    psycopg[binary] \
    pymysql \
    cryptography \
    newrelic

# Copy your application script, database seeding file, and startup coordinator
COPY db.py .
COPY init.sql .
COPY entrypoint.sh .

# Ensure the startup script has execution permissions
RUN chmod +x entrypoint.sh

EXPOSE 9001

# Run the entrypoint coordinator script instead of uvicorn directly
CMD ["./entrypoint.sh"]