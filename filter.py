import time

start = time.time()

with open("./input/600TypeA.csv", "r") as input_data:
    with open("./output/process_y.csv", "w") as process_y:
        with open("./output/process_x.csv", "w") as process_x:
            for _ in input_data:
                line = _.strip('\n')

                # sanitize input file
                value_list = [int(x) for x in line.split(',') if x != '']

                # enumerate value_list to include index
                enumerate_value_list = list(enumerate(value_list))

                # filter value > 10
                filtered_enumerate_value_list = [x for x in enumerate_value_list if x[1] > 10]

                if len(filtered_enumerate_value_list) > 0:
                    process_x.write(','.join(list(map(lambda x: str(x[0]), filtered_enumerate_value_list))))
                    process_x.write('\n')
                    process_y.write(','.join(list(map(lambda x: str(x[1]), filtered_enumerate_value_list))))
                    process_y.write('\n')

end = time.time()

print(end-start, "seconds")
