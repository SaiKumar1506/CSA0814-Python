input_string=input("enter a string:")
vowels='aeiouAEIOU'
vowels_count=0
for char in input_string:
  if char in vowels:
    vowels_count+=1
print(vowels_count)
