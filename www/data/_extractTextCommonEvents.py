import json
import codecs

names = {
    'シエル': '希尔 Ciel',
    'ノエル': '诺尔 Noel',
    'モモノ': '桃野 Momono',
    'ヴァイオ': '薇欧 Vaio',
    'ラム': '拉姆 Ram',
    'リラ': '莉拉 Lilla',
    'ツツジ': '杜娟 Tsutsuji',
    'ワカバ': '若叶 Wakaba',
    'コハク': '琥珀 Kohaku',
    'サフィー': '青玉 Sapphie',
    'ヒスイ': '翡翠 Hisui',
    'オランジュ': '柑橘 Orange',
    'アズ': '阿梓 Azu',
    'グレア': '格蕾亚 Grea',
    'アナウンス': '广播',
    '子ども': '小孩子',
    '女性の声': '女性的声音',
    '機械的な声': '机械的声音',
    '中性的な声': '中性的声音',
    '男性の声': '男性的声音',
    '研究員': '研究员',
    '研究員A': '研究员A',
    '研究員B': '研究员B'
}

def to_json(f : str):
    j = None

    try:
        with open(f + '.json', 'r', encoding='utf-8') as rd:
            j = json.loads(rd.read())
    except:
        return

    with open('text/' + f + '.csv', 'w', encoding='utf-8') as wd:
        wd.write(codecs.BOM_UTF8.decode('utf-8'))

        for p in j:
            if p is not None:
                last = -1
                for i in p['list']:
                    if i['code'] == 401:
                        if last == 101 and i['parameters'][0] in names:
                            wd.write(names[i['parameters'][0]] + '\n')
                        else:
                            wd.write(i['parameters'][0] + '\n')
                    last = i['code']
                        
if __name__ == '__main__':
    to_json('CommonEvents')