with open('data.txt') as f:
    lines = f.readlines()
f.close()

i = 0
horizontal = 0
depth = 0

while i < len(lines):
    command = lines[i].split()
    if command[0] == 'forward':
        horizontal += int(command[1])
    elif command[0] == 'up':
        depth -= int(command[1])
    elif command[0] == 'down':
        depth += int(command[1])
    i+=1

print('horizontal position: ',horizontal)
print('depth: ',depth)

print(horizontal*depth)