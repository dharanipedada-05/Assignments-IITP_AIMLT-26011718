def calculate_grade(*scores, **adjustments):
    average = sum(scores) / len(scores)
    bonus = sum(adjustments.values())
    final_grade = average + bonus
    return round(final_grade, 2)

# Student 1: No bonus
grade1 = calculate_grade(85, 90, 78)
print(f"Final Grade: {grade1}%")

# Student 2: With bonus
grade2 = calculate_grade(70, 65, 80, attendance=5, project=10)
print(f"Final Grade: {grade2}%")