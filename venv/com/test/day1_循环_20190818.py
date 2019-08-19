#循环
for  ever_letter in 'hello world!' :
    print(ever_letter)

for num in range(1,11):#不包含11
    print(str(num)+' + 1 =',num +1)


songslist = ['Holy Diver','Thunderstruck','Reble Reble']
for song in songslist:
    if song == 'Holy Diver':
        print(song,'- Dio')
    elif song == 'Thunderstruck':
        print(song,'-AC -DC')
    elif song == 'Rebel Rebel':
        print(song, ' - David Bowie')