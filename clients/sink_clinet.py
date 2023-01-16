from abc import ABCMeta, abstractmethod


class SinkClient(metaclass=ABCMeta):

    @abstractmethod
    def upload_file(self, remote, local):
        return NotImplemented
