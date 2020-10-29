# import pandas as pd
# import os
#
#
# def DataStore(softskills, workplace, min_salary, fair_salary, max_salary, wish_salary):
#     if os.path.isfile("user_data.xlsx"):
#         df = pd.read_excel("user_data.xlsx")
#         df.append([softskills, workplace, min_salary, fair_salary, max_salary, wish_salary])
#         df.to_excel("user_data.xlsx", index=False)
#     else:
#         df = pd.DataFrame([softskills, workplace, min_salary, fair_salary, max_salary, wish_salary],
#                           columns=["softskills", "workplace", "min_salary", "fair_salary", "max_salary",
#                                    "wish_salary"])
#         df.to_excel("user_data.xlsx", index=False)
