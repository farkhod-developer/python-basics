import pygal
line_chart = pygal.Line()
line_chart.title = "Yillik hisobot"
line_chart.x_labels = ['I-Bosqich', 'II-Bosqich', 'III-Bosqich', 'IV-Bosqich']
smm = int(input('Ijtimoiy tarmoqlar sonini kiriting: '))

i = 0
while i<smm:
    i += 1
    name = input("Ijtimoiy Tarmoq nomi: ")
     
    bir = float(input("Birinchi bosqich ko`rsatkichi: "))
    ikki = float(input("Ikkinchi bosqich ko`rsatkichi: "))
    uch = float(input("Uchinchi bosqich ko`rsatkichi: "))
    tort = float(input("To'rtinchi bosqich ko`rsatkichi: "))
    
    line_chart.add(name, [bir, ikki, uch, tort])
line_chart.render_in_browser()