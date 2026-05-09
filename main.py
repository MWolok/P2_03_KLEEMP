
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Tworzenie folderu na wyniki jeśli nie istnieje
if not os.path.exists('outputs'):
    os.makedirs('outputs')

# 1. Wczytanie danych
try:
    df = pd.read_csv('data/vgsales.csv')
    print("Dane wczytane pomyślnie!")
except FileNotFoundError:
    print("BŁĄD: Nie znaleziono pliku data/vgsales.csv. Pobierz go z Kaggle!")
    exit()

# 2. Czyszczenie i przygotowanie
df = df.dropna(subset=['Year'])
df['Year'] = df['Year'].astype(int)
df['Decade'] = (df['Year'] // 10) * 10

# Filtrujemy dane do pełnych dekad (np. do 2010)
df = df[df['Decade'] >= 1980]

# 3. Analiza: Najlepsze gatunki na dekadę
genre_sales = df.groupby(['Decade', 'Genre'])['Global_Sales'].sum().reset_index()
plt.figure(figsize=(12, 6))
sns.barplot(data=genre_sales, x='Decade', y='Global_Sales', hue='Genre')
plt.title('Sprzedaż globalna gier według gatunków i dekad')
plt.ylabel('Sprzedaż (mln kopii)')
plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left')
plt.tight_layout()
plt.savefig('outputs/top_genres.png')
print("Wygenerowano: outputs/top_genres.png")

# 4. Analiza: Najlepsze platformy na dekadę
platform_sales = df.groupby(['Decade', 'Platform'])['Global_Sales'].sum().reset_index()
# Wybieramy tylko topowe platformy dla czytelności
top_platforms = platform_sales.sort_values(['Decade', 'Global_Sales'], ascending=[True, False]).groupby('Decade').head(3)

plt.figure(figsize=(12, 6))
sns.barplot(data=top_platforms, x='Decade', y='Global_Sales', hue='Platform')
plt.title('Top 3 Platformy z najwyższą sprzedażą w każdej dekadzie')
plt.ylabel('Sprzedaż (mln kopii)')
plt.tight_layout()
plt.savefig('outputs/top_platforms.png')
print("Wygenerowano: outputs/top_platforms.png")
