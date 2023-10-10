import sys
try:
    if  sys.argv[1] != '':
        n = sys.argv[1]
    print(n)
except Exception as ex:
    print ('no variable passed')
