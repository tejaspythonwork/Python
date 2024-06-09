# 30-05-2024
# accept miniutes from user and convert it into second and hour
# combination of 2 programs

minutes = int(input('Enter Minutes : '))
hour = (minutes/60)
second = (hour*3600)
print(F'hour = {int(hour)} and minutes = {int(minutes)} and seconds = {int(second)}')