# PROJ-Led-Board-with-REST-API-FontTool
Narzędzie do generowania tablic do znaków, komplementujące projekt PROJ-Led-Board-with-REST-API

## Biblioteki
```
pip install -r requirements.txt
```

## Działanie

Obrazy `19x32` px są umieszczane w katalogu `input`. Po wykonaniu skryptu `letter_tool.py` są tworzone tablice na podstawie bitmap. Wynikowe tablice są zapisywane jako gotowy kod języka C w plikach `.txt` o takiej samej nazwie jak bitmapa. Dodatkowo tworzony jest plik `all.txt` będący konkatenacją wszystkich danych wyjściowych.


## Przykład

Utworzony gotowy przykładowy zestaw znaków *A-Z 0-9* w postaci bitmap, którego użyto w głównym projekcie.
Wzorowano się na otwartym foncie [Fira Code](https://github.com/tonsky/FiraCode).
