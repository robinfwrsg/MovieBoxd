watchlist=[]
watchedlist=[]
def add_movies(movie):
    watchlist.append(movie)
    print(f"{movie} has been added to your watchlist")
def watched_movies(film,rate):
    watchedlist.append((film, rate))
    print(f"{film} has been added, your rating :{rate}")

def view_watched():
    if not watchedlist:
        print("No movies watched yet")
    else:
        print(" Your watched movies:")
        for index, (movie,rate)in enumerate(watchedlist, start=1):
            print(f"{index}. {movie} - {rate}/10")

def view_movies():
    if not watchlist:
        print("No movies added yet")
    else:
        print("Your watchlist:")
        for index, movie in enumerate(watchlist,start=1):
            print(f"{index}. {movie}")
def remove_movie(index):
    if 0<=index<len(watchlist):
        removed= watchlist.pop(index)
        print(f"The movie {removed} has been removed")
    else:
        print("Invalid index")
    
while True:
        print("Welcome to MovieBoxd")
        print("1.Add Movie")
        print("2.View your Watchlist")
        print("3.Remove a movie")
        print("4.Rate a movie")
        print("5.View watched movies")
        print("6.Exit")
        
        choice=int(input("Enter your choice:"))
        if choice ==1:
            movie=input("Enter the Movie's Name:")
            add_movies(movie)
        elif choice==2:
            view_movies()
        elif choice==3:
            view_movies()
            try:
                delete_movie= int(input("Movie you want removed:"))
                remove_movie(delete_movie-1)
            except ValueError:
                print("Movie unavailable")
        elif choice==6:
            print("Your have exited the MovieBoxd")
            break
        elif choice==4:
            movie=input("Add the Movie you want to rate:")
            rate=input("Enter your rating for the movie:")
            watched_movies(movie, rate)
        elif choice==5:
            view_watched()
        else:
            print("Wrong choice, Try again :)")

