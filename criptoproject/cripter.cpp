#include <iostream>
#include <string>

#include <random>

using namespace std;

int get_random(int min, int max)
{
    random_device rd;
    mt19937 gen(rd());
    uniform_int_distribution<> dist(min, max);

    int numero = dist(gen);

    return numero;
}

void cripter1(string p, string fin)
{

    // funzione che cripta i dati di tipo 1, uso di valori randomici da 1 a 10 e con verifica del apri o del dipsari;
    // pref !!!!ffff_
    // suff meta ::

    int min = 0;
    int max = 9;
    int provv = 0;

    for (int i = 0; i < p.length(); i++)
    {

        if (p[i] == 'a')
        {
            provv = get_random(min, max);
            if (provv % 2 == 0)
            {
                fin[i] = '!'; // punto di domanda
            }
            else
            {
                fin[i] = '"'; // uso virgoletta singola
            }
        }

        if (p[i] == 'b')
        {
            provv = get_random(min, max);
            if (provv % 2 == 0)
            {
                fin[i] = '='; // i accentata
            }
            else
            {
                fin[i] = ')'; // è accentata dritta
            }
        }

        if (p[i] == 'c')
        {
            provv = get_random(min, max);
            if (provv % 2 == 0)
            {
                fin[i] = '^'; // ele potenza
            }
            else
            {
                fin[i] = '?'; // punto domanda
            }
        }

        if (p[i] == 'd')
        {
            provv = get_random(min, max);
            if (provv % 2 == 0)
            {
                fin[i] = '&'; // i accentata
            }
            else
            {
                fin[i] = '$'; // è accentata dritta
            }
        }
    }

    return;
}

int main()
{
    string in = "abcd";
    string pluto;
    string fin;

    cripter1(in, fin);
    return 0;
}