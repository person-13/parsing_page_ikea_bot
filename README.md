# Description
A Python program that notifies about the availability of the IKEA online store site via a Telegram bot

The code in this repository will launch Chrome, open the IKEA waiting page, after that it will check the page's level 1 header every second. Next, if the title of the 1st level of the page coincides with the title of the main page of the online store, send a telegram message about the availability of the site for ordering goods.
