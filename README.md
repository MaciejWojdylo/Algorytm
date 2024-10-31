Jest to program który zawiera dwa algorytmy porównujące ciągi znaków oparte na Algorytmach  Needleman-Wunsch i Smith-Waterman
Program jest podzielony na dwa foldery każdy z nich zawiera implementacje algorytmu taką jak nazywa się folder
w każdym folderze można znaleźć 2 pliki:
1 to skrypt który uruchomiony może zostać zarówno poprzez IDE np.Pycharm lub z wiersza poleceń 
2 to plik zawierający przykładowe 2 sekwencje testowe jakie wykorzystywaliśmy do tworzenia naszych algorytmów

1.Przygotowanie plików
Sekwencje które chcemy porównać muszą być napisane w formacie FASTA.

np.
 '>'Nazwa_Sekwencji
   Przykładowa sekwencja
 '>'Nazwa_Drugiej_Sekwencji
   Przykładowa druga sekwencja

Program nasz obsługuje tylko 2 sekwencje podanie tutaj większej ilości spowoduje braku wyniku dla innych sekwencji prócz pierwszej i drugiej.
Nasz program nie dopuszcza różnicy wielkości znaków to znaczy że małe i duże litery będą tak samo traktowane 
Nasz program nie wymaga zapisania sekwencji w jednej lini mogą one być rozdzielone na mniejsz fragmenty przy zachowaniu formatu fasta.
Nasz program nie wykrywa błędów spowodowanych błędnym wprawadzeniem danych np. jeżeli gdzieś przypadkowo dodamy literke program nie będzie działał zgodnie z naszymi oczekiwaniami dodatkowo program dopuszcz możliwość innych znaków prócz A,T,C,G i ma to wpływ na wynik

Poradnik jak uruchomić program 
a)Uruchamiamy program w IDE np. PyCharm
1.Należy w programie PyCharm ściągnąć repozytorium
2.Należy wybrać katalog z Algorytmem jaki nas interesuje 
3.Należy wybrać plik SW.py lub NW.py w zależności od wybranego folderu.
4.Wybór Plik
  a)Jeżeli nie chcemy zmieniać kodu możemy przy pomocy dowolnego edytora tekstu zmienić plik seq1.fasta który znajduje się w kazdym folderze z Algorytmem
  b)Jeżeli chcemy wybrać inny plik musimy zmienić go w kodzie konkretnie linijke parser.add_argument("-i", "--input", default="seq1.fasta", help="Ścieżka do pliku FASTA") i należy zmienić default na ścieżke do pliku z którego odczytamy dane 
5.Po odpaleniu skryptu pojawi nam się w folderze roboczym plik result.txt lub output w którym jest zapisana nasza odpowiedź 

b)Uruchamiamy program z lini poleceń  
po przejściu do folderu z interesujacym nas algorytmem w którym znajduje się  plik SW.py albo NW.py należy wpisać komende python SW.py lub NW.py -h lub --help to otwiera nam pomoc jakie przełączniki są dostępe wraz z opisem co robią 
jeśli nie podamy nic program domyślnie ustawi wartości gap missmatch oraz match na wartości kolejno -2 -1 1 a także wybierze nam plik seq1.fasta a wynik da do pliku result.txt lub output który będzie w tym samym folderze
przykładowa komenda uruchomienia naszego skryptu python SW.py -i "ścieżka pliku wejściowego" -o "ścieżka do folderu gdzie zostanie zapisana nasza odpowiedź" -g -2 -mm -1 -m 1 

Opis Algorymtów jako iż są to bardzo podobne ALgorytmy skupimy się na samej koncepcji  gdyż jest ona podobna różnice są dopiero na samym końcu które zostaną wyróżnione niżej
Nasz algorytm odczytuje z lini poleceń parametry i wartości jakie podaliśmy przy braku jakiegokolwiek parametru zostanie on ustawiony na domyślny 
1. Odczytuje plik podany lub domyślny i zapisuje dane do tablicy
2. Przypisujemy wartości parametrów do zmeinnych o tej samej nazwie np -g lub --gap podana wartość zostanie zapisana do zmiennej gap i analogicznie z resztą przełączników
3. Zostaje utworzona tablica dwuwymairowa na podstawie zmiennych row i collumn które odpowiadają długości naszych sekwencji i dodajemy +1 do każdej zmiennej ponieważ nasza macież musi mieć pierwszy wiersz i pierwszą kolumnę już odpowiednio wypełnioną
  3.1 w przypadku algorymtmu SW pierwszy wiersz i pierwsza kolumna jest wypełniona samymi zerami gdyż algorytm ten w przypadku wartości ujemnych wpisuje 0
  3.2 w przypadku algorymtmu NW pierwszy wiersz i pierwsza kolumna jest wypełniona kolenymi wartościami pomniejszonymi o gap licząc od zera np w przypadku gdy gap = -2 wtedy nasz wiersz i kolumna będą pokolei przyjmować wartości 0,-2,-4,-6,-8 itd do długości i szerkokości macierzy 
4. Zgodnie z algorytmem macierz zostaje wypełniona mianowicie 2 pętle i oraz j zaczynając od komórki 1,1 gdzie nasz algorytm sie rozpoczyna bierze maksymalną wartość z komórki lewej, od góry i po lewej przekątnej.
I wyciaga z nich wartości maksymalne zmienione o gap lub missmatch lub match i wprowadza do naszej obecnie analizowanej komórki
5. Po uzupełnieniu całej macierzy program w pętli odtwarza ścieżke i zapisuje wyniki do dwóch zmiennych dokładając kolejne znaki lub "-" w przypadku gap
   5.1.algorytm NW zaczyna swoje odtwarzanie ścieżki od prawej dolnej komórki
   5.2 algorytm SW zaczyna swoje odtwarzanie ścieżki od największej wartości jaka występuje w macierzy
6. Po utworzeniu ścieżki nasze zmienne zostają odwrócone a i zapisane do pliku  
