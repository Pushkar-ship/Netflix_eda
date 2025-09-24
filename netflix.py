import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('netflix_titles.csv')

df = pd.DataFrame(data)



df['director']= df['director'].fillna('Unknown')
#df['cast'] = df['cast'].fillna('Unknown')
df['country'] = df['country'].fillna('Unknown')
df['date_added'] = df['date_added'].fillna('Unknown')
df['rating'] = df['rating'].fillna('Unrated')
df['duration'] = df['duration'].fillna('Unknown')

#print(df.isnull().sum())

unknown_country_titles = df[df['country']=='Unknown']

#------------------------------------------------------------------------------------------------------------------------------------
#unknown_titles_release_year = unknown_country_titles['release_year'].value_counts()

#unknown_titles_release_year = unknown_titles_release_year[unknown_titles_release_year.index >= 1980]

#missing_country = df['country'].value_counts()['Unknown']
#plt.figure(figsize=(10,10))
#plt.bar(unknown_titles_release_year.index, unknown_titles_release_year.values, align='center', width=.8, color='#008000')
#plt.xticks(rotation=90)
#plt.title('Lost origins of Movies $ TV Shows')
#plt.ylabel('Number of Movies & TV Shows')
#plt.xlabel('Release Year')
#plt.show()
#------------------------------------------------------------------------------------------------------------------------------------

#unknown_movies_ratings = unknown_country_titles['rating'].value_counts()
#plt.figure(figsize=(10,10))
#plt.bar(unknown_movies_ratings.index, unknown_movies_ratings.values, align='center', width=.8, color='#0096c7')
#plt.title('Unknown Movie & TV Shows Ratings')
#plt.xlabel('Ratings')
#plt.ylabel('No. of movies & TV Shows')
#plt.xticks(rotation=90)
#plt.show()

#------------------------------------------------------------------------------------------------------------------------------------

#types_over_year = df.groupby(['release_year', 'type']).size().unstack(fill_value=0)
#types_over_year = types_over_year[types_over_year.index>1980]
#plt.figure(figsize=(12,6))
#plt.plot(types_over_year.index,types_over_year['Movie'], color = '#3a86ff')
#plt.plot(types_over_year.index, types_over_year['TV Show'], color = '#ffbe0b')
#plt.grid(True)
#plt.legend(['Movie','TV Show'])
#plt.title('Trends of Movies & TV Shows Production')
#plt.xlabel('Year')
#plt.ylabel('No. of Movies & TV Shows')
#plt.show()

#------------------------------------------------------------------------------------------------------------------------------------

#plt.figure(figsize=(10,10))
#producer = df['country'].value_counts().head(10)
#plt.bar(producer.index, producer.values, color='#00bbf9')
#plt.xticks(rotation=45)
#plt.xlabel('Country')
#plt.ylabel('No. of Movies & TV Shows')
#plt.title('Top 10 Movies & TV Shows Producer')
#plt.show()

#------------------------------------------------------------------------------------------------------------------------------------

#df = df.dropna(subset=['director'])
#best_director = df['director'].value_counts().head(10)
#plt.figure(figsize=(10,10))
#plt.bar(best_director.index,best_director.values, color="#9b5de5")
#plt.xticks(rotation=45)
#plt.title('Top 10 Directors')
#plt.xlabel('Name')
#plt.ylabel('No. of Movies & TV Shows')
#plt.show()

#------------------------------------------------------------------------------------------------------------------------------------

#movies = df[df['type']=='Movie'].copy()

#movies["duration_minutes"] = movies['duration'].str.extract(r'(\d+)').astype(float)
#plt.figure(figsize=(10,10))
#plt.hist(movies['duration_minutes'], bins=30, color ='#FCA6A7', edgecolor='#230102')
#plt.title('Range of Movie Duration')
#plt.xlabel('Movie Duration')
#plt.ylabel('No. of movies')
#plt.xlim(0,240)
#plt.show()

#------------------------------------------------------------------------------------------------------------------------------------

#plt.figure(figsize=(6,6))
#type_counts = df['type'].value_counts()
#plt.pie(type_counts, labels=type_counts.index, autopct='%1.1f%%', colors=['#EDE569','#90e0ef'])
#plt.title('Movies VS TV Shows')
#plt.axis('equal')
#plt.show()

#------------------------------------------------------------------------------------------------------------------------------------
df= df.dropna(subset=['listed_in'])
actors = df['listed_in'].value_counts().head(10)
plt.bar(actors.index,actors.values, align='center', alpha=0.5)
plt.xticks(rotation=45)
plt.show()