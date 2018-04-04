#!/usr/bin/env python3


from common import imp


class Config:

    __instance = None

    def __new__(cls, *args, **kwargs):
        if Config.__instance is None:
            Config.__instance = object.__new__(cls)
        return Config.__instance

    def __init__(self, **kwargs):
        self.__dict__.update(kwargs)
        for k, v in self.__dict__.items():
            setattr(Config, k, v)

    @staticmethod
    def load(**kwargs):
        if Config.__instance is None:
            return Config(**kwargs)
        Config.__init__(Config.__instance, **kwargs)

    @staticmethod
    def loadApp(appname):
        Config.load(**imp(Config.NAME['CONF'], 'CONFIG', appname))

    def __setattr__(self, name, value):
        if name not in self.__dict__:
            self.__dict__[name] = value

    @staticmethod
    def items():
        return Config.__instance.__dict__.items()


if __name__ == '__main__':
    c = Config(name='Kyo', age=17)
    print(c.name, c.age)
    print(Config.name, Config.age)

    Config.load(name="kyo", age=17)


