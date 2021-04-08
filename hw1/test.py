class CountList:
    def __init__(self, *args):
        self.values = [x for x in args]
        self.count = {}.fromkeys(range(len(self.values)),0)
    def __len__(self):
        return len(self.values)
    def __getitem__(self, key):
        self.count[key] += 1
        return self.values[key]

c1 = CountList(1,3,5,7,9)
c2 = CountList(2,4,6,8,10)
print("c1.values:", c1.values)
print("c2.values:", c2.values)
print("c1[1]:", c1[1])
print("c2[1]:", c2[1])
print("c1[1]+c2[1]:", c1[1]+c2[1])
print("c1.count:", c1.count)
print("c2.count:", c2.count)
# print("c1.count:", c1.count)
# print("c2.count:", c2.count)
# # 调用
# c1[1]  ## 3
# c2[1]  ## 4
# c1[1] + c2[1] 	## 7
# c1.count  ## {0:0,1:2,2:0,3:0,4:0}
# c2.count  ## {0:0,1:2,2:0,3:0,4:0}	
