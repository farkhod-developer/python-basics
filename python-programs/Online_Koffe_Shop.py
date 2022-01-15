a = ["Gender,Email,Age,City,Device,Coffee Quantity,Order At","Male,ummon, Carl,Wilderman,carl,yahoo.com,21->40,Seattle,Safari iPhone,2,afternoon", "Male,Marvin,Lind,marvin,hotmail.com,66->99,Detroit,Chrome Android,2,afternoon", "Female,Shanelle,Marquardt,shanelle,hotmail.com,21->40,Las Vegas,Chrome,1,afternoon", "Female,Lavonne,Romaguera,lavonne,yahoo.com,66->99,Seattle,Chrome,2,morning", "Male,Derick,McLaughlin,derick,hotmail.com,41->65,Chicago,Chrome Android,1,afternoon"]

def app(lists): 
    asd = {"Male":0,"Female":0, "yahoo.com":0,"hotmail.com":0, "21->40":0,"66->99":0,"41->65":0, "Seattle":0,"Detroit":0,"Las Vegas":0,"Chicago":0, "Safari iPhone":0,"Chrome Android":0,"Chrome":0, "afternoon":0,"morning":0}
    for i in lists:
        data = i.split(',') 
        for j in data: 
            if type(j) == str and not j.isnumeric():
                try:
                    a = asd.get(j)
                    a += 1
                    asd[j] = a
                except:
                    pass    
    data = {"Gender": {"Male": asd.get('Male'), 'Female': asd.get('Female')}, 'Email': {'yahoo.com': asd.get('yahoo.com'), 'hotmail.com': asd.get('hotmail.com')}, 'Age': {'21->40': asd.get('21->40'), '66->99': asd.get('66->99'), '41->65': asd.get('41->65')}, 'City': {'Seattle': asd.get('Seattle'), 'Detroit': asd.get('Detroit'), 'Las Vegas': asd.get('Las Vegas'), 'Chicago': asd.get('Chicago')}, 'Device': {'Safari iPhone': asd.get('Safari iPhone'), 'Chrome Android': asd.get('Chrome Android'), 'Chrome': asd.get('Chrome')}, 'Order At': {'afternoon': asd.get('afternoon'), 'morning': asd.get('morning')}}
    return str(data).replace(", ", ",").replace(": ",":").replace("'", '"')
print(app(a))
print(type(app(a)))