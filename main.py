from datetime import datetime

from modules.Dieta import Dieta
from modules.Dietetyk import Dietetyk
from modules.Pacjent import Pacjent
from modules.Zamowienie import Zamowienie

pacjent = Pacjent(1, "Jan", "Kowalski",
                  datetime(1968, 1, 25),
                  ["orzechy", "laktoza"])
dietetyk = Dietetyk(2, "Adam", "Nowak",
                    datetime(1964, 2, 12),
                    datetime(2016, 6, 1))
dieta1 = Dieta(1, "Dieta specjalna",
               "Dieta wyłączająca nabiał oraz orzechy",
               "Dieta bez laktozy",
               4, 1800, 5.99, 30)
dieta2 = Dieta(2, "Dieta wegetariańska",
               "Dieta wyłączająca mięso",
               "Dieta wegetariańska",
               5, 1700, 7.25, 30)

zamowienie = Zamowienie()
zamowienie.id = 1
zamowienie.pacjent = pacjent
zamowienie.dietetyk = dietetyk
zamowienie.diety = [dieta1, dieta2]
zamowienie.data_zamowienia = datetime.now()
print(zamowienie)
