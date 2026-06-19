txt = 'Data,Science,Machine,Learning'
txtSplit = txt.split(',')
print("Print the list:",txtSplit)

x = txtSplit[1]
print("Print the second element:",x)

sLength = len(txtSplit)
print("The total number of elements:",sLength)

txtJoin = '->'.join(txtSplit)
print("Joined String:",txtJoin)