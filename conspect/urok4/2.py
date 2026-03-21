class Hello:
    def __init__(self):
        print("Hello")


class Hello_world(Hello):
    def __init__(self):
        super().__init__()
        print("end")


first = Hello_world()
 