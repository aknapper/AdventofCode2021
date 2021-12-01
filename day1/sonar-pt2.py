with open('data.txt') as f:
    lines = f.readlines()
    data = [int(item) for item in lines]
f.close()

i = 0
windows = []

while i < (len(data)-2):
    windows.append(data[i]+data[i+1]+data[i+2])
    i += 1

k = 0
num_of_larger_measurements = 0
while k < len(windows):
    if k == 0:
        pass
    elif windows[k] > windows[k-1]:
        num_of_larger_measurements += 1
    k+=1

print('number of sums larger than previous sums: ',num_of_larger_measurements)