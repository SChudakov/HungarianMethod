class HMTable:
    empty_line = ''

    sharp_marking = "#"
    ampersand_marking = "&"

    star_marking = "*"
    cross_out_marking = "^"

    def __init__(self, spending_matrix):
        self.spending_matrix = spending_matrix
        self.spending_matrix_size = len(spending_matrix)

        self.zero_elements_marking = [[''] * len(spending_matrix) for x in range(len(spending_matrix))]

        self.rows_sharp_marking = [''] * len(spending_matrix)
        self.columns_sharp_marking = [''] * len(spending_matrix)

        self.rows_ampersand_marking = [''] * len(spending_matrix)
        self.columns_ampersand_marking = [''] * len(spending_matrix)

    def mark_zero(self, row, column):
        self.zero_elements_marking[row][column] = HMTable.star_marking

    def is_marked_zero(self, row, column):
        return self.spending_matrix[row][column] == 0 and self.zero_elements_marking[row][
            column] == HMTable.star_marking

    def cross_out_zero(self, row, column):
        self.zero_elements_marking[row][column] = HMTable.cross_out_marking

    def is_crossed_out_zero(self, row, column):
        return self.spending_matrix[row][column] == 0 and self.zero_elements_marking[row][
            column] == HMTable.cross_out_marking

    def zero_has_no_marking(self, row, column):
        return self.spending_matrix[row][column] == 0 and not (self.is_marked_zero(row, column)) and not (
            self.is_crossed_out_zero(row, column))

    def mark_row_sharp(self, row):
        self.rows_sharp_marking[row] = HMTable.sharp_marking

    def mark_row_ampersand(self, row):
        self.rows_ampersand_marking[row] = HMTable.ampersand_marking

    def row_marked_sharp(self, row):
        return self.rows_sharp_marking[row] == HMTable.sharp_marking

    def row_marked_ampersand(self, row):
        return self.rows_ampersand_marking[row] == HMTable.ampersand_marking

    def mark_column_sharp(self, column):
        self.columns_sharp_marking[column] = HMTable.sharp_marking

    def mark_column_ampersand(self, column):
        self.columns_ampersand_marking[column] = HMTable.ampersand_marking

    def column_marked_sharp(self, column):
        return self.columns_sharp_marking[column] == HMTable.sharp_marking

    def column_marked_ampersand(self, column):
        return self.columns_ampersand_marking[column] == HMTable.ampersand_marking

    def remove_all_markings(self):
        self.zero_elements_marking = [[''] * self.spending_matrix_size for x in range(self.spending_matrix_size)]

        self.rows_sharp_marking = [''] * self.spending_matrix_size
        self.columns_sharp_marking = [''] * self.spending_matrix_size

        self.rows_ampersand_marking = [''] * self.spending_matrix_size
        self.columns_ampersand_marking = [''] * self.spending_matrix_size

    def output_table(self):
        print("spending matrix")
        print()
        print('\n'.join(map(str, self.spending_matrix)))
        print()
        print("zero elements marking")
        print()
        print('\n'.join(map(str, self.zero_elements_marking)))
        print()

        print("rows sharp marking")
        print(self.rows_sharp_marking)

        print("columns sharp marking")
        print(self.columns_sharp_marking)

        print("rows ampersand marking")
        print(self.rows_ampersand_marking)

        print("columns ampersand marking")
        print(self.columns_ampersand_marking)
