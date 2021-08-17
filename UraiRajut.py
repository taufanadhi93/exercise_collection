def urai(kata):
    a=''
    for i in range(1,len(kata)+1):
        a=a+kata[0:i]
    print(a)    
    

def rajut(kata):
    ans=kata
    for i in range(1,len(kata)+1):
        b=kata[0:i]
        ans=ans-b
        print(ans)

urai(kata=input('Masukan kata: '))
rajut(kata=input('Masukan Kata: '))
