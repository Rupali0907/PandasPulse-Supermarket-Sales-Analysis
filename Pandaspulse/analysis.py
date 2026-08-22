
# Supermarket Sales Analysis using Pandas
import pandas as pd

# Read CSV file(Loading)
df = pd.read_csv("data/supermarket_sales.csv")
print("Dataset Loaded Successfully!")

# Data Exploration

print("First 5 Rows:")
print(df.head())

print("Last 5 Rows:")
print(df.tail())

print("Shape of Dataset:")
print(df.shape)

print("Column Names:")
print(df.columns)

print("Data Types:")
print(df.dtypes)

print("Dataset Information:")
df.info()

print("Statistical Summary:")
print(df.describe())

print("Missing Values in Each Column:")   # Observation:No missing values found in the dataset.
print(df.isnull().sum())

print("\nDuplicate Rows:")
print(df.duplicated().sum())       #Observation:No duplicate rows found in the dataset.

# Data Cleaning

df_clean = df.copy()
print("Copy created successfully.")

# Create missing values

df_clean.loc[5, "City"] = None
df_clean.loc[10, "Payment"] = None
df_clean.loc[15, "Total"] = None
df_clean.loc[20, "Quantity"] = None

print("Missing Values After Creating:")
print(df_clean.isnull().sum())

# Fill missing values in text columns

df_clean["City"] = df_clean["City"].fillna("Unknown")
df_clean["Payment"] = df_clean["Payment"].fillna("Not Available")

# Fill missing values in numeric columns

df_clean["Total"] = df_clean["Total"].fillna(
    df_clean["Total"].mean())

df_clean["Quantity"] = df_clean["Quantity"].fillna(
    df_clean["Quantity"].median())
print(df_clean.isnull().sum())

# Create duplicate rows

df_clean = pd.concat([df_clean, df_clean.iloc[[0]]], ignore_index=True)
df_clean = pd.concat([df_clean, df_clean.iloc[[5]]], ignore_index=True)

print("Duplicate rows created successfully!")

print("Duplicate Rows:")
print(df_clean.duplicated().sum())

# Remove duplicate rows

df_clean = df_clean.drop_duplicates()

print("Duplicate rows removed successfully!")

print("Duplicate Rows After Cleaning:")
print(df_clean.duplicated().sum())

# Create extra spaces

df_clean.loc[0, "City"] = " Yangon "
df_clean.loc[1, "Payment"] = " Cash "

print(df_clean.loc[[0,1], ["City", "Payment"]])

df_clean["City"] = df_clean["City"].str.strip()     
df_clean["Payment"] = df_clean["Payment"].str.strip()

print(df_clean.loc[[0,1], ["City", "Payment"]])

#rename columns

df_clean.rename(columns={
    "Customer type": "Customer_Type",
    "Product line": "Product_Line",
    "Unit price": "Unit_Price",
    "Invoice ID": "Invoice_ID",
    "Cost of goods sold": "COGS",
    "Gross margin percentage": "Gross_Margin_Percentage",
    "Gross income": "Gross_Income",
    "Customer stratification rating": "Customer_Rating"
}, inplace=True)
print(df_clean.columns)

df_clean.to_csv("output/cleaned_supermarket_sales.csv", index=False)

# Data Analysis 

#SALES BY CITIES
print("Total Sales by City: ")

city_sales = df_clean.groupby("City")["Total"].sum()

print(city_sales)

city_sales = df_clean.groupby("City")["Total"].sum().sort_values(ascending=False)

print(city_sales)

#Which branch generated the highest revenue
branch_sales = df_clean.groupby("Branch")["Total"].sum().sort_values(ascending=False)

print(branch_sales)

#Which product category is most profitable?
product_sales = df_clean.groupby("Product_Line")["Total"].sum().sort_values(ascending=False)

print(product_sales)

#Which payment method is used the most?
payment = df_clean["Payment"].value_counts()

print(payment)

#Are male or female customers more frequent?
gender = df_clean["Gender"].value_counts()

print(gender)

#Returns the top 5 rows having the highest Total.
print("\nHighest 5 Sales Transactions:\n")

highest_sales = df_clean.nlargest(5, "Total")

print(highest_sales[["Invoice_ID", "City", "Product_Line", "Total"]])

#Lowest 5 Sales Transactions
print("Lowest 5 Sales Transactions:")

lowest_sales = df_clean.nsmallest(5, "Total")

print(lowest_sales[["Invoice_ID", "City", "Product_Line", "Total"]])

#Average Sales by City
print("Average Sales by City:")

avg_city = df_clean.groupby("City")["Total"].mean().sort_values(ascending=False)

print(avg_city)

#Average Customer Rating by Product Line
print("Average Customer Rating:")

rating = df_clean.groupby("Product_Line")["Customer_Rating"].mean().sort_values(ascending=False)

print(rating)

#Filter Sales Greater Than 500
print("Sales Greater Than 500:")

high_sales = df_clean[df_clean["Total"] > 500]

print(high_sales.head())

#Cash Payments
print("Cash Payments:")

cash = df_clean[df_clean["Payment"] == "Cash"]

print(cash.head())

#male customer
male = df_clean[df_clean["Gender"] == "Male"]

print(male[["Invoice_ID", "City", "Gender", "Payment", "Total"]].head())

#Number of Unique Cities
print("Number of Unique Cities:")

print(df_clean["City"].nunique())

city_sales.to_csv("output/city_sales.csv")

branch_sales.to_csv("output/branch_sales.csv")

product_sales.to_csv("output/product_sales.csv")

payment.to_csv("output/payment_analysis.csv")

gender.to_csv("output/gender_analysis.csv")
