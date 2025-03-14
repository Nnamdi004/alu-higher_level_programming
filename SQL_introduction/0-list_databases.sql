#!/bin/bash

# Replace 'root' with your MySQL username
# Replace 'your_password' with your actual MySQL password
MYSQL_USER="root"
MYSQL_PASSWORD="your_password"

# List all databases
mysql -u "$MYSQL_USER" -p"$MYSQL_PASSWORD" -e "SHOW DATABASES;"
