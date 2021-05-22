import time
from plyer import notification

if __name__ == '__main__':
    
    while True:

        notification.notify(
            title="Drink Water Notification!",
            message="Chacha Paani Pilo!!! Marjaoge. Chacha Rest Karlijiye Warna Rest In Peace Hojayenge",
            app_icon="/Project 2/water-bottle.png",
            timeout=12
        )

        time.sleep(60*60)
