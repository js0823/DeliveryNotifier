# Grocery Delivery Notifier
Auto grocery delivery notifier. It currently works on Amazon Fresh and WholeFoods.

I wrote this for myself as I became frustrated with Amazon not having enough time slots to deliver my groceries due to the coronavirus crisis in New York.

Please note while it works on my testing environments, I haven't tested anywhere else.
I recommend trying the release version first.

# Current Progress

- Now works on Windows and Mac.
- Chrome is the only browser that works for now.
- Amazon Fresh and WholeFoods should both work up to navigating to delivery page.
- Sound is very simple, and it will play it for 1000 times for now when delivery is available. Texting would be better but it costs from what I've googled so far.
- Delivery notification is now tested. The program should now navigate from the homepage to the delivery page, and keep checking if delivery date is available, and alert when it is.
- Created first pre-release to the public.

# Prerequisite

- Python 3
- Requires chromedriver for chrome.
- Use selenium to navigate through webpage.
- Uses playsound package to play mp3 alert.

# How to use

If you want to run using Python, use the "requirements.txt" to install Python packages. You can run by running the command

```
pip install -r requirements.txt
```

1. Make sure chromedriver is working on your OS.
2. Make sure you can access Chrome through your terminal.
3. Close all Chrome browser.

4a. For Windows, type 
```
chrome --remote-debugging-port=9222
```
4b. For Mac OS, you must have Google Chrome in your PATH environment variable. Then type:
```
Google\ Chrome --remote-debugging-port=9222
```
5. Type "Python run.py" on your other terminal, or just run the binary if you downloaded them from the release.
