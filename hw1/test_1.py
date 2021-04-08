'''
测试训练资料的程序
'''
import csv
import numpy as np
path = '../data/covid.train.csv'
with open(path, 'r') as fp:
    data = list(csv.reader(fp))
    # print("type(csv.reader(fp)):", csv.reader(fp))
    # print("len(data):", len(data))
    # print("type(data):", type(data))
    # print("len(data[1:]):", len(data[1:]))
    test = np.array(data)
    np.savetxt("test.txt", test, delimiter=" ", fmt="%s")
    # print("test.shape:", test.shape)
    # print("test:", test)
    a = np.array(data[1:])
    b = a[:, 1:]
    np.savetxt("b.txt", b, delimiter=" ", fmt="%s")
    # print("type(a):", type(a))
    print("a:", a)
    np.savetxt("a.txt", a, delimiter=" ", fmt="%s")
    # np.savetxt("test.txt", a, newline=" ")
    # np.save("test.npy", a)
    # with open('test.txt', 'w') as f:
        # for row in a:
            # np.savetxt(f, row, delimiter=',', fmt='%s')
    print("b.shape:", b.shape)
    print("a.shape:", a.shape)
    data = np.array(data[1:])[:, 1:].astype(float)