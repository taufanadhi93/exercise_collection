#user input
seconds=int(input('Masukan detik: '))

#fungsi untuk mengkonversi detik
def timeConverter (seconds):
    hour=int(seconds//3600)
    minute=int((seconds-(hour*3600))/60)
    second=int(seconds-(hour*3600)-(minute*60))

    return hour,minute,second

#pengecekan input HANYA menerima angka bulat maks 359999
#jika input string maka output akan menampilkan "Invalid Input !"
if type(seconds)!=int:
    print('Invalid Input !')
    print(seconds,'a',type(seconds))

#jika input float maka output akan menampilkan "Invalid Input !"
elif seconds == float:
    print('Invalid Input !')
    print(seconds,'b',type(seconds))

#jika input bilangan negatif maka output akan menampilkan "Invalid Input !"
elif seconds < 0:
    print('Invalid Input !')
    print(seconds,'c',type(seconds))

#jika input lebih dari 359999 maka output akan menampilkan "Invalid Input !"
elif seconds > 359999:
    print('Invalid Input !')
    print(seconds,'d',type(seconds))

else:
    #memasukan data hour,minute,second dengan memanggil fungsi timeConverter
    hour,minute,second = timeConverter(seconds)
    
    print(f"Konversi : {hour:02d}:{minute:02d}:{second:02d}")
    


