import os
class Item:
    def __init__(self, name, category, price, featured):
        self.name = name
        self.category = category
        self.price = price
        self.featured = featured

class CreditCard:
    def __init__(self, number, name, limit):
        self.number = number
        self.name = name
        self.limit = limit

class AuctionPortal:
    def __init__(self,):
        self.items_list = [
            Item('iPhone 12 Pro', 'elektronika', 4600, True),
            Item('Konsola Playstation 5', 'elektronika', 2899, False),
            Item('Bluza Adidas Meska Szara', 'odziez', 249, True),
            Item('Spodnie Wrangler Arizona', 'odziez', 189, False),
            Item('Basen ogrodowy Premium', 'dom i ogrod', 1199, False),
            Item('Krzeslo skandynwskie granatowe', 'dom i ogrod', 88, False),            
            ]
        self.items_list.sort(key=lambda item: item.name)
        self.items_list.sort(key=lambda item: item.featured, reverse=True)

        self.credit_cards = [
            CreditCard("0001", "Visa", 100),
            CreditCard("0002", "Mastercard", 10000),
            CreditCard("0003", "American Express", 3000),
            CreditCard("0004", "Diners Club", 1000),

        ]

    def display_items(self):
            index = 1
            for item in portal.items_list:
                print(f"{index}.",item.name,'|',  item.category,'|', item.price, '|', item.featured )
                index += 1
    
    def add_item(self):
        clear_console()
        name = input('Podaj nazwe przedmiotu(nazwa z wielkiej litery): ')
        category = str(input('Podaj kategorie przedmiotu: '))
        price = int(input('Podaj cene przedmiotu: '))
        featured_input = input('Czy przedmiot ma byc promowany?: (tak/nie)')
        if featured_input == 'tak':
            featured = True
        elif featured_input == 'nie':
            featured = False
        item = Item(name, category, price, featured)
        self.items_list.append(item)
        self.items_list.sort(key=lambda item: item.name)
        self.items_list.sort(key=lambda item: item.featured, reverse=True)
        clear_console()
    def buy_item(self):
        clear_console()
        print('Wybierz przedmiot, ktory chcesz kupic: ')
        print()
        for i, item in enumerate(self.items_list, start=1):
            item.name = (f'{i}. {item.name} | {item.category} | {item.price}zl')
            print(item.name)
        choice = int(input())
        if choice > 0 and choice <= len(self.items_list):
            item_to_buy = self.items_list[choice - 1]
            price = item_to_buy.price
            credit_id = input('Wpisz numer karty(cztery cyfry): ')
            for card in self.credit_cards:
                if card.number == credit_id:
                    if price > card.limit:
                        print('Cena przedmiotu przekracza limit karty kredytowej.')
                        break
                    else:
                        clear_console()
                        print(f'Zakupiono przedmiot {item_to_buy.name}')
                        del self.items_list[choice - 1]
                        break
            else:
                clear_console()
                print('Nie znaleziono karty kredytowej o podanym numerze.')
                
        else:
            clear_console()
            print('Nieprawidlowy wybor')

portal = AuctionPortal()

def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

while True:
    print('Wybierz opcje:')
    print('1 --> Zakup')
    print('2 --> Sprzedaz')
    print('3 --> Koniec')
    option = input()

    if option == '1':
        portal.buy_item()
    elif option == '2':
        portal.add_item()
    elif option == '3':
        break
    else:
        print('Nieporawidla akcja.')