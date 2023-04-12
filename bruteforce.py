from rich.console import Console
import time

from data_reader_class import Reader
from brute_force_class import BruteForce

c = Console()


def main():
    INVESTMENT = 500

    df = Reader.csv_reader("actions.csv")
    dfAction = Reader.creat_list_from_culumn(df, "Actions #")
    dfPrice = Reader.creat_list_from_culumn(df, 'Coût par action (en euros)')
    dfPercentage = Reader.creat_list_from_culumn(
        df, "Bénéfice\xa0(après 2 ans)")

    start_time = time.time()

    best_price, best_profit, action_name_list = BruteForce.brute_force_to_best_choice(
        INVESTMENT, dfPrice, dfPercentage, dfAction)

    end_time = time.time() - start_time

    return end_time, best_price, best_profit, action_name_list


if __name__ == '__main__':
    execution_duration, best_price, best_profit, action_name_list = main()
    c.print("[bold green3] - La meilleur combinaison d'Actions pour un investissement maximum de 500€ est:\
            \n[bold green3]")
    c.print(f"[bold yellow] - {action_name_list}\n[bold yellow]")
    c.print(
        f"[bold green3] - Pour un coût de: [bold yellow]{best_price}[bold yellow] €\n")
    c.print(
        f"[bold green3] - Et une retabilité de: [bold yellow]{round(best_profit,2)}[bold yellow] € / 2ans\n")
    c.print(
        f"[bold green3] - Le temps d'exécution de l'algoritme est de:[bold yellow] {round(execution_duration,2)} sec.")
