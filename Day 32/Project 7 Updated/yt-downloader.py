from pytube import YouTube

greet = '''
=============================

WELCOME TO YT DOWNLOADER

=============================
'''

print(greet)

link = input("Enter Youtube Link Of Video/Playlist: \n")

print("DOWNLOADING THE VIDEO FOR YOU...................")

YouTube(link).streams.first().download()

print("****Your Video Has Been Downloaded Successfully!!!!!****")

with open('history.txt', 'a') as f:
    f.write(f"====Downloaded The Video/ Playlist Successfully!!!!====\nVideo Links Is {link}\n")