from pygame.sprite import AbstractGroup

from src.objects import Object


class LivingObject(Object):
    __health: float

    def __init__(self, health: float, *groups: AbstractGroup):
        super().__init__(*groups)
        self.__health = health

    def do_damage(self, damage: float) -> None:
        self.__health -= damage

    def heal(self, health_boost: float) -> None:
        self.__health += health_boost

    @property
    def health(self) -> float:
        return self.__health

    @health.setter
    def health(self, health) -> None:
        self.__health = health

    def update(self, *args, **kwargs) -> None:
        super(LivingObject, self).update(*args, **kwargs)
        if self.__health <= 0:
            self.kill()
