# Goals for this session:
# 1. Understand some key features of OOP
# 2. Learn how to use type hints to improve code readability and other good practice
# 3. Understand how abstraction can be used to improve code maintainability

# Setting up development environment

# • IDE: VSCode / Cursor
# • Extensions incl:
#   - Linter (Ruff or Black + mypy), set as default formatter then SHIFT + ALT + F (demo on system_configuration.py)
#   - .gitignore, pyproject.toml, launch.json, environment.yml
# • Project structure

# Object-oriented programming

# • Fundamental principle is encapsulation of state and behaviour in an object (class instance)
# • 'Class' is the blueprint for an object.
# • 'Object' is an instance of a class.
# • OOP is suitable for modelling large, complex systems and systems with many classes.
# • Note: Some languages enforce OOP, e.g. Java, but Python isn't strictly object-oriented, as it supports functional, procedural and object-oriented programming.
# • Functional and procedural are more suitable for modelling small, simple systems e.g. self-contained scripts.

# • Languages that enforce OOP tend to be statically typed, which means variable type is declared and known at compile time.
# • Python is dynamically typed, but can be made quasi-statically typed with type hints.
# • Type hints are a way to annotate variables with their type.
# • This significantly improves code readability and error detection.
# • Type hints are not enforced at runtime, so they are only a suggestion.
# • Linters e.g. Ruff and mypy can be configured to enforce (or strongly encourage) type hints.
# • Most popular libraries (e.g. Pandas, NumPy) have supporting stubs packages which can be used to type check code.

# • As well as type hints, we can improve code with:
#   - Docstrings
#   - Constants defined in a separate file instead of magic numbers
#   - Short, self-contained functions
#   - Access modifiers which indicate whether a method is public, protected or private (not enforced in Python, but good practice)

# • A core feature of OOP is abstraction, which provides an interface for classes that expose what an object can do (its contract) and hides its implementation.
#   - Inheritance allows a class to inherit attributes and methods from another class or interface.
#   - This decouples callers of the class/its functions/properties from implementation, which allows for safer refactors and extensibility.
#   - E.g. consider an abstract class that defines an interface for shapes, with a method to calculate the area.
#   - A square, circle and triangle can all inherit from this abstract class and implement the area method.
#   - This allows a caller to calculate the area of a collection of shapes without knowing the specific shape type.
#   - Note: Over-abstraction can lead to code that is difficult to understand and maintain, a balance is needed.

import math

from common.constants import ComponentConstants
from session_1.inheritance.system_components_abstracted import PCS, Cable, Component, Converter, Transformer


class SessionRunner:
    def __init__(self) -> None:
        self.system_components = self._initialise_components()

    def _initialise_components(self) -> list[Component]:
        return [
            Converter(0.995, "ENV-3450"),
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

# Not covered (asked at start):
# - Using properties for dynamically calculated values (Andrew)
# - Deep-dive on current codebase and how we can improve it. Focus on augmentation code (Emerald)
# - Perspectives on using AI tools in code (Cursor, browser LLMs). How much should we rely on them for code? For research?

# Possible future sessions:
# - Features of Python language (comprehensions, generators/iterators, set vs list vs tuple, dunder methods) *
# - Paradigms of programming (functional, object-oriented, procedural, etc)
# - Writing performant code (profiling, memory usage, vectorised operations with Pandas/NumPy etc) * (Pandas)
# - Web development (APIs, serverless functions, web frameworks, relational and non-relational databases)
# - Back-end with AWS (Lambda, S3, Cognito, EC2)
# - DevOps on GitHub (CI/CD, task boards, Actions, GitHub Pages, how to code review, repo policies)
# - Event-driven architecture (producers/consumers, queues, message buses, data push services)
# - Data science (Gradient descent, SVMs, neural networks, popular libraries) *
# - Data engineering (ETL, data pipelines, data lakes, data warehouses)
# - Take-home challenges (refactoring tasks, small projects e.g. create a web dashboard, LeetCode/HackerRank style problems) *
