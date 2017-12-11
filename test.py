from riotwatcher import RiotWatcher

watcher = RiotWatcher(key)

challenger = watcher.league.challenger_by_queue("na1", "RANKED_SOLO_5x5")
print(challenger['tier'])

challenger_Ids = list()
challenger_name = list()
challenger_accountIds = list()
for key in challenger['entries']:
    challenger_Ids.append(key['playerOrTeamId'])
    challenger_name.append(key['playerOrTeamName'])


#print(challenger_Ids[1])
#print(challenger_name[1])
#print(watcher.summoner.by_id("na1", challenger_Ids[1])['accountId'])

print(watcher.match.matchlist_by_account_recent("na1",watcher.summoner.by_id("na1", challenger_Ids[1])['accountId']))
