import pandas as pd
from rich.console import Console

c = Console()


class Reader:
    @staticmethod
    def csv_reader(csv_file_name):
        """This method is just a .csv reader
        with pandas library

        Args:
            csv_file_name (str): "action.csv"

        Returns:
            class: pandas object readable
        """
        data_frame = pd.read_csv(csv_file_name)
        return data_frame

    @staticmethod
    def creat_list_from_culumn(df, culumn):
        """This method creat a list of data
        from .csv column choosed by user

        Args:
            culumn (str): header chooses "Action #"

        Returns:
            list: list of culumn content
        """
        list_from_culumn = []
        for element in df[culumn]:
            try:
                list_from_culumn.append(int(element.strip("%")))
            except (AttributeError, ValueError):
                list_from_culumn.append(element)
        return list_from_culumn

    @staticmethod
    def return_price_action_percentage(csv_file, action_culumn, price_culumn, percentage_culumn):
        """This methode return all array culumns in variable list

        Args:
            csv_file (path): path to csv file
            action_culumn (header): for column action name
            price_culumn (header): for column price
            percentage_culumn (header): for %/2years

        Returns:
            list: one list for each column
        """
        df = Reader.csv_reader(csv_file)
        dfAction = Reader.creat_list_from_culumn(df, action_culumn)
        dfPrice = Reader.creat_list_from_culumn(df, price_culumn)
        dfPercentage = Reader.creat_list_from_culumn(df, percentage_culumn)
        return dfAction, dfPrice, dfPercentage

    @staticmethod
    def display_result(execution_duration, best_price, best_profit, action_name_list):
        """This method make a friendly display for result

        Args:
            execution_duration (int or str): int if > 1
            best_price (int): best amount spent
            best_profit (int): best profit
            action_name_list (list): action name list
        """
        c.print("[bold green3] - La meilleur combinaison d'Actions pour un investissement maximum de 500€ est:\
                \n[bold green3]")
        c.print(f"[bold yellow] - {action_name_list}\n[bold yellow]")
        c.print(
            f"[bold green3] - Pour un coût de: [bold yellow]{best_price}[bold yellow] €\n")
        c.print(
            f"[bold green3] - Et une retabilité de: [bold yellow]{round(best_profit,2)}[bold yellow] € / 2ans\n")
        c.print(
            f"[bold green3] - Le temps d'exécution de l'algoritme est de:[bold yellow] {execution_duration} sec.")
