
action_name_list = ["Action-1", "Action-2", "Action-3", "Action-4", "Action-5",
                    "Action-6", "Action-7", "Action-8", "Action-9", "Action-10",
                    "Action-11", "Action-12", "Action-13", "Action-14", "Action-15",
                    "Action-16", "Action-17", "Action-18 ", "Action-19", "Action-20"]
action_cost = [20, 30, 50, 70, 60, 80, 22, 26, 48,
               34, 42, 110, 38, 14, 18, 8, 4, 10, 24, 114]
action_profit = [5, 10, 15, 20, 17, 25, 7, 11,
                 13, 27, 17, 9, 23, 1, 3, 8, 12, 14, 21, 18]
MAX_COST = 500


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


# la contrainte du max dès le brut force à implémenter dans max_buy


binary_possibilities = creat_binary_possibilities(action_cost)


def all_possibilities_for_max_buy(binary_p):

    combination_cost = []
    combination_profit = []
    cleaned_possibilities = []

    for combination in binary_p:
        cost_sum = 0
        profit_sum = 0
        for index in combination:
            if index[1] == "1":
                cost_sum += int(action_cost[index[0]])
                profit_sum += int(action_cost[index[0]]) * \
                    int(action_profit[index[0]]) / 100
        if cost_sum < MAX_COST:
            combination_cost.append(cost_sum)
            combination_profit.append(profit_sum)
            cleaned_possibilities.append(combination)

    return combination_cost, combination_profit, cleaned_possibilities


max_cost_list, max_profit_list, cleaned_possibilities = all_possibilities_for_max_buy(
    binary_possibilities)


def determine_best_choice(max_profit):
    best_index = max_profit.index(max(max_profit))
    return best_index


def determine_best_action_name(index, binary_list, action_name_list):
    best_action_names = []
    for action_name in binary_list[index]:
        best_action_names.append(action_name_list[action_name[0]])
    return best_action_names


best_index = determine_best_choice(max_profit_list)

best_comb = cleaned_possibilities[best_index]
best_cost = max_cost_list[best_index]
best_profit = max_profit_list[best_index]


print(
    " - La meilleur combinaison est : "
    f"{determine_best_action_name(best_index, cleaned_possibilities, action_name_list)}\n"
    f" - Pour un coût de {best_cost} €\n - Et une retabilité de {best_profit} € / 2ans")
