class AbstractAuto:
    def move(self):
        raise NotImplementedError

    def pull_over(self):
        raise NotImplementedError


class Buss(AbstractAuto):
    def move(self):
        return "I'm moving"

    def pull_over(self):
        return "I'm pulling over"
