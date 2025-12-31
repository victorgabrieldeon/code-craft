"""
Example 3: Control Flow

This example demonstrates various control flow structures.
From PRD Section 5.3
"""

from codecraft import CodeBuilder

with CodeBuilder() as code:
    with code.function("process_items", params=["items: list"], returns="list"):
        code.line("results = []")
        code.blank_line()

        with code.for_("item", "items"):
            with code.try_():
                code.line("processed = item.process()")

                with code.if_("processed.is_valid()"):
                    code.line("results.append(processed)")
                with code.else_():
                    code.line('print(f"Invalid: {item}")')

            with code.except_("Exception", "e"):
                code.line('print(f"Error: {e}")')

        code.blank_line()
        code.line("return results")

# Generate and print the code
generated_code = code.generate()
print(generated_code)
print("\n" + "=" * 60 + "\n")

# Validate
print(f"Valid Python: {code.validate()}")
