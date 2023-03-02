import re



def arithmetic_arranger(problems,*args):

    strip_problem = [q.replace(' ','') for q in problems]
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


    for i in strip_problem:   ### for loop that trigger error msg if argument doesn't meet requirement

        if re.search('\+|\-',i) == None: 
            
            return "Error: Operator must be '+' or '-'"
            
            
        elif re.match('[\d]{1,4}[\+|\-][\d]{1,4}',i) == None: 
            
            return"Error: Numbers cannot be more than four digits."
            

        elif len(strip_problem) > 4: 
            
            return "Error: Too many problems"
            

        elif re.match('[\d]+[\+|\-][\d]+',strip_problem[strip_problem.index(i)]) == None:
            
            return '#Error: Numbers must only contain digits.'
        

        else:
            #print('checked no problem, proceed format arrangement')  ## debug purposes
            green_light = 1


    if green_light == 1:

        
        for i in strip_problem:
            
            opfind = re.search('[+\-]',i)
            split_data = re.split(pattern,i)
            pad_len = max(len(split_data[0]),len(split_data[1]))
            padding.append(int(pad_len))


            operator.append(i[opfind.start()])   ## appending '+' and '-' into list
            l_operand.append(split_data[0])  ## appending left operand in string type
            num_l_operand.append(int(split_data[0])) ## convern and append left operant in int type
            r_operand.append(split_data[1])  ## right operand in string type
            num_r_operand.append(int(split_data[1]))  ## right operand in int type

            if re.search('\+',i) != None:

                ans = int(split_data[0]).__add__(int(split_data[1]))
                num_answer.append(ans)

            else:
                
                ans = int(split_data[0]).__sub__(int(split_data[1]))
                num_answer.append(ans)


        for i in range(len(operator)):

            breakline.append(''.rjust(padding[i]+2,'-')) #added 2 , one is for space btwn operator and r_operand , another is right under opertor


        l_concate = '    '.join([i.rjust(padding[l_operand.index(i)]+2) for i in l_operand])
        r_o_concate = '    '.join([operator[i] + r_operand[i].rjust(padding[i]+1) for i in range(len(operator))])
        ans_concate = '    '.join([str(num_answer[i]).rjust(len(breakline[i])) for i in range(len(num_answer))])

        breakline = '    '.join(breakline)


        arranged_problems = l_concate+'\n'+r_o_concate+'\n'+breakline+'\n'+ans_concate 

        if args == True:

            return arranged_problems