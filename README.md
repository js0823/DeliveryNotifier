# Delivery Notifier
Auto food delivery notifier. It currently works on Amazon Fresh and WholeFoods.

I wrote this for myself as I became frustrated with Amazon not having enough time slots to deliver my food due to the coronavirus crisis in New York.

Please note while it works on my testing environments, I haven't tested anywhere else.
I recommend trying the release version first.

# Current Progress

- Now works on Windows and Mac.
- Chrome is the only browser I am using right now.
- Amazon Fresh and WholeFoods should both work up to navigating to delivery page.
- Sound is very simple, and it will play it for 1000 times for now when delivery is available. Texting would be better but it costs from what I've googled so far.
- Cannot test when delivery date is open, as I haven't encountered one single instance where the slot became available.
- Created first pre-release to the public.

# Prerequisite

- Python 3
- Requires chromedriver for chrome.
- Use selenium to navigate through webpage.
- Uses playsound package to play mp3 alert.

# Notes

## Creating binaries
- To create binary, use pyinstaller package and run the following command

```
Windows:
pyinstaller --onefile --add-data "assets/slotfound.mp3;." run.py

Mac:
pyinstaller --onefile --add-data 'assets/slotfound.mp3:.' run.py
```
## Mac

- In order to make playsound package work on Mac, try running the following command on your favorite Python environment if it doesn't work.
```
pip install PyObjC pyObjC-core
```

# How to use

1. Make sure chromedriver is working on your OS.
2. Make sure you can access Chrome through your terminal.
3. Close all Chrome browser.
4a. For Windows, type "chrome --remote-debugging-port=9222".
4b. For Mac OS, type "Google\ Chrome --remote-debugging-port=9222".

Type "Python run.py" on your other terminal, or just run the binary if you have them.
