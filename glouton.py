from rich.console import Console
import time

from data_reader_class import Reader


c = Console()


INVESTMENT = 500

df = Reader.csv_reader("actions.csv")
dfAction = Reader.creat_list_from_culumn(df, "Actions #")
dfPrice = Reader.creat_list_from_culumn(df, 'Coût par action (en euros)')
dfPercentage = Reader.creat_list_from_culumn(
    df, "Bénéfice\xa0(après 2 ans)")


def creat_dict_with_yield(defPrice, defPercentage, defAction):
    """This function creat in a list, for each action, a dictionary
    with action name, price, percentage, and yield

    Args:
        defPrice (list): price list
        defPercentage (list): percentage list
        defAction (list): action name list

    Returns:
        _type_: _description_
    """
    result = []
    actionYield = []
    index = -1
    for element in range(len(defAction)):
        index += 1
        actionYield.append(
            round((defPrice[element] * (defPercentage[element] / 100)), 2))
        result.append({'Action': defAction[index],
                       'Price': defPrice[index],
                       'Percentage': dfPercentage[index],
                       'Yield': actionYield[index]})

    sorted_result = sorted(result, key=lambda x: -x['Yield'])

    return sorted_result


dict_with_yield = creat_dict_with_yield(dfPrice, dfPercentage, dfAction)


def algo_glouton(max_investment, list_of_data):
    """This function implemant glouton algoritm to a
    a list of dictionary.

    Args:
        max_investment (int): max user investment
        list_of_data (dict list): list of dict for each data action name price percentage and yield

    Returns:
        Best Invest : spent as int, action_to_buy as list, benefit as flaot, execution time
    """
    spent = 0
    action_to_buy = []
    benefit = 0
    start_time = time.time()
    for element in range(len(list_of_data)):
        if spent + list_of_data[element]["Price"] <= max_investment:
            spent += list_of_data[element]["Price"]
            benefit += list_of_data[element]["Yield"]
            action_to_buy.append(list_of_data[element]["Action"])
    execution_time = round(time.time() - start_time)
    if execution_time < 1:
        execution_time = "Moins d'une Seconde"
    return spent, action_to_buy, round(benefit, 2), execution_time


amount_invest, action_list, benefit, execution_time = algo_glouton(
    INVESTMENT, dict_with_yield)


print(amount_invest, action_list, benefit, execution_time)
