from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt

ROOT = Path(__file__).resolve().parents[1]
DATA_PATH = ROOT / "data" / "doctor_visits.csv"
OUTPUT_DIR = ROOT / "outputs"
OUTPUT_DIR.mkdir(exist_ok=True)

def main():
    df = pd.read_csv(DATA_PATH)

    print("DATASET OVERVIEW")
    print(f"Rows: {len(df):,}")
    print(f"Columns: {len(df.columns)}")
    print("\nColumn data types:")
    print(df.dtypes)
    print("\nMissing values per column:")
    print(df.isna().sum())

    if "visits" not in df.columns:
        raise ValueError("Expected target column 'visits' was not found.")

    print("\nVISIT SUMMARY")
    print(df["visits"].describe())
    zero_visits = int((df["visits"] == 0).sum())
    print(f"\nRecords with zero visits: {zero_visits:,} ({zero_visits / len(df):.1%})")
    print(f"Mean visits per record: {df['visits'].mean():.3f}")

    if "illness" in df.columns:
        illness_summary = (
            df.groupby("illness", dropna=False)["visits"]
              .agg(records="size", average_visits="mean", median_visits="median")
              .round(3)
        )
        print("\nVISITS BY ILLNESS COUNT")
        print(illness_summary)
        ax = illness_summary["average_visits"].plot(kind="bar", rot=0)
        ax.set_title("Average Doctor Visits by Illness Count")
        ax.set_xlabel("Illness count")
        ax.set_ylabel("Average visits")
        plt.tight_layout()
        plt.savefig(OUTPUT_DIR / "average_visits_by_illness.png", dpi=160)
        plt.close()

    for col in ["gender", "private", "freepoor", "freerepat", "nchronic", "lchronic"]:
        if col in df.columns:
            summary = (
                df.groupby(col, dropna=False)["visits"]
                  .agg(records="size", average_visits="mean", median_visits="median")
                  .round(3)
            )
            print(f"\nVISITS BY {col.upper()}")
            print(summary)

    # Visit-count distribution grouped into 0, 1, 2, 3, and 4+ visits.
    grouped_visits = pd.cut(
        df["visits"],
        bins=[-1, 0, 1, 2, 3, float("inf")],
        labels=["0", "1", "2", "3", "4+"]
    ).value_counts(sort=False)
    ax = grouped_visits.plot(kind="bar", rot=0)
    ax.set_title("Distribution of Doctor Visits")
    ax.set_xlabel("Number of visits")
    ax.set_ylabel("Number of records")
    plt.tight_layout()
    plt.savefig(OUTPUT_DIR / "visit_distribution.png", dpi=160)
    plt.close()

    print(f"\nCharts saved to: {OUTPUT_DIR}")

if __name__ == "__main__":
    main()
