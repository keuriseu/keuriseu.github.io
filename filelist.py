import os

DIR = 'assets/img/'
MON = '1809/'

PRE = '![](/'
SUF = ' "")'

def main():
    flist = os.listdir(DIR+MON)
    for f in flist:
        s = PRE+DIR+MON+f+SUF
        print(s)

if __name__ == "__main__":
    main()