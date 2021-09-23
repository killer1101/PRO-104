import csv
from collections import Counter

new_data = "whitehatjr"
data = Counter(new_data)
print(data)
new_list = data.items()
print(new_list)
new_list1 = data.values()
print(new_list1)

