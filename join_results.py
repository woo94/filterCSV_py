import _io
import time


def concat_rows(input_file: _io.TextIOWrapper, output_file: _io.TextIOWrapper, concat_size: int):
    counter = 0
    concat_list = []

    for line in input_file:
        counter = counter + 1
        value_list = [int(x) for x in line.split(',')]

        if counter != concat_size:
            concat_list += value_list

        else:
            output_file.write(','.join(list(map(str, concat_list))))
            output_file.write('\n')
            concat_list.clear()
            counter = 0

    output_file.write(','.join(list(map(str, concat_list))))


with open("./output/process_x.csv", "r") as process_x:
    with open("./output/process_y.csv", "r") as process_y:
        with open("./output/process_x_10.csv", "w") as process_x_10:
            with open("./output/process_y_10.csv", "w") as process_y_10:
                start = time.time()

                concat_rows(process_x, process_x_10, 10)
                concat_rows(process_y, process_y_10, 10)

                end = time.time()

                print(end-start, "seconds")
