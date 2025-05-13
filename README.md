# The Game: daily reminder
Have some folks you really want to piss off? Set some daily notifications to make sure they don't forget.

<img src="https://github.com/aubravo/thegame_daily_reminder/blob/main/src/thegame.svg?raw=true" width="200" />


The current setup of the project needs either a Twilio API key for sending SMS notifications
or an Amazon SES for sending emails.

## Usage

Clone the repo:
```
git clone https://github.com/aubravo/thegame_daily_reminder.git
```

Move into the folder and create your .env file where you'll store the configs
```
cd thegame_daily_reminder & cp sample.env .env & touch phone_list.txt
```

Edit your .env and phone_list accordingly (each phone must be on a single line)

**Optional:** create a virtual environment
```
python -m venv venv
source venv/bin/activate
```

Install the requirements
```
pip install -r requirements.txt
```

Run as:
```
python -m send_sms_notification.py
```

## Other uses

I recommend setting up a cronjob so that the notification is sent daily to the list of phones, you can do that editing your crontab file in Linux using:
```
crontab -e
```

And adding a line to run the script, like:
```
* * * * * cd /projects/thegame_daily_reminder && ./venv/bin/activate -m send_sms_notification 
```
The above example would send a notification every minute



