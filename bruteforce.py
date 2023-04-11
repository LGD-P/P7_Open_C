from data_reader_class import Reader
from brute_force_class import BruteForce

df = Reader.csv_reader("actions.csv")

INVESTMENT = 500

dfAction = Reader.creat_list_from_culumn(df, "Actions #")
dfPrice = Reader.creat_list_from_culumn(df, 'Coût par action (en euros)')
dfPercentage = Reader.creat_list_from_culumn(df, "Bénéfice\xa0(après 2 ans)")

binary_possibilities = BruteForce.creat_binary_possibilities(dfPrice)
max_cost_list, max_profit_list, cleaned_possibilities = BruteForce.all_possibilities_for_max_buy(
    binary_possibilities, dfPrice, dfPercentage, INVESTMENT)

best_index = BruteForce.determine_best_choice(max_profit_list)

best_comb = cleaned_possibilities[best_index]
best_cost = max_cost_list[best_index]
best_profit = max_profit_list[best_index]


if __name__ == '__main__':

    print(
        " - La meilleur combinaison d'Actions pour un investissement maximum de 500€ est: \n\n"
        f" - {BruteForce.determine_best_action_name(best_index, cleaned_possibilities, dfAction)}\n"
        f" - Pour un coût de {best_cost} €\n - Et une retabilité de {best_profit} € / 2ans")
