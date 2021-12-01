with open('data.txt') as f:
    lines = f.readlines()
f.close()

i = 0
num_of_larger_measurements = 0
while i < len(lines):
    if i == 0:
        pass
    elif int(lines[i]) > int(lines[i-1]):
        num_of_larger_measurements += 1
    i+=1

print('total num of larger than previous values: ',num_of_larger_measurements)