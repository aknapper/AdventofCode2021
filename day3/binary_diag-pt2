def readdata(filepath):
    with open(filepath) as f:
        lines = f.readlines()
    f.close()
    return lines

def remove_newline(data):
    converted_list = []
    for element in data:
        converted_list.append(element.strip())
    return converted_list

def binary_list_2_decimal_int(binary_list):
    return int("".join(str(x) for x in binary_list), 2)

def findOxygenGeneratorRating(binary_list, digit = 0):

    if len(binary_list) == 1:
        return binary_list
    else:
        ones = []
        zeros = []
        for number in binary_list:
            if number[digit] == '1':
                ones.append(number)
            elif number[digit] == '0':
                zeros.append(number)

        if len(ones) >= len(zeros):
            return findOxygenGeneratorRating(ones, digit+1)
        elif len(ones) < len(zeros):
            return findOxygenGeneratorRating(zeros, digit+1)

def findC02ScrubberRating(binary_list, digit = 0):

    if len(binary_list) == 1:
        return binary_list
    else:
        ones = []
        zeros = []
        for number in binary_list:
            if number[digit] == '1':
                ones.append(number)
            elif number[digit] == '0':
                zeros.append(number)

        if len(ones) >= len(zeros):
            return findC02ScrubberRating(zeros, digit+1)
        elif len(ones) < len(zeros):
            return findC02ScrubberRating(ones, digit+1)

data = readdata('data.txt')
cleaned_data = remove_newline(data)

oxy_gen_rating = findOxygenGeneratorRating(cleaned_data)
c02_rating = findC02ScrubberRating(cleaned_data)

oxygen_dec = binary_list_2_decimal_int(oxy_gen_rating)
c02_dec = binary_list_2_decimal_int(c02_rating)

print('Oxygen - Bin: ',oxy_gen_rating, '\nOxygen - Dec: ',oxygen_dec)
print('C02 - Bin: ',c02_rating, '\nC02 - Dec: ',c02_dec)

print('Life suport rating is: ',oxygen_dec*c02_dec)