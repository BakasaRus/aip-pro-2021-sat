class A:
    class __B:
        pass

    def __init__(self):
        A.__B()


test = A.__B()
