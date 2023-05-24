movies = ['Seal team', 'John wick', '13 hours of Benghazi', 'Friends']

print(movies[1]) #returns the second indexed item on the list
print(movies[0]) #returns the first item on the list
print(movies[1:3]) #returns the first indexed number on the list untill the last number
print(movies[1:]) #returns the first number on the index list untill the last number
print(movies[:1]) #returns only the first item on the list
print(movies[-1]) #returns the last item on the list

print(len(movies)) #count the numbers of items on a list

movies.append('Six')
print(movies) #appends to the end of the list

movies.insert(2, 'Peaky Blinders')
print(movies) #Adds the movie peaky blinders to the second index on the list

movies.pop()
print(movies) #removes the last item on the list

movies.pop(0)
print(movies) #removes the first indexed item on the list

#INDEXES START COUNTING FROM 0 TO THE LAST NUMBER AND THINS ALSO INCLUDES CONTING SPACES.

Diasy_movies = ['Shreck forever after', 'Minions', 'Kirikuu']
our_favourite_movies = movies + Diasy_movies
print(our_favourite_movies) #Combines the two lists made

grades = [['Bob',78],['Alice', 71], ['Jane', 34]]
Bobs_grades = grades [0][1]
print(Bobs_grades) #returns bobs grade only

grades[0][1] = 29
print(grades) #Appends Bobs grade and prints the whole new list