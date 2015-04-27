import ysports

# Authorization object
Y = ysports.YAuth()

# League object
league_key = ysports.settings.DFT_LEAGUE_KEY
L = ysports.YLeague(Y, league_key)
print L.name

# League sub-resources (JSON objects)
scoreboard_week_2 = L.scoreboard(2)
standings = L.standings()
teams = L.teams()
players = L.players()
draftresults = L.draftresults()
transactions = L.transactions()

# Print the id and name for each team in the league
print "\nTeams\n------\nid\tname\n--\t----"
for x in teams:
    if x != u"count":
        team = teams[x]["team"][0]
        print "{}\t{}".format(team[1]["team_id"], team[2]["name"])
