from models import User, CV, CoverLetter
from utils import validate_email, format_date
from data_handler import load_data, save_data
import matplotlib.pyplot as plt
from functools import reduce


def main():
    data = load_data()
    users = data.get('users', [])

    while True:
        print("\nKreator CV i Listów Motywacyjnych")
        print("1. Dodaj użytkownika")
        print("2. Wyświetl użytkowników")
        print("3. Edytuj użytkownika")
        print("4. Wyszukaj użytkownika")
        print("5. Generuj CV")
        print("6. Generuj list motywacyjny")
        print("7. Pokaż statystyki")
        print("8. Wyjdź")

        choice = input("Wybierz opcję: ")

        if choice == "1":
            name = input("Imię i nazwisko: ")
            email = input("Email: ")
            if not validate_email(email):
                print("Nieprawidłowy email!")
                continue
            education = input("Wykształcenie: ")
            experience = input("Doświadczenie zawodowe: ")
            skills = input("Umiejętności (oddzielone przecinkami): ").split(',')
            user = User(name, email, education, experience, skills)
            users.append(user.__dict__)
            save_data({'users': users})
            print("Użytkownik dodany!")

        elif choice == "2":
            for user in users:
                print(f"Imię: {user['name']}, Email: {user['email']}")

        elif choice == "3":
            email = input("Podaj email użytkownika do edycji: ")
            for user in users:
                if user['email'] == email:
                    user['name'] = input("Nowe imię i nazwisko: ")
                    user['education'] = input("Nowe wykształcenie: ")
                    user['experience'] = input("Nowe doświadczenie: ")
                    user['skills'] = input("Nowe umiejętności (oddzielone przecinkami): ").split(',')
                    save_data({'users': users})
                    print("Dane zaktualizowane!")
                    break
            else:
                print("Użytkownik nie znaleziony!")

        elif choice == "4":
            search_term = input("Wprowadź szukaną frazę (imię lub email): ")
            results = list(
                filter(lambda u: search_term.lower() in u['name'].lower() or search_term.lower() in u['email'].lower(),
                       users))
            for user in results:
                print(f"Imię: {user['name']}, Email: {user['email']}")

        elif choice == "5":
            email = input("Podaj email użytkownika: ")
            for user in users:
                if user['email'] == email:
                    # Konwersja słownika na obiekt User
                    user_obj = User(
                        name=user['name'],
                        email=user['email'],
                        education=user['education'],
                        experience=user['experience'],
                        skills=user['skills']
                    )
                    cv = CV(user_obj)  # Przekazujemy obiekt User, a nie słownik
                    cv.generate_cv()
                    print("CV wygenerowane!")
                    break
            else:
                print("Użytkownik nie znaleziony!")

        elif choice == "6":
            email = input("Podaj email użytkownika: ")
            for user in users:
                if user['email'] == email:
                    # Konwersja słownika na obiekt User
                    user_obj = User(
                        name=user['name'],
                        email=user['email'],
                        education=user['education'],
                        experience=user['experience'],
                        skills=user['skills']
                    )
                    company = input("Nazwa firmy: ")
                    position = input("Stanowisko: ")
                    cl = CoverLetter(user_obj, company, position)  # Przekazujemy obiekt User
                    cl.generate_cover_letter()
                    print("List motywacyjny wygenerowany!")
                    break
            else:
                print("Użytkownik nie znaleziony!")

        elif choice == "7":
            dates = list(map(lambda u: format_date(u.get('created_at', '2025-06-23')), users))
            date_counts = reduce(lambda acc, date: {**acc, date: acc.get(date, 0) + 1}, dates, {})
            plt.bar(date_counts.keys(), date_counts.values())
            plt.title("Liczba utworzonych CV według daty")
            plt.savefig("output/statistics.png")
            plt.close()
            print("Statystyki zapisane w output/statistics.png")

        elif choice == "8":
            break
        else:

            print("Nieprawidłowy wybór!")


if __name__ == "__main__":
    main()