fname = input("Enter file name: ")
if len(fname) < 1:
    fname = "mbox-short.txt"

fh = open(fname)
words = list()
dictionary = dict()

for i in fh:
    i = i.rstrip()
    if i.startswith('From '):
        words = i.split()
        desired_word = words[1]
        dictionary[desired_word] = dictionary.get(desired_word, 0) + 1
    else:
        continue
# print(dictionary)

v_list = list()
temp_v = 0
max_v = 0
max_k = ""
for k,v in dictionary.items():
    if temp_v < v:
        max_v = v
        temp_v = max_v
        max_k = k
    else:
        continue
print(max_k, max_v)
