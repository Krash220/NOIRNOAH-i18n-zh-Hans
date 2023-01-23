import codecs
import os

commonMap = [[1, 350, 1], [363, 377, 496], [385, 483, 511], [486, 879, 761], [880, 880, 1162], [883, 1039, 1268], [1041, 1093, 1483], [1098, 1104, 1536], [1107, 1112, 1549], [1113, 1684, 1588], [1686, 1807, 2202]]

def filelines(fn):
    with open(fn, encoding='utf-8') as fd:
        ls = fd.readlines()
        for i in range(len(ls)):
            ls[i] = ls[i].strip('\n').strip(codecs.BOM_UTF8.decode('utf-8'))
        return ls

if __name__ == '__main__':
    f15 = filelines('text/CommonEvents.csv')

    os.system('git checkout R-18 text/CommonEvents.csv')

    f18 = filelines('text/CommonEvents.csv')

    for item in commonMap:
        offset = item[2] - item[0]
        for i in range(item[0] - 1, item[1]):
            f15[i] = f18[i + offset]

    with open('text/CommonEvents.csv', 'w', encoding='utf-8') as wd:
        wd.write(codecs.BOM_UTF8.decode('utf-8'))

        for i in f15:
            wd.write(i)
            wd.write('\n')
    
    os.system('git checkout R-18 text/Map*.csv')
    os.system('git checkout R-15 text/Map030.csv')

    map025 = filelines('text/Map025.csv')[:31]

    with open('text/Map025.csv', 'w', encoding='utf-8') as wd:
        wd.write(codecs.BOM_UTF8.decode('utf-8'))

        for i in map025:
            wd.write(i)
            wd.write('\n')