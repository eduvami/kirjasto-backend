import json

class Rating:

    def __init__(self):
        self.Mean_score = {}
        self.Book_score = {}

    def initialize_Bookscore(self, file_from, file_to):

        with open(file_from) as datafile:
            data = datafile.read()
        Information = json.loads(data)
        for rating in Information:
            self.Book_score[rating["Name"]] = []

    def give_rating(self, book_name, user_name: str, number: int):
        if len(self.Book_score) == 0:
            pass
        else:
            self.Book_score[book_name].append({user_name : number})

    def assess_ratings(self):
        average = 0
        sum = 0
        for i in self.Book_score:
            for e in self.Book_score[i]:
                if len(self.Book_score[i]) > 0:
                    print("e")
                    #for key in e:
                        #print(f"{key} -> {e[key]}")
            #sum += self.Book_score[i]["name"]
        if len(self.Book_score[i]) > 0:
            average = sum / len(self.Book_score[i])
            return average
        else:
            return 0
    
    #tää pitää korjata
    # mulla on nyt kahdenlaista sanakirjaa listan sisältävä + vaan sanakirja
    # KeyError: "Don't make me think" tai KeyError: "bookname"?
    # tulostus onnistuu print(rating["Book_name"])
    # muttei tää? print(self.Book_score[rating["Book_name"]])
    
    #def get_data(self, file):

        #with open(file) as datafile:
            #data = datafile.read()
        #Information = json.loads(data)
        #for rating in Information:
            #self.Book_score[rating["Book_name"]].append({rating["Name"]: rating["Rating"]})
            #self.Book_score[rating["Book_name"]].append("1")
            #print(rating["Book_name"])
            #print(rating["Rating"])
            #print(rating["Name"])

    def set_data(self, data):
        with open("test3.json", "w") as datafile:
            json.dump(self.Book_score, datafile)

    def assess_given(self, ratings: list):
        average = 0
        sum = 0
        for number in ratings:
            sum += number
        average = sum / len(ratings)
        return average

    def get_data_from_file(self, file):

        with open(file) as datafile:
            data = datafile.read()
        Information = json.loads(data)
        #for rating in Information:
            #print(rating)
        return Information
    def set_data_to_file(self, file):

        with open(file) as datafile:
            data = datafile.read()
        Information = json.loads(data)
        #for rating in Information:
            #print(rating)
        return Information

#def all_ratings(ratings: list):

    #def __str__(self):
        #return self.Book_score

if __name__ == "__main__":
    rating = Rating()
    rating.initialize_Bookscore("test2.json", "test3.json")
    rating.give_rating("Eloquent Javascript", "kalle", 2)
    print(rating.get_data_from_file("test.json"))
    #rating.get_data("test.json")
    print(rating.assess_ratings())