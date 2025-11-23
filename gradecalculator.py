

print("Student Grade Calculator")

total = 0
marks = []

for i in range(1, 6):
    while True:
        try:
            m = float(input(f"Enter marks for Subject {i}: "))
            if m < 0 or m > 100:
                print("Please enter a valid mark (0–100).")
                continue
            marks.append(m)
            total += m
            break
        except ValueError:
            print("Invalid input. Enter a number only.")

average = total / 5

if average >= 90:
    grade = "A"
    feedback = "Excellent performance!"
elif average >= 75:
    grade = "B"
    feedback = "Good performance!"
elif average >= 60:
    grade = "C"
    feedback = "Satisfactory performance."
elif average >= 40:
    grade = "D"
    feedback = "Need to improve."
else:
    grade = "F"
    feedback = "Fail. Work harder next time."

print("\n Result")
print("Total Marks:", total)
print("Average Marks:", average)
print("Grade:", grade)
print("Feedback:", feedback)
