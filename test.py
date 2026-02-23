class ME:
    def __init__(self, my_name, my_age, my_cat):
        self.my_name = my_name
        self.my_age = my_age
        self.my_cat = my_cat

    def my_fav_cat (self):
        print (f"{self.my_cat}")

da = ME("Dima", "18", "Chupa")
da.my_fav_cat()
