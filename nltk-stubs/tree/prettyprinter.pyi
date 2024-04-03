from _typeshed import Incomplete

__all__ = ['TreePrettyPrinter']

class TreePrettyPrinter:
    def __init__(self, tree, sentence: Incomplete | None = None, highlight=()) -> None: ...
    @staticmethod
    def nodecoords(tree, sentence, highlight): ...
    def text(self, nodedist: int = 1, unicodelines: bool = False, html: bool = False, ansi: bool = False, nodecolor: str = 'blue', leafcolor: str = 'red', funccolor: str = 'green', abbreviate: Incomplete | None = None, maxwidth: int = 16): ...
    def svg(self, nodecolor: str = 'blue', leafcolor: str = 'red', funccolor: str = 'green'): ...
