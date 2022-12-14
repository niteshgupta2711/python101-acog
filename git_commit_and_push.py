import os, typer


app = typer.Typer()


@app.command()
def commit_push(mess: str = "git push automated", branch: str = "main") -> None:
    os.system(f'git add . && git commit -m "{mess}" && git push -u origin "branch"')


if __name__ == "__main__":
    app()
