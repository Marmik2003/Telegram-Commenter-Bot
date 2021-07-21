Thank you for using my bot
This bot helps you get followed messages
First of all, you have to collect your api id and hash from http://my.telegram.org/auth
Then, From Telegram App, search for @BotFather and create new bot by command /newbot and get your Bot API_KEY
Open .env file and edit your credentials and save it!

configuration of .env file
--------------------------------
API_KEY= your bot api key
user_id= YOUR_TELEGRAM_ID (7 digits)
user_hash= YOUR_TELEGRAM_HASH (32 characters)
user_phone= YOUR_TELEGRAM_NUMBER (your number with country code e.g., +1111111111)
--------------------------------

make sure you have installed python 3

run command `pip3 install virtualenv`
run command `virtualenv venv`
run command `venv/Scripts/activate` if you are in windows else run `source venv/bin/activate` if you are in linux

After activating virtual environment, run command `pip install -r requirements.txt`

run Follower.py file and follow the groups that you want by group number.

Whenever you run Commenter.py file, your bot will be live.

you can test it with typing /start in telegram after running Commenter.py and get first messages of followed groups by /getMessage

