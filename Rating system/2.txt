import json

class Rating:

    def __init__(self):
        self.dictionary = {}

    def initialize_dictionary(self, file):

        with open(file) as datafile:
            data = datafile.read()
        Information = json.loads(data)
        for rating in Information:
            self.dictionary[rating["Name"]] = []

    def give_rating(self, book_name, user_name: str, number: int):
        if len(self.dictionary) == 0:
            pass
        else:
            #self.dictionary[book_name].append({user_name: number})
            self.dictionary[book_name].append({user_name : number})

    def assess_ratings(self):
        average = 0
        sum = 0

        for i in self.dictionary:
            print(i)
            print(self.dictionary[i])
            #sum += self.dictionary[i]["name"]
        if len(self.dictionary[i]) > 0:
            average = sum / len(self.dictionary[i])
            return average
        else:
            return 0
    
    def get_data(self, file):

        with open(file) as datafile:
            data = datafile.read()
        Information = json.loads(data)
        for rating in Information:
            self.dictionary[rating["Name"]] = rating["Rating"]

    def set_data(self, data):
        with open("test3.json", "w") as datafile:
            json.dump(self.dictionary, datafile)

    def assess_given(self, ratings: list):
        average = 0
        sum = 0
        for number in ratings:
            sum += number
        average = sum / len(ratings)
        return average
        

#def all_ratings(ratings: list):

    #def __str__(self):
        #return self.dictionary

if __name__ == "__main__":
    rating = Rating()
    rating.initialize_dictionary("testi2.json")
    rating.give_rating("Eloquent Javascript", "kalle", 2)
    rating.get_data("testi.json")
    print(rating.assess_ratings())
    #print(rating)