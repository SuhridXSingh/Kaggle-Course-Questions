def read_budget(num_entries):
    budget={}
    for _ in range(num_entries):
        category= int(input())
        amount= int(input())
        budget[category]= budget.get(category , 0) +amount
    return budget
    
n= int(input())
budget1= read_budget(n)
m=int(input())
budget2= read_budget(m)
merged_budget =  budget1.copy()
for category, amount in budget2.items():
    merged_budget[category]=merged_budget.get(category , 0) +amount
print(f"Merged Budget {merged_budget}")
