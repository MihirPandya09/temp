import pandas as pd

data_dictionary = {
    "Age": [25, 32, 28, 45, 22, 34, 29, 40, 31, 27],
    "Salary": [50000, 64000, 58000, 72000, 48000, 61000, 59000, 70000, 62000, 53000],
    "Experience_Years": [2, 5, 3, 10, 1, 6, 4, 9, 5, 3],
    "Department": ["HR", "Tech", "Finance", "Tech", "HR", "Finance", "Tech", "HR", "Finance", "Tech"],
    "Performance_Rating": [3.2, 4.5, 3.8, 4.9, 2.9, 4.1, 4.0, 4.6, 3.9, 3.5]
}

df = pd.DataFrame(data_dictionary,columns=data_dictionary.keys())

df.to_csv('temp.csv')
    