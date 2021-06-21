from dataclasses import dataclass


@dataclass
class DataTransferObject(object):
    context: str
    f_name: str
    dframe: object

    @property
    def context(self) -> str: return self._context

    @context.setter
    def context(self, context): self._context = context

    @property
    def f_name(self) -> str: return self._f_name

    @f_name.setter
    def f_name(self, f_name): self._f_name = f_name

    @property
    def dframe(self) -> object: return self._dframe

    @dframe.setter
    def dframe(self, dframe): self._dframe = dframe