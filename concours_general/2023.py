#3
def nombre_polices_utilisees(dic:dict,lst:list) -> int :
    sett = set()
    for values in dic.values():
        for police in values :
            for install_police in lst :
                if police == install_police:
                    sett.add(police)
                    break
    return len(sett)

polices = {
'p': ['Verdana', 'Tahoma', 'Georgia'],
'code': ['Roboto', 'Lucida Console'],
'pre': ['Lucida Console', 'Roboto'],
'h1': ['Tahoma', 'Georgia'],
'h2': ['Georgia', 'Verdana']
}

lst = ["Helvetica", "Roboto", "Tahoma", "Verdana"]

print(nombre_polices_utilisees(polices,lst))

#4
'''
'body': ['p1'],

'p': ['p2', 'Tahoma', 'Georgia'],
'code': ['P1', 'Lucida Console'],
'pre': ['p2', 'Roboto'],
'h1': ['p', 'Georgia'],
'h2': ['p6', 'Verdana']

'''