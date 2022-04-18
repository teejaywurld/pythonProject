import pyshorteners

link = input("enter your link here: ")

shortener = pyshorteners.Shortener()

x = shortener.tinyurl.short(link)

print(x)
