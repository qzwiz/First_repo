

n = 5000

# Calculate hours, minutes, and seconds
hours = n // (60 * 60)
print('skoko chasov?>>>',hours)
minutes = (n % (60 * 60)) // 60
seconds = n % 60

# Check if seconds equal 23 and print a message if true
if minutes == 23:
    print("22 + fff")

# Print the result
print(f"Hours: {hours}, Minutes: {minutes}, Seconds: {seconds}")
