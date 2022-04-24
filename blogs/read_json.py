import json
with open('django_basic'+'\\'+'blogs'+'\\'+'lazada'+'\\'+'sportsbag2.json',encoding='utf-8') as f:
    s = f.read()
    result = json.loads(s)
print(result['sellername'][0])