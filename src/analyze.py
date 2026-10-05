from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data" / "evaluated_responses.csv"
RESULTS = ROOT / "results"
RESULTS.mkdir(exist_ok=True)

df = pd.read_csv(DATA)

score_cols = [
    "instruction_adherence",
    "factual_consistency",
    "language_quality",
    "contextual_appropriateness",
    "completeness",
    "overall_quality",
]

for col in score_cols:
    df[col] = pd.to_numeric(df[col], errors="coerce")

summary = (
    df.groupby("language")[score_cols]
      .mean()
      .round(2)
)
summary.to_csv(RESULTS / "language_score_summary.csv")

error_counts = (
    df["error_category"]
      .fillna("none")
      .value_counts()
      .rename_axis("error_category")
      .reset_index(name="count")
)
error_counts.to_csv(RESULTS / "error_category_counts.csv", index=False)

hallucination_rate = (
    df["hallucination"]
      .astype(str)
      .str.strip()
      .str.lower()
      .eq("yes")
      .mean()
)
with open(RESULTS / "headline_metrics.txt", "w", encoding="utf-8") as f:
    f.write(f"Evaluated responses: {len(df)}\n")
    f.write(f"Hallucination rate: {hallucination_rate:.1%}\n")
    f.write(f"Average overall quality: {df['overall_quality'].mean():.2f}/5\n")

summary["overall_quality"].plot(kind="bar", title="Average Overall Quality by Language")
plt.ylabel("Average score (1-5)")
plt.tight_layout()
plt.savefig(RESULTS / "overall_quality_by_language.png", dpi=180)
plt.close()

print("\nLanguage score summary:")
print(summary)
print("\nError categories:")
print(error_counts)
print(f"\nHallucination rate: {hallucination_rate:.1%}")
