import psycopg2

# Connect to the database
conn = psycopg2.connect(database="todo", user="postgres", password="password", host="localhost", port="5432")
cur = conn.cursor()

# Create the table if it doesn't exist
cur.execute("CREATE TABLE IF NOT EXISTS todo (id SERIAL PRIMARY KEY, task VARCHAR(255) NOT NULL)")

# Define a function to add a task to the to-do list
def add_task(task):
    cur.execute("INSERT INTO todo (task) VALUES (%s)", (task,))
    conn.commit()
    print("Task added to to-do list")

# Define a function to display the to-do list
def display_list():
    cur.execute("SELECT * FROM todo")
    rows = cur.fetchall()
    if not rows:
        print("To-do list is empty")
    else:
        for row in rows:
            print(row[0], "-", row[1])

# Add some tasks to the to-do list
add_task("Buy groceries")
add_task("Do laundry")
add_task("Clean the kitchen")

# Display the to-do list
display_list()

# Close the database connection
cur.close()
conn.close()

