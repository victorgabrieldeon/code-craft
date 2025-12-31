"""
Example 2: API Generation

This example demonstrates creating a FastAPI endpoint.
From PRD Section 5.2
"""

from codecraft import CodeBuilder

with CodeBuilder() as code:
    code.add_from_import("fastapi", ["FastAPI", "HTTPException"])
    code.add_from_import("pydantic", ["BaseModel"])
    code.blank_lines(2)

    code.line("app = FastAPI()")
    code.blank_lines(2)

    with code.class_("UserCreate", bases=["BaseModel"]):
        code.attr("name", "str")
        code.attr("email", "str")

    code.blank_lines(2)

    with code.function(
        "create_user",
        params=["user: UserCreate"],
        returns="dict",
        decorators=["@app.post('/users')"],
    ):
        with code.if_("not user.email"):
            code.line('raise HTTPException(400, "Email required")')
        code.line('return {"id": 1, "name": user.name}')

# Generate and print the code
generated_code = code.generate()
print(generated_code)
print("\n" + "=" * 60 + "\n")

# Save to file
code.save("/tmp/api.py", format=False)
print("Saved to /tmp/api.py")
