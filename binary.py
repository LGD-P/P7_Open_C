
action_name_list = ["Une", "Deux", "Trois", "Quatre"]
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


print(cleaned_possibilities)
print("*" * 20)
print(max_cost_list)
print("*" * 20)
print(max_profit_list)


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
    f" - Pour un coût de {best_cost} \n - Et une retabilité de {best_profit}")
