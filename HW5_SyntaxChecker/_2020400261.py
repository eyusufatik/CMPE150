import sys
import re

tdigit_to_number_str = {"nokta": ".", "sifir": "0", "bir": "1", "iki": "2", "uc": "3",
                        "dort": "4", "bes": "5", "alti": "6", "yedi": "7", "sekiz": "8", "dokuz": "9"}

reserverd_keywords = {'0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'nokta', 'sifir', 'bir', 'iki', 'uc', 'dort', 'bes', 'alti',
            'yedi', 'sekiz', 'dokuz', 'dogru', 'yanlis', '+', '-', '*', 'arti', 'eksi', 'carpi', 've', 'veya', '(', ')',
            'ac-parantez', 'kapa-parantez', 'AnaDegiskenler', 'YeniDegiskenler', 'Sonuc', 'degeri', 'olsun'}

expression_keywords = {'0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'nokta', 'sifir', 'bir', 'iki', 'uc', 'dort', 'bes', 'alti',
            'yedi', 'sekiz', 'dokuz', 'dogru', 'yanlis', '+', '-', '*', 'arti', 'eksi', 'carpi', 've', 'veya', '(', ')',
            'ac-parantez', 'kapa-parantez'}

tdigit = {}

def throw_syntax_error():
    with open("calc.out", "w") as f:
        f.write("Dont Let Me Down")

    #print("syntax error")
    sys.exit()


def get_val_from_str(string):
    if string == "dogru":
        return True
    elif string == "yanlis":  # booleans
        return False
    else: # numbers
        if re.match(r"^\d$", string) != None:  
            return float(string)
        elif re.match(r"^\d\.\d$", string) != None:
            return float(string)
        else:
            if re.match(r"^[a-z]+$", string) != None:
                if string in tdigit_to_number_str:
                    num = float(tdigit_to_number_str[string])
                    return num
                else:
                    throw_syntax_error()
            elif re.match(r"^[a-z]+\s+nokta\s+[a-z]+$", string) != None:
                words = string.split()
                s = ""
                for word in words:
                    if word in tdigit_to_number_str:
                        s += tdigit_to_number_str[word]
                    else:
                        throw_syntax_error()
                return float(s)
            else:
                throw_syntax_error()

def get_index_paran_couple(lst):
    if ")" in lst:
        i = lst.index(")")
        j = len(lst) - 1 - lst[::-1].index("(",len(lst)-i-1)
        return i,j
    else:
        return 0,0

def evaluate_expression(exp_string):
    terms = exp_string.split()
    #check if parantheses match
    open_parantheses_num = 0
    close_parantheses_num = 0
    for term in terms:
        if term == "(" or term == "ac-parantez":
            open_parantheses_num += 1
        elif term == ")" or term == "kapa-parantez":
            close_parantheses_num += 1
        if close_parantheses_num > open_parantheses_num:
            throw_syntax_error()
    if open_parantheses_num != close_parantheses_num:
        throw_syntax_error()
    else:
        exp_type = None
        for i in range(len(terms)):
            if terms[i] in program_variables:
                terms[i] = program_variables[terms[i]]
                if i != len(terms)-1:
                    if terms[i+1]  == "nokta" or terms[i+1] == ".":
                        throw_syntax_error()
            elif terms[i] in expression_keywords:
                if terms[i] == "dogru":
                    terms[i] = True
                elif terms[i] == "yanlis":  # booleans
                    terms[i] = False
                else:
                    if re.match(r"^\d$", terms[i]) != None:  
                        terms[i] = float(terms[i])
                        if i != len(terms)-1:
                            if terms[i+1]  == "nokta":
                                throw_syntax_error()
                    elif terms[i] in tdigit_to_number_str:
                        terms[i] = tdigit_to_number_str[terms[i]]
                        if terms[i] != ".":
                            terms[i] = float(terms[i])
                        else:
                            if i == 0 or i == len(terms)-1:
                                throw_syntax_error()
                            else:
                                if re.match(r"^\d$", terms[i+1]) != None or re.match(r"^\d\.\d$", terms[i+1]) != None or terms[i+1] == "nokta" or terms[i+1] in program_variables: 
                                    throw_syntax_error()
                    elif terms[i] == "arti" or terms[i] == "+":
                        terms[i] = "+"
                        if i == 0 or i == len(terms) - 1:
                                throw_syntax_error()
                    elif terms[i] == "eksi" or terms[i] == "-":
                        terms[i] = "-"
                        if i == 0 or i == len(terms) - 1:
                                throw_syntax_error()
                    elif terms[i] == "carpi" or terms[i] == "*":
                        terms[i] = "*"
                        if i == 0 or i == len(terms) - 1:
                                throw_syntax_error()
                    elif terms[i] == "ve":
                        if i == 0 or i == len(terms) - 1:
                            throw_syntax_error()
                    elif terms[i] == "veya":
                        if i == 0 or i == len(terms) - 1:
                            throw_syntax_error()
                    elif terms[i] == "ac-parantez":
                        terms[i] = "("
                    elif terms[i] == "kapa-parantez":
                        terms[i] = ")"
            else:
                if re.match(r"^\d\.\d$", terms[i]) != None:
                        terms[i] = float(terms[i])
                        if i != len(terms)-1:
                            if terms[i+1]  == "nokta":
                                throw_syntax_error()
                else:
                    throw_syntax_error()
            
            if exp_type == type(1.0) and (terms[i] == "ve" or terms[i] == "veya"):
                throw_syntax_error()
            
            if exp_type == None and not isinstance(terms[i], str):
                    exp_type = type(terms[i])
            elif exp_type == type(1.0) and isinstance(terms[i], bool):
                throw_syntax_error()
            elif exp_type == type(True) and isinstance(terms[i], float):
                throw_syntax_error()
            # elif exp_type == None:
            #     throw_syntax_error()
        #print(terms) #TODO:check for double operands
        for i in range(len(terms)):
            term = terms[i]
            if term == "+" or term == "-" or term == "*" or term == ".":
                if terms[i-1]==")" and terms[i+1] == "(":
                    pass
                elif terms[i-1]==")" and isinstance(terms[i+1],float):
                    pass
                elif isinstance(terms[i-1],float) and terms[i+1] == "(":
                    pass
                elif isinstance(terms[i-1],float) and isinstance(terms[i+1],float):
                    pass
                else:
                    throw_syntax_error()
            elif term=="ve" or term == "veya":
                if terms[i-1]==")" and terms[i+1] == "(":
                    pass
                elif terms[i-1]==")" and isinstance(terms[i+1],bool):
                    pass
                elif isinstance(terms[i-1],bool) and terms[i+1] == "(":
                    pass
                elif isinstance(terms[i-1],bool) and isinstance(terms[i+1],bool):
                    pass
                else:
                    throw_syntax_error()
            elif term != "(" and term != ")":
                if i != len(terms)-1:
                    if terms[i+1] == "(":
                        throw_syntax_error()
                    elif isinstance(terms[i+1], float) or isinstance(terms[i+1], bool):
                        throw_syntax_error()
                    

        #ADD CALC HERE   #TODO: consecutive bool or float
        while len(terms) != 1:
            if "." in terms:
                i = terms.index(".")
                terms[i] = terms[i-1] + terms[i+1]/10
                terms[i-1] = ""
                terms[i+1] = ""
            elif ")" in terms:
                close_index, open_index = get_index_paran_couple(terms)
                if close_index - open_index == 1:
                    throw_syntax_error()
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
        return terms[0]


program_file = open("calc.in")
full_program = program_file.readlines()

start_line_num = 0
while full_program[start_line_num].strip() == "":
    start_line_num += 1

# checking if file starts with AnaDegiskenler
if full_program[start_line_num].strip() != "AnaDegiskenler":
    throw_syntax_error()

# checking if YeniDegiskenler and Sonuc exist, and YD comes before Sonuc
yenidegiskenler_found = False
sonuc_found = False
sonuc_index = 0
for line in full_program:
    stripped_line = line.strip()
    if stripped_line == "YeniDegiskenler" and sonuc_found == False:
        yenidegiskenler_found = True

    if stripped_line == "Sonuc" and yenidegiskenler_found == True:
        sonuc_found = True
    else:
        if sonuc_found == False:
            sonuc_index += 1

if yenidegiskenler_found == False or sonuc_found == False:
    throw_syntax_error()

# checking if there is zero or one non-empty lines after Sonuc
after_sonuc_count = 0
for line in full_program[sonuc_index+1:]:
    if line.strip() != "":
        after_sonuc_count += 1
if after_sonuc_count > 1:
    throw_syntax_error()  # more than one non-empty(empty=only whitespace) lines

check_mode = "init-stmt"  # mid-stmt final-stmt
program_variables = dict()
line_number = start_line_num
for line in full_program[start_line_num+1:]:
    stripped_line = line.strip()
    #print(stripped_line)
    if stripped_line == "YeniDegiskenler":
        check_mode = "mid-stmt"
        continue  # starting with the next line, check for <mid-stmt>

    if stripped_line == "Sonuc":
        check_mode = "final-stmt"
        continue  # starting with the next line, check for <final-stmt>

    if check_mode == "init-stmt":
        if stripped_line != "":
            match = re.match(
                r"^([0-9a-zA-Z]{1,10})\s+degeri\s+([0-9a-zA-Z\. ]+?)\s+olsun$", stripped_line)
            if match == None:
                throw_syntax_error()
            else:
                # print(match.groups())
                var_name = match.group(1)
                value = match.group(2)
                # print(var_name, value)
                if var_name in program_variables or var_name in reserverd_keywords:
                    throw_syntax_error()
                else:
                    program_variables[var_name] = get_val_from_str(value)

    if check_mode == "mid-stmt":
        if stripped_line != "":
            #print(stripped_line)
            match = re.match(r"^([0-9a-zA-Z]{1,10})\s+degeri\s+([a-zA-Z0-9\(\)\.\*\+\-\s]+?)\s+olsun$", stripped_line)
            if match == None:
                throw_syntax_error()
            else:
                var_name = match.group(1)
                expression = match.group(2)
                if var_name in program_variables or var_name in reserverd_keywords:
                    throw_syntax_error()
                else:
                    program_variables[var_name] = evaluate_expression(expression)
    if check_mode == "final-stmt":
        if stripped_line != "":
            #print(stripped_line)
            match = re.match(r"^([a-zA-Z0-9\(\)\.\*\+\-\s]+?)$", stripped_line)
            if match == None:
                throw_syntax_error()
            else:
                expression = match.group(1)
                #print(evaluate_expression(expression))
    line_number += 1

#print(program_variables)
with open("calc.out","w") as f:
    f.write("Here Comes the Sun")