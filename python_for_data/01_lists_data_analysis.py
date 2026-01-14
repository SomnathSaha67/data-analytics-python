marks = [45, 67, 89, 34, 78, 56, 91, 23, 65, 72]
# 1. Calculate total marks
total_marks = sum(marks)
# 2. Calculate average marks
average_marks = total_marks / len(marks)
# 3. Find highest mark without using max()
highest_mark = marks[0]
for mark in marks:
    if mark>highest_mark:
        highest_mark=mark
# 4. Find lowest mark without using min()
lowest_mark = marks[0]
for mark in marks:
    if mark<lowest_mark:
        lowest_mark=mark
# 5. Count how many students passed (marks >= 40)
passed_count = 0
for mark in marks:
    if mark >= 40:
        passed_count += 1
# 6. Count how many students got distinction (marks >= 75)
distinction_count = 0
for mark in marks:
    if mark >= 75:
        distinction_count += 1
# 7. Create a new list with marks increased by 5%
grace_marks = []
for mark in marks:
    new_mark = mark * 1.05
    grace_marks.append(new_mark)
# 8. Print original and updated marks side by side
print("Original Marks:", marks)
print("Total:", total_marks)
print("Average:", average_marks)
print("Highest:", highest_mark)
print("Lowest:", lowest_mark)
print("Passed:", passed_count, "students")
print("Distinction:", distinction_count, "students")
print("\nAfter 5% grace:")
for i in range(len(marks)):
    print(f"Student {i+1}: {marks[i]} → {grace_marks[i]:.2f}")
