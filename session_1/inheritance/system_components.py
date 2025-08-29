class PCS:
    """Class to represent a PCS."""

    def __init__(self, efficiency: float, model: str) -> None:
        self.efficiency = (
            efficiency
            if efficiency is not None
            else 0.985
        )
        self.model = model


class Cable:
    """Class to represent a cable."""

    def __init__(self, voltage_level=None, material=None, efficiency=None, not_present=False) -> None:
        self.voltage_level = voltage_level
        self.material = material
        self.not_present = not_present

        if self.not_present:
            self.efficiency = 1.0
        elif efficiency is None:
            if self.voltage_level == "LV_DC" and self.material == "Copper":
                self.efficiency = 0.9975
            elif self.voltage_level == "LV_DC" and self.material == "Aluminium":
                self.efficiency = 0.995
            elif self.voltage_level == "LV_AC":
                self.efficiency = 1.0
            elif self.voltage_level == "MV" and self.material == "Copper":
                self.efficiency = 0.997
            elif self.voltage_level == "MV" and self.material == "Aluminium":
                self.efficiency = 0.995
            elif (self.voltage_level == "HV" and self.material == "Copper") or (self.voltage_level == "HV" and self.material == "Aluminium"):
                self.efficiency = 0.997
            else:
                raise ValueError("Non-standard cable voltage level or material")
        else:
            self.efficiency = efficiency


class Transformer:
    """Class to represent a transformer."""

    def __init__(self, voltage_level: str | None=None, transformer_standard: str | None=None, efficiency: float | None=None, impedance: float | None=None, not_present: bool=False) -> None:
        self.voltage_level = voltage_level
        self.transformer_standard = transformer_standard
        self.not_present = not_present

        # Set impedance to 0 and efficiency to 1 if transformer is not present.
        if self.not_present:
            self.impedance = 0.0
            self.efficiency = 1.0
        else:
            # Set impedance to a default value if not provided at object creation.
            if impedance is None:
                if self.voltage_level == "LV/MV":
                    self.impedance = 0.09
                elif self.voltage_level == "MV/HV":
                    self.impedance = 0.16
                else:
                    raise ValueError("Non-standard transformer voltage level")
                # warnings.warn(f'impedance set to default for {self.voltage_level}: {self.impedance}')
            else:
                self.impedance = impedance

            # Set efficiency to a default value based on voltage level and location, if not provided at object creation.
            if efficiency is None:
                if self.voltage_level == "LV/MV" and self.transformer_standard == "EU Ecodesign":
                    self.efficiency = 0.9938
                elif self.voltage_level == "LV/MV" and self.transformer_standard == "China (GB)":
                    self.efficiency = 0.99
                elif self.voltage_level == "MV/HV" and self.transformer_standard == "EU Ecodesign":
                    self.efficiency = 0.997
                elif self.voltage_level == "MV/HV" and self.transformer_standard == "China (GB)":
                    self.efficiency = 0.995
                else:
                    raise ValueError("Non-standard transformer voltage level or standard")
            else:
                self.efficiency = efficiency