fruits=["banana","apple","cherry","grapes"]
print(fruits)
for x in fruits:
    print(x)
b="Hello world"
for x in b:
    print(x)
print(fruits)
print("Break statement")
for x in fruits:
    print(x)
    if x=="cherry":
        break
print("Continue Statement")
for x in fruits:
    print(x)
    if x=="cherry":
        continue