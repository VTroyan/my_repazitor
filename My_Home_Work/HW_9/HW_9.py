from dataclasses import dataclass

# Класс данных


@dataclass
class Notebook:

    records: str
    pages: int
    name: str


class MyNotebook:

    def __init__(self, _note):
        self.note = _note

    def show_note(self):
        """
        Показывает данные из библиотеки data
        """
        print(f"Records {self.note.records}!")
        print(f"Pages {self.note.pages}!")
        print(f"Name {self.note.name}!")


note = Notebook(records="NONE", pages=100, name="Vitalii")
Nt = MyNotebook(note)
Nt.show_note()

# Класс метод и Статик метод


class User:

    def __init__(self, name, web):
        self.name = name
        self.web = web

    def get_info(self):
        print(f"{self.name} - {self.web}")

    @classmethod
    def get_info_class(cls, data):
        name, web = data
        return cls(name, web)

    @staticmethod
    def get_info_static(self):
        print(f"{self.name} - {self.web}")


user_list = ["Author", "VitaliiT.com"]
user = User.get_info_class(user_list)
user.get_info()
user.get_info_static(user)


# 4 - Попытка мета класса
# class User(metaclass=type):
#     def __init__(self):
#         print("Constanta")
#         super().__init__()
