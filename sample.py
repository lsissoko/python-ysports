import ysports

# Authorization object
Y = ysports.YAuth()

# League object
league_key = "223.l.431" # yahoo example league
L = ysports.YLeague(Y, league_key)
print L.name

# League sub-resources (JSON)
scoreboard_week_2 = L.scoreboard(2)
standings = L.standings()
teams = L.teams()
players = L.players()
draftresults = L.draftresults()
transactions = L.transactions()

# Print team names and ids
print "\nTeams:"
for x in teams:
    if x != u"count":
        team = teams[x]["team"][0]
        print "> name: " + team[2]["name"]
        print "  id:   " + team[1]["team_id"]
