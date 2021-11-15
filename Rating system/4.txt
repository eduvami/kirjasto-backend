import json

class Rating:

    def __init__(self):
        self.Mean_score = {}
        self.Book_score = {}

    def give_rating(self, book_name, user_name: str, number: int):
        if book_name not in self.Book_score:
            self.Book_score[book_name] = []
        if user_name not in self.Mean_score:
            self.Mean_score[user_name] = []

        self.Book_score[book_name].append({user_name : number})
        self.Mean_score[user_name].append({book_name : number})

    #kaikkien kirjojen yhteinen rating
    def assess_overall_book_ratings(self):
        average = 0
        sum = 0
        for i in self.Book_score:
            for e in self.Book_score[i]:
                if len(self.Book_score[i]) > 0:
                    for key in e:
                        sum += e[key]

        if len(self.Book_score) > 0:
            average = sum / len(self.Book_score)
            return f"Overall book rating: {average}"
        else:
            return 0

    def assess_book_rating(self, book_name):
        average = 0
        sum = 0
        count = 0
        for i in self.Book_score:
            if i == book_name:
                count += 1
                for e in self.Book_score[i]:
                    if len(self.Book_score[i]) > 0:
                        for key in e:
                            sum += e[key]
        if count > 0:
            average = sum / count
            return f"{book_name}: {average}"
        else:
            return 0

    def assess_overall_mean_score(self):
        average = 0
        sum = 0
        for i in self.Mean_score:
            for e in self.Mean_score[i]:
                if len(self.Mean_score[i]) > 0:
                    for key in e:
                        sum += e[key]
        if len(self.Mean_score) > 0:
            average = sum / len(self.Mean_score)
            return f"Overall meanscore: {average}"
        else:
            return 0
    
    def assess_mean_rating(self, user_name):
        average = 0
        sum = 0
        count = 0
        for i in self.Mean_score:
            if i == user_name:
                count += 1
                for e in self.Mean_score[i]:
                    if len(self.Mean_score[i]) > 0:
                        for key in e:
                            sum += e[key]
        if count > 0:
            average = sum / count
            return f"{user_name}: {average}"
        else:
            return 0

    #toimii oikein
    #pitää viel muokkaa oikeeseen muotoon
    #pitää kattoo onnistuuko dumpin kans
    def set_data(self, file, data):
        with open(file, "w") as datafile:
            json.dump(data, datafile)

    def assess_given(self, ratings: list):
        average = 0
        sum = 0
        for number in ratings:
            sum += number
        average = sum / len(ratings)
        return average

    #pitää miettii miten säilyttää tietoja
    #missä on uusimmat tiedot vai liikkuuko kokoajan
    def get_data_from_file(self, file):

        with open(file) as datafile:
            data = datafile.read()
        Information = json.loads(data)
        #for rating in Information:
            #print(rating)
        return Information

    #Pitää miettii haluuko siirtää tiedostosta toiseen tietoja
    def set_data_to_file(self, file):

        with open(file) as datafile:
            data = datafile.read()
        Information = json.loads(data)
        #for rating in Information:
            #print(rating)
        return Information
    
    def get_mean_info(self):
        return self.Mean_score

    def get_book_info(self):
        return self.Book_score

if __name__ == "__main__":
    rating = Rating()
    rating.give_rating("Eloquent Javascript", "Petteri", 2)
    rating.give_rating("Eloquent Javascript", "Saana", 2)
    rating.give_rating("Don't make me think", "Petteri", 2)

    print(rating.get_data_from_file("test.json"))
    ##rating.get_data("test.json")

    rating.set_data("tryout.json", rating.get_mean_info())
    rating.set_data("tryout2.json", rating.get_book_info())

    #print(rating.assess_book_rating("Eloquent Javascript"))
    #print(rating.assess_overall_book_ratings())
    #print(rating.assess_overall_mean_score())
    #print(rating.assess_mean_rating("Petteri"))
    #print(rating.get_book_info())
    #print(rating.get_mean_info())