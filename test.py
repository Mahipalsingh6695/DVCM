import pandas as pd

data=[
    {"name":"sunny","age":27,"city":"bhopal"},
    {"name":"Mahipal","age":27,"city":"bhim"},
    {"name":"Ravi","age":29,"city":"beawar"},
    {"name":"shagun","age":25,"city":"bhinay"}
]

df=pd.DataFrame(data)

df.to_csv("data/data.csv",index=False)