import requests

class BookList:
    def __init__(self):
        self.buecher = []

    def add_book_from_api(self, title):

        #API endpoint
        url = f"https://openlibrary.org/search.json?title={title}"

        # GET request
        response = requests.get(url)

        if response.status_code == 200:
            data = response.json()

            #Erstes Element aus den Daten
            docs = data.get("docs", [])

            if docs:
                first_book = docs[0]
                title = first_book.get("title")

                #Fuege Titel dem Array hinzu
                self.buecher.append(title)
                print(f"Buch '{title}' wurde hinzugefuegt.")
            else:
                print("Keine Buecher gefunden.")


    def show_books(self):
        if not self.buecher:
            print("Keine Buecher vorhanden.")
        else:
            print("----------\n" + "Buecher in Liste:\n----------")
            for index, buch in enumerate(self.buecher, start=1):
                print(f"{index}. {buch}\n----------")


bl = BookList()

while True:
    user_input = input("Gib den Namen eines englischen Buches ein oder 'Exit' zum Beenden - 'Show' zum Anzeigen der Liste ")
    if user_input.lower() == "exit":
        break
    elif user_input.lower() == "show":
        bl.show_books()
    else:
        bl.add_book_from_api(user_input)
