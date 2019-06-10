import datetime

TITLE = "Board Man Gets Paid"
DIR = '_posts/'
DATENOW = datetime.datetime.now()
SUF = ".md"
CT = "-0500"
DEF = 'def.md'

def main():
    date = str(DATENOW.date())
    date_time = str(DATENOW).split('.')[0]
    title = TITLE.replace(" ", "-")
    filename = date+'-'+title.lower()+SUF
    
    with open(DIR+filename, 'w') as out_file:
        with open(DEF, 'r') as in_file:
            for line in in_file:
                if line.startswith('date'):
                    out_file.write(line.rstrip('\n') + " " + date_time + " " + CT + '\n')
                elif line.startswith('title'):
                    out_file.write(line.rstrip('\n') + " " + TITLE + '\n')
                else:
                    out_file.write(line)
    

if __name__ == "__main__":
    main()