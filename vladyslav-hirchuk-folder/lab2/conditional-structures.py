
#conditional-structures

avg_salary = float(input("What is your salary per month? "))

if avg_salary < 0:
    print("Are you in debt?")
elif avg_salary == 0:
    print("You don't have a job.")
elif avg_salary < 2000:
    print("You have an average salary in the US.")
elif avg_salary >= 2000 and avg_salary <= 5000:
    print("You have a good job, which pays well!")
else:
    print("Well, soon you're gonna be a billionaire :D")


