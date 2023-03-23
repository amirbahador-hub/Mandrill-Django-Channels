from dataclasses import dataclass


class Event(list):
    def __call__(self, *args, **kwargs):
        for item in self:
            item(*args, **kwargs)

@dataclass
class EmailEvent:
    data: dict
    actions = Event() # observer pattern

    def broadcast(self) -> None:
        self.actions(self.data)

