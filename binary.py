

action_cost = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
action_profit = [5, 8, 10]
MAX_COST = 17

best_comb = []
best_profit = 0
best_cost = 0


def creat_binary_possibiliies(action_cost_list):
    """This function calculate each combinations possibilies in binary, 
    then creat a tuple with index and possibilities. Store result in list
    Args:
        action_cost_list (list): actions price

    Returns:
        list: (action price index, binary avalability)
    """
    n_comb = 2 ** (len(action_cost_list))
    bin_combination_available = []
    for possibilities in range(1, n_comb):
        bin_comb = list(enumerate(reversed(bin(possibilities)[2:])))
        bin_combination_available.append(bin_comb)
    return bin_combination_available


def creat_action_price_possibilities(binary_availability):
    """This function uses creat_binary_possibiliies() to get back 
    the price of each actions possibilites in list

    Args:
        binary_availability (list): list generate from creat_binary_possibiliies()

    Returns:
        list: list of action price
    """

    price_combination_available = []
    for comb in binary_availability:
        price_choice_available = []
        for el in comb:
            if el[1] == "1":
                price_choice_available.append(action_cost[el[0]])
        price_combination_available.append(price_choice_available)

    return price_combination_available


binary_possibilities = creat_binary_possibiliies(action_cost)

action_price_possibilities = creat_action_price_possibilities(
    binary_possibilities)
