
print('\n')

we="бла бла бла бла 4 бла 6"
if '4' in we and '6' in we:
    S1=True
else:
    S1=False

print(S1)

print('\n')

qw="тонна"

# new_qw=qw[2]+qw[1]+qw[0]+qw[4]
for i in qw:
    if 'н'==i:
        f="н"
    if 'о'==i:
        a='о'    
    if 'т'==i:
        k='т'
    if 'а'==i:
        t='а'

print(f+a+k+t)

print('\n')

name=input('введіт ім\'я: ')
city=input('введіт місто: ')

print(f"{name} мешкає в місті {city}")

print('\n')

er=input("Напишіть речення: ")

new_er=er.replace("від","до")

print(new_er)

print('\n')