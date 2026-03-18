import argparse
from contracts.modules import Module


def main():
    parser = argparse.ArgumentParser(
        description="Artificial Intelligence/Machine Learning")

    parser.add_argument("-m", "--module", type=str, required=True,
                        help="Module to run (e.g., 'manim', 'pytorch')", choices=[module.value for module in Module])

    args = parser.parse_args()

    module = Module(args.module)
    if module == Module.MANIM:
        print("Please run the Manim module from Makefile using the command 'make manim CLASS=<classname>'")


if __name__ == "__main__":
    main()
