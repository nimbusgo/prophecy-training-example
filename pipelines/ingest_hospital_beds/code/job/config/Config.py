from prophecy.config import ConfigBase


class Config(ConfigBase):

    def __init__(self, INPUT_DATE: str=None):
        self.spark = None
        self.update(INPUT_DATE)

    def update(self, INPUT_DATE: str="2020_03_30"):
        self.INPUT_DATE = INPUT_DATE
        pass
