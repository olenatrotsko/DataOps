
import sys
from pathlib import Path

import matplotlib
matplotlib.use("Agg")

import matplotlib.pyplot as plt
import pandas as pd

def main():
    input_file = Path(sys.argv[1])
    
    output_file = Path(f"/app/output/chart_{input_file.name}.png")

    df = pd.read_csv(input_file)

    df.plot(
        x="month",
        y="sales",
        kind="bar",
        legend=False,
        title="Monthly Sales",
    )

    plt.ylabel("Sales")
    plt.tight_layout()

    output_file.parent.mkdir(parents=True, exist_ok=True)
    plt.savefig(output_file)

    print(f"Chart saved to {output_file}")


if __name__ == "__main__":
    main()
