#program to convert seconds to hours, minutes, and seconds
total_seconds = int(input("Enter total seconds: "))
hours = total_seconds // 3600
minutes = (total_seconds % 3600) // 60
seconds = total_seconds % 60
print(f"Time: {hours} hours, {minutes} minutes, {seconds} seconds")