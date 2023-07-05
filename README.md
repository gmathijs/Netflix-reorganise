# netflix reorganise history

Anyone can download their NETFLIX viewing history from their profile. You get a a CSV file which you can open with Excel or Numbers (on Mac)

This project is more for me to be get aquinted with Visual Code python and using github.
The list which Netflix creates has a lot of data and for series each episode is given. 
But since I just wanted to see the series name and the movie name, I thoughed this was a nice project to practice my python and pandas skils

The python code (netflix_reorganise_history.py) reads the standard netflix file called NetflixViewingHistory.csv and outputs a csv file 
called NetflixViewingHistory_out.csv. 
I have addded a column called type, so you can filter. For each serie the serie name is given. This way the reorganized file is more compact and easier to search in.
In the random example given the original file has 3171 rows, the reorganized file has 751 rows.

Todo: I want each serie listed followed by season number 
