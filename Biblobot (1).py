#FINAL PROJECT

#FIRST DOING MLA BIBLIOGRAPHY

#BIBLOBOT

#Elise Schatzki-McClain



listSource = []


def addSource():

    answer = input("What kind of source is this? (BOOK, MAGAZINE, NEWSPAPER, WEBSITE, JOURNAL, FILM)")

    if answer in ["BOOK", "Book", "book"]:
        createBook()

    if answer in ["MAGAZINE", "Magazine", "magazine"]:
        createMagazine()

    if answer in ["NEWSPAPER", "Newspaper", "newspaper"]:
        createNewspaper()

    if answer in ["WEBSITE", "Website", "website"]:
        createWebsite()

    if answer in ["JOURNAL", "Journal", "journal"]:
        createJournal()

    if answer in ["FILM", "Film", "film"]:
        createFilm()

def createWebsite():

    source = {}

    source["sourcetype"] = "website"

    
    #titles
    articletitle = input("Article Title: ")
    source["articletitle"] = articletitle

    #authors last name
    firstname = input("Author's First Name: ")
    source["authorfirstname"] = firstname

    lastname = input("Author's Last Name: ")
    source["authorlastname"] = lastname

    #online info
    url = input("URL: ")
    source["url"] = url

    #date published
    day = input("Day: ")
    source["day"] = day
    
    month = input("Month: ")
    source["month"] = month
    
    year = input("Year: ")
    source["year"] = year

    #date accessed
    day_accessed = input("Day Accessed: ")
    source["day"] = day_accessed
    
    month_accessed = input("Month Accessed: ")
    source["month"] = month_accessed
    
    year_accessed = input("Year Accessed: ")
    source["year"] = year_accessed
    
    listSource.append(source)
    

def createJournal():

    source = {}

    source["sourcetype"] = "journal"


    #titles
    articletitle = input("Article Title: ")
    source["articletitle"] = articletitle
    
    journaltitle = input("Journal Title: ")
    source["journaltitle"] = journaltitle

    #authors last name
    firstname = input("Author's First Name: ")
    source["authorfirstname"] = firstname

    lastname = input("Author's Last Name: ")
    source["authorlastname"] = lastname

    #publishing info
    volume = input("Volume: ")
    source["volume"] = volume
    
    edition = input("Edition: ")
    source["edition"] = edition
                    
    series = input("Series: ")
    source["series"] = series

    year = input("Year: ")
    source["year"] = year

    #pages
    start = input("Starting Page: ")
    source["start"] = start
    
    end = input("Ending Page: ")
    source["end"] = end
        
    listSource.append(source)






def createFilm():

    
    print("hi, not ready yet, sorry")

def createNewspaper():

    source = {}

    source["sourcetype"] = "newspaper"

    #titles
    articletitle = input("Article Title: ")
    source["articletitle"] = articletitle
    
    newspapertitle = input("Newspaper/Site Title: ")
    source["newspapertitle"] = newspapertitle
    
    #authors last name
    firstname = input("Author's First Name: ")
    source["authorfirstname"] = firstname

    lastname = input("Author's Last Name: ")
    source["authorlastname"] = lastname

    #publishing info
    publisher = input("Publisher: ")
    source["publisher"] = publisher
        
    #date published
    day = input("Day: ")
    source["day"] = day
    
    month = input("Month: ")
    source["month"] = month
    
    year = input("Year: ")
    source["year"] = year

    listSource.append(source)


def createMagazine():

    source = {}

    source["sourcetype"] = "magazine"

    #titles
    articletitle = input("Article Title: ")
    source["articletitle"] = articletitle
    
    magazinetitle = input("Magazine Title: ")
    source["magazinetitle"] = magazinetitle

    #authors last name
    firstname = input("Author's First Name: ")
    source["authorfirstname"] = firstname

    lastname = input("Author's Last Name: ")
    source["authorlastname"] = lastname

    #date published
    day = input("Day: ")
    source["day"] = day
    
    month = input("Month: ")
    source["month"] = month
    
    year = input("Year: ")
    source["year"] = year

    #pages
    start = input("Starting Page: ")
    source["start"] = start
    
    end = input("Ending Page: ")
    source["end"] = end
        
    listSource.append(source)


def createBook():
    
    source = {}


    source["sourcetype"] = "book"
    
    #authors last name
    firstname = input("Author's First Name: ")
    source["authorfirstname"] = firstname

    lastname = input("Author's Last Name: ")
    source["authorlastname"] = lastname

    #Source info
    sourcetitle = input("Source title: ")
    source["sourcetitle"] = sourcetitle

    volume = input("Volume: ")
    source["volume"] = volume
    
    edition = input("Edition: ")
    source["edition"] = edition
                    
    series = input("Series: ")
    source["series"] = series

    #publication info
    publisher = input("Publisher: ")
    source["publisher"] = publisher
    
    city = input("City: ")
    source["city"] = city
    
    state = input("State: ")
    source["state"] = state
    
    year = input("Year: ")
    source["year"] = year

    listSource.append(source)


def printAPA():

    for source in listSource:
        sourcetype = source["sourcetype"]

    #(BOOK, MAGAZINE, NEWSPAPER, WEBSITE, JOURNAL, FILM)
        if sourcetype = "book":
            #Author, A. (Year of Publication). Title of work. Publisher City, State: Publisher.
            print("hi")

        if sourcetype = "magazine":
            #Author, A. (Year, month of Publication). Article title. Magazine Title, Volume(Issue), pp.-pp.
            print("hi")
            
        if sourcetype = "newspaper":
            #Author, A. (Year, Month Date of Publication). Article title. Newspaper Title, pp. xx-xx.
            print("hi")

        if sourcetype = "website":
            #Author, A. (Year, Month Date of Publication). Article title. Retrieved from URL
            print("hi")

        if sourcetype = "journal":
            #Author, A. (Publication Year). Article title. Periodical Title, Volume(Issue), pp-pp.
            print("hi")

        if sourcetype = "film":
            #Producer, A. (Producer), & Director, A. (Director). (Release Year). Title of motion picture [Motion Picture]. Country of Origin: Studio.
            print("hi")
        
def printChicago():
    print("hi, not ready yet, sorry")
        
def printMLA():
    print("hi, not ready yet, sorry")

def printBibliography(cite_style):
    


    #REFRESHER, APA, CHICAGO, or MLA
    if cite_style in ["APA", "Apa", "apa"]:
        printAPA()

    if cite_style in ["CHICAGO", "Chicago", "chicago"]:
        printChicago()

    if cite_style in ["MLA", "Mla", "mla"]:
        printMLA()

    

        


def removeSource():

    removed_source = int(input("Which number source do you want to remove? "))
    removed_source_location = removed_source - 1
    del listSource[removed_source_location]

    

def editSource():
    print("hi, not ready yet, sorry")


def Bibliography():


    cite_style = input("Which citation style are you using? (APA, Chicago, MLA) ")

    source_addition = "yes"
    while source_addition not in ["FINISH", "Finish", "finish"]:
        #change question phrasing and options
        source_addition = input("Do you want to ADD, REMOVE, or EDIT a source or FINISH your Biblobot bibliography? ")
        if source_addition in ["ADD", "Add", "add"]:
            addSource()
        if source_addition in ["REMOVE", "Remove", "remove"]:
            removeSource()
        if source_addition in ["EDIT", "Edit", "edit"]:
            editSource()
        printBibliography(cite_style)

    print(" ")
    print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>")
    print("Final Biblobot Bibliography:")
    print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>")
    print(" ")
    

    #make the bibliography into a list
    #add the list to a .txt document




def welcomeMessage():
    print("==========")
    print("Welcome to")
    print(" BIBLOBOT ")
    print("==========")
    print(" ")
    print("Lets create a bibliography!!!")



def main():
    
    welcomeMessage()
    Bibliography()



main()
