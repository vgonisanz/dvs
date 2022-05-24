"""
Train a new model with your awesome parameters
"""
import typer

from dvs.utils import setup_logger


def main():
    typer.echo(f"Running {__file__}")


if __name__ == "__main__":
    setup_logger()
    typer.run(main)
