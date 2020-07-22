from bs4 import BeautifulSoup
import requests
import urllib3
#Gather Ps4 Games played
#All this information can be taken from playstation's in house API

Game_to_country = {
 "Grand Theft Auto V": ("USA"),
 "Uncharted 4: A Thief's End": ("Panama", "USA", "Italy", "Scotland","Madagascar"), 
 "Marvel's Spider-Man": ("USA"),
 "The Witcher 3: Wild Hunt": ("Velen","Novigrad"),
 "God of War": ("Midgard"),
 "The Last of Us Remastered": ("USA"),
 "Horizon Zero Dawn": ("USA"),
 "Gran Turismo Sport": ("USA", "Belgium", "France", "Italy", "Spain", "Brazil", "Austria", "Mexico"),
 "The Last of Us Part II": "USA",
 "NieR: Automata": "Japan",
 "BioShock Remastered": "Rapture",
 "BioShock Infinite: The Complete Edition": "Columbia",
 "Deus Ex: Mankind Divided": "Prague",
 "L.A. Noire": "USA",
 "Wolfenstein: The New Order": ("USA","Moon"),
 "Wolfenstein II: The New Colossus": ("USA","Venus"),
 "Call of Duty: Modern Warfare Remastered": ("Russia","Azerbaijan","Ukraine","United Kingdom"),
 "Metro 2033 Redux": "Russia",
 "Metro: Last Light Redux": "Russia",
 "Metro Exodus": "Russia",
 "Control": "USA",
 "Battlefield 4": ("Azerbaijan","China","Russia","Singapore"),
 "Outlast": "USA",
 "Outlast 2": "USA",
 "Assassin's Creed Unity": "France",
 "Hitman": ("France","Italy","Kingdom of Morocco","Thailand","USA","Japan"),
 "Doom": ("Mars","Hell"),
 "DOOM Eternal": ("Mars", "Argent D'Nur","Urdak","Fortress of Doom","Phobos","USA"),
 "Call of Duty: Modern Warfare": ("United Kingdom","Moldova","Russia","Georgia"),
 #"Monster Hunter: World":
 "Final Fantasy VII Remake": ("Gaia"),
 "Persona 5":("Japan"),
 "Detroit: Become Human": ("USA"),
 "Death Stranding": ("USA"),
 "FIFA 18":("Brazil","England"),
 "Killzone Shadow Fall": ("Vekta"),
 "Metal Gear Solid V: The Phantom Pain":("Afghanistan","Republic of Zaire"),
 "Call of Duty: Black Ops III": ("Ethiopia","Singapore","Egypt","Switzerland"),
 "Infamous Second Son": ("USA"),
 "Yakuza Kiwami": ("Japan"),
 "Yakuza Kiwami 2":("Japan"),
 "Judgment":("Japan"),
 "Yakuza: Like a Dragon":("Japan"),
 "Yakuza 6":("Japan"),
 "Yakuza 0":("Japan"),
 "Yakuza 5":("Japan"),
 "Yakuza 4":("Japan"),
 "Yakuza 3":("Japan"),
 "Nioh":("Japan"),
 "Destiny 2": ("The Sun", "Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn","Nessus"),
 "Final Fantasy XV": ("Eos"),
 "Titanfall 2": ("The Frontier"),
 "Battlefield 1": ("France","Egypt","Iraq","Germany")
}

#print(Game_to_country)


def Data_Generator(nametext):
    Game_List =[]
    Games_to_country_TRUE = []
    list_of_countries = []

    UserName = nametext
    link = "https://psnprofiles.com/"+UserName
    html_content = requests.get(link).text
    soup = BeautifulSoup(html_content,"lxml")
    #print(soup.prettify())
    name1 = ""
    #print(soup.title)
    #print(soup.title.txt)
    for link in soup.find_all("a"):
        #if name1 != "Platinum, not 100%":
        #    name1 = link.text
        #    print(link.text)
        #else:  
        #    Game_List.append(link.text)
        
        if name1 != "Platinum, not 100%":
            name1 = link.text
            #print(link.text)
        else:
            name2 = link.text
            if name2 == "See Benefits":
                Game_List.pop(0)
                break
            else:
                if "\n" not in name2:
                    Game_List.append(link.text)
        
    #print(Game_List)


    for game in Game_List:
        if game in Game_to_country.keys():
            Games_to_country_TRUE.append((game,Game_to_country.get(game)))

    #print(Games_to_country_TRUE)

    countries_dict = {}

    for values in Games_to_country_TRUE:
        if type(values[1]) == str:
            #print(values[1])
            if values[1] not in countries_dict.keys():
                countries_dict.update({values[1]: 1})

                #
                #Country_to_game_list.append()
                #
                #countries_dict[values[1]]: 1
            elif values[1] in countries_dict.keys():
                countries_dict[values[1]] += 1

                

        else:
            for countries in values[1]:
                #print(countries)
                if countries not in countries_dict.keys():
                    countries_dict[countries]: 1
                    countries_dict.update({countries: 1})
                elif countries in countries_dict.keys():
                    countries_dict[countries] += 1


    def Sort(sub_li):
        sub_li.sort(key = lambda x: x[1], reverse=True) 
        return sub_li 

    dictlist = []
    for key, value in countries_dict.items():
        temp = [key,value]
        dictlist.append(temp) 

    list_of_countries = Sort(dictlist) 
    countrygamedictionary = {}

    my_inverted_dict = dict()
    for key, value in Game_to_country.items():
        if len(value) > 1 and type(value) is tuple:
            for i in value:
                my_inverted_dict.setdefault(i, list()).append(key)
        else:
            my_inverted_dict.setdefault(value, list()).append(key)


    #print(my_inverted_dict)

    gl = []
    #list not taking values of seperate identities 
    for nation in list_of_countries:
        if nation[0] in list(my_inverted_dict.keys()):
            for game in Game_List:
                if game in list(my_inverted_dict.get(nation[0])):
                    if game not in gl:
                        gl.append([nation[0],game])
                    else:
                        gl[nation[0]].append(game)

    nl = dict()
    for value in gl:
        if value[0] in nl:
            nl[value[0]].append(value[1]) 
        else:
            nl[value[0]] = [value[1]]

    ndicd = []
    for key, value in nl.items():
        temp = [key,value]
        ndicd.append(temp)       
    #print(ndicd) 
    #print(len(countries_dict))
    #print(gl)
    if len(list_of_countries) >= 1:
        return list_of_countries, ndicd, Game_List, len(countries_dict)
    else:
        return False
        
    #return c1,c2,c3,c4,c5,c6,c7,c8,c9,c10 

Data_Generator("Asq4_")

    
    



