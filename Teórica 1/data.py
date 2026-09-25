from datetime import datetime
now = datetime.now()

print()
print(str(now))

print()
print("Current date and time using instance attributes:")
print()
print("Current year:", now.year)
print("Current month:", now.month)
print("Current day:", now.day)
print("Current hour:", now.hour)
print("Current minute:", now.minute)
print("Current second:", now.second)
print("Current microsecond:", now.microsecond)