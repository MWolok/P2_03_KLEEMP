# PROJEKT: Analiza sprzedaży gier wideo i Fine-Tuning LLM (Finał)

**Grupa:** 3 (KLEEMP)

## OPIS PROJEKTU:
Celem projektu jest analiza trendów w branży gier wideo na przestrzeni dekad (zmiany popularności gatunków i platform) oraz wykorzystanie tych danych do wytrenowania modelu sztucznej inteligencji. Przy użyciu biblioteki Hugging Face i modelu `flan-t5-small` stworzyliśmy "Automatycznego Redaktora", realizując zadanie Data-to-Text – zamianę surowych danych tabelarycznych w płynne notki prasowe.

## OPIS ELEMENTÓW REPOZYTORIUM:
- `data/`: zawiera zbiór `vgsales.csv` z Kaggle (dane wejściowe).
- `outputs/`: zawiera wygenerowane wykresy EDA z pierwszego skryptu.
- `main.py`: skrypt w Pythonie przeprowadzający czyszczenie danych i analizę EDA.
- `finetuning_colab.ipynb`: notatnik Jupyter z kodem przygotowującym zbiór treningowy i douczającym model LLM.
- `requirements.txt`: lista bibliotek potrzebnych do uruchomienia skryptu `main.py`.
- `Raport_Koncowy_NR3.pdf`: pełny opis projektu, wnioski, architektura modelu i wyniki fine-tuningu.

## JAK URUCHOMIĆ KOD I ODTWORZYĆ WYNIKI:

**Część 1: Analiza EDA (Lokalnie)**
1. Pobierz repozytorium na swój komputer.
2. Zainstaluj wymagane biblioteki poleceniem: `pip install -r requirements.txt`
3. Uruchom skrypt poleceniem: `python main.py`
4. Kod automatycznie przetworzy dane i zapisze gotowe wykresy w folderze `outputs/`.

**Część 2: Fine-Tuning modelu LLM (W chmurze)**
Ze względu na wymagania sprzętowe, trening modelu należy przeprowadzić w Google Colab.
1. Otwórz darmowe środowisko Google Colab.
2. Zmień typ środowiska wykonawczego na T4 GPU (Runtime -> Change runtime type -> T4 GPU).
3. Zaimportuj do środowiska plik `finetuning_colab.ipynb` oraz plik z danymi `vgsales.csv`.
4. Uruchom wszystkie komórki w notatniku (Runtime -> Run all). Skrypt pobierze model, przetrenuje go na przygotowanych parach danych i wyświetli testowy wynik tekstowy na samym dole.

## WYKORZYSTANIE AI W PROJEKCIE:
Podczas realizacji projektu wspieraliśmy się asystentem AI w następującym zakresie:
- Generowanie szkieletu kodu w bibliotece Pandas i Seaborn do czyszczenia i wizualizacji danych.
- Pomoc w napisaniu i poprawnym skonfigurowaniu pliku `.gitignore` dla środowisk wirtualnych PyCharm.
- Generowanie kodu HTML i CSS do estetycznego formatowania raportów PDF (biblioteka WeasyPrint).
- Pomoc w napisaniu kodu trenującego (Trainer API z Hugging Face) dla środowiska Google Colab(Naprawa bledow i wskazowki).

Ostateczne decyzje analityczne, wybór zbioru, definicja zadania dla modelu językowego (Data-to-Text) oraz weryfikacja poprawności kodu były podejmowane w całości przez zespół.
