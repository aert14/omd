import random


def log(params: str) -> object:
    """Dec. factory for logging."""
    def decorator(func):
        """Decorator for logging."""
        def wrapper(self,*args, **kwargs):
            """Wrapper for logging."""
            if "bake" in func.__name__: # если bake, то время зависит от размера
                if self.size == "L":
                    time = random.randint(1, 5)
                else:
                    time = random.randint(5, 10)

            elif "deliver" in func.__name__: # если deliver, то время больше
                time = random.randint(10, 20)
            else: # если pickup, то время меньше
                time = random.randint(1, 5)
            print(params.format(time))

        return wrapper
    return decorator
