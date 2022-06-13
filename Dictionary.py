print("Enter the books: ")
stock = {'Basics of Python': 50, 'Statistical Modelling':30}
print("Original list: ",stock)
up1 = {'Basics of Python': 60}
stock.update(up1)
print("Updated list: ",stock)
remove = stock.popitem()
print("Deleted item: ",remove)
print("New List: ", stock)
stock.update({'Probabilities and Statistics':55})
print("Final List: ",stock)
