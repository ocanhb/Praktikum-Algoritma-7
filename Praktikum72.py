print('Ordinal Number')
print('ketik 0 untuk menghentikan program')

def ordinal_number(num):
    if 0 <= num % 100 <= 1000:
            suffix = {1: 'st', 2: 'nd', 3: 'rd'}.get(num % 10, 'th')
    return f'({num}, \'{num}{suffix}\')'

while True:
    try:
        input_number = int(input('Masukkan angka : '))
        if input_number == 0:
            print('(0, \'0th\')')
            break
        else:
            print(ordinal_number(input_number))
    except ValueError:
        print('Masukkan harus berupa angka.')
