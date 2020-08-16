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


def is_bangalore_call(phone_number):
    return phone_number[0:5] == "(080)"


def is_fixed_number(phone_number):
    return phone_number[0] == "("


def is_mobile_phone(phone_number):
    return " " in phone_number.strip()


def parse_area_code(phone_number):
    if is_fixed_number(phone_number):
        return phone_number.split(')')[0] + ')'
    elif is_mobile_phone(phone_number):
        return phone_number[0:4]
    else:
        return phone_number[0:3]


called_set = set()
total_call = 0
answerer_in_bangalore = 0

for call in calls:
    caller, answerer = call[0], call[1]

    if is_bangalore_call(caller):
        total_call += 1
        called_set.add(parse_area_code(answerer))
        if is_bangalore_call(answerer):
            answerer_in_bangalore += 1

called_list = sorted(called_set)
print("The numbers called by people in Bangalore have codes:")
for number in called_list:
    print(number)


percent = round(100.0 * answerer_in_bangalore / total_call, 2)
print("{} percent of calls from fixed lines in Bangalore are calls to other fixed lines in Bangalore.".format(percent))

"""
TASK 3:
(080) is the area code for fixed line telephones in Bangalore.
Fixed line numbers include parentheses, so Bangalore numbers
have the form (080)xxxxxxx.)

Part A: Find all of the area codes and mobile prefixes called by people
in Bangalore.
 - Fixed lines start with an area code enclosed in brackets. The area
   codes vary in length but always begin with 0.
 - Mobile numbers have no parentheses, but have a space in the middle
   of the number to help readability. The prefix of a mobile number
   is its first four digits, and they always start with 7, 8 or 9.
 - Telemarketers' numbers have no parentheses or space, but they start
   with the area code 140.

Print the answer as part of a message:
"The numbers called by people in Bangalore have codes:"
 <list of codes>
The list of codes should be print out one per line in lexicographic order with no duplicates.

Part B: What percentage of calls from fixed lines in Bangalore are made
to fixed lines also in Bangalore? In other words, of all the calls made
from a number starting with "(080)", what percentage of these calls
were made to a number also starting with "(080)"?

Print the answer as a part of a message::
"<percentage> percent of calls from fixed lines in Bangalore are calls
to other fixed lines in Bangalore."
The percentage should have 2 decimal digits
"""
