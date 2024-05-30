class Person:
    def __init__(self, name, age, birth_date, address, id_card, username, password):
        self._name = name
        self._age = age
        self._birth_date = birth_date
        self._address = address
        self._id_card = id_card
        self.__username = username
        self.__password = password
    def get_user_info(self):
        return self.__username, self.__password
    def change_password(self, current_password, new_password):
        if current_password == self.__password:
            self.__password = new_password
            print("Password changed")
        else:
            print("Error")
    def forgot_password(self):
        return "Salom"

user = Person("Saidkabr", 20, "10-02-2004", "Tajikistan", "12345678", "s_boistov", "salom")

current_password = input("Enter password: ")
new_password = input("Enter new password: ")
user.change_password(current_password, new_password)




