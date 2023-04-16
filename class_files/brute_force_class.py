class BruteForce:
    @staticmethod
    def brute_force_to_best_choice(max_investment, action_cost_list, action_profit, action_name_list):
        """This function calculate each combinations possibilies in binary,
        then creat a tuple with index and possibilities. During the loop each combination
        is compared to precedent and actualised if it's a better choice.

        Args:
            action_cost_list (list): list of action cost
            action_profit (list): list of action name
            action_name_list (list): list of action name


        Returns:
            int and list: list of best action choice, int(best profit_sum),
            int(best_cost_sum)
        """

        n_comb = 2 ** (len(action_cost_list))
        best_cost, best_profit, best_action_list = 0, 0, []

        for possibilities in range(1, n_comb):
            cost_sum, profit_sum, combination = 0, 0, []
            bin_comb = list(enumerate(reversed(bin(possibilities)[2:])))
            for index in bin_comb:
                if index[1] == "1":
                    cost_sum += int(action_cost_list[index[0]])
                    profit_sum += int(action_cost_list[index[0]]) * \
                        int(action_profit[index[0]]) / 100
                    combination.append(action_name_list[index[0]])

            if cost_sum < max_investment and profit_sum > best_profit:
                best_cost = cost_sum
                best_profit = profit_sum
                best_action_list = combination

        return best_cost, best_profit, best_action_list
