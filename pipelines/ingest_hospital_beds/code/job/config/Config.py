from prophecy.config import ConfigBase


class Config(ConfigBase):

    def __init__(self, fabricName: str=None, INPUT_DATE: str=None):
        self.spark = None
        self.update(fabricName, INPUT_DATE)

    def update(self, fabricName: str, INPUT_DATE: str):
        self.fabricName = fabricName
        self.INPUT_DATE = INPUT_DATE
