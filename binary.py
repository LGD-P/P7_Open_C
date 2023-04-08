

action_cost = [1, 2, 3, 4]
action_profit = [5, 8, 10, 4]
MAX_COST = 8

best_comb = []
best_profit = 0
best_cost = 0


def creat_binary_possibilities(action_cost_list):
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


def creat_action_price_possibilities(binary_availability, action_cost_list, action_profit):
    """This function uses creat_binary_possibilities() to get back
    the price of each actions possibilites in list

    Args:
        binary_availability (list): list generate from creat_binary_possibiliies()

    Returns:
        list: list of action price
    """

    price_combination_available = []
    sum_cost_for_combination = []
    profit_for_combination = []
    for comb in binary_availability:
        price_choice_available = []
        cost_sum = 0
        profit_sum = 0
        for el in comb:
            if el[1] == "1":
                cost_sum += int(action_cost_list[el[0]])
                price_choice_available.append(action_cost_list[el[0]])
                profit_sum += int(action_cost_list[el[0]]) * \
                    int(action_profit[el[0]]) / 100

        price_combination_available.append(price_choice_available)
        sum_cost_for_combination.append(cost_sum)
        profit_for_combination.append(profit_sum)

    return price_combination_available, sum_cost_for_combination, profit_for_combination


def calculate_possibilities_for_invest_list(max_invest, all_price_possibility):
    """This function calculation all combination of stock purchase
    with a max investment.

    Args:
        max_invest (int): fixed by user
        all_price_possibility (list): list of all combination without price limit

    Returns:
        list: list of combination available with a max price
    """
    all_possibility = []
    for possibility in all_price_possibility:
        wallet = 0
        investment = []
        for action in possibility:
            wallet += action
            if wallet > max_invest:
                wallet -= action
            else:
                investment.append(action)
        if investment not in all_possibility:
            all_possibility.append(investment)
    return all_possibility


binary_possibilities = creat_binary_possibilities(action_cost)

action_price_possibilities, max_buy, max_profit = creat_action_price_possibilities(
    binary_possibilities, action_cost, action_profit)

possibilities = calculate_possibilities_for_invest_list(
    MAX_COST, action_price_possibilities)

print(binary_possibilities)
print(action_price_possibilities)
print(max_buy)
print(max_profit)
