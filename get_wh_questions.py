# extract wh-questions from a book without any special library
# and module
# by Cheonkam Jeong
# Basically, I view the text as a big string, make the computer probe every character,
# and split sentences by starting (i.e., letters) and ending points (i.e., punctuation marks)
# Thereafter, I extracted wh-questions.

f = open('alice.txt', 'r')
temp = f.read()
bigString = temp.replace("\n", " ")        # to replace "\n" with space to make the file into a big string
f.close()

start_end = []       # a list of all starting and ending points [starting1, ending1, starting2...] 
odd_even = "start"  

for i in range(0, len(bigString) - 1):
    # to find and store starting points
    if odd_even == "start":                
        if bigString[i] != " ":            # store the index of the first character of the sentence
            start_end.append(i)            
            odd_even = "end"               # now it has a starting point
    # to find and store ending points
    elif odd_even == "end":                

        # for those with punctuation marks followed by spaces
        if (bigString[i] == "." or bigString[i] == "?" or bigString[i] == "!") and bigString[i+1] == " ":
            start_end.append(i)
            odd_even = "start"             # after storing it as an ending point, change the current state

        # for those that are not spaces and follow punctuation marks 
        elif bigString[i] != " " and (bigString[i-1] == "." or bigString[i-1] == "?" or bigString[i-1] == "!"):
            start_end.append(i)
            odd_even = "start"             

        # for those that belong to neither above but have weird endings, such as chapter titles
        # I will regard those that are not spaces but have two spaces as ending points
        # Since the last one has no i+1 and i+2, the range should be (< len(bigString) - 2)
        elif i < (len(bigString) - 2) and bigString[i] != " " and bigString[i+1] == " " and bigString[i+2] == " ":
            start_end.append(i)
            odd_even = "start"

# to print out characters between starting and ending points (a.k.a. sentences)
# w = 0
# while w < len(start_end)-1:                             # range should be the length of the start_end list minus 1 because of index mechanism
#     for k in range(start_end[w], start_end[w+1]+1):     # range plus 1 for the same reason
#         print(bigString[k], end='')                    
#     print()                                             
#     w += 2                                              # should increase 2 because the list stores both starting and ending points

# to find all the questions in this text

question_mark = []   # a list of all questions

e = 1
while e < len(start_end) - 1:                       # odd elements are ending points in the list start_end

    if bigString[start_end[e]] == "?" or bigString[start_end[e] -1] == "?":    # for checking both ? and ?' and the like
        question_mark.append(start_end[e - 1])
        question_mark.append(start_end[e])

    e += 2

#print(question_mark)

# to find all wh-questions in this text

d = 0
wh_all = []
what_mark = []
who_mark = []
why_mark = []
whether_mark = []
when_mark = []
where_mark = []
how_mark = []
sentence = ""

# Since this is based on characters...
g = open('alice_wh.txt', 'w')

while d < len(question_mark) - 1:
    for s in range (question_mark[d], question_mark[d+1] + 1): # bring all the corresponding characters between each starting and ending point
        sentence += bigString[s]

    if "What" in sentence:                                
        what_mark.append(sentence)
        sentence += "\n"
        g.write(sentence)

    elif "Who" in sentence:
        who_mark.append(sentence)
        sentence += "\n"
        g.write(sentence)

    elif "Why" in sentence:
        why_mark.append(sentence)
        sentence += "\n"
        g.write(sentence)

    elif "Whether" in sentence:
        whether_mark.append(sentence)
        sentence += "\n"
        g.write(sentence)

    elif "When" in sentence:
        when_mark.append(sentence)
        sentence += "\n"
        g.write(sentence)

    elif "Where" in sentence:
        where_mark.append(sentence)
        sentence += "\n"
        g.write(sentence)

    elif "How" in sentence:
        how_mark.append(sentence)
        sentence += "\n"
        g.write(sentence)

    d += 2
    sentence = ""

#print(what_mark)
#print(who_mark)
#print(why_mark)
#print(whether_mark)
#print(when_mark)
#print(where_mark)
#print(how_mark)

# all wh-questions
wh_all = what_mark + who_mark + why_mark + whether_mark + when_mark + where_mark + how_mark
print(wh_all)
print("A total of wh-questions in this text is: ", len(wh_all))

#g.write(str(wh_all))
g.close()
