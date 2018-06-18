import numpy as np
import sys


def solve_hm_table(table):
    initial_spending_matrix = np.copy(table.spending_matrix)

    solving_complete = False
    iteration = 1
    subtract_min_values(table)
    while not solving_complete:
        print()
        print("ITERATION: {}".format(iteration))
        iteration += 1
        print()
        solve_to_cases(table)
        print("SOLVED TO CASES")
        table.output_table()
        print()
        solving_complete = complete_solving(table)

    return form_solution(table, initial_spending_matrix)


def subtract_min_values(table):
    # for i in range(table.spending_matrix_size):
    #     row_min_value = table.spending_matrix[i][0]
    #     for j in range(table.spending_matrix_size):
    #         if row_min_value > table.spending_matrix[i][j]:
    #             row_min_value = table.spending_matrix[i][j]
    #     for j in range(table.spending_matrix_size):
    #         table.spending_matrix[i][j] -= row_min_value

    min_by_rows = table.spending_matrix.min(1)
    table.spending_matrix -= min_by_rows.transpose()
    print("AFTER SUBTRACTING ROWS MIN VALUES")
    table.output_table()

    # for j in range(table.spending_matrix_size):
    #     column_min_value = table.spending_matrix[0][j]
    #
    #     for i in range(table.spending_matrix_size):
    #         if column_min_value > table.spending_matrix[i][j]:
    #             column_min_value = table.spending_matrix[i][j]
    #     for i in range(table.spending_matrix_size):
    #         table.spending_matrix[i][j] -= column_min_value

    min_by_columns = table.spending_matrix.min(0)
    table.spending_matrix -= min_by_columns
    print("AFTER SUBTRACTING COLUMNS MIN VALUES")
    table.output_table()


def solve_to_cases(table):
    marked_by_rows = True
    marked_by_columns = True
    marking_iteration = 1
    while marked_by_rows or marked_by_columns:
        print()
        print("MARKING INTERATION {}".format(marking_iteration))
        marking_iteration += 1
        print()
        print("MARK BY ROWS")
        marked_by_rows = mark_zeros_by_rows(table)
        print("MARK BY COLUMNS")
        marked_by_columns = mark_zeros_by_columns(table)


def mark_zeros_by_rows(table):
    zero_marked = False
    for i in range(table.spending_matrix_size):
        num_of_not_marked_zeros = 0
        for j in range(table.spending_matrix_size):
            if table.zero_has_no_marking(i, j):
                num_of_not_marked_zeros += 1
        print("ROW: {}, NUM OF NOT MARKED ZEROS: {}".format(i, num_of_not_marked_zeros))
        if num_of_not_marked_zeros == 1:
            for j in range(table.spending_matrix_size):
                if table.zero_has_no_marking(i, j):
                    table.mark_zero(i, j)
                    zero_marked = True
                    print("MARK zero at [{}][{}]".format(i, j))
                    for k in range(table.spending_matrix_size):
                        if not (k == i):
                            if table.zero_has_no_marking(k, j):
                                print("CROSS OUT zero at [{}][{}]".format(k, j))
                                table.cross_out_zero(k, j)
    return zero_marked


def mark_zeros_by_columns(table):
    zero_marked = False
    for j in range(table.spending_matrix_size):
        num_of_not_marked_zeros = 0
        for i in range(table.spending_matrix_size):
            if table.zero_has_no_marking(i, j):
                num_of_not_marked_zeros += 1
        print("COLUMN: {}, NUM OF NOT MARKED ZEROS: {}".format(j, num_of_not_marked_zeros))
        if num_of_not_marked_zeros == 1:
            for i in range(table.spending_matrix_size):
                if table.zero_has_no_marking(i, j):
                    print("MARK zero at [{}][{}]".format(i, j))
                    table.mark_zero(i, j)
                    zero_marked = True
                    for k in range(table.spending_matrix_size):
                        if not (k == j):
                            if table.zero_has_no_marking(i, k):
                                print("CROSS OUT zero at [{}][{}]".format(i, k))
                                table.cross_out_zero(i, k)
    return zero_marked


def is_first_case(table):
    for i in range(table.spending_matrix_size):
        has_marked_zero = False
        for j in range(table.spending_matrix_size):
            if table.is_marked_zero(i, j):
                has_marked_zero = True
        if not has_marked_zero:
            return False
    return True


def is_second_case(table):
    second_case_in_row = False
    for i in range(table.spending_matrix_size):
        num_of_unmarked_zeros = 0
        for j in range(table.spending_matrix_size):
            if table.zero_has_no_marking(i, j):
                num_of_unmarked_zeros += 1
        if num_of_unmarked_zeros > 1:
            second_case_in_row = True
            break

    second_case_in_column = False
    for j in range(table.spending_matrix_size):
        num_of_unmarked_zeros = 0
        for i in range(table.spending_matrix_size):
            if table.zero_has_no_marking(i, j):
                num_of_unmarked_zeros += 1
        if num_of_unmarked_zeros > 1:
            second_case_in_row = True
            break
    return second_case_in_row or second_case_in_column


def is_third_case(table):
    num_of_marked_zeros = 0
    for i in range(table.spending_matrix_size):
        for j in range(table.spending_matrix_size):
            if table.is_marked_zero(i, j):
                num_of_marked_zeros += 1

    return num_of_marked_zeros < table.spending_matrix_size


def complete_solving(table):
    if is_first_case(table):
        print()
        print("FIRST CASE")
        print()
        return True
    if is_second_case(table):
        print()
        print("SECOND CASE")
        print()
        handle_second_case(table)
        return False
    if is_third_case(table):
        print()
        print("THIRD CASE")
        print()
        handle_third_case(table)
        return False


def handle_second_case(table):
    zero_marked = False
    for i in range(table.spending_matrix_size):
        for j in range(table.spending_matrix_size):
            if table.zero_has_no_marking(i, j):
                table.mark_zero(i, j)
                zero_marked = True
                print("MARK zero at [{}][{}]".format(i, j))
                for k in range(table.spending_matrix_size):
                    if not (k == j) and table.zero_has_no_marking(i, k):
                        table.cross_out_zero(i, k)
                        print("CROSS OUT zero at [{}][{}]".format(i, k))
                    if not (k == i) and table.zero_has_no_marking(k, j):
                        table.cross_out_zero(k, j)
                        print("CROSS OUT zero at [{}][{}]".format(k, j))
                break
        if zero_marked:
            break


def handle_third_case(table):
    mark_rows_without_assignments(table)
    print("ROWS WITHOUT ASSIGNMENTS MARKED")
    table.output_table()
    while True:
        column_marked = mark_columns_with_crossed_out_zeros_in_marked_rows(table)
        row_marked = mark_rows_with_assignments_in_not_marked_columns(table)
        if not column_marked and not row_marked:
            break
    print("MARKING ROWS AND COLUMNS COMPLETE")
    table.output_table()

    for i in range(table.spending_matrix_size):
        if not table.row_marked_sharp(i):
            table.mark_row_ampersand(i)
        if table.column_marked_sharp(i):
            table.mark_column_ampersand(i)
    print("ROWS AND COLUMNS CROSSED OUT")
    table.output_table()

    min_element = min_element_in_non_crossed_out_rows_amd_columns(table)
    print()
    print("MIN ELEMENTS: {}".format(min_element))
    print()

    for i in range(table.spending_matrix_size):
        if not table.row_marked_ampersand(i):
            for j in range(table.spending_matrix_size):
                table.spending_matrix[i][j] -= min_element

    for j in range(table.spending_matrix_size):
        if table.column_marked_ampersand(j):
            for i in range(table.spending_matrix_size):
                table.spending_matrix[i][j] += min_element
    print("MIN ELEMENT SUBTRACTED")
    table.output_table()
    print()
    table.remove_all_markings()
    print("ALL MARKINGS REMOVED")
    table.output_table()
    print()


def mark_rows_without_assignments(table):
    for i in range(table.spending_matrix_size):
        has_assignment = False
        for j in range(table.spending_matrix_size):
            if table.is_marked_zero(i, j):
                has_assignment = True
        if not has_assignment:
            table.mark_row_sharp(i)


def mark_columns_with_crossed_out_zeros_in_marked_rows(table):
    marked = False
    for i in range(table.spending_matrix_size):
        for j in range(table.spending_matrix_size):
            if table.is_crossed_out_zero(i, j) and table.row_marked_sharp(i) and not table.column_marked_sharp(j):
                table.mark_column_sharp(j)
                marked = True
    return marked


def mark_rows_with_assignments_in_not_marked_columns(table):
    marked = False
    for i in range(table.spending_matrix_size):
        for j in range(table.spending_matrix_size):
            if table.is_marked_zero(i, j) and table.column_marked_sharp(j) and not table.row_marked_sharp(i):
                table.mark_row_sharp(i)
                marked = True
    return marked


def min_element_in_non_crossed_out_rows_amd_columns(table):
    result = sys.maxsize

    for i in range(table.spending_matrix_size):
        for j in range(table.spending_matrix_size):
            if not table.row_marked_ampersand(i) and not table.column_marked_ampersand(j) \
                    and table.spending_matrix[i][j] < result:
                result = table.spending_matrix[i][j]

    return result


def form_solution(table, initial_spending_matrix):
    appointments_matrix = np.zeros(
        shape=[table.spending_matrix_size, table.spending_matrix_size],
        dtype=np.int
    )
    for i in range(table.spending_matrix_size):
        for j in range(table.spending_matrix_size):
            if table.is_marked_zero(i, j):
                appointments_matrix[i][j] = 1

    print("ASSIGNMENT MATRIX")
    print("\n".join(map(str, appointments_matrix)))

    function_value = np.sum(initial_spending_matrix * appointments_matrix)
    print("FUNCTION VALUE {}".format(function_value))

    return appointments_matrix, function_value
