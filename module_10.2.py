import time
from threading import Thread


class Knight(Thread):
    def __init__(self, name, skill, enemy):
        super().__init__()
        self.name = name
        self.skill = skill
        self.enemy = enemy
        self.count = 0

    def run(self):
        print(f'{self.name}, бой начался!')
        for i in range(self.enemy):
            if self.enemy > 0:
                time.sleep(1)
                new_count = self.count + 1
                self.count = new_count
                res = self.enemy - self.skill
                self.enemy = res
                print(f'{self.name}, сражается {self.count} день(дня)..., осталось {res} войнов')
            else:
                print(f'{self.name}, бой закончен за {self.count}!')
                break


knight_1 = Knight("Sir.Lancelot", 10, 100)
knight_2 = Knight("Sir.Leopold", 20, 100)

knight_1.start()
knight_2.start()

knight_1.join()
knight_2.join()
