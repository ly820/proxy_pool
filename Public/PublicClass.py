from configparser import ConfigParser

class ConfigParse(ConfigParser):
    """
    rewrite ConfigParser, for support upper option
    """

    def __init__(self):
        super(ConfigParse,self).__init__()

    def optionxform(self, optionstr):
        return optionstr