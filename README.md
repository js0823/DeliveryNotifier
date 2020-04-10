# Delivery Notifier
Auto food delivery notifier.

I wrote this for myself as I became frustrated with Amazon not having enough time slots to deliver my food amid the coronavirus crisis in New York.

# Current Progress

- Currently working on Mac and Ubuntu only. No Windows testing yet.
- Chrome is the only browser I am using right now.
- Amazon Fresh and WholeFoods should both work up to navigating to delivery page.
- Sound is very simple, and it will play it for 1000 times for now when delivery is available. Texting would be better but it costs from what I've googled so far.
- Cannot test when delivery date is open, as I haven't encountered one single instance where the slot became available.

# Prerequisite

1. Requires chromedriver for chrome.
2. Use selenium to navigate through webpage.
3. Playing sound requires installing sox on Mac, or speech-dispatcher on Ubuntu.

# How to use

1. Make sure chromedriver is working on your OS.
2. Make sure you can access Chrome through your terminal.
3. Close all Chrome browser.
4a. For Mac OS, type "Google\ Chrome --remote-debugging-port=9222".
4b. For Linux, type "google-chrome --remote-debugging-port=9222".
5. Type "Python run.py" on your other terminal.
