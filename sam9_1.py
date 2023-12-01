class Tomato:
    states = {'отсутствует': 0, 'цветение': 1, 'зеленый': 2, 'красный': 3}

    def __init__(self, index):
        self._index = index  # защищенный атрибут
        self._state = self.states['отсутствует']    # защищенный атрибут

    def grow(self):
        self._state += 1

    def is_ripe(self):
        if self._state == 3:
            return True
        else:
            return False


class TomatoBush:
    def __init__(self, num):
        self.tomatoes = [Tomato(index) for index in range(num)]

    def grow_all(self):
        for tomato in self.tomatoes:
            tomato.grow()

    def all_are_ripe(self):
        for tomato in self.tomatoes:
            if not (tomato.is_ripe()):
                return False
        return True

    def give_away_all(self):
        self.tomatoes = None


class Gardener:
    def __init__(self, name, plant: TomatoBush):
        self.name = name  # Публичный атрибут
        self._plant = plant  # Защищенный атрибут

    def work(self):
        self._plant.grow_all()

    def harvest(self):
        if self._plant.all_are_ripe():
            self._plant.give_away_all()
        else:
            print('Не все томаты еще созрели')

    @staticmethod
    def knowledge_base():
        print('Справка')
        print('Дана настоящая в том, что садовник являлся с 1964 года по день смерти 21 января 2003\n '
              'года членом садоводческого некоммерческого товарищества "Восход", находящегося в массиве Васкелово\n '
              'Всеволожского района Ленинградской области. Садовник по праву частной собственности\n '
              'принадлежали возведённые в соответствии с Уставом садовый дом и надворные постройки, '
              'которые расположены на участке № 10 вышеуказанного садоводческого некоммерческого товарищества\n '
              '"Восход" Земельный участок, на котором находятся названные строения, являлся собственностью садовника.\n'
              'Задолженностей по членским, целевым взносам и налогам за садовником в садоводческом\n '
              'некоммерческом товариществе не значится.')


Gardener.knowledge_base()
tomatoBash1 = TomatoBush(5)
gardener1 = Gardener('ivan', tomatoBash1)
gardener1.work()
gardener1.harvest()
gardener1.work()
gardener1.work()
gardener1.harvest()
