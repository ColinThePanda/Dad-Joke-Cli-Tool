import requests
import json
import typer

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
def main(count: int = typer.Argument(10, help="Number of jokes to fetch")):
    """
    Fetch and print a specified number of jokes.
    """
    jokes = [get_joke() for _ in range(count)]
    for index, joke in enumerate(jokes, start=1):
        print(f"{index}. {joke}")

if __name__ == "__main__":
    app()
