from typing import Optional, List, Union
from typing_extensions import AnyStr
import torch
def func(a: int, b: Optional[int] = None, c: List[int] = None) -> str:
    """Function with optional and default arguments.
    Args:
        a (int): First argument.
        b (Optional[int]): Second argument, optional.
        c (List[int]): Third argument, default to empty list.
    Returns:
        str: A string.
    """
    print(a, b, c)
    return "a"


def func2(a: Optional[int], b: Optional[int], c: Optional[int]) -> int:
    """Function with default arguments.
    Args:
        a (Optional[int]): First argument, default to None.
        b (Optional[int]): Second argument, default to None.
        c (Optional[int]): Third argument, default to None.
    Returns:
        int: The sum of a, b, and c.
    """
    return a + b + c

class Transform:
    def forward(
        self, 
        x: torch.Tensor,
        y: Optional[torch.Tensor] = None
    ) -> torch.Tensor:
        if y is None:
            y = torch.zeros_like(x)
        return x + y

def func3(a:int, b:Optional[int] = 0) -> int:
    return a + b

print(func3(1, 2))
print(func3(1))

def func4(a:List[Union[int, float, str]], b:Dict[str, AnyStr]) -> List[Union[int, float]]:
    """
    Args:
        a (List[Union[int, float, str]]): A list of integers, floats, and strings.
    Returns:
        List[Union[int, float]]: A list of integers and floats.
    """
    return [1, 'a']

ans=func4([1, 2, 'a'])
print(ans)
