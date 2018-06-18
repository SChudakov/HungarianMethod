import numpy as np

if __name__ == "__main__":

    print(np.array([[0, 0], [0, 0]]).__eq__(np.zeros((2, 2))))
    # print(np.empty(shape=[2, 2], dtype=str))

    # matrix = np.arange(1, 10).reshape(3, 3)
    # print(np.arange(9))
    # for x in np.nditer(matrix):
    #     print(x)

    # min_by_rows = matrix.min(1)
    # matrix -= min_by_rows.transpose()
    # min_by_columns = matrix.min(0)
    # matrix -= min_by_columns
    # print(matrix)
