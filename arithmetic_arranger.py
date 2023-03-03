import re



def arithmetic_arranger(problems,show=False):

    strip_problem = [q.replace(' ','') for q in problems]
    split_problem = [s.split() for s in problems]
    pattern = re.compile("[+\-]")
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
            
            return print("Error: Operator must be '+' or '-'.")
            
            
        elif (len(i[0]) > 4) or (len(i[2]) > 4) : 
            
            return print("Error: Numbers cannot be more than four digits.")
            

        elif len(strip_problem) > 5: 
            
            return print("Error: Too many problems.")
            

        elif (i[0].isnumeric() and i[2].isnumeric()) == False:
            
            return print("Error: Numbers must only contain digits.")
        

        else:
            green_light = 1



    if green_light == 1:


        
        for i in split_problem:
            
            pad_len = max(len(i[0]),len(i[2]))
            padding.append(int(pad_len))

            print(f'pad len = {pad_len}')
            print(padding)


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


        # l_concate = '    '.join([i.rjust(padding[l_operand.index(i)]+2) for i in l_operand])
        # r_o_concate = '    '.join([operator[i] + r_operand[i].rjust(padding[i]+1) for i in range(len(operator))])
        # ans_concate = '    '.join([str(num_answer[i]).rjust(len(breakline[i])) for i in range(len(num_answer))])




        l_concate = '    '.join([i.rjust(padding[index]+2) for index, i in enumerate(l_operand)])
        r_o_concate = '    '.join([operator[i] + r_operand[i].rjust(padding[i]+1) for i in range(len(operator))])
        ans_concate = '    '.join([str(num_answer[i]).rjust(len(breakline[i])) for i in range(len(num_answer))])

        breakline = '    '.join(breakline)

        print(l_operand) ## debug
        print(r_operand)  ## debug


        if show == True:

            arranged_problems = print(l_concate+'\n'+r_o_concate+'\n'+breakline+'\n'+ans_concate)

        else:

            arranged_problems = print(l_concate+'\n'+r_o_concate+'\n'+breakline)


        return arranged_problems
    


arithmetic_arranger(['11 + 4', '3801 - 2999', '1 + 2', '123 + 49', '1 - 9380'])

## ['1 + 2', '1 - 9380']  the 2nd '1' won't align due to python though it is the 1st '1'    SOLVED

## ['11 + 4', '3801 - 2999', '1 + 2', '123 + 49', '1 - 9380']   same issue as above    SOLVED

## ['24 + 85215', '3801 - 2', '45 + 43', '123 + 49'] doesnt trigge error "Error: Numbers cannot be more than four digits." SOLVED

## ['98 + 3g5', '3801 - 2', '45 + 43', '123 + 49'] this test triggered a python value error instead of "Error: Numbers must only contain digits."   SOLVED