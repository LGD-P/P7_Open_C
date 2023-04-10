import pandas as pd


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
            except ValueError:
                list_from_culumn.append(element)
        return list_from_culumn
