harf = str(input('lotin alifbosidan birorta harf kiriting: '))
if harf.isidentifier():
    
    if harf == 'a' or harf == 'e' or harf == 'u' or harf == 'i' or harf == 'o':
        print(f'"{harf}" unli harf')
    elif len(harf) > 1:
        print('Faqat bitta harf kiriting')
    else:
        print(f'"{harf}" undosh harf')
else:
    print('siz raqam yoki belgi kiritdingiz iltimos lotin harfini kiriting')