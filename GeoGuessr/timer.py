import time

my_time = 300

for x in range(my_time, 0, -1):
    seconds = x % 60
    minutes = int(x / 60) % 60
    print(f'{minutes:02}:{seconds:02}')
    time.sleep(1)
    if(x == 180):
        print('yellow')
    if(x == 60):
        print('red')
    if(x == 30):
        print('flashing red')



print("Time's up")