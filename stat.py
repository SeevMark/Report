print("APPDEVLAB ~ Activity 2".center(50, "="))
print("\033[94m=" *50)
print("\033[91mStudent Grading and Scholarship Eligibility System")
print("\033[94m=" * 50)

def get_academic_average(average):
    if average >= 96:
        return "With Highest Honor"
    elif average >= 90:
        return "With Honors"
    elif average >= 75:
        return "Passed"
    else:
        return "Failed"
    
    def main():
    while True:
        try:
            # Input student name
            student_name = str(input("\nEnter a Student Name: "))
            if not student_name:
                print("Student Name must not be empty")
                continue