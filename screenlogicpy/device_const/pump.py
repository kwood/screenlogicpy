from ..const import SLIntEnum
from ..const.common import SLValueRange


class PUMP_TYPE(SLIntEnum):
    NONE = 0
    INTELLIFLO_VF = 1
    INTELLIFLO_VS = 2
    INTELLIFLO_VSF = 3

    @property
    def title(self) -> str:
        return self._title().replace("Intelliflow", "IntelliFlow")


class PUMP_RANGE:
    RPM = SLValueRange(450, 3450)
    GPM = SLValueRange(15, 130)
