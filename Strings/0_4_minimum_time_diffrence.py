import sys

def get_minimum_time_diffrence(timePoints,N):
    # extract hour and minits from timepoint array...
    # make a new array that srore minits.

    minits_arr = []
    for time in timePoints:
        hour,minit = int(time[:2]),int(time[3:])
        total_minits = hour * 60 + minit
        minits_arr.append(total_minits)

    # sort the array ... and get the minimum diffrence...
    minits_arr.sort()

    mini = sys.maxsize

    # get the minimum diffrence...
    i = 0
    while i < N - 1:
        diff = minits_arr[i+1] - minits_arr[i]
        mini = min(diff,mini)
        i += 1
    
    # get circular difffrence... and return minimum diffrennce...
    
    circular_diffrence = minits_arr[0] + 1440 - minits_arr[-1]
    mini = min(circular_diffrence,mini)

    return mini
    

if __name__ == "__main__":
    timePoints = ["00:00","23:59","00:00"]
    timePoints = ["23:59","00:00"]
    N = len(timePoints)
    result = get_minimum_time_diffrence(timePoints,N)
    print(result)