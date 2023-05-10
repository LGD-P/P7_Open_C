import time


class Optimized:
    @staticmethod
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
        for element in range(len(defAction)):
            actionYield.append(
                round((defPrice[element] * (defPercentage[element] / 100)), 2))

            result.append({'Action': defAction[element],
                           'Price': defPrice[element],
                           'Percentage': defPercentage[element],
                           'Yield': actionYield[element]})

        sorted_result = sorted(result, key=lambda x: -x['Yield'])

        return sorted_result

    @staticmethod
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
            if list_of_data[element]["Price"] > 0.0 and spent + list_of_data[element]["Price"] <= max_investment:
                spent += list_of_data[element]["Price"]
                benefit += list_of_data[element]["Yield"]
                action_to_buy.append(list_of_data[element]["Action"])
        execution_time = round(time.time() - start_time)
        if execution_time < 1:
            execution_time = "Moins d'une Seconde"
        return spent, action_to_buy, round(benefit, 2), execution_time
