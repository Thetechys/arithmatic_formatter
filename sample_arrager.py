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
from string import punctuation




def arithmetic_arranger(problem):

     strip_problem = [q.replace(' ','') for q in problem]

     print(strip_problem)

     for i in strip_problem: 

          if re.search('\+|\-',i) == None: 
               
               print("Error: Operator must be '+' or '-'")
               break
               
               
          elif re.match('[\d]{1,4}[\+|\-][\d]{1,4}',i.replace(' ','')) == None: 
               
               print("Error: Numbers cannot be more than four digits.")
               break

          elif len(strip_problem) > 4: 
               
               print("Error: Too many problems")
               break


          ## check if operand isdigit()
          elif i.isdigit() == False:

               print('#Error: Numbers must only contain digits.')
               break


          else:

               print('checked no problem')
     
    
#     return arranged_problems


mytxt = 'test'

# print(mytxt)
# print(mytxt.ljust(10,'-'))
# print(mytxt.rjust(10))


myq = ["32 + 3698"]


def arranger(q):

     pro_q = [q.split(sep=' ') for q in myq]

     print(pro_q[0][0].rjust(6))
     print(pro_q[0][1].ljust(1),pro_q[0][2].rjust(4))
     print('------')
     #print(pro_q[0][2].rjust(6))
     # print(pro_q[0][2].rjust(5))
     #print(pro_q)

#arranger(myq)


#arithmetic_arranger(q1_1)


#print(myq[0].isdigit())


def arithmetic_sampler(problem):

     strip_problem = [q.replace(' ','') for q in problem]

     peel_problem = [(q.replace('+','')).replace('-','') for q in problem]

     print(peel_problem)


arithmetic_sampler(q1_1)