using Aukcja;
using System;
using System.Collections.Generic;

class Program
{
    static void Main(string[] args)
    {

        // Lista przedmiotów
        List<Przedmiot> przedmioty = new List<Przedmiot> {
            new Przedmiot(1, "Konsola Playstation 5", "Elektronika", 2899, true),
            new Przedmiot(2, "Smartfon Samsung Galaxy S21", "Elektronika", 2999, false),
            new Przedmiot(3, "Smartwatch Apple Watch Series 6", "Elektronika", 1799, true),
            new Przedmiot(4, "Laptop Lenovo Legion 5", "Elektronika", 5299, false),
            new Przedmiot(5, "Kamera Sony Alpha 7 III", "Fotografia", 7999, false),
            new Przedmiot(6, "Książka Czysty kod", "Książki", 49, true)
        };

        // Lista kart kredytowych
        List<KartaKredytowa> karty = new List<KartaKredytowa> {
            new KartaKredytowa("Mastercard", "0001", 5000),
            new KartaKredytowa("Visa", "0002", 3000),
            new KartaKredytowa("American Express", "0003", 8000),
            new KartaKredytowa("Discover", "0004", 10000)
        };

        // Pętla główna programu
        while (true)
        {
            Console.WriteLine("Co chcesz zrobić?");
            Console.WriteLine("1. Kupić przedmiot");
            Console.WriteLine("2. Sprzedać przedmiot");
            Console.WriteLine("3. Wyjść z programu");
            int wybor = Convert.ToInt32(Console.ReadLine());

            switch (wybor)
            {
                case 1: // Kupno przedmiotu
                    Console.WriteLine("Dostępne przedmioty:");

                    // Sortowanie przedmiotów: najpierw wyróżnione, potem alfabetycznie
                    przedmioty.Sort((x, y) => {
                        if (x.Wyrozniony && !y.Wyrozniony) return -1;
                        else if (!x.Wyrozniony && y.Wyrozniony) return 1;
                        else return x.Nazwa.CompareTo(y.Nazwa);
                    });

                    // Wyświetlenie listy przedmiotów
                    foreach (var przedmiot in przedmioty)
                    {
                        Console.WriteLine($"{przedmiot.Id}. {przedmiot.Nazwa} ({przedmiot.Kategoria}) - {przedmiot.Cena} PLN");
                    }

                    // Wybór przedmiotu do kupienia
                    Console.WriteLine("Podaj numer przedmiotu, który chcesz kupić:");
                    int idPrzedmiotu = Convert.ToInt32(Console.ReadLine());
                    Przedmiot wybranyPrzedmiot = przedmioty.Find(p => p.Id == idPrzedmiotu);

                    // Sprawdzenie poprawności numeru karty kredytowej
                    Console.WriteLine("Podaj numer karty kredytowej:");
                    string numerKarty
