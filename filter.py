import numpy as np

if __name__ == "__main__":
    with open('delete.txt', 'a', encoding='utf16') as ftarget:
        with open ('error.txt', 'rt', encoding='utf16') as ferror:
            for line in ferror:
                line = line.split()
                if line[3] == 'c': 
                    continue
                else: 
                    print(line[3][21:-3])
                    ftarget.write(line[3][21:-3] + '\n')
