
from rich.console import Console


from class_files.data_reader_class import Reader
from class_files.optimized_class import Optimized

c = Console()


def main():
    INVESTMENT = 500
    dfAction1, dfPrice1, dfPercentage1 = Reader.return_price_action_percentage(
        "data/dataset1_Python+P7.csv", "name", "price", "profit")
    dfAction2, dfPrice2, dfPercentage2 = Reader.return_price_action_percentage(
        "data/dataset2_Python+P7.csv", "name", "price", "profit")

    dict_with_yield1 = Optimized.creat_dict_with_yield(
        dfPrice1, dfPercentage1, dfAction1)

    dict_with_yield2 = Optimized.creat_dict_with_yield(
        dfPrice2, dfPercentage2, dfAction2)

    amount_invest1, action_list1, benefit1, execution_time1 = Optimized.algo_glouton(
        INVESTMENT, dict_with_yield1)

    amount_invest2, action_list2, benefit2, execution_time2 = Optimized.algo_glouton(
        INVESTMENT, dict_with_yield2)

    return amount_invest1, action_list1, benefit1, execution_time1, \
        amount_invest2, action_list2, benefit2, execution_time2


if __name__ == "__main__":

    amount_invest1, action_list1, benefit1, execution_time1, \
        amount_invest2, action_list2, benefit2, execution_time2 = main()

    print("Pour le dataset1:")
    Reader.display_result(execution_time1, amount_invest1,
                          benefit1, action_list1)
    print("")
    print("Pour le dataset2:")
    Reader.display_result(execution_time2, amount_invest2,
                          benefit2, action_list2)
