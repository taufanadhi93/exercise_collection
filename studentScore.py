marks={}
size=int(input('Masukan jumlah siswa: '))

def beasiswa (ipk,kodeProdi):
    if kodeProdi == 'TI' or kodeProdi =='SI':
        if 75 < ipk <= 85:
            beasiswa='beasiswa 20 %'
        elif 85 < ipk <= 100:
            beasiswa='beasiswa 30 %'
        else:
            beasiswa='tidak dapat beasiswa'
    elif kodeProdi == 'DKV' or kodeProdi =='Teknik Industri':
        if 75 < ipk <= 85:
            beasiswa='beasiswa 25 %'
        elif 85 < ipk <= 100:
            beasiswa='beasiswa 35 %'
        else:
            beasiswa='tidak dapat beasiswa'
    else:
        beasiswa=' '

    return beasiswa


for i in range (size):
    nim=input('Masukan NIM: ')
    nama=input('Masukan Nama Mahasiswa: ')
    alamat=input('Masukan Alamat Mahasiswa: ')
    asalSekolah=input('Masukan Asal Sekolah: ')
    kodeProdi=input('Masukan Kode Prodi: ')
    ipkAwal=float(input('Masukan Nilai IPK Awal: '))
    uts=float(input('Masukan Nilai UTS: '))
    uas=float(input('Masukan Nilai UAS: '))
    tm=float(input('Masukan Nilai Tugas: '))
    ips=((0.3*uts)+(0.3*tm)+(0.4*uas))
    ipk=(ips+ipkAwal)/2
    bea=beasiswa(ipk,kodeProdi)
    marks[nim]=nama,alamat,asalSekolah,kodeProdi,ipk,bea

print(marks)
