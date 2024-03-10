a = input("Enter any word or sentence or number with charactor : ")
vowel = "aeiouAEIOU"
count = 0
for i in a:
    if (i in vowel):
        print(i,end=",")
        count+=1
print()
print("Number of the Vowel in ",a,": ",count)