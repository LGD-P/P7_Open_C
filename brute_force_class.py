class BruteForce:
    @staticmethod
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

    @staticmethod
    def all_possibilities_for_max_buy(binary_p, action_cost, action_profit, MAX_COST):
        """This method return all data possibility
        from each data_lists concerned

        Args:
            binary_p (list): each binary possibilities
            action_cost (list): action list
            action_profit (list): profit list
            MAX_COST (int): Max user investment

        Returns:
            lists: action cost - profit - binary list compared to investment
        """
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

    @staticmethod
    def determine_best_choice(max_profit):
        """This method get the best profit index to be used
        in each list concerned (action name and action cost)

        Args:
            max_profit (list): to get max()

        Returns:
            int: best index for each list
        """
        best_index = max_profit.index(max(max_profit))
        return best_index

    @staticmethod
    def determine_best_action_name(index, binary_list, action_name_list):
        """This method return best action name investment

        Args:
            index (int): best index
            binary_list (list): binary list using max investment
            action_name_list (list): actions name list

        Returns:
            list: best action name list to invest with
        """
        best_action_names = []
        for action_name in binary_list[index]:
            best_action_names.append(action_name_list[action_name[0]])
        return best_action_names
