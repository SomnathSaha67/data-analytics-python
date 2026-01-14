attendance_data = [
    {'name': 'amit kumar', 'attendance': '85', 'status': 'present'},
    {'name': 'PRIYA SHAH', 'attendance': '92', 'status': 'Present'},
    {'name': 'rohit  verma', 'attendance': 'N/A', 'status': 'absent'},  # Missing data
    {'name': 'sneha123', 'attendance': '78', 'status': 'PRESENT'},
    {'name': '', 'attendance': '65', 'status': 'present'},  # Missing name
    {'name': 'vikram', 'attendance': '150', 'status': 'present'},  # Invalid data (>100)
]
cleaned_data = []
for record in attendance_data:
    name = record['name'].strip().title()
    if not name:
        continue #Skip records with missing names
    attendance = record['attendance'].strip()
    if attendance.upper() == 'N/A':
        attendance = 0
    else:
        attendance = int(attendance)
        if attendance > 100:
            attendance = 100
    status = record['status'].strip().lower()
    cleaned_data.append({'name': name, 'attendance': attendance, 'status': status})
# Calculate statistics
total_attendance = 0
warning_students = []
for record in cleaned_data:
    total_attendance += record['attendance']
    if record['attendance'] < 75:
        warning_students.append(record['name'])
average_attendance = total_attendance / len(cleaned_data)
# Print cleaned data and statistics
print("Original records:", len(attendance_data))
print("Cleaned records:", len(cleaned_data), "(1 removed due to missing name)")
print("\nCleaned Data:")
for record in cleaned_data:
    print(f"{record['name']} - {record['attendance']}% - {record['status']}")
print("\nAverage Attendance: {:.0f}%".format(average_attendance))
print("Students needing warning:", ", ".join(warning_students))
# Save cleaned data to a new file
with open('cleaned_attendance.txt', 'w') as file:
    for record in cleaned_data:
        file.write(f"{record['name']},{record['attendance']},{record['status']}\n")
# Cleaned data saved to 'cleaned_attendance.txt'
