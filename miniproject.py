import pandas as pd
from sqlalchemy import create_engine
from urllib.parse import quote_plus
data=pd.read_excel("C:\\Users\\Tejeshewini\\OneDrive\\Desktop\\harsha1\\shopping data.xlsx")
print(data)
print(data.columns)
print(data.isnull())
print(data["Category"].isnull())
print(data.dtypes)
d1=data.rename(columns={"Purchase Amount (USD)":"purchaseAmount"})
print(d1)
print(d1.columns)
print(data.isnull())
print(data.head(100))


username = "root"
password =quote_plus("harsha@2005")

host = "localhost"
port = 3306
database = "mysql"

engine = create_engine(f"mysql+pymysql://{username}:{password}@{host}:{port}/{database}")
shopping=data
data.to_sql("shopping",con=engine, if_exists="replace", index=False)

print("done")




