from fastapi import FastAPI
import os
import psycopg
import newrelic.agent
import time

app = FastAPI()

# Wrap the FastAPI application instance to automatically track async transactions
app = newrelic.agent.ASGIApplicationWrapper(app)

@app.get("/")
async def read_root():
    # This will now print a valid Transaction object instead of None
    print("TXN =", newrelic.agent.current_transaction())
    
    # Fixed the uppercase typo here
    db_host = os.getenv("DB_HOST", "localhost")
    db_port = os.getenv("DB_PORT", "5432")
    
    conn_string = (
        f"postgres://astronomy_user:astronomy_pass@"
        f"{db_host}:{db_port}/astronomy_db?sslmode=disable"
    )
    products = []

    with psycopg.connect(conn_string) as conn:
        with conn.cursor() as cur:
            cur.execute("""
                SELECT
                    p.id,
                    p.name,
                    p.description,
                    p.picture,
                    p.price_currency_code,
                    p.price_units,
                    p.price_nanos,
                    p.categories
                FROM catalog.products p
                ORDER BY p.id
            """)

            for row in cur.fetchall():
                products.append(
                    {
                        "id": row[0],
                        "name": row[1],
                        "description": row[2],
                        "picture": row[3],
                        "currency": row[4],
                        "units": row[5],
                        "nanos": row[6],
                        "categories": row[7],
                    }
                )

    import pymysql

    # Some MySQL Transactions 
    conn = pymysql.connect(
        host='localhost',
        user='app_user',
        password='app_password_here',
        database='astronomy_shop_db',
        cursorclass=pymysql.cursors.DictCursor
    )

    products = []

    try:
        with conn.cursor() as cur:
            # Execute the select query targeting your new MySQL schema
            cur.execute("""
                SELECT 
                    id, 
                    name, 
                    description, 
                    price, 
                    stock_quantity 
                FROM products 
                ORDER BY id
            """)
            
            # Since DictCursor is active, fetchall() returns a list of dictionaries directly
            products = cur.fetchall()
            time.sleep(0.003)
    finally:
        # Always close the connection pool binding when the execution loop ends
        conn.close()
        
    return {
        "count": len(products),
        "products": products,
    }


@app.get("/health")
async def health():
    return {"status": "ok"}