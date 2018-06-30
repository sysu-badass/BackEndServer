order_items = [{'a':1, 'b':2}, {'a':3, 'b':4}]
temp_item = {}
items = []
for i in order_items:
    temp_item['A'] = i['a']
    temp_item['B'] = i['b']
    items.append(dict(temp_item))

print(items)
