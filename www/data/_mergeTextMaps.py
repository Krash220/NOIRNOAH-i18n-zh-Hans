import json
import codecs

def from_csv(f : str):
    j = None

    try:
        with open(f + '.json', 'r', encoding='utf-8') as rd:
            j = json.loads(rd.read())
    except:
        return

    with open('text/' + f + '.csv', 'r', encoding='utf-8') as wd:
        events = j['events']

        for e in events:
            if e is not None:
                for p in e['pages']:
                    for i in p['list']:
                        if i['code'] == 401:
                            i['parameters'][0] = wd.readline().strip('\n').strip(codecs.BOM_UTF8.decode('utf-8'))

    with open(f + '.json', 'w', encoding='utf-8') as wd:
        wd.write(json.dumps(j, ensure_ascii=False, indent=4, sort_keys=True))

if __name__ == '__main__':
    for i in range(50):
        from_csv('Map%03d' % i)