# 7. Dla chętnych Stworzyć skrypt pythonowy, który połączy się z API, które zawiera
# informacje o browarach (dokumentacja
# https://www.openbrewerydb.org/documentation).
# Należy w pythonie zrobić klasę Brawery , która będzie zawierała takie atrybuty jakich
# dostarcza API wraz z odpowiednim typowaniem.
# W klasie należy zaimplementować magiczną metodę __str__ która będzie
# opisywała dane przechowywane w obiekcie.
# Skrypt ma się połączyć do API i pobrać 20 pierwszych obiektów, a następnie
# utworzyć listę 20 instancji klasy Brawery , którą przeiteruje i wyświetli każdy obiekt z
# osobna.

import Brawery
import json
import urllib.request
contents = urllib.request.urlopen("https://api.openbrewerydb.org/breweries").read()


brawery_list = json.loads(contents)