
user_input = input("Enter number more than 0 and less 8640000:")
print(user_input)
minutes, seconds = divmod(int(user_input), 60)
hours, minutes = divmod(minutes, 60)
days, hours = divmod(hours, 24)

days, hours, minutes, seconds = str(days), str(hours), str(minutes), str(seconds)

declination ="days, "

if days == "1":
    declination = "day, "

print(f"{days} {declination} {hours.zfill(2)}:{minutes.zfill(2)}:{seconds.zfill(2)} ")

