def cache(func):
    def wrapper(num):
        if not wrapper.log.get(num):  # 0(1)
            wrapper.log[num] = func(num)

        return wrapper.log[num]

    wrapper.log = {}

    return wrapper

