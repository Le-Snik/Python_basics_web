duration = int(input("Ввести продолжительность "))

secs = [31536000, 2629743, 86400, 3600, 60, 1]
names = ['год.', 'мес.', 'дн.', 'час.', 'мин', 'cек.']
total = []
rest = duration

for i in secs:
    total.append(rest // i)
    rest = rest % i

for tot in range(len(total)):
    if total[tot] != 0:
        print(total[tot], names[tot])


