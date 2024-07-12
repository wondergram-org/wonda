from typing_extensions import Generic

from wonda.tools.text.styling.abc import ABCStyle, E


class StyleChain(ABCStyle[E], Generic[E]):
    def __init__(self, *styles: ABCStyle[E]) -> None:
        self.styles = list(styles)

    def __add__(self, style: "ABCStyle[E] | StyleChain[E]") -> "StyleChain[E]":
        """
        Add a style to a chain. If a style chain is given,
        combine both together.
        """
        if isinstance(style, StyleChain):
            return StyleChain(*self.styles, *style.styles)

        return StyleChain(*self.styles, style)

    def __repr__(self) -> str:
        return f"StyleChain({', '.join(repr(style) for style in self.styles)})"

    def to_entities(self) -> list[E]:
        """
        Convert a chain to a list of actionable entity objects.
        """
        entity_list = []
        cursor = 0

        for style in self.styles:
            entities = style.to_entities()
            text = style.to_string()

            for entity in entities:
                entity.offset += cursor

            cursor += len(text)
            entity_list.extend(entities)

        return entity_list

    def to_string(self) -> str:
        return "".join(style.to_string() for style in self.styles)
