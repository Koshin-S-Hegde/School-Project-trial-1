import random
from typing import Type
import singleton_decorator
from src.game_objects import GameObject


@singleton_decorator.singleton
class GameObjectHandler:
    __game_objects: dict[int, GameObject]

    def __init__(self) -> None:
        self.__game_objects = dict()

    def add_game_object(self, game_object: GameObject, object_id: int = None) -> int:
        if object_id is None:
            object_id = random.randint(100000, 1000000000)

        self.__game_objects[object_id] = game_object

        return object_id

    def get_object_by_id(self, object_id: int) -> GameObject:
        """
        Use this to get a game_object if id is know.
        WARNING:- This raises a KeyError if object_id does not exist
        """
        try:
            return self.__game_objects[object_id]
        except KeyError:
            raise KeyError(f"GameObject with {object_id} does not exist")

    def get_object_by_type(self, object_type: Type[GameObject]) -> list[GameObject]:
        required_game_objects: list[GameObject] = list()
        for game_object in self.__game_objects.values():
            if isinstance(game_object, object_type):
                required_game_objects.append(game_object)

        return required_game_objects
