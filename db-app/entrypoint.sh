#!/bin/bash
set -e

echo "Creating required MariaDB runtime directories..."
mkdir -p /run/mysqld
chown -R mysql:mysql /run/mysqld

echo "Initializing MariaDB system databases..."
# Using the native binary with explicit directory configuration
mariadb-install-db --user=mysql --datadir=/var/lib/mysql

echo "Starting MariaDB service..."
mariadbd-safe --user=mysql &

echo "Waiting for MariaDB to start..."
until mariadb-admin ping -h "localhost" --silent; do
    sleep 1
done

echo "Configuring database users and seeding astronomy data..."
mariadb -u root <<EOF
CREATE DATABASE IF NOT EXISTS astronomy_shop_db;
CREATE USER IF NOT EXISTS 'app_user'@'localhost' IDENTIFIED BY 'app_password_here';
GRANT ALL PRIVILEGES ON astronomy_shop_db.* TO 'app_user'@'localhost';
FLUSH PRIVILEGES;
EOF

# Inject your astronomy tables and orders
mariadb -u root astronomy_shop_db < init.sql

echo "Database is ready. Starting Uvicorn web application..."

# Execute your primary application command sequence
exec newrelic-admin run-program uvicorn db:app --host 0.0.0.0 --port 9001