# import pandas as pd
# import csv
# from datetime import datetime
# from data_entry import get_amount,get_category,get_date,get_description
# import matplotlib.pyplot as plt

# class CSV:
#     CSV_FILE="finance_data.csv"
#     COLUMNS=["date","amount","category","description"]
#     FORMAT= "%d-%m-%Y"

#     @classmethod
#     def initialize_csv(cls):
#         try:
#             pd.read_csv(cls.CSV_FILE)
#         except FileNotFoundError:
#             df=pd.DataFrame(columns=cls.COLUMNS)
#             df.to_csv(cls.CSV_FILE,index=False)

#     @classmethod
#     def add_entry(cls,date,amount,category,description):
#         new_entry={
#             "date":date,
#             "amount":amount,
#             "category":category,
#             "description":description
#         }

#         with open(cls.CSV_FILE,"a",newline="") as csvfile:
#             writer=csv.DictWriter(csvfile,fieldnames=cls.COLUMNS)
#             writer.writerow(new_entry)
#             print("data added sucessfully......")


#     @classmethod
#     def get_transcation(cls,start_date,end_date):
#         df=pd. read_csv(cls.CSV_FILE)
#         df["date"]=pd.to_datetime(df["date"],format=CSV.FORMAT)
#         start_date=datetime.strptime(start_date,CSV.FORMAT)
#         end_date=datetime.strptime(end_date,CSV.FORMAT)


#         mask=(df["date"] >= start_date) & (df["date"] <= end_date)
#         filtered_df=df.loc[mask]

#         if filtered_df.empty:
#             print("No transctaion is found in the  given date range")

#         else:
#             print(f"Transcations from {start_date.strftime(CSV.FORMAT)}  to  {end_date.strftime(CSV.FORMAT)} ")
#             print(filtered_df.to_string(
#                 index=False,formatters={"date":lambda x: x.strftime(CSV.FORMAT)}))
            
#             total_amount=filtered_df[filtered_df["category"]=="Income"]["amount"].sum()
#             total_expense=filtered_df[filtered_df["category"]=="Expense"]["amount"].sum()
#             print("\nsummary :")
#             print(f"Total Income  : ${total_amount:.2f}")
#             print(f"total expense :${total_expense:.2f}")
#             print(f"Net Savings: ${(total_amount-total_expense):.2f}")
#         return  filtered_df

# def add():
#     CSV.initialize_csv()
#     date=get_date(
#         "enter the date of the trabscations (dd-mm-yy) or enter for todays date :",
#         allow_default=True,

#     )
#     amount=get_amount()
#     category=get_category()
#     description=get_description()
#     CSV.add_entry(date,amount,category,description)

# def plot_transcation(df):
#     # Ensure the amount column is numeric
#     df["amount"] = pd.to_numeric(df["amount"], errors="coerce")
    
#     df.set_index("date", inplace=True)
#     income_df = (
#         df[df["category"] == "Income"]
#         .resample("D")
#         .sum()
#         .reindex(df.index, fill_value=0)
#     )
#     expense_df = (
#         df[df["category"] == "Expense"]
#         .resample("D")
#         .sum()
#         .reindex(df.index, fill_value=0)
#     )

#     plt.figure(figsize=(10, 5))
#     plt.plot(income_df.index, income_df["amount"], label="Income", color="g")
#     plt.plot(expense_df.index, expense_df["amount"], label="Expense", color="r")
#     plt.xlabel("Date")
#     plt.ylabel("Amount")
#     plt.title("Income and Expenses Over Time")
#     plt.legend()
#     plt.grid(True)
#     plt.show()
    


# def main():
#     while True:

#         print("\n1. Add new Transcations")
#         print("2. view transcation and summary within a date  range")
#         print("3. Exits")
#         choice=input("Enter your choice (1-3) :")

#         if choice=="1":
#             add()
#         elif choice=="2":
#             start_date=get_date("enter the start date (dd-mm-yy) :")
#             end_date=get_date("enter the end date (dd-mm-yy) :")
#             df=CSV.get_transcation(start_date,end_date)
#             if input("Do yiu want to see the plot ? (y/n) :").lower()=="y":
#                 plot_transcation(df)
                
#         elif choice=="3":
#             print("exiting .....")
#             break
#         else:
#             print("invalid from (1-3) in the choice 1, 2, 3")
            
# # CSV.get_transcation("01-01-2023","31-12-2024")
# # add()
# if __name__=="__main__":
#     main()

import pandas as pd
import csv
from datetime import datetime
from data_entry import get_amount, get_category, get_date, get_description
import matplotlib.pyplot as plt

class CSV:
    CSV_FILE = "finance_data.csv"
    COLUMNS = ["date", "amount", "category", "description"]
    FORMAT = "%d-%m-%Y"

    @classmethod
    def initialize_csv(cls):
        try:
            pd.read_csv(cls.CSV_FILE)
        except FileNotFoundError:
            df = pd.DataFrame(columns=cls.COLUMNS)
            df.to_csv(cls.CSV_FILE, index=False)

    @classmethod
    def add_entry(cls, date, amount, category, description):
        new_entry = {
            "date": date,
            "amount": amount,
            "category": category,
            "description": description
        }

        with open(cls.CSV_FILE, "a", newline="") as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=cls.COLUMNS)
            writer.writerow(new_entry)
            print("Data added successfully...")

    @classmethod
    def get_transcation(cls, start_date, end_date):
        df = pd.read_csv(cls.CSV_FILE)
        # Ensure the "amount" column is numeric
        df["amount"] = pd.to_numeric(df["amount"], errors="coerce")
        df = df.dropna(subset=["amount"])  # Drop rows with invalid amounts

        # Convert "date" column to datetime
        df["date"] = pd.to_datetime(df["date"], format=CSV.FORMAT)
        start_date = datetime.strptime(start_date, CSV.FORMAT)
        end_date = datetime.strptime(end_date, CSV.FORMAT)

        # Filter data based on the date range
        mask = (df["date"] >= start_date) & (df["date"] <= end_date)
        filtered_df = df.loc[mask]

        if filtered_df.empty:
            print("No transactions found in the given date range.")
        else:
            print(f"Transactions from {start_date.strftime(CSV.FORMAT)} to {end_date.strftime(CSV.FORMAT)}:")
            print(filtered_df.to_string(index=False, formatters={"date": lambda x: x.strftime(CSV.FORMAT)}))
            
            # Calculate totals for Income and Expense
            total_income = filtered_df[filtered_df["category"] == "Income"]["amount"].sum()
            total_expense = filtered_df[filtered_df["category"] == "Expense"]["amount"].sum()
            
            print("\nSummary:")
            print(f"Total Income  : ${total_income:.2f}")
            print(f"Total Expense : ${total_expense:.2f}")
            print(f"Net Savings   : ${(total_income - total_expense):.2f}")
        return filtered_df


def add():
    CSV.initialize_csv()
    date = get_date(
        "Enter the date of the transaction (dd-mm-yyyy) or press Enter for today's date:",
        allow_default=True,
    )
    amount = get_amount()
    category = get_category()
    description = get_description()
    CSV.add_entry(date, amount, category, description)


def plot_transcation(df):
    # Ensure the "amount" column is numeric
    df["amount"] = pd.to_numeric(df["amount"], errors="coerce")
    df.set_index("date", inplace=True)

    income_df = (
        df[df["category"] == "Income"]
        .resample("D")
        .sum()
        .reindex(df.index, fill_value=0)
    )
    expense_df = (
        df[df["category"] == "Expense"]
        .resample("D")
        .sum()
        .reindex(df.index, fill_value=0)
    )

    plt.figure(figsize=(10, 5))
    plt.plot(income_df.index, income_df["amount"], label="Income", color="g")
    plt.plot(expense_df.index, expense_df["amount"], label="Expense", color="r")
    plt.xlabel("Date")
    plt.ylabel("Amount")
    plt.title("Income and Expenses Over Time")
    plt.legend()
    plt.grid(True)
    plt.show()


def main():
    while True:
        print("\n1. Add New Transaction")
        print("2. View Transactions and Summary Within a Date Range")
        print("3. Exit")
        choice = input("Enter your choice (1-3): ")

        if choice == "1":
            add()
        elif choice == "2":
            start_date = get_date("Enter the start date (dd-mm-yyyy): ")
            end_date = get_date("Enter the end date (dd-mm-yyyy): ")
            df = CSV.get_transcation(start_date, end_date)
            if not df.empty and input("Do you want to see the plot? (y/n): ").lower() == "y":
                plot_transcation(df)
        elif choice == "3":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please select 1, 2, or 3.")


if __name__ == "__main__":
    main()

