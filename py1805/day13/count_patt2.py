import re
from collections import Counter

def count_patt(fname, patt):
    result = Counter()
    cpatt = re.compile(patt)
    with open(fname) as fobj:
        for line in fobj:
            m = cpatt.search(line)
            if m:   # 如果成功匹配，则为真
                key = m.group()
                result.update([key])
    return result


if __name__ == '__main__':
    logfile = 'access_log'
    ip = '^(\d+\.){3}\d+'
    c = count_patt(logfile, ip)
    print(c)
    print(c.most_common(5))
