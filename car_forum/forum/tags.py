def tags(func):
    def wrapper(msg):
        return f"<{func}> {msg} </{func}>"
    return wrapper
