mt1 = float(input())
mt2 = float(input())
mt3 = float(input())

if not (0 <= mt1 <= 20 and 0 <= mt2 <= 20 and 0 <= mt3 <= 20):
    print("Input error")
else:
    grade_float = mt1 * 0.4 + mt2 * 0.4 + mt3 * 0.2
    grade = int(grade_float + 0.5)
    
    if grade < 10:
        print("RFF")
    else:
        print(grade)