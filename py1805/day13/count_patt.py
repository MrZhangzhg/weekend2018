import re

def count_patt(fname, patt):
    result = {}
    cpatt = re.compile(patt)
    with open(fname) as fobj:
        for line in fobj:
            m = cpatt.search(line)
            if m:   # 如果成功匹配，则为真
                key = m.group()
                result[key] = result.get(key, 0) + 1
    return result


if __name__ == '__main__':
    logfile = 'access_log'
    ip = '^(\d+\.){3}\d+'
    br = 'MSIE|Firefox|Chrome'
    print(count_patt(logfile, ip))
    print(count_patt(logfile, br))
