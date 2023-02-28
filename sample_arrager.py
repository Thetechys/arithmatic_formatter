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

     print(strip_problem)

     green_light = 0

     for i in strip_problem: 

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

          elif strip_problem.index(i) != -1 and len(strip_problem) != 1:
               continue

          else:
               print('checked no problem')
               green_light = 1

     
     # if green_light == 1:


     #      for i in strip_problem:

     #           print(i)

          #arranged_problems = [strip_problem[0][0].rjust(6),strip_problem[0][1].ljust(1),strip_problem[0][2].rjust(4)]



     #return arranged_problems





def arranger(myq):

     pro_q = [q.split(sep=' ') for q in myq]

     print(pro_q[0][0].rjust(6))
     print(pro_q[0][1].ljust(1),pro_q[0][2].rjust(4))
     print('------')
     #print(pro_q[0][2].rjust(6))
     # print(pro_q[0][2].rjust(5))
     print(pro_q)




def sampler(que):

     strip_problem = [q.replace(' ','') for q in que]
     gex = re.compile("[+\-]")

     for i in strip_problem:

          print(i)
          pattern = str(re.findall(gex,i))
          clean_data = re.split(gex, i)

          print(clean_data)
          print(pattern)


def sampler2(que):

     strip_problem = [q.replace(' ','') for q in que]
     gex = re.compile("[+\-]")
     

     l_operand = []
     operator = []
     r_operand = []


     for i in strip_problem:
          
          opfind = re.search('[+\-]',i)
          split_data = re.split(gex,i)


          operator.append(i[opfind.start()])
          l_operand.append(split_data[0])
          r_operand.append(split_data[1])

          
     print(operator) ##debug
     print(l_operand) ##debug
     print(r_operand) ##debug




              

#sampler2(q1_1)






os1 = '1034'
os2 = '+'


s0 = ['hell','asdf','qwer']
s1 = ['+','*','-']
s2 = ['no','yes','may']

print(s0[0].rjust(5)+' '.rjust(4)+s2[0].rjust(5)+'\n'+s0[1].rjust(5)+' '.rjust(4)+s2[1].rjust(5)+'\n'+s0[2].rjust(5)+' '.rjust(4)+s2[2].rjust(5))
# print(s0.rjust(5)+' '.rjust(4)+s2.rjust(5))
# print(s0.rjust(5)+' '.rjust(4)+s2.rjust(5))




j_count = 0
j_string = str

for i in s1:

     j_count += 1
     j_obj = i.ljust(1)+s2[j_count-1].rjust(5)
     #j_string = j_string + j_obj