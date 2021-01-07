"""
Read file into texts and calls.
It's ok if you don't understand how to read files
"""
import csv

with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)


def find_longest_call(call_list):
    longest_time = [None, 0]  # [phone_number, total_time]
    time_spend = {}
    for call in call_list:
        phone1 = call[0]  # incoming
        phone2 = call[1]  # answering
        spent = int(call[3])

        time_spend[phone1] = time_spend.get(phone1, 0) + spent
        time_spend[phone2] = time_spend.get(phone2, 0) + spent

        if time_spend[phone1] > longest_time[1]:
            longest_time = [phone1, time_spend[phone1]]

        if time_spend[phone2] > longest_time[1]:
            longest_time = [phone2, time_spend[phone2]]

    return longest_time


longest_call_data = find_longest_call(calls)

print("{} spent the longest time, {} seconds, on the phone during September 2016.".format(*longest_call_data))
"""
TASK 2: Which telephone number spent the longest time on the phone
during the period? Don't forget that time spent answering a call is
also time spent on the phone.
Print a message:
"<telephone number> spent the longest time, <total time> seconds, on the phone during 
September 2016.".
"""
