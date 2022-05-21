# Making Class of two popular Music Producers Alan Walker & Marshmello
class MusicArtist_AlanWalker:
    def __init__(self,name,age,dob,pop_songs):
        self.name = name
        self.age = age
        self.dob = dob
        self.pop_songs = pop_songs


    def AlanWalker_Details(self):
        print("Airtist:",self.name)
        print("Airtist's Age:",self.age)
        print("Airtist's Date of Birth:",self.dob)
        print("Airtist's Popular Songs:",self.pop_songs)

A1 = MusicArtist_AlanWalker('Alan Olav Walker',24,'24/08/1997','Faded,Spectre,Force,Ignite,On my Way,etc')


class MusicArtist_Marshmello:
    def __init__(self,name,age,dob,pop_songs):
        self.name = name
        self.age = age
        self.dob = dob
        self.pop_songs = pop_songs


    def Marshmello_Details(self):
        print("Airtist:",self.name)
        print("Airtist's Age:",self.age)
        print("Airtist's Date of Birth:",self.dob)
        print("Airtist's Popular Songs:",self.pop_songs)

M1 = MusicArtist_Marshmello('Christopher Comstock',30,'19/05/1992','Alone,Summer,Friends,Power,Happier,Stars,etc')

fav_edm_producer = input("Which one is your Favourite: Alan Walker or Marshmello: ")

if fav_edm_producer == "Alan Walker":
    print(A1.AlanWalker_Details())
elif fav_edm_producer == "Marshmello":
    print(M1.Marshmello_Details())
else:
    print("Incorrect Name!")

    






        