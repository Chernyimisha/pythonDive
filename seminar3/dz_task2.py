text = 'Iterates over the response data.  When stream=True is set on the ' \
       'request, this avoids reading the content at once into memory for' \
       'large responses.  The chunk size is the number of bytes it should' \
       'read into memory.  This is not necessarily the length of each item' \
       'returned as decoding can take place. chunk_size must be of type int ' \
       'or None. A value of None will function differently depending on the value ' \
       'of `stream`. stream=True will read data as its arrives in whatever size the' \
       'chunks are received. If stream=False, data is returned as a single chunk. ' \
       'If decode_unicode is True, content will be decoded using the best ' \
       'available encoding based on the response. 89'

for element in text:
    if not element.isalnum() and element != ' ' and element != '`':
        text = text.replace(element, "")
text = text.replace('`', ' ')
text_split = text.lower().split()
res_dict = {}
for element in text_split:
    if element.isalpha():
        res_dict[element] = res_dict.get(element, 0) + 1
print(res_dict)
keys = sorted((set(res_dict.keys())), reverse=True)
values = sorted(set(res_dict.values()), reverse=True)
print(keys)
print(values)
res_list = []
new_dict = {}
for key in keys:
    for item, value in res_dict.items():
        if item == key:
            new_dict[item] = value
print(new_dict)
max_counter = 10
for value in values:
    for item, val in new_dict.items():
        if max_counter > 0 and val == value:
            res_list.append((item, val))
            max_counter -= 1

print(res_list)


