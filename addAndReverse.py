#user input, bilangan integer maksimal 359999
#inputan bilangan desimal, bilangan negatif atau string akan memberi output "Invalid Input"

while True:
    try:
        num1=int(input('Masukan angka ke 1: '))
        #jika input user bernilai lebih dari 359999 atau bilangan negatif, maka output "Invalid Input"
        while num1 > 359999 or num1 < 0:
            print('Invalid Input')
            num1=int(input('Masukan angka ke 1: '))

        num2=int(input('Masukan angka ke 2: '))
        while num2 > 359999or num2 < 0:
            print('Invalid Input')
            num2=int(input('Masukan angka ke 2: '))

        break
    #apabila data type dari input yang dimasukan bukan integer, maka output "Invalid Input"
    except ValueError:
        print('Invalid Input')


def tambah_mundur(num1,num2):
    #merubah variable num1 menjadi str agar dapat dibaca dari terbalik
    x=str(num1)
    rNum1=x[::-1]
    
    #untuk pengecekan nilai rNum1 pada saat pembuatan kode
    # print(rNum1) 

    #merubah variable num1 menjadi str agar dapat dibaca dari terbalik
    y=str(num2)
    rNum2=y[::-1]

    #untuk pengecekan nilai rNum1 pada saat pembuatan kode
    #print(rNum2)
    
    #mengkomputasi angka yang sudah dibalik dalam bentuk 'int', lalu diubah ke 'str' kembali agar bisa dibaca terbalik
    hasil=str(int(rNum1)+int(rNum2))
    rHasil=hasil[::-1]
    print(hasil)
    print(rHasil)

tambah_mundur(num1,num2)
