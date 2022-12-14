import os, sys
import typer
from typing import Optional


# one can think of typer as sibling for FastAPI
# Currently we use typer for passing command arguments to a python module

app = typer.Typer()


# @app.command()
# def helloworld(string: str) -> Optional[str]:
#     print("Hello world")


# for string type checking use mypy module_name.py




if __name__ == "__main__":
    app()
