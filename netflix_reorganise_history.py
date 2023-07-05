# This code rearanges the standard netflix history file to a more readable file
# It identifies the series and movies and sort it on name.

# 2023-07-05 Gaston M


import pandas as pd


#---------------------------------------------------------------------------- Initialise ----
# read existing csv file with stock prices 
df_all=pd.read_csv('NetflixViewingHistory.csv', encoding ='utf-8',  index_col=False,
                        decimal="," )  

df_all['Date'] = pd.to_datetime(df_all['Date'], format='%d-%m-%y')



# Remove empty titles 
df_all = df_all[~(df_all['Title'] == (" "))]

#-----  Getting the movies  and clean the data ----------------------------- MOVIES ----

# Filter all rows which do not contain a :
df_movies = df_all[~df_all['Title'].str.contains(":")]


# Sort on title.
df_movies=df_movies.sort_values(by=['Title'])
df_movies['Type']= "movie"



#-----  Getting the series and clean the data ------------------------------ SERIES ----

#Filter all entries on one or two :
df_series = df_all[df_all['Title'].str.contains(":")]
df_series= df_series.sort_values(by=['Title'])

df_series.Title= df_series.Title.str.split(':').str[0]

# Groepeer de title 
df_series = df_series.groupby(df_series['Title'], as_index=False).last()

df_series['Type']= "serie"
df_series.reset_index

#--------------------------------------------------------------------------- Finishing touch ----
# Combine the dataframes
df_out = pd.concat([df_series,df_movies], ignore_index=True)
df_out= df_out.sort_values(by=['Title'])

df_out.to_csv('NetflixViewingHistory_out.csv', header=True, index=0)


