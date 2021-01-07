"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv

with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

incoming_set = set()
others_set = set()

for call in calls:
    incoming_set.add(call[0])
    others_set.add(call[1])

for text in texts:
    others_set.add(text[0])
    others_set.add(text[1])

telemarketers = incoming_set - others_set

print("These numbers could be telemarketers: ")
telemarketers = sorted(telemarketers)
for i in telemarketers:
    print(i)

"""
TASK 4:
The telephone company want to identify numbers that might be doing
telephone marketing. Create a set of possible telemarketers:
these are numbers that make outgoing calls but never send texts,
receive texts or receive incoming calls.

Print a message:
"These numbers could be telemarketers: "
<list of numbers>
The list of numbers should be print out one per line in lexicographic order with no duplicates.
"""
