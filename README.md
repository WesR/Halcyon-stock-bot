# Halcyon stock bot
Hello! This is an example / template bot using the [halcyon](https://github.com/WesR/Halcyon) matrix bot library.

## Bot goals
This bot will
1. Sit in a room, and respond with the current price of a stock when some calls the ticker. For example "Hey guys, did you see that $UVKY just spiked?"
2. Respond with the
	+ Stock name
	+ Current price
	+ Todays Percent change
3. Have a small "index" that only moderators or higher can add stocks to
4. Give the index when someone says "!index"


## Requirments
1. A matrix account for the bot
2. An free api key from (IEX)[https://iexcloud.io/s/ec26bc7b]
3. A place to run the bot

## Bot setup
1. `python3 -m pip install halcyon`
2. Create the Halcyon token `python3 -m halcyon -s server.xyz -u @hstockbot:server.xyz -p "password"`
3. Save the above key, and your iex key in a file called `creds.json`, formatted like below.
```json
{
	"halcyon":"eyJ0e==",
	"iex": "pk_12",
	"iex_dev":"Tpk_78"
}
```
4. Run the bot `python3 bot.py`
5. Invite the bot to an unencrypted room, and give it a test