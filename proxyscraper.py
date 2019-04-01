import csv
import requests
from bs4 import BeautifulSoup

list_of_rows = []


def saveproxy():
    filename = raw_input("File Name: ")
    with open (filename + '.txt','w') as file:
        writer=csv.writer(file)
        writer.writerow(['IP'":"'Port'])
        for row in list_of_rows:
            writer.writerow(row)
    print("File Saved Successfully")

def makesoup(url):
    page=requests.get(url)
    print(url + "  scraped successfully")
    return BeautifulSoup(page.text,"lxml")

def proxyscrape(table):
    for row in table.findAll('tr'):
        list_of_cells = []
        for cell in row.findAll('td'):
            text = cell.text.replace('&nbsp;', '')
            list_of_cells.append(text)
        list_of_rows.append(list_of_cells)

def scrapeproxies(url):
    soup=makesoup(url)
    proxyscrape(table = soup.find('table', attrs={'id': 'proxylisttable'}))

def menu():
        print("   _______      ___      .______      .______       _______ .___________.___________. ")
        print("  /  _____|    /   \     |   _  \     |   _  \     |   ____||           |           | ")
        print(" |  |  __     /  ^  \    |  |_)  |    |  |_)  |    |  |__   `---|  |----`---|  |----` ")
        print(" |  | |_ |   /  /_\  \   |      /     |      /     |   __|      |  |        |  |      ")
        print(" |  |__| |  /  _____  \  |  |\  \----.|  |\  \----.|  |____     |  |        |  |      ")
        print("  \______| /__/     \__\ | _| `._____|| _| `._____||_______|    |__|        |__|      ")
        print("")
        print("Please Select A Source To Scrape From:")
        print(" 1. http://sslproxies.org")
        print(" 2. http://free-proxy-list.net")
        print(" 3. http://us-proxy.org")
        print(" 4. http://socks-proxy.net")
        print(" 5. Exit")
        choice = input("Option: ")
        return int(choice) 

while True:          #use while True
    choice = menu()
    if choice == 1:
        scrapeproxies(url = "https://www.sslproxies.org")
    elif choice == 2:
        scrapeproxies(url = "https://free-proxy-list.net")
    elif choice == 3:
        scrapeproxies(url = "https://us-proxy.org")
    elif choice == 4:
        scrapeproxies(url = "https://socks-proxy.net")
    elif choice == 5:
        break
    else:
        print("Invalid choice!")
    if 1 <= choice <= 4:
        saveproxy()
        exit()


    
