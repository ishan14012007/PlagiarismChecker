from difflib import SequenceMatcher 

def check(name):
    with open(name, 'r') as file:
        return file.read()

def checker(t1, t2):
    match = round(SequenceMatcher(None, t1, t2).ratio() * 100, 2)
    return match

def remarks1(percent):
    if percent < 10:
        return "completely different"
    elif percent < 20:
        return "barely similar, mostly original"
    elif percent < 40:
        return "a few matching parts"
    elif percent < 60:
        return "noticeable similarities"
    elif percent < 80:
        return "a lot is same"
    else:
        return "almost identical"

print("\nSimple Plagiarism Checker\n")

first = input("Enter first file name: ")
second = input("Enter second file name: ")

d1 = check(first)
d2 = check(second)

similarity = checker(d1, d2)  
remarks = remarks1(similarity)  
print(f"\nSimilarity: {similarity}%")
print(f"Feedback: {remarks}\n")