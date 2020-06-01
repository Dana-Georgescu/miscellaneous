#! usr/bin/python3.7
'''Challenge https://www.hackerrank.com/challenges/time-conversion/problem'''

def timeConversion():
    s = input()
    if s.startswith('12') and s.endswith('AM'):
        s = '00' + s[2:-2]
    elif s.endswith('AM') or s.startswith('12') and s.endswith('PM'):
        s = s[:-2]
    elif s.startswith('0') and s.endswith('PM'):
        s = str(int(s[1])+12) + s[2:-2]
    elif s.endswith('PM'):
        s = str(int(s[:2])+12) + s[2:-2]
    return s    
        
   

print(timeConversion())


