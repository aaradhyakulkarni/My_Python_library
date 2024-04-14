input_string = input('input any string : ')
vowels = 'aeiouAEIOU'
vowels_in_string = [char for char in input_string if char in vowels]
print("vowels in " + input_string + " are:", vowels_in_string)