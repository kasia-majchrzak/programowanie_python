from datetime import datetime

from modules.FirmaSpozywcza import FirmaSpozywcza
from modules.Kurs import Kurs
from modules.Odcinek import Odcinek
from modules.Pojazd import Pojazd

mercedes_vito = Pojazd('Mercedes-Benz', 'Vito', 2018, 210546.86, 150, 1000)
katowice_czestochowa = Odcinek('Katowice', 'Częstochowa', 88.565, 5)
czestochowa_lodz = Odcinek('Częstochowa', 'Łódź', 106.565, 5)
firma_spozywcza = FirmaSpozywcza('Food', 'Katowice, ul. Długa 5', '438320974', 'food@gmail.com', 678492747,
                                 datetime(2019, 11, 21, 8, 0, 0))
kurs = Kurs('Kowalski Jan', 'Katowice, ul. Długa 5', 'Łódź, ul. Kościuszki 54', datetime(2021, 11, 25, 6, 0, 0),
            datetime(2021, 11, 25, 11, 0, 0), mercedes_vito, firma_spozywcza, [katowice_czestochowa, czestochowa_lodz],
            800)

print(kurs)

