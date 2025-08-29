from typing import ClassVar


class ComponentConstants:
    class Cable:
        """Constants for cables."""

        class Material:
            """Materials for cables."""

            COPPER = "Copper"
            ALUMINIUM = "Aluminium"

        class Voltage:
            """Voltage levels for cables."""

            LV_DC = "LV_DC"
            LV_AC = "LV_AC"
            MV = "MV"
            HV = "HV"

        DEFAULT_EFFICIENCY_BY_MATERIAL: ClassVar[dict[str, dict[str, float]]] = {
            Material.COPPER: {
                Voltage.LV_DC: 0.9975,
                Voltage.LV_AC: 1.0,
                Voltage.MV: 0.997,
                Voltage.HV: 0.997,
            },
            Material.ALUMINIUM: {
                Voltage.LV_DC: 0.995,
                Voltage.LV_AC: 1.0,
                Voltage.MV: 0.995,
                Voltage.HV: 0.997,
            },
        }

    class Transformer:
        """Constants for transformers."""

        class Voltage:
            """Voltage levels for transformers."""

            LV_MV = "LV/MV"
            MV_HV = "MV/HV"

        class Standard:
            """Standards for transformers."""

            EU_ECOSIGN = "EU Ecodesign"
            CHINA_GB = "China (GB)"

        IMPEDANCE_BY_VOLTAGE_LEVEL: ClassVar[dict[str, float]] = {
            Voltage.LV_MV: 0.09,
            Voltage.MV_HV: 0.16,
        }

        EFFICIENCY_BY_STANDARD: ClassVar[dict[str, dict[str, float]]] = {
            Standard.EU_ECOSIGN: {
                Voltage.LV_MV: 0.9938,
                Voltage.MV_HV: 0.997,
            },
            Standard.CHINA_GB: {
                Voltage.LV_MV: 0.99,
                Voltage.MV_HV: 0.995,
            },
        }

    class PCS:
        """Constants for PCS."""

        EFFICIENCY_DEFAULT = 0.985
