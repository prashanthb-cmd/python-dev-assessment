def filter_and_sort_evens(numbers):
    list1=[]
    for i in numbers:
        if i%2==0:
            list1.append(i)
    list1.sort()
    return list1
print(filter_and_sort_evens([3, 1, 4, 1, 5, 9, 2, 6]))

def count_character_frequency(text):
    freqtext={}
    for char in text.lower():
        if char in freqtext:
            freqtext[char]+=1
        else:
            freqtext[char]=1
    return freqtext
print(count_character_frequency("Hello World"))