import requests
import json
import typer
from add_to_path import add_to_path

app = typer.Typer()

def get_joke() -> str:
    headers = {"Accept": "application/json"}
    url = "https://icanhazdadjoke.com"

    r = requests.get(url, headers=headers)

    if r.status_code == 200:
        data = r.json()
        return data.get("joke", "No joke found.")
    return "Failed to fetch a joke."

@app.command()
def main(count: int = typer.Argument(1, help="Number of jokes to fetch")):
    """
    Fetch and print a specified number of jokes.
    """
    add_to_path()  # Ensure the path is added to the environment if needed
    jokes = [get_joke() for _ in range(count)]
    if len(jokes) <= 1 and len(jokes) > 0:
        print(jokes[0])
    elif len(jokes) > 1 and len(jokes) > 0:
        for index, joke in enumerate(jokes, start=1):
            print(f"{index}. {joke}")
    else:
        print("that is not a valid number of jokes")

if __name__ == "__main__":
    app()
