
total_seconds = int(input("Введіть кількість секунд (0-8639999): "))


days = total_seconds // (24 * 3600)
remain = total_seconds % (24 * 3600)

hours = remain // 3600
remainder = remain % 3600

minutes = remain// 60
seconds = remain % 60

if days % 10 == 1 and days % 100 != 11:
    day_word = "день"
elif 2 <= days % 10 <= 4 and (days % 100 < 10 or days % 100 >= 20):
    day_word = "дні"
else:
    day_word = "днів"


hours_str = str(hours).zfill(2)
minutes_str = str(minutes).zfill(2)
seconds_str = str(seconds).zfill(2)


print(f"{days} {day_word}, {hours_str}:{minutes_str}:{seconds_str}")