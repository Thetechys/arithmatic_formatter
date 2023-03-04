import re


def arithmetic_arranger(problems,show=False):

    split_problem = [s.split() for s in problems]
    l_operand = list()
    operator = list()
    r_operand = list()
    num_l_operand = list()
    num_r_operand = list()
    num_answer = list()
    breakline = list()
    padding = list()
    green_light = 0



    for i in split_problem:   ### for loop that trigger error msg if argument doesn't meet requirement


        if re.search('\+|\-',i[1]) == None:             
            return "Error: Operator must be '+' or '-'."
                        
        elif (len(i[0]) > 4) or (len(i[2]) > 4) :       
            return "Error: Numbers cannot be more than four digits."
            
        elif len(strip_problem) > 5:             
            return "Error: Too many problems."
            
        elif (i[0].isnumeric() and i[2].isnumeric()) == False:
            return "Error: Numbers must only contain digits."
        
        else:
            green_light = 1



    if green_light == 1:

        for i in split_problem:            
            pad_len = max(len(i[0]),len(i[2]))
            padding.append(int(pad_len))
            operator.append(i[1])   ## appending '+' and '-' into list
            l_operand.append(i[0])  ## appending left operand in string type
            num_l_operand.append(int(i[0])) ## convern and append left operant in int type
            r_operand.append(i[2])  ## right operand in string type
            num_r_operand.append(int(i[2]))  ## right operand in int type


            if re.search('\+',i[1]) != None:
                ans = int(i[0]).__add__(int(i[2]))
                num_answer.append(ans)

            else:                
                ans = int(i[0]).__sub__(int(i[2]))
                num_answer.append(ans)


        for i in range(len(operator)):
            breakline.append(''.rjust(padding[i]+2,'-')) #added 2 , one is for space btwn operator and r_operand , another is right under opertor


        l_concate = '    '.join([i.rjust(padding[index]+2) for index, i in enumerate(l_operand)])
        r_o_concate = '    '.join([operator[i] + r_operand[i].rjust(padding[i]+1) for i in range(len(operator))])
        ans_concate = '    '.join([str(num_answer[i]).rjust(len(breakline[i])) for i in range(len(num_answer))])
        breakline = '    '.join(breakline)




        if show == True:
            arranged_problems = l_concate+'\n'+r_o_concate+'\n'+breakline+'\n'+ans_concate

        else:
            arranged_problems = l_concate+'\n'+r_o_concate+'\n'+breakline

            
        return arranged_problems
