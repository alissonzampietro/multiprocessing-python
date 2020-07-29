import time

start = time.perf_counter()

def sleep():
    print('Sleeping 1 second...')
    time.sleep(1)
    print('Waking up dude...')

sleep();

finish = time.perf_counter()

print(f'Finished in {round(finish-start, 2)} second(s)')