import json, re
import halcyon, requests


client = halcyon.Client()
with open('creds.json') as data:
    keys = json.load(data)


def get_stock_info(ticker):
    """
    This function returns a String message with stock info, or none if the stock wasn't found

    :param ticker: String this is the ticker to look for
    :return: String stock info
    """
    resp = requests.get(url="https://cloud.iexapis.com/stable/stock/"+ticker+"/quote?token="+keys["iex"])
    if resp.status_code == 200:
        #We can use markdown here, because we use the send markdown feature later
        """
        Output goal:
            Vanguard Group, Inc. - Vanguard S&P 500 ETF
            $410.69 (-2.%)
        """
        message = resp.json()["companyName"] + "\n\n"
        message += "${price} __({change}%)__ \n".format(price=resp.json()["delayedPrice"], change=(str(resp.json()["changePercent"]*100)[:3]))
        return message
    else:
        return None


@client.event
async def on_room_invite(room):
    print("Someone invited us to join " + room.name)
    await client.join_room(room.id)
    await client.send_message(room.id, body="Hello humans, to find a stock price, search with $ticker")


@client.event
async def on_message(message):

    #If we see a message by the bot, don't respond
    if message.sender == "@hstockbot:blackline.xyz":#this is our bot username
        return

    if "$" in message.content.body:
        tickers = re.findall("\$[\w.]+", message.content.body)#This is just some fancy regex to get a list of tickers

        responce_comment = str()
        for stock in tickers:
            resp = get_stock_info(stock.strip("$"))#remove the $ sign, and get the info
            if resp:#if it has content
                responce_comment += resp + "\n"

        if responce_comment:#if we found a stock, and have a comment, send it
            await client.send_message(message.room.id, body=responce_comment, textFormat = "markdown", replyTo=message.event.id)

@client.event
async def on_ready():
    print("Online!")
    await client.change_presence(statusMessage="Reading the ticker tape")

if __name__ == '__main__':
    client.run(halcyonToken=keys["halcyon"], longPollTimeout=3)