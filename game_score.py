player_name = input("Enter player name: ")                   #Input Collection
games_played = int(input("Enter number of games played: "))  #Numeric input Processing
total_score = int(input("Enter total score: "))		     #Score Data Entry
average_score = total_score/games_played 		     #Computation

# Output Display
print(f"\nPlayer: {player_name}")
print(f"\nGames Played: {games_played}")
print(f"\nTotal Score: {total_score}")
print(f"\nAverage Score: {average_score}")


