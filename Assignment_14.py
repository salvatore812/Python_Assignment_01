txt = 'Banana'
txtFind = txt.find('a')
print("Find ('a') in 'Banana':",txtFind)

txtCount = txt.count('a')
print("Count ('a') in 'Banana':",txtCount)

print(f"Starts with ('Ba') in 'Banana': {txt.startswith('Ba')} ")

print("Ends with ('na') in 'Banana':",txt.endswith('na'))

print("isdigit() in 'Banana':",txt.isdigit())

strNumber = '12345'
strWord = '123a5'
print("Is '12345' all caracters are number?\nAns:",strNumber.isdigit())
print("Is '123a5' all caracters are number?\nAns:",strWord.isdigit())