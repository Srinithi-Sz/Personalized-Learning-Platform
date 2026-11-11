import mysql.connector

def create_database_and_tables():
    # Step 1: Connect to MySQL (without database first)
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="root@123"   # change this
    )

    cur = conn.cursor()

    # Step 2: Create database
    cur.execute("CREATE DATABASE IF NOT EXISTS learning_platform")

    # Step 3: Use database
    cur.execute("USE learning_platform")

    # Step 4: Create users table
    cur.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INT AUTO_INCREMENT PRIMARY KEY,
            username VARCHAR(50),
            password VARCHAR(50)
        )
    """)

    # Step 5: Create progress table
    cur.execute("""
        CREATE TABLE IF NOT EXISTS progress (
            id INT AUTO_INCREMENT PRIMARY KEY,
            user_id INT,
            course VARCHAR(100),
            progress INT DEFAULT 0
        )
    """)

    conn.commit()
    conn.close()

    print("Database and tables created successfully!")

# Run setup
create_database_and_tables()