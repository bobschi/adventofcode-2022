from pathlib import Path
import typer


def most_calories_carried(
    input: Path = typer.Option(
        "inputs/day01_sample.txt",
        exists=True,
    )
) -> None:
    print("Let's go!")

    with open(input, "r") as packing_list_file:
        packing_list = packing_list_file.read()

    packing_list = [map(int, elf.split("\n")) for elf in packing_list.split("\n\n")]

    sorted_by_calories = sorted([sum(elf) for elf in packing_list], reverse=True)

    maximum_calories = sorted_by_calories[0]
    sum_of_top_three = sum(sorted_by_calories[0:3])

    print(maximum_calories, sum_of_top_three)


if __name__ == "__main__":
    typer.run(most_calories_carried)
