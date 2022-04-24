import csv
import json
ebay = []
with open('django_basic'+'\\'+'blogs'+'\\'+'EBAY.csv',encoding='utf-8') as f:
    d = csv.reader(f)
    for row in d:
        ebay.append(row)

for k in ebay:
    k[-1] = k[-1].replace('[','').replace(']','').replace(',','').replace("'",'')
    k[-1] = k[-1].split()

# print(ebay[-1][-1])
with open('django_basic'+'\\'+'blogs'+'\\'+'ebay'+'\\'+'sportbag3.json',"w",encoding='utf-8') as json_obj  :

    sellername = []
    item = []
    price = []
    img = []
    for i in ebay:
        if(i[-1][0] == 'Bags' or i[-1][-1] == 'Handbags' ):
            sellername.append(i[0])
            item.append(i[1])
            price.append(i[2])
            img.append(i[3])
    get_txt_to_json = {
                                "sellername":sellername,
                                "item":item,
                                "price":price,
                                "img":img
                        }        
    json_obj.write(json.dumps(get_txt_to_json,indent=4,ensure_ascii=False))
