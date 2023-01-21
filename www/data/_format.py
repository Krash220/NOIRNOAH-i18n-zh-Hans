import os
import json

files = os.listdir('.')

for fn in files:
    if fn.endswith('.json'):
        f = open(fn, 'r', encoding='utf-8')
        j = json.loads(f.read())
        f.close()
        
        f = open(fn, 'w', encoding='utf-8')
        f.write(json.dumps(j, ensure_ascii=False, indent=4, sort_keys=True))
        f.close()