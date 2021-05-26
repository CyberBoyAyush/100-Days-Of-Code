from pytube import YouTube

link = input("Enter Youtube Link Of Video: \n")

print("Downloding...")

YouTube(link).streams.first().download()

print("****Your Video Has Been Downloaded Successfully!!!!!****")