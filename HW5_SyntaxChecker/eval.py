def throw_syntax_error():
    with open("calc.out", "w") as f:
        f.write("Dont Let Me Down")

    print("syntax error")
    exit()

def get_index_paran_couple(lst):
    if ")" in lst:
        i = lst.index(")")
        j = len(lst) - 1 - lst[::-1].index("(",len(lst)-i-1)
        return i,j
    else:
        return 0,0

terms = [9.0, '.', 8.0, '+', "(", 3.5, "*", 4.0, "-",3.0, ")", '+', '(', 8.0, "+","(", 7.0, "*", 5.0, ")", ')', '-', "(",7.9,")"]
#t3 degeri b1 ve ( b1 ve  b2 veya b1 ) olsun
#terms = [False, "ve", "(",True,"ve",True,"veya",False,")"]
try:
    while len(terms) != 1:
        if "." in terms:
            i = terms.index(".")
            terms[i] = terms[i-1] + terms[i+1]/10
            terms[i-1] = ""
            terms[i+1] = ""
        elif ")" in terms:
            close_index, open_index = get_index_paran_couple(terms)
            while close_index - open_index >= 2:
                if close_index - open_index == 2:
                    if isinstance(terms[open_index+1], float) or isinstance(terms[open_index+1], bool):
                        terms[open_index] = ""
                        terms[close_index] = ""
                    else:
                        throw_syntax_error()
                elif "*" in terms[open_index:close_index]:
                    i = terms[open_index:close_index].index("*")
                    terms[open_index+i] = terms[open_index+i-1] * terms[open_index+i+1]
                    terms[open_index+i-1] = ""
                    terms[open_index+i+1] = ""
                elif "+" in terms[open_index:close_index]:
                    i = terms[open_index:close_index].index("+")
                    terms[open_index+i] = terms[open_index+i-1] + terms[open_index+i+1]
                    terms[open_index+i-1] = ""
                    terms[open_index+i+1] = ""
                elif "-" in terms[open_index:close_index]:
                    i = terms[open_index:close_index].index("-")
                    terms[open_index+i] = terms[open_index+i-1] - terms[open_index+i+1]
                    terms[open_index+i-1] = ""
                    terms[open_index+i+1] = ""
                elif "ve" in terms[open_index:close_index]:
                    i = terms[open_index:close_index].index("ve")
                    terms[open_index+i] = terms[open_index+i-1] and terms[open_index+i+1]
                    terms[open_index+i-1] = ""
                    terms[open_index+i+1] = ""
                elif "veya" in terms[open_index:close_index]:
                    i = terms[open_index:close_index].index("veya")
                    terms[open_index+i] = terms[open_index+i-1] or terms[open_index+i+1]
                    terms[open_index+i-1] = ""
                    terms[open_index+i+1] = ""
                if "" in terms: 
                    terms = [x for x in terms if x!=""]
                close_index, open_index = get_index_paran_couple(terms)
        elif "*" in terms:
            i = terms.index("*")
            terms[i] = terms[i-1] * terms[i+1]
            terms[i-1] = ""
            terms[i+1] = ""     
        elif "+" in terms:
            i = terms.index("+")
            terms[i] = terms[i-1] + terms[i+1]
            terms[i-1] = ""
            terms[i+1] = ""
        elif "-" in terms:
            i = terms.index("-")
            terms[i] = terms[i-1] - terms[+i+1]
            terms[i-1] = ""
            terms[i+1] = ""
        elif "ve" in terms:
            i = terms.index("ve")
            terms[i] = terms[i-1] and terms[i+1]
            terms[i-1] = ""
            terms[i+1] = ""
        elif "veya" in terms:
            i = terms.index("veya")
            terms[i] = terms[i-1] or terms[i+1]
            terms[i-1] = ""
            terms[i+1] = ""
        
        if "" in terms:
            terms = [x for x in terms if x!=""]
except KeyboardInterrupt:
    pass
print(terms)
