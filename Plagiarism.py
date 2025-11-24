from difflib import SequenceMatcher 

d1 = ""
d2 = ""
similarity = 0
fb = ""

def check(name):
    global d1, d2
    file = open(name, 'r')
    content = file.read()
    file.close()
    if d1 == "":
        d1 = content
    else:
        d2 = content

def checker(t1, t2):
    global similarity
    obj = SequenceMatcher(None, t1, t2)
    rv = obj.ratio()
    pv = rv * 100
    match = round(pv , 2)
    similarity = match

def remarks1(percent):
    global fb
    if percent < 10:
        fb = "completely different"
    elif percent < 20:
        fb = "somewhat similar majority portion is original"
    elif percent < 40:
        fb = "a little bit of similarity"
    elif percent < 60:
        fb = "very much same"
    elif percent < 80:
        fb = "too much identical very high copied content"
    else:
        fb = "almost totally same"

heading = "\nSimple Plagiarism Checker\n"
print(heading)

input1 = "Give the first file which needs to be checked "
first = input(input1)

input2 = "Give the other file for checking "
second = input(input2)

check(first)
check(second)

checker(d1, d2)
similarity_score = similarity

score = similarity_score
remarks1(score)
final = fb

output_line1 = f"\nSimilarity: {similarity}%"
print(output_line1)

output_line2 = f"Feedback: {fb}\n"
print(output_line2)
