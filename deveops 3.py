emp - {'eno':[1,2,3],'ename':['A','B','C'],'esal':[10000,22000,20000]}
print("\n the employee dataset is:")
print(emp)
print("----------------------------------------------------")
print("\n the employeee name are:",emp['ename'])
print("----------------------------------------------------")
print("\n the employeee salaries are:")
print("----------------------------------------------------")
for i in emp['esal']:
    print(i)