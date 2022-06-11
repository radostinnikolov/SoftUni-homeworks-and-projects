def grade_eval(grade):
    if 2 <= grade <= 2.99:
        return "Fail"
    elif grade <= 3.49:
        return "Poor"
    elif grade <= 4.49:
        return "Good"
    elif grade <= 5.49:
        return "Very Good"
    elif grade <= 6.00:
        return "Excellent"

grade_input = float(input())
print(grade_eval(grade_input))
