class Man:
    def __init__(self, name, age, country):
        """Create a man with name, age, and living country"""
        self._name = name
        self.age = age
        self.country = country

    @property
    def name(self):
        """Man cannot change his name, it is prohibited"""
        return self._name

    def change_country(self, new_country):
        """Here is an opportunity for human to change country"""
        if self.country == new_country:
            print(f'Hey, you are already live in {self.country}')
        else:
            print(f'{self.name} change his country from {self.country} to {new_country}')
            self.country = new_country

    def grew_up(self, new_age):
        """Called to change the man age. It works like 'growing up', so human cannot reduce his age"""
        if new_age > self.age:
            self.age = new_age
            print(f'Oh, {self.name} has grown up, now he is {self.age}')
        else:
            print('Hey, something wrong happened, man cannot reduce his age')


class Worker(Man):

    def __init__(self, name, age, country, company, position, salary):
        """We describe the man as a worker. He work in company on some position and receive a salary"""
        super().__init__(name, age, country)
        self.company = company
        self.position = position
        self.salary = salary

    def __repr__(self):
        return f'{self.__class__.__name__}(Name = {self.name}, Age = {self.age}, ' \
               f'Country = {self.country}, Company = {self.company!r}, Position = {self.position}, ' \
               f'Salary = {self.salary}.'

    def __str__(self):
        return f'Man {self.name} work in the {self.company!r} at position -- {self.position}. ' \
               f'He is {self.age} years old and live in the beautiful country - {self.country}. ' \
               f'He receive a {self.salary} USD per month'


class Family(Man):
    def __init__(self, name, country, age, wife, children, pet):
        """Man has a family: wife, child, and a pet"""
        super().__init__(name, country, age)
        self._wife = wife
        self._children = children
        self.change_pet(pet)

    @property
    def wife(self):
        """Man cannot change his wife, it is prohibited"""
        return self._wife

    @property
    def children(self):
        """Man cannot change his child, it is prohibited"""
        return self._children

    def change_pet(self, new_pet):
        """Here is some info about pet"""
        self.pet = new_pet
        return f'{self.pet} is a pet'

    def __str__(self):
        return f'{self.name} is a family guy. Hi has a beautiful wife {self.wife} and a little child {self.children}.' \
               f'Also an important member of this family is {self.pet}. '


if __name__ == '__main__':
    ...
