students = [
    {'name': 'Amit', 'age': 21, 'branch': 'CSE', 'cgpa': 8.5, 'city': 'Delhi'},
    {'name': 'Priya', 'age': 20, 'branch': 'ECE', 'cgpa': 7.8, 'city': 'Mumbai'},
    {'name': 'Rohit', 'age': 22, 'branch': 'CSE', 'cgpa': 6.9, 'city': 'Delhi'},
    {'name': 'Sneha', 'age': 21, 'branch': 'ME', 'cgpa': 8.2, 'city': 'Kolkata'},
    {'name': 'Anjali', 'age': 20, 'branch': 'ECE', 'cgpa': 7.5, 'city': 'Mumbai'}
]
# 1. Find all students from 'CSE' branch
cse_students=[student['name'] for student in students if student['branch']=='CSE']
# 2. Find students with CGPA > 8.0
high_performers=[student['name'] for student in students if student['cgpa'] > 8.0]
# 3. Calculate average CGPA
total_cgpa=sum(student['cgpa'] for student in students)
average_cgpa=total_cgpa/len(students)
# 4. Find student with highest CGPA
topper=students[0]
for student in students:
    if student['cgpa']>topper['cgpa']:
        topper=student
# 5. Add 'eligible_for_placement' field
for student in students:
    student['eligible_for_placement']=student['cgpa']>=7.0
# 6. Count how many students are from each city
city_distribution={}
for student in students:
    city=student['city']
    if city in city_distribution:
        city_distribution[city]+=1
    else:
        city_distribution[city]=1
# 7. Print summary report
print("CSE Students:", ", ".join(cse_students))
print("High Performers (CGPA > 8):", ", ".join(high_performers))
print("Average CGPA:", round(average_cgpa, 2))
print("Topper:", topper['name'], "({})".format(topper['cgpa']))
placement_eligible_count=sum(1 for student in students if student['eligible_for_placement'])
print("Placement Eligible:", placement_eligible_count, "students")
print("City Distribution:", ", ".join(f"{city}-{count}" for city, count in city_distribution.items()))