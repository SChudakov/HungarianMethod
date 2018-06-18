from hm_table import HMTable

line_end = '\n'


def input_hm_table(string_table):
    spending_matrix = [list(map(float, s.split())) for s in string_table.split(line_end)]
    result = HMTable(spending_matrix)
    return result
