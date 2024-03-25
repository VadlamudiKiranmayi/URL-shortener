import pyshorteners

def shorten_url():
    link = input("Enter the link: ")
    shortener = pyshorteners.Shortener()
    shortened_url = shortener.tinyurl.short(link)
    return shortened_url

def main():
    shortened_url = shorten_url()
    print('Shortened URL:', shortened_url)

if __name__ == "__main__":
    main()
