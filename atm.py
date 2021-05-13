# Non-uniform probability ATM where one note is preferred over another
import random
from collections import Counter


def get_note_index(probability):
    probability_count = 0
    sum_probability = []

    for p in probability:
        probability_count += p
        sum_probability.append(probability_count)
    r = random.random()
    for index, s_p in enumerate(sum_probability):
        if r <= s_p:
            return index
    return len(probability) - 1


def dispense(dollar_bills, probability):
    bill_index = get_note_index(probability)
    return dollar_bills[bill_index]


def notes(bill_value):
    dollar_bills = [1, 5, 10, 20, 50]
    probability = [1 / 8, 1 / 6, 1 / 6, 1 / 3, 2 / 3]
    dollar_notes = []
    while bill_value > 0:
        while bill_value < dollar_bills[-1]:
            del dollar_bills[-1]
            del probability[-1]
            # print(dollar_bills)
        note = dispense(dollar_bills, probability)
        bill_value -= note
        dollar_notes.append(note)
    return dollar_notes


if __name__ == '__main__':
    value = input("Enter amount to be dispensed: ")
    total_notes = notes(int(value.replace(' ', '').replace(',','')))
    bills = Counter(total_notes)
    for bill, count in sorted(bills.most_common()):
        if count > 1:
            x = "times"
        else:
            x = 'time'
        print("$"+str(bill), count, x)
        print("{0:.3f}".format(count / len(total_notes)), "$" + str(bill))
    # print(dispense([1, 5, 10, 20, 50]))
    # print(sum(bills))
