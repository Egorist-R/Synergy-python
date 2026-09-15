desyatki_tysyach, tysyachi, sotni, desyatki, edinicy = input().split()

desyatki_tysyach = int(desyatki_tysyach)
tysyachi         = int(tysyachi)
sotni            = int(sotni)
desyatki         = int(desyatki)
edinicy          = int(edinicy)

stepen = desyatki ** edinicy
umnozhenie = stepen * sotni
raznost = desyatki_tysyach - tysyachi

rezultat = umnozhenie / raznost

print(rezultat)
