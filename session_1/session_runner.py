# Setting up development environment

# • IDE: VSCode / Cursor
# • Extensions incl:
#   - Linter (Ruff or Black + mypy), set as default formatter then SHIFT + ALT + F (demo on system_configuration.py)
#   - .gitignore, pyproject.toml, launch.json, environment.yml

import math

from common.constants import ComponentConstants
from session_1.inheritance.system_components_abstracted import PCS, Cable, Component, Transformer


class SessionRunner:
    def __init__(self) -> None:
        self.system_components = self._initialise_components()

    def _initialise_components(self) -> list[Component]:
        return [
            Cable(voltage_level=ComponentConstants.Cable.Voltage.LV_DC, material=ComponentConstants.Cable.Material.COPPER),
            PCS(0.99, "ENV-3450"),
            Cable(voltage_level=ComponentConstants.Cable.Voltage.LV_AC, material=ComponentConstants.Cable.Material.COPPER),
            Transformer(voltage_level=ComponentConstants.Transformer.Voltage.LV_MV, transformer_standard=ComponentConstants.Transformer.Standard.EU_ECOSIGN),
            Cable.get_not_present_default(voltage_level=ComponentConstants.Cable.Voltage.MV, material=ComponentConstants.Cable.Material.COPPER),
        ]

    def run(self) -> None:
        self.demo_inheritance()

    def demo_inheritance(self) -> None:
        system_repr = "DC Block --> " + "".join([f"{component.component_name()} --> " for component in self.system_components]) + "PCC (33kV)"
        dc_to_ac_efficiency = math.prod([component.real_power_efficiency() for component in self.system_components])

        print(f"System:\n{system_repr}")
        print(f"DC to AC efficiency: {dc_to_ac_efficiency:.3g}")

# Possible future sessions:
# - Features of Python language (comprehensions, generators/iterators, set vs list vs tuple, dunder methods)
# - Paradigms of programming (functional, object-oriented, procedural, etc)
# - Writing performant code (profiling, memory usage, vectorised operations with Pandas/NumPy etc)
# - Web development (APIs, serverless functions, web frameworks, relational and non-relational databases)
# - Back-end with AWS (Lambda, S3, Cognito, EC2)
# - DevOps on GitHub (CI/CD, task boards, Actions, GitHub Pages, how to code review, repo policies)
# - Event-driven architecture (producers/consumers, queues, message buses, data push services)
# - Data science (Gradient descent, SVMs, neural networks, popular libraries)
# - Data engineering (ETL, data pipelines, data lakes, data warehouses)
# - Take-home challenges (refactoring tasks, small projects e.g. create a web dashboard, LeetCode/HackRank style problems)
