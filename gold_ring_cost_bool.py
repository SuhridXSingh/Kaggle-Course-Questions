def cost_of_project(engraving, solid_gold):
    cost = solid_gold * (100+ len(engraving)*10) or (not solid_gold) * (50+ len(engraving)*7)
    return cost
