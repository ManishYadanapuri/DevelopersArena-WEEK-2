# Simple Student Grade Calculator

# Ask the user to enter marks
marks = float(input("Enter your marks (out of 100): "))

# Determine the grade based on marks
if marks >= 90:
    grade = "A+"
    message = "Outstanding performance! Keep it up! 🌟"
elif marks >= 80:
    grade = "A"
    message = "Excellent work! You're doing great! 💪"
elif marks >= 70:
    grade = "B"
    message = "Good job! Keep aiming higher! 👍"
elif marks >= 60:
    grade = "C"
    message = "Nice effort! You can do even better! 😊"
elif marks >= 50:
    grade = "D"
    message = "You passed! Keep improving! 💡"
else:
    grade = "F"
    message = "Don’t give up! Learn from mistakes and try again! 💪"

# Display the result
print("\n--- Grade Report ---")
print(f"Marks: {marks}")
print(f"Grade: {grade}")
print(f"Message: {message}")
