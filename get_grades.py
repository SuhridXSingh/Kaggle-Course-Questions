def get_grade(score):
    if score>=90:
        return "A"
    elif 90>score>=80:
        return "B"
    elif 80>score>=70:
        return "C"
    elif 70>score>=60:
        return "D"
    else:
        return "F"
    
# Check your answer
q1.check()
