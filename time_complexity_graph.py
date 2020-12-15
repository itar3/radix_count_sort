def time_radix_sort():
    from timeit import default_timer as timer
    import random
    import long_file

    f1 = open("./output_task2.csv", 'w')
    bases = [2**1,2**5,2**10,100000, 200000,2**22,2**23]
    output = []
    test_data = [random.randint(1,(2**64)-1) for _ in range(100000)]
    for base in bases:
        start = timer()
        long_file.radix_sort(test_data, base)
        end = timer()
        output.append((base, end-start))
    print(output)
    for i in range(len(output)):
        s = str(output[i][0]) + ", " + str(output[i][1]) + '\n'
        f1.write(s)
    f1.close()

time_radix_sort()


def plot_csv(csv_file, title=None):
    import numpy as np
    import matplotlib.pyplot as plt
    with open(csv_file) as csv_file:
        base, time = np.loadtxt(csv_file, delimiter=',', unpack=True)
        # Set up the figure and axes
        plt.scatter(base, time)
        plt.plot(base,time, label = 'time to base correlation')
        plt.xlabel('base used')
        plt.ylabel('time taken (s)')
        plt.legend()
        plt.show()

plot_csv('output_task2.csv')