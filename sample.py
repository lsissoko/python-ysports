import ysports
import json
import os


def create_folder(path):
    try:
        os.makedirs(path)
    except OSError:
        if not os.path.isdir(path):
            raise
    return path


def export_json(object, file):
    with open(file, 'wt') as out:
        json.dump(
            object, out, sort_keys=True, indent=2, separators=(',', ': '))


def leagueTest(Y, export_flag):
    print "\n-------------\nleagueTest\n"
    # League object
    league_key = ysports.settings.DFT_LEAGUE_KEY
    L = ysports.YLeague(Y, league_key)
    print "League:", L.name

    # League sub-resources (JSON objects)
    scoreboard_week_2 = L.scoreboard(2)
    standings = L.standings()
    teams = L.teams()
    players = L.players()
    draftresults = L.draftresults()
    transactions = L.transactions()

    # Export to JSON file
    if (export_flag):
        create_folder("json/leagueTest")
        export_json(
            scoreboard_week_2, 'json/leagueTest/scoreboard_week_2.json')
        export_json(standings, 'json/leagueTest/standings.json')
        export_json(teams, 'json/leagueTest/teams.json')
        export_json(players, 'json/leagueTest/players.json')
        export_json(draftresults, 'json/leagueTest/draftresults.json')
        export_json(transactions, 'json/leagueTest/transactions.json')

    # Print the id and name for each team in the league
    print "\nTeams\n------\nid\tname\n--\t----"
    for x in teams:
        if x != u"count":
            team = teams[x]["team"][0]
            print "{}\t{}".format(team[1]["team_id"], team[2]["name"])


def gameTest(Y, export_flag):
    print "\n-------------\ngameTest\n"

    # Game object
    game_key = ysports.settings.DFT_GAME_KEY
    G = ysports.YGame(Y, game_key)
    print "Game:", G.name

    # Game sub-resources (JSON objects)
    game_weeks = G.game_weeks()
    stat_categories = G.stat_categories()
    position_types = G.position_types()
    roster_positions = G.roster_positions()

    # Export to JSON file
    if (export_flag):
        create_folder("json/gameTest")
        export_json(game_weeks, 'json/gameTest/game_weeks.json')
        export_json(stat_categories, 'json/gameTest/stat_categories.json')
        export_json(position_types, 'json/gameTest/position_types.json')
        export_json(roster_positions, 'json/gameTest/roster_positions.json')

    # A YLeague object is returned instead of a JSON object
    leagues = G.leagues([ysports.settings.DFT_LEAGUE_KEY])
    print "League:", leagues[0].name

    # Print roster positions information
    print "\nPositions\n------"
    for x in roster_positions:
        pos = x["roster_position"]
        print "{} - {}".format(pos["abbreviation"], pos["display_name"])


if __name__ == "__main__":
    Y = ysports.YAuth()  # Authorization object

    leagueTest(Y, False)  # set to True to export json data

    gameTest(Y, False)  # set to True to export json data
