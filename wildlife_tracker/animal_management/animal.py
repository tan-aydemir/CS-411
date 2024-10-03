from typing import Any, Optional

class Animal:
    def __init__(
            self, 
            animal_id: int, 
            species: str,
            health_status: Optional[str] = None, 
            age: Optional[int] = None):
        self.animal_id = animal_id
        self.age = age
        self.health_status = health_status
        self.species = species

    def register_animal(self, Animal) -> None:
        pass

    def update_animal_details(self, **kwargs: Any) -> None:
        pass

    def remove_animal(self) -> None:
        pass

