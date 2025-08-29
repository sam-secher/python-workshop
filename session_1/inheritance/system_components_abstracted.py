from abc import ABC, abstractmethod

from common.constants import ComponentConstants


class Component(ABC):
    """Abstract base for electrical components."""

    def __init__(self, efficiency: float, model: str) -> None:
        if not (0 < efficiency <= 1):
            msg = "efficiency must satisfy 0 < η ≤ 1 (per-unit)."
            raise ValueError(msg)
        self.model = model
        self._efficiency = efficiency

    def real_power_efficiency(self) -> float:
        """Compute real power efficiency (%)."""
        return self._efficiency

    @abstractmethod
    def component_name(self) -> str:
        """Return the name of the component."""

    @abstractmethod
    def calculate_p_loss(self, s_in: float) -> float:
        """Calculate power loss over component."""

    @abstractmethod
    def calculate_q_demand(self, s_in: float) -> float:
        """Calculate reactive power demand over component."""

class PCS(Component):
    """Class to represent a PCS."""

    def __init__(self, efficiency: float | None=None, model: str="Envision") -> None:

        efficiency_to_use = efficiency if efficiency is not None else ComponentConstants.PCS.EFFICIENCY_DEFAULT
        super().__init__(efficiency_to_use, model)

    def component_name(self) -> str:
        return "PCS"

    def calculate_p_loss(self, s_in: float) -> float:
        raise NotImplementedError

    def calculate_q_demand(self, s_in: float) -> float:
        raise NotImplementedError

class Cable(Component):
    """Class to represent a cable."""

    def __init__(self, voltage_level: str, material: str, efficiency: float | None=None) -> None:
        self.voltage_level = voltage_level
        self.material = material
        self.efficiency = self._get_default_efficiency() if efficiency is None else efficiency
        super().__init__(self.efficiency, material)

    def _get_default_efficiency(self) -> float:
        material_dict = ComponentConstants.Cable.DEFAULT_EFFICIENCY_BY_MATERIAL.get(self.material)
        if material_dict is None:
            err_msg = f"Cable efficiency not known for material {self.material}"
            raise ValueError(err_msg)

        default_efficiency = material_dict.get(self.voltage_level)
        if default_efficiency is None:
            err_msg = f"Cable efficiency not known for voltage level {self.voltage_level}"
            raise ValueError(err_msg)

        return default_efficiency

    def calculate_p_loss(self, s_in: float) -> float:
        raise NotImplementedError

    def calculate_q_demand(self, s_in: float) -> float:
        raise NotImplementedError

    def component_name(self) -> str:
        return f"{self.voltage_level} Cable"

    @staticmethod
    def get_not_present_default(voltage_level: str, material: str) -> "Cable":
        return Cable(voltage_level, material, 1.0)


class Transformer(Component):
    """Class to represent a transformer."""

    def __init__(self, voltage_level: str, transformer_standard: str, efficiency: float | None=None, impedance: float | None=None) -> None:
        self.voltage_level = voltage_level
        self.transformer_standard = transformer_standard

        # Set impedance to a default value if not provided at object creation.
        efficiency, impedance = (
            self._get_default_efficiency_and_impedance()
            if (efficiency is None or impedance is None)
            else (efficiency, impedance)
        )

        self.impedance = impedance

        super().__init__(efficiency, transformer_standard)

    def _get_default_efficiency_and_impedance(self) -> tuple[float, float]:
        standard_dict = ComponentConstants.Transformer.EFFICIENCY_BY_STANDARD.get(self.transformer_standard)
        if standard_dict is None:
            err_msg = f"Unknown transformer standard {self.transformer_standard}"
            raise ValueError(err_msg)

        efficiency = standard_dict.get(self.voltage_level)
        if efficiency is None:
            err_msg = f"Unknown transformer efficiency for voltage level {self.voltage_level}"
            raise ValueError(err_msg)

        impedance = ComponentConstants.Transformer.IMPEDANCE_BY_VOLTAGE_LEVEL.get(self.voltage_level)
        if impedance is None:
            err_msg = f"Unknown transformer impedance for voltage level {self.voltage_level}"
            raise ValueError(err_msg)

        return efficiency, impedance

    def component_name(self) -> str:
        return f"{self.voltage_level} Transformer"

    def calculate_p_loss(self, s_in: float) -> float:
        raise NotImplementedError

    def calculate_q_demand(self, s_in: float) -> float:
        raise NotImplementedError

    @staticmethod
    def get_not_present_default(voltage_level: str, transformer_standard: str) -> "Transformer":
        # Set impedance to 0 and efficiency to 1 if transformer is not present.
        return Transformer(voltage_level, transformer_standard, 1.0, 0.0)
