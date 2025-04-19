#Create points table

def champions(stats):
    table = dict()
    for team in stats:
        total_points = (team["wins"]*3)+(team["draws"])
        goal_diff = team["scored"] - team["conceded"]
        table[team["name"]] = [total_points, goal_diff]
    
    sorted_table = dict(sorted(
        table.items(),
        reverse = True,
        key=lambda item:(item[1][0], item[1][1])
    ))
    
    print(sorted_table)
    sorted_table=list(sorted_table)
    print("Champion: ", sorted_table[0])
        
        

stats=[{
"name": "Manchester United",
"wins": 30,
"loss": 3,
"draws": 5,
"scored": 88,
"conceded": 20,
},
{
"name": "Arsenal",
"wins": 30,
"loss": 6,
"draws": 5,
"scored": 98,
"conceded": 29,
},
{
"name": "Chelsea",
"wins": 22,
"loss": 8,
"draws": 8,
"scored": 98,
"conceded": 29,
}
]
# stats=[]
# for _ in range(3):
#     name = input("Enter name of the team: ")
#     wins = int(input("Enter how many wins: "))
#     loss = int(input("Enter the number of losses: "))
#     draws = int(input("Enter tied matches: "))
#     goals_scored = int(input("Enter goals scored: "))
#     goals_conceded= int(input("Enter goals conceded: "))
#     stat = {
#         "name": name,
#         "wins": wins,
#         "loss": loss,
#         "draws": draws,
#         "scored": goals_scored,
#         "conceded": goals_conceded
#     }
#     stats.append(stat)

champions(stats)