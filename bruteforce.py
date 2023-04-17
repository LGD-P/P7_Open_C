
import time

from class_files.data_reader_class import Reader
from class_files.brute_force_class import BruteForce


def main():
    """This main function, from data reader and brute force class
    will excecute brute force algorithm for a dataset of 20 actions
    and max invest of 500€.

    Returns:
        str: message with result
    """
    INVESTMENT = 500

    dfAction, dfPrice, dfPercentage = Reader.return_price_action_percentage(
        "data/actions.csv", "Actions #", "Coût par action (en euros)", "Bénéfice\xa0(après 2 ans)")

    start_time = time.time()

    best_price, best_profit, action_name_list = BruteForce.brute_force_to_best_choice(
        INVESTMENT, dfPrice, dfPercentage, dfAction)

    end_time = time.time() - start_time
    if end_time > 1:
        end_time = round(end_time, 2)

    return end_time, best_price, best_profit, action_name_list


if __name__ == '__main__':
    execution_duration, best_price, best_profit, action_name_list = main()
    Reader.display_result(execution_duration, best_price,
                          best_profit, action_name_list)
