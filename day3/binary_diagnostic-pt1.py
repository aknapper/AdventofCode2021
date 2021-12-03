with open('data.txt') as f:
    lines = f.readlines()
f.close()

mcb = []
i = 0
while i < len(lines):
    j = 0
    while j < len(lines[i]):
        if lines[i][j] == '1':
            try:
                mcb[j] += 1
            except IndexError:
                mcb.append(1)
        elif lines[i][j] == '0':
            try:
                mcb[j] -= 1
            except IndexError:
                mcb.append(-1)    
        j += 1
    i+=1

gamma_rate = []
epsilon_rate = []
k = 0
while k < len(mcb):
    if mcb[k] > 0:
        gamma_rate.append(1)
        epsilon_rate.append(0)
    elif mcb[k] < 0:
        gamma_rate.append(0)
        epsilon_rate.append(1)
    k += 1   

gamma_dec = int("".join(str(x) for x in gamma_rate), 2)
epsilon_dec = int("".join(str(x) for x in epsilon_rate), 2)

print('Gamma - Bin: ',gamma_rate, '\nGamma - Dec: ',type(gamma_dec))
print('Epsilon - Bin: ',epsilon_rate, '\nEpsilon - Dec: ',epsilon_dec)

print('Power consumption of the sub is: ',gamma_dec*epsilon_dec)