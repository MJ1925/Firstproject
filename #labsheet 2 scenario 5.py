#labsheet 2 scenario 5
score=int(input("Enter score: "))
if score>=90:
    grade="A"
elif score>=80 and score<=89:
    grade="B"
elif score>=70 and score<=79:
    grade="C"
elif score>=60 and score<=69:
    grade="D"
else: grade="F"
print(grade)