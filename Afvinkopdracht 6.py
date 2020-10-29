def leesinhoud(enzymen_bestand):
    """Leest het bestand en zet het in een lijst en stuurt het terug naar main

    Input:
    enzymen_bestand - str - bestand met restrictie enzymen
    
    Output:
    restrictie_enzymen - list - lijst met restrictie enzymen
    """

    restrictie_enzymen = []
    try:
        with open(enzymen_bestand, "r") as bestand_open:     
            for regel in bestand_open:                                   
                regel = regel.strip()                                    #Elke regel in het bestand wordt gelezen en de enters worden verwijderd
                restrictie_enzymen += [regel.replace("^", "")]           #De regels worden toegevoegd aan de aangemaakte lijst en het 'dakje' wordt verwijderd

            return restrictie_enzymen                                    #De lijst wordt teruggestuurd naar de main
     except IOError
         print("Het bestand kan niet worden gevonden")
     except:
         print("Onbekende fout")



def match(seq, enzymen):                                             #De sequentie en de lijst met enzymen worden als parameters geaccepteerd
    """Checkt of de enzymen knippen in de sequentie knippen

    Input:
    seq - str - de sequentie
    enzymen - list - lijst met de restrictie enzymen                

    """

    try:
        for i in enzymen:
            naam, enzym = i.split()                                      #Er wordt op spatie gesplit waardoor de naam van het enzym en het deel waar die in knipt apart worden opgeslagen in variablen
            if enzym in seq:                                             #Er wordt gezocht naar een match en de positie van de match wordt opgeslagen in een variable
                positie = seq.index(enzym)                                  
                print("De sequentie matcht met het enzym" , naam, "op positie", positie)
                print(seq)
                print(enzym)
    except IndexError:
        print("Index bestaat niet")
    except:
        print("Onbekende fout")
        

if __name__ == "__main__":
    enzymen_bestand = "enzymen.txt"
    restrictie_enzymen = leesinhoud(enzymen_bestand)
    sequentie = "ACTAGCAACCTCAAACAGACACCATGGTGCACCTGACTCCTGTGGAGAAGTCTGCCGTTACTGCCCTGTGGGGCAAGGTGAACGTGGATGAAGTTGGTGGTGAGGCC"
    match(sequentie, restrictie_enzymen)                         
