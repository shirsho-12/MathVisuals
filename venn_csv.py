import csv
from matplotlib_venn import venn3
import matplotlib.pyplot as plt
from sympy import FiniteSet


# Creating a CSV file
def create_file():
    from random import randint
    with open('sports.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['StudentID', 'Football', 'Others'])
        for i in range(1, 21):
            writer.writerow([str(i), str(randint(0, 1)), str(randint(0, 1))])


def get_sets():
    with open('sports.csv') as file:
        reader = csv.reader(file)
        header_row = next(reader)
        football, other, all_ids = [], [], []
        for row in reader:
            # print(row)

            student_id = int(row[0])
            play_football = int(row[1])
            play_other = int(row[2])
            all_ids.append(student_id)
            # print(student_id, play_football, play_other)
            if play_football == 1:
                football.append(student_id)
            if play_other == 1:
                other.append(student_id)
            # print(football, other)
        return all_ids, football, other


def draw_venn():
    arr_universal, arr_1, arr_2 = get_sets()
    sets = [FiniteSet(*arr_universal) ,FiniteSet(*arr_1), FiniteSet(*arr_2)]
    venn3(subsets=sets, set_colors=('w', 'r', 'b'), set_labels=('', 'Football', 'Other Sports'))
    plt.show()
    # plt.savefig('students_play_set.png')


if __name__ == '__main__':
    # create_file()
    draw_venn()

