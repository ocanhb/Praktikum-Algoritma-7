def bilangan_prima (p):
    if p <= 1:
        return False

    for i in range(2, p):
        if p % i == 0:
            return False
    return True

prima = int(input("Masukkan sebuah bilangan: "))

if bilangan_prima (prima):
    print(f"{prima} adalah bilangan prima.")
else:
    print(f"{prima} bukan bilangan prima.")