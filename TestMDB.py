from database_manager import DatabaseManager

# Instantiate the DatabaseManager
db_manager = DatabaseManager()

# Add data to the "students" collection
db_manager.add_data("students", name="John", surname="Doe", age=25, student_id=1)
db_manager.add_data("students", name="Jane", surname="Smith", age=22, student_id=2)

# Add data to the "advisors" collection
db_manager.add_data("advisors", name="Dr. Johnson", surname="Brown", age=40, advisor_id=101)
db_manager.add_data("advisors", name="Prof. Williams", surname="Davis", age=35, advisor_id=102)

# Add student-advisor relationships to the "student_advisor" collection
db_manager.add_data("student_advisor", student_id=1, advisor_id=101)
db_manager.add_data("student_advisor", student_id=2, advisor_id=102)

# Get existing relations
existing_relations = db_manager.get_existing_relations()
print("Existing relations:", existing_relations)

# Update a student record
db_manager.update("students", 1, name="Johnny", surname="Doe", age=26)

# Delete a student record
db_manager.delete_row("students", 2)

# Search for students named "John"
search_results = db_manager.search("students", name="John")
print("Search results:", search_results)

# Check if the "student_advisor" collection is empty
is_empty = db_manager.check_bd()
print("Is student_advisor collection empty?", is_empty)

# List advisors with the number of their students
advisors_with_students_count = db_manager.list_advisors_with_students_count(1)
print("Advisors with students count:", advisors_with_students_count)

# List students with the number of their advisors
students_with_advisors_count = db_manager.list_students_with_advisors_count(1)
print("Students with advisors count:", students_with_advisors_count)
