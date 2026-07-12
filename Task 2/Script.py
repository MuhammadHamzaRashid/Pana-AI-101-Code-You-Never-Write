# Teacher's Grading Policy
# Assignments = 30 marks (drop the lowest assignment)
# Mid-Term = 120 marks
# Final Exam = 150 marks

# Get assignment scores
assignments = []
for i in range(1, 4):
    score = float(input(f"Enter Assignment {i} score (out of 10): "))
    assignments.append(score)

# Get exam scores
midterm_score = float(input("Enter Mid-Term score (out of 120): "))
final_exam_score = float(input("Enter Final Exam score (out of 150): "))

# Drop the lowest assignment
assignments.remove(min(assignments))

# Scale assignments to 30 marks
assignment_score = (sum(assignments) / 20) * 30

# Calculate total and percentage
total_marks = assignment_score + midterm_score + final_exam_score
percentage = (total_marks / 300) * 100

# Assign grade
if percentage >= 90:
    grade = "A"
elif percentage >= 80:
    grade = "B"
elif percentage >= 70:
    grade = "C"
elif percentage >= 60:
    grade = "D"
else:
    grade = "Fail"

# Display results
print("\n----- Result -----")
print(f"Assignment Marks (after dropping lowest): {assignment_score:.2f}/30")
print(f"Mid-Term Marks: {midterm_score:.2f}/120")
print(f"Final Exam Marks: {final_exam_score:.2f}/150")
print(f"Total Marks: {total_marks:.2f}/300")
print(f"Percentage: {percentage:.2f}%")
print(f"Final Grade: {grade}")
