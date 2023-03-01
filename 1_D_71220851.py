print('='*20,'BARIS ARITMATIKA', '='*20 )
def aritmatika(a, b, n):
    total = (1/2)*n*(2*a + (n-1)*b)
    return total
a= int(input('Masukan bilangan awal : '))
b= int(input('Masukan selisih bilangan : '))
n= int(input('Masukan banyaknya suku : '))
print('Total dari deret artimatika tersebut adalah : ', aritmatika(a,b,n))

