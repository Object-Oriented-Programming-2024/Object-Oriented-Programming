class SchoolTeam:
 def __init__(self, name, points):
     self.name = name
     self.points = points

 # Overloading addition operator
 def __add__(self, other_team):
         new_points = self.points + other_team.points
         return SchoolTeam(f"{self.name} & {other_team.name}", new_points)

 # Overloading greater than operator to compare teams
 def __gt__(self, other_team):
         return self.points > other_team.points

 # Overloading __str__ method to support printing objects
 def __str__(self):
     return f"{self.name} ({self.points} points)"


# Example usage of Team class
swim_team_Yasmina = SchoolTeam("Team A - AlYasmina", 30)
swim_team_Raha = SchoolTeam("Team B - Al Raha", 20)
soccer_team_Yasmina = SchoolTeam("Team C  - AlYasmina", 15)
soccer_team_Raha = SchoolTeam("Team D - Al Raha", 20)

# Adding two school teams
totalPerformance_Al_Yasmina  = swim_team_Yasmina + soccer_team_Yasmina
totalPerformance_Al_Raha  = swim_team_Raha + soccer_team_Raha

# Comparing two school teams
if totalPerformance_Al_Yasmina>totalPerformance_Al_Raha:
 print(f"Winning School {totalPerformance_Al_Yasmina}")
else:
 print(f"Winning School {totalPerformance_Al_Raha}")
