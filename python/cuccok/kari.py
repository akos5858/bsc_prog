import random as rd

#names = ["Szeri", "Gyuri", "Dina", "Beni", "Viki", "Guszti", "Emil"]
#pairs = [("Szeri", "Gyuri"), ("Dina", "Beni"), ("Viki", "Guszti")]

names = ["Szeri", "Gyuri", "Beni", "Viki", "Guszti", "Emil"]
pairs = [("Szeri", "Gyuri"), ("Viki", "Guszti")]

def kari(lst: list):
    d = {}
    for i in lst:
        d[i] = rd.choice(names)
        
    for c in lst:
        if d[c] == c:
            return kari(lst)
    for a, b in pairs:
        if d[a] == b:
            return kari(lst)
        if d[b] == a:
            return kari(lst)
        
    l = []
    for v in d.values(): l.append(v)
    l = list(dict.fromkeys(l))
    if len(l) != len(names): return kari(lst)

    return d

def meta():
    def execute():
        for ajandekozo, megajandekozott in (kari(names).items()):
            print(f'{ajandekozo} {megajandekozott}t húzta.')
       
    def meta2(): 
        try: execute()
        except RecursionError: return meta1()

    def meta1():
        try: execute()
        except RecursionError: return meta2()

    meta1()

def txt():
    def execute():
        with open('kari.txt', "w+") as f:
            a = []
            for ajandekozo, megajandekozott in (kari(names).items()):
                a.append(f'{ajandekozo} {megajandekozott}t huzta.')
            for i in a:
                l = [str(i), "\n"]
                f.writelines(l)
        
    def meta2(): 
        try: execute()
        except RecursionError: return meta1()

    def meta1():
        try: execute()
        except RecursionError: return meta2()

    meta1()

if __name__ == "__main__":
    txt()
    
    
    