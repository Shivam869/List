lst=['apple','guava','mango','kiwi','banana']
print("Lenght of list",len(lst))
lst.append("papaya")
print("Append list:",lst)
lst.remove("guava")
print("Remove list:",lst)
lst.sort()
print("Sort list:",lst)
lst.reverse()
print("Reverse list:",lst)
lst=lst[:4]
print("Slice list:",lst)
lst.clear()
print("Clear list:",lst)
