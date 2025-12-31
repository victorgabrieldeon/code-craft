"""
Example 1: Basic Class Generation

This example demonstrates creating a simple dataclass with attributes.
From PRD Section 5.1
"""

from codecraft import CodeBuilder

# Basic class generation
with CodeBuilder() as code:
    code.add_import("dataclasses", ["dataclass"])
    code.add_import("typing", ["TYPE_CHECKING"])

    with code.if_("TYPE_CHECKING"):
        code.add_import("abc", ["ABC", "abstractmethod"])

    code.blank_line()

    with code.class_("User", decorators=["@dataclass"]):
        code.docstring("Represents a user in the system.")
        code.attr("name", "str")
        code.attr("email", "str")
        code.attr("age", "int | None", default="None")

        with code.method("greet", returns="str"):
            code.docstring("Returns a greeting message.")

            with code.if_("self.age"):
                code.return_('f"Hello, {self.name}! You are {self.age} years old."')

            code.return_('f"Hello, {self.name}!"')

# Generate and print the code
generated_code = code.generate()
print(generated_code)
print("\n" + "=" * 60 + "\n")

# Validate the code
is_valid = code.validate(detailed=True)
print(f"Code validation: {is_valid}")
