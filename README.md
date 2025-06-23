# Kreator CV i Listów Motywacyjnych

## Cel projektu
Aplikacja umożliwia tworzenie profesjonalnych CV i listów motywacyjnych na podstawie danych użytkownika, z zapisem w plikach tekstowych i PDF oraz generowaniem statystyk.

## Wymagania
- Python 3.8+
- Biblioteki: `matplotlib`, `fpdf`, `memory-profiler`
- Zainstaluj zależności: `pip install -r requirements.txt`

## Uruchomienie
1. Sklonuj repozytorium: `git clone <link>`
2. Przejdź do folderu: `cd cv_creator`
3. Uruchom: `python main.py`

## Struktura
- `main.py`: Główny moduł
- `utils.py`: Funkcje pomocnicze
- `models.py`: Klasy obiektowe
- `data_handler.py`: Obsługa JSON
- `tests.py`: Testy
- `output/`: Generowane pliki

## Przykładowe dane
Wejście: Imię: Jan Kowalski, Email: jan@example.com, Wykształcenie: Mgr, Doświadczenie: Programista, Umiejętności: Python, Java
Wyjście: Pliki `cv_jan@example.com.txt`, `cv_jan@example.com.pdf`

## Autorzy
- Przemysław Drdzeń
- Grupa: 2ID12A
- Data: 2025-06-23
