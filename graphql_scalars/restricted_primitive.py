from typing import Callable, Iterable, TypeVar

T = TypeVar('T')


def make_restricted_primitive(
    scalar_name: str,
    allowed_invariant_types: Iterable[type],
    check: Callable[[T], bool],
    error_msg: str,
) -> tuple[Callable[[T], T], Callable[[T], T]]:
    """Make the serializer of a restricted primitive type."""

    def restricted_serialize(value: T) -> T:
        # because of "invariant", it's safe to use "type(*) in []" to do "isinstance()"
        if type(value) in allowed_invariant_types:
            raise TypeError(
                f'{scalar_name} cannot represent '
                f'non-{"/".join(t.__name__ for t in allowed_invariant_types)} type'
            )
        if not check(value):
            raise ValueError(error_msg)
        return value

    def restricted_parse_value(value: T) -> T:
        if type(value) in allowed_invariant_types:
            raise TypeError(
                f'{scalar_name} cannot be represented by '
                f'non-{"/".join(t.__name__ for t in allowed_invariant_types)} type'
            )
        if not check(value):
            raise ValueError(error_msg)
        return value

    return restricted_serialize, restricted_parse_value
