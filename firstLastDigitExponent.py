def digitAwal(number1,number2):
    hasil=number1**number2
    a=str(hasil)
    dAwal=a[:1:]
    print('Hasil pemangkatan',number1,'^',number2, 'adalah: ',hasil)
    print('Digit awal dari',hasil,'adalah',dAwal)


def digitAkhir(number1,number2):
    hasil=number1**number2
    b=str(hasil)
    dAkhir=b[-1]
    print('Hasil pemangkatan',number1,'^',number2, 'adalah: ',hasil)
    print('Digit akhir dari',hasil,'adalah',dAkhir)


digitAwal(10,8)
print()
digitAwal(2,3)
print()
digitAwal(6,3)
print()
digitAkhir(10,8)
print()
digitAkhir(2,3)
print()
digitAkhir(6,3)

    