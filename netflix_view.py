#!/usr/local/bin/python3
import os
import csv

class Netflix:

    def __init__(self):
        self.file = self._find_viewing_history()
        self.shows = []
        self._get_unique_shows()

    def length(self):
        print("Number Of Unique Shows Watched: " + str(len(self.shows)))

    def list_shows(self):
        for show in set(self.shows):
            print(show)

    def output(self):
        with open(self.output_file, "w+") as file:
            for show in self.shows:
                file.write(f"{show}\n")

    def _get_unique_shows(self):
        with open(self.file) as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            for row in csv_reader:
                 show = row[0].split(':')[0]
                 self.shows.append(show)
            self.shows = set(self.shows)
            return set(self.shows)

    def _find_viewing_history(self):
        for root, dirs, files in os.walk(os.getenv('HOME')):
            for file in files:
                if file.startswith("NetflixViewingHistory"):
                    self.output_file = os.path.join(root, "NetflixIndividualViewingHistory.csv")
                    return os.path.join(root, file)


if __name__ == "__main__":
    netflix = Netflix()
    netflix.length()
    netflix.output()