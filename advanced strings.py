my_name = 'Gitahi'
print(my_name[0]) #prints the first letter
print(my_name[-1]) #prints the last letter

sentence = 'This is a sentence'
print(sentence[:4])
print(sentence.split()) #delimiter - default delimeter is a space

sentence_split = sentence.split()
sentence_join = ' ' .join(sentence_split)
print(sentence_join) #join the sentences

quote = 'He said, "give me all your money!"'
print(quote)

too_much_space = '                   HELLO                    '
print(too_much_space.strip())

print('A' in 'Apple') #true
print('a' in 'Apple') #False

letter = 'A'
word = 'Apple'
print(letter.lower() in word.lower())

movie = 'Seal team'
print('My favourite movie is {}.'.format(movie))
print('My favourite movie is %s.'%movie) #percent formating
print('My favourite movie is {movie}.') #f string /string litteral