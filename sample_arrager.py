q1 = ["32 + 698"] #normal problem 
q1_1 = ["32 + 698", "3801 - 2", "45 + 43", "123 - 49"] #normal but longer problem
q2 = ['15 + 12', '1000 - 99', '3525 + 78' , '342 + 10', '55 - 66']  #Error: Too many problems.
q3 = ['100 * 3','15 + 12', '231 + 321'] #Error: Operator must be '+' or '-'
q4 = ['15 + 12','yourmom + yoursis'] #Error: Numbers must only contain digits.
q5 = ['12345 + 45678'] #Error: Numbers cannot be more than four digits.

#There should be a single space between the operator and the longest of the two operands, 
#the operator will be on the same line as the second operand, both operands will be in the same order as provided 
# (the first will be the top one and the second will be the bottom).
#Numbers should be right-aligned.
#There should be four spaces between each problem.
#There should be dashes at the bottom of each problem. 
# The dashes should run along the entire length of each problem individually. (The example above shows what this should look like.)


'------------------------------------------------------------------------'

import re



def arithmetic_arranger(problem):

     strip_problem = [q.replace(' ','') for q in problem]
     pattern = re.compile("[+\-]")
     l_operand = list()
     operator = list()
     r_operand = list()
     num_l_operand = list()
     num_r_operand = list()
     num_answer = list()
     breakline = list()
     green_light = 0
     


     print(f'strip_problem: {strip_problem}')


     for i in strip_problem:   ### for loop that trigger error msg if argument doesn't meet requirement

          print(i)

          if re.search('\+|\-',i) == None: 
               print("Error: Operator must be '+' or '-'")
               break
               
          elif re.match('[\d]{1,4}[\+|\-][\d]{1,4}',i) == None: 
               print("Error: Numbers cannot be more than four digits.")
               break

          elif len(strip_problem) > 4: 
               print("Error: Too many problems")
               break

          elif re.match('[\d]+[\+|\-][\d]+',strip_problem[strip_problem.index(i)]) == None:
               print('#Error: Numbers must only contain digits.')
               break

          else:
               print('checked no problem')
               green_light = 1

     print('debug level')

     print('debug level')
     
     if green_light == 1:

          
          for i in strip_problem:
               
               opfind = re.search('[+\-]',i)
               split_data = re.split(pattern,i)


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


          l_concate = '    '.join([i.rjust(5) for i in l_operand])
          r_o_concate = '    '.join([operator[i] + r_operand[i].rjust(4) for i in range(len(operator))])
          ans_concate = '    '.join([str(num_answer[i]).rjust(5) for i in range(len(num_answer))])

          for i in range(len(operator)):
               break_len = len([r_operand[i].rjust(4) for i in range(len(operator))])
               print(f'breaklen: {break_len}')
               breakline.append(''.rjust(break_len+1,'-'))

          

          print(f'l_operand: {l_operand}')
          print(f'r_operand: {r_operand}')
          print(f'num_l_operand: {num_l_operand}')
          print(f'num_r_operand: {num_r_operand}')
          print(f'num_answer: {num_answer}')

          print(l_concate)
          print(r_o_concate)
          print('    '.join(breakline))
          print(ans_concate)


arithmetic_arranger(q1_1)