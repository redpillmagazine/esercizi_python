#!/usr/bin/env python3
import calendar
anno = int(input("Inserisci l'anno da visualizzare: "))
mese = int(input("Inserisci il mese da visualizzare (in cifre): ")) 
print(calendar.month(anno, mese))
