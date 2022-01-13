import math
import operator

def _get_log_pair(n, base):
    try:
        log = math.log(n, base)
        return log, math.floor(log)
    except ValueError:
        return 0, 0

def _abs_g_dump(n, base):
    if n < base or not n:
        return (yield str(n))
    while operator.sub(*(logpair := _get_log_pair(n, base))) and n:
        n, remainder = divmod(n, base)
        yield str(remainder)
    else:
        yield str(0) * logpair[1]
        yield str(1)

def abs_g_dump(n, base):
    yield from _abs_g_dump(abs(n), base)
    if n < 0 and base - 1:
        yield '-'
        
def abs_dump(n, base):
    return ''.join(abs_g_dump(n, base))[::-1]
    
def main():
    print(abs_dump(*map(int, input().split())))

if __name__ == '__main__':
    while True:
        main()
        print()
