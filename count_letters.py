import string

sentence = 'Two roads diverged in a yellow wood, And sorry I could not travel both And be one traveler, long I stood And looked down one as far as I could To where it bent in the undergrowth'
alaphabet = list(string.ascii_lowercase)
count_letter = {}
for letter in alaphabet:
    count_letter.update({letter :"0"})

lower_sentence = sentence.lower()
