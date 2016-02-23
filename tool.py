def simplify(eq_operations):
 eq_operations_len = len(eq_operations)
 count_length = 0
 while count_length < eq_operations_len:
  if eq_operations[count_length] == '**':
   eq_operations[count_length] = int(eq_operations[count_length - 1]) ** int(eq_operations[count_length + 1])
   del(eq_operations[count_length + 1])
   del(eq_operations[count_length - 1])
   count_length += 1
  else:
   count_length += 1
  eq_operations_len = len(eq_operations)
 count_length = 0
 while count_length < eq_operations_len:
  if eq_operations[count_length] == '*':
   eq_operations[count_length] = int(eq_operations[count_length - 1]) * int(eq_operations[count_length + 1])
   del(eq_operations[count_length + 1])
   del(eq_operations[count_length - 1])
   count_length -= 1
  else:
   count_length += 1
  eq_operations_len = len(eq_operations)
 count_length = 0 
 while count_length < eq_operations_len:
  if eq_operations[count_length] == '/':
   eq_operations[count_length] = int(eq_operations[count_length - 1]) / int(eq_operations[count_length + 1])
   del(eq_operations[count_length + 1])
   del(eq_operations[count_length - 1])
   count_length -= 1
  else:
   count_length += 1 
  eq_operations_len = len(eq_operations)
 count_length = 0 
 while count_length < eq_operations_len:
  if eq_operations[count_length] == '+':
   eq_operations[count_length] = int(eq_operations[count_length - 1]) + int(eq_operations[count_length + 1])
   del(eq_operations[count_length + 1])
   del(eq_operations[count_length - 1])
   count_length -= 1
  else:
   count_length += 1 
  eq_operations_len = len(eq_operations)
 count_length = 0
 while count_length < eq_operations_len:
  if eq_operations[count_length] == '-':
   eq_operations[count_length] = int(eq_operations[count_length - 1]) - int(eq_operations[count_length + 1])
   del(eq_operations[count_length + 1])
   del(eq_operations[count_length - 1])
   count_length -= 1
  else:
   count_length += 1
   eq_operations_len = len(eq_operations)

equation = input()
eq_operations = equation.split()
while len(eq_operations) > 1:
 simplify(eq_operations)
 
print (eq_operations)
