working_hours = float (input("Input the hour that worked per week:"))
salary = float (input("Input the hourly salary:"))
standard_time = 44 
excess_hours = max(0, working_hours - standard_time)
net_pay = (standard_time * salary) + (excess_hours * salary * 1.5)
print(f"The net pay is: {net_pay}")