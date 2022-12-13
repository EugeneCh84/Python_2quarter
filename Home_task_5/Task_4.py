def rle_encode(data): 
    encoding = '' 
    prev_char = '' 
    count = 1 
    if not data: 
        return '' 
    for char in data: 
        if char != prev_char: 
            if prev_char: 
                encoding += str(count) + prev_char 
            count = 1 
            prev_char = char 
        else: 
            count += 1  
    else: 
        encoding += str(count) + prev_char 
        return encoding

value = rle_encode('EEEEEEEEVVVVVVVVVVVVGFDDDDDDDDDDSSSSSSSSSWWWWWWGGGGGGHHHHHHHHHH')


def rle_decode(data): 
    decode = '' 
    count = '' 
    for char in data: 
        if char.isdigit(): 
            count += char 
        else: 
            decode += char * int(count) 
            count = '' 
    return decode

with open('file1.txt', 'w') as data:
        data.write(value)   


with open('file1.txt', 'r') as data:
        file1 = data.readline()   


value1= rle_decode(file1)
with open('file2.txt', 'w') as data:
        data.write(value1)   

