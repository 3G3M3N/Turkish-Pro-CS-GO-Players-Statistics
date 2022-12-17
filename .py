import pandas as pd

df = pd.read_csv("csgo_players.csv")
df

turkishplayers = df.loc[(df["country"]=="Turkey")]
turkishplayers

turkishplayers.columns

#Ages
age = turkishplayers["age"]
age = age.rename(index = turkishplayers["nickname"])
pd.DataFrame(age)

dfage = df.sort_values("age")
dfage = dfage.reset_index()
dfage.describe()
turks = dfage.loc[(dfage["country"]=="Turkey")]

#Teams
summary = turkishplayers["current_team"]
summary = summary.rename(index = turkishplayers["nickname"])
#ngiN playing on Sangal, but data is false. I did correct this.
summary[7]="Sangal"
pd.DataFrame(summary)

oldteam = turkishplayers["teams"]
oldteam = oldteam.rename(index = turkishplayers["nickname"])
pd.DataFrame(oldteam)

headshot = turkishplayers["headshot_percentage"]
headshot = headshot.rename(index = turkishplayers["nickname"])

pd.DataFrame(headshot)

totaldeath = turkishplayers["total_deaths"]
totaldeath = totaldeath.rename(index = turkishplayers["nickname"])
pd.DataFrame(totaldeath)

ace = turkishplayers["5_kill_rounds"]
ace = ace.rename(index = turkishplayers["nickname"])
pd.DataFrame(ace)

rifle = turkishplayers["rifle_kills"]
sniper = turkishplayers["sniper_kills"]
smg = turkishplayers["smg_kills"]
pistol = turkishplayers["pistol_kills"]
grenade = turkishplayers["grenade_kills"]
other = turkishplayers["other_kills"]
weaponkills = pd.concat([rifle,sniper,smg,pistol,grenade,other], axis = 1)
weaponkills.rename(index = turkishplayers["nickname"])
weaponkills

mapp = turkishplayers["maps_played"]
mapp = mapp.rename(index = turkishplayers["nickname"])
pd.DataFrame(mapp)

rounds = turkishplayers["rounds_played"]
rounds = rounds.rename(index = turkishplayers["nickname"])
pd.DataFrame(rounds)

dmgraund = turkishplayers["damage_per_round"]
dmgraund = dmgraund.rename(index = turkishplayers["nickname"])
pd.DataFrame(dmgraund)

killround = turkishplayers["kills_per_round"]
killround = killround.rename(index = turkishplayers["nickname"])
pd.DataFrame(killround)

assists = turkishplayers["assists_per_round"]
assists = assists.rename(index = turkishplayers["nickname"])
pd.DataFrame(assists)

openkill = turkishplayers["total_opening_kills"]
openkill = openkill.rename(index = turkishplayers["nickname"])
pd.DataFrame(openkill)

opendeath = turkishplayers["total_opening_deaths"]
opendeath = opendeath.rename(index = turkishplayers["nickname"])
pd.DataFrame(opendeath)

teamwinafterfirstkill = turkishplayers["team_win_percent_after_first_kill"]
teamwinafterfirstkill = teamwinafterfirstkill.rename(index = turkishplayers["nickname"])
pd.DataFrame(teamwinafterfirstkill)

firstkillinwonround = turkishplayers["first_kill_in_won_rounds"]
firstkillinwonround = firstkillinwonround.rename(index = turkishplayers["nickname"])
pd.DataFrame(firstkillinwonround)

zero = turkishplayers["0_kill_rounds"]
one = turkishplayers["1_kill_rounds"]
two = turkishplayers["2_kill_rounds"]
three = turkishplayers["3_kill_rounds"]
four = turkishplayers["4_kill_rounds"]
five = turkishplayers["5_kill_rounds"]
roundperkillstaticts = pd.concat([zero, one, two, three, four, five], axis = 1)
roundperkillstaticts
roundperkillstaticts.rename(index = turkishplayers["nickname"])

savedteammatesperround = turkishplayers["saved_teammates_per_round"]
savedteammatesperround = savedteammatesperround.rename(index = turkishplayers["nickname"])
pd.DataFrame(savedteammatesperround)

savedbyteammatesperround = turkishplayers["saved_by_teammate_per_round"]
savedbyteammatesperround = savedbyteammatesperround.rename(index = turkishplayers["nickname"])
pd.DataFrame(savedbyteammatesperround)


