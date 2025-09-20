def cost_of_project(engraving, solid_gold):
    if solid_gold == True:
        return (len(engraving)*10+(100))
    else:
        return (len(engraving)*7+(50))
      
  
project_one = cost_of_project("Charlie+Denver", True)
print(project_one)

project_two = cost_of_project("08/10/2000", False)
print(project_two)
