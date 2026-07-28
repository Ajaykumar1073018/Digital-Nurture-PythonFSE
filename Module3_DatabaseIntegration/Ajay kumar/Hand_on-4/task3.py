import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="your_password",
    database="college_db"
)

cursor = conn.cursor()

query_count = 1

cursor.execute("SELECT * FROM enrollments")
enrollments = cursor.fetchall()

for enrollment in enrollments:
    student_id = enrollment[1]

    cursor.execute(
        "SELECT first_name, last_name FROM students WHERE student_id=%s",
        (student_id,)
    )

    student = cursor.fetchone()
    print(student)

    query_count += 1

print("Total Queries Executed:", query_count)

cursor.close()
conn.close()
