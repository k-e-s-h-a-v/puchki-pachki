import string

letter_values = dict((l, i) for i, l in enumerate(string.ascii_lowercase, start=1))
english_dict = open('path of the txt file containing all the words in a dictionary-(avilable in the same repository)-fileName:words_alpha.txt', 'r')

winning_words = []
count=0
for word in english_dict:
    count+=1
    word = word.rstrip().replace('-', '')
    value = sum([letter_values[l.lower()] for l in word])
    if value is 100:
        winning_words.append(word)

print(len(winning_words), 'out of {0} words where position count sums to 100'.format(count))
print('Shortest:', min(winning_words, key=len))
print('Longest:', max(winning_words, key=len), '\n')
print('\n'.join(winning_words))
