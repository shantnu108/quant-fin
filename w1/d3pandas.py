# series
import pandas as pd
def fx(a):
    return a+9
# s=pd.Series([1,2,3,4,5])
# print(s)


# # dataframe
# df=pd.DataFrame({"names":["shantnu","akshat","jatin"],"marks":[101,123,221]})
# print(df)

df=pd.read_csv("F:/qf/w1/mydata.csv")
# print(df)
# print(df.head())
# print(df.tail())
# print(df.describe())
# print(df.info())


#data selction
# print(df[["Year","Units"]])

# print(type(df.iloc[0]))
# print(df.dropna())
# print(df.fillna(0,inplace=True))
# df.rename(columns={"Year":"Saal"},inplace=True)
# print(df.head())
# print(df.describe())
# df.rename(columns={"Saal":"Year"},inplace=True)
# df["Year"]=df["Year"].astype(int)
# print(df.info())
# print(df.head())
# print(df["Year"][0])
df["zeros"]=[0 for i in range(len(df))]
df["zero + 1"]=df["zeros"].apply(fx)
print(df)


df.to_csv("F:/qf/w1/export.csv")









































































# class Graph:
#     def __init__(self, size):
#         self.size = size
#         self.links = [[] for _ in range(size)]

#     def connect(self, source, target):
#         self.links[source].append(target)

#     def depth_search(self, origin):
#         visited = [False] * self.size
#         stack = [origin]

#         print("DFS Order:", end=" ")

#         while stack:
#             current = stack.pop()

#             if not visited[current]:
#                 print(current, end=" ")
#                 visited[current] = True

#                 for nxt in reversed(self.links[current]):
#                     if not visited[nxt]:
#                         stack.append(nxt)



# net = Graph(4)
# net.connect(0, 1)
# net.connect(0, 2)
# net.connect(1, 2)
# net.connect(2, 0)
# net.connect(2, 3)
# net.connect(3, 3)

# net.depth_search(0)
