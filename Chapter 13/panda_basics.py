import pandas as pd

data={"Name":["Motu","Patlu","Chotu","Totu"],
      "Age":[12,45,14,67],
      "Salary":[234,125,357,674]}
df=pd.DataFrame(data)
print(df)
# hotel_data=pd.read_csv("D:/vscode/Python__/Files/hotel_booking.csv")
# print(hotel_data)
testing = pd.read_excel("D:/Data Analyst/Testing.xlsx")
# print(testing)
print(testing.info())
print(testing.describe())