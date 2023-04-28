import string


class Alphabet:
    def __init__(self, lang, letters):
        self.lang = lang
        self.letters = letters

    def print_(self):
        print(self.letters)

    def letters_num(self):
        print(len(self.letters))


class EngAlphabet(Alphabet):
    __letters_num = 26

    def __init__(self):
        self.lang = 'En'
        self.letters = string.ascii_uppercase

    def is_en_letter(self, letter):
        letter = letter.upper()
        if letter in self.letters:
            print("It's english letter")
        else:
            print("It's not english letter")

    def letters_num(self):
        print(self.__letters_num)

    @staticmethod
    def example():
        print('To be, or not to be, that is the question:\n'
              'Whether ’tis nobler in the mind to suffer\n'
              'The slings and arrows of outrageous fortune,\n'
              'Or to take arms against a sea of troubles\n'
              'And by opposing end them. To die—to sleep,\n'
              'No more; and by a sleep to say we end\n'
              'The heart-ache and the thousand natural shocks\n'
              'That flesh is heir to: ’tis a consummation\n'
              'Devoutly to be wish’d. To die, to sleep;\n'
              'To sleep, perchance to dream—ay, there’s the rub:\n'
              'For in that sleep of death what dreams may come,\n'
              'When we have shuffled off this mortal coil,\n'
              'Must give us pause—there’s the respect\n'
              'That makes calamity of so long life.')


en_alph = EngAlphabet()
en_alph.print_()
en_alph.letters_num()
en_alph.is_en_letter('f')
en_alph.is_en_letter('Щ')
EngAlphabet.example()


class Tomato:
    states = ['green', 'yellow', 'red']

    def __init__(self):
        self._state = self.states[0]

    def grow(self):
        index = self.states.index(self._state)
        index += 1
        self._state = self.states[index]

    def is_ripe(self):
        if self.states.index(self._state) == 2:
            print('Tomato is ripe')
        else:
            print("Tomato isn't ripe")


class TomatoBush:

    def __init__(self, tomato_quantity):
        self.tomatoes = []
        quantity = 1
        while tomato_quantity >= quantity:
            self.tomatoes.append(Tomato())
            quantity += 1

    def grow_all(self):
        for i in self.tomatoes:
            i.grow()

    def all_is_ripe(self):
        for i in self.tomatoes:
            self.answer = []
            if i.states.index(i._state) == 2:
                self.answer.append(1)
            else:
                self.answer.append(0)
        if 0 not in self.answer:
            return True
        else:
            return False

    def give_away_all(self):
        self.tomatoes.clear()


class Gardener:
    def __init__(self, name, tomato_amount):
        self.name = name
        self.tomato_amount = tomato_amount
        self._plants = TomatoBush(self.tomato_amount)

    def work(self):
        self._plants.grow_all()

    def harvest(self):
        if self._plants.all_is_ripe():
            self._plants.give_away_all()
            print('Harvest was done))')
        else:
            print('Plants are not ripe yet!')

    @staticmethod
    def knowledge_base():
        print('Growing tomatoes can be as quick and easy as cutting open a tomato and chucking the seeds into a sunny\n'
              'patch of soil. I have a friend who grows a vegetable garden in exactly that way. Whenever she prepares\n'
              'food, anything that has a seed is scattered into the small garden patch outside the side door of her \n'
              'home. While she waters every day or two, that is all she does. Over the years, some seeds have taken, \n'
              'including two or three tomato bushes.')


Gardener.knowledge_base()
worker = Gardener('Ivan', 8)

worker.work()
worker.harvest()
worker.work()
worker.harvest()
