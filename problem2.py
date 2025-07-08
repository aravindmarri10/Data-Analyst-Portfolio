number =int(input('Enter the terms of sequence '))

fibu = []
if number <= 2:
  print('Input should be 2 or more')
else:
  fibu.extend([1,1]) #[1,1]
  i = 0
  while len(fibu) < number:
    element = sum(fibu[i:i+2]) # fibu[2,4]
    fibu.append(element) #[1,1,2]
    i+=1
  print(f"Fibonacci sequence: {fibu}")
