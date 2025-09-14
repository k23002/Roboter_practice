class View:
    def get_user_name(self):
        return input("robota: 名前を教えてください。\n")
    
    def Recommend_restaurant(self, name, restaurant):
        return input(f"robota:{name}さん、私のおすすめは{restaurant}です。\nこのレストランは好きですか？[Yes/No]\n").strip().upper()
    
    def get_restaurant_name(self, name):
        return input(f"robota: {name}さん、おすすめのレストランの名前を教えてください。\n")
    
    
    def finish_application(self, name):
        return print(f"robota: {name}さん、ありがとうございました。良い1日を！さようなら。\n")