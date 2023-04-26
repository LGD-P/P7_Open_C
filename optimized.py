

from class_files.data_reader_class import Reader
from class_files.optimized_class import Optimized


def main():
    """This main function, from data reader and optimized class
    will excecute optimized glouton algorithm for  dataset1 and dataset2
    and max invest of 500€.

    Returns:
        str: message with result
    """
    INVESTMENT = 500
    data_set_list = ["data/dataset1_Python+P7.csv",
                     "data/dataset2_Python+P7.csv"]

    index = 0
    for set in data_set_list:
        index += 1
        dfAction, dfPrice, dfPercentage = Reader.return_price_action_percentage(
            set, "name", "price", "profit")
        dict_with_yield1 = Optimized.creat_dict_with_yield(
            dfPrice, dfPercentage, dfAction)

        amount_invest, action_list, benefit, execution_time = Optimized.algo_glouton(
            INVESTMENT, dict_with_yield1)

        print(f"Pour le dataset{index}:")
        Reader.display_result(execution_time, amount_invest,
                              benefit, action_list)


if __name__ == "__main__":

    main()
