import numpy as np

def sigmoid(x: list | float) -> np.ndarray | float:
    """
    Returns the sigmoid value for a scalar or each element of a list.
    """
    # Write code here
    ans=np.array(x)
    ans=1+np.exp(-ans)
    ans=1/ans
    return ans