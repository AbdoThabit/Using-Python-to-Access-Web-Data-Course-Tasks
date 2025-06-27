import re
with open('Actual data.txt', 'r') as file:
     content = file.read()

        
digits = re.findall('[0-9]+', content)

total_sum = 0

for digit in digits:
    total_sum += int(digit)
    
    
print("Total sum of digits found in the file:", total_sum)    