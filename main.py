from data_reader import Reader

df = Reader.csv_reader("actions.csv")

INVESTMENT = 500

dfAction = Reader.creat_list_from_culumn(df, "Actions #")
dfPrice = Reader.creat_list_from_culumn(df, 'Coût par action (en euros)')
dfPercentage = Reader.creat_list_from_culumn(df, "Bénéfice\xa0(après 2 ans)")
