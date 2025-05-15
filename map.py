import matplotlib.pyplot as plt
from collections import defaultdict

papers = [
    ("Survey-based Research", 2024),
    ("Survey-based Research", 2021),
    ("Survey-based Research", 2024),
    ("Model-Agnostic Explanation Techniques", 2021),
    ("Model-Agnostic Explanation Techniques", 2024),
    ("Framework and Architecture Innovations", 2023),
    ("Framework and Architecture Innovations", 2025),
    ("Framework and Architecture Innovations", 2022),
    ("Emerging Applications and LLM-enhanced Models", 2024),
    ("Emerging Applications and LLM-enhanced Models", 2023)
]


years = sorted(set(year for _, year in papers))
categories = [
    "Survey-based Research",
    "Model-Agnostic Explanation Techniques",
    "Framework and Architecture Innovations",
    "Emerging Applications and LLM-enhanced Models"
]

category_colors = {
    "Survey-based Research": "#4C78A8",
    "Model-Agnostic Explanation Techniques": "#F58518",
    "Framework and Architecture Innovations": "#54A24B",
    "Emerging Applications and LLM-enhanced Models": "#B279A2"
}

year_category_counts = defaultdict(lambda: defaultdict(int))
for category, year in papers:
    year_category_counts[year][category] += 1

data_per_category = {cat: [year_category_counts[year][cat] for year in years] for cat in categories}

plt.figure(figsize=(10, 6))
bottom = [0] * len(years)

for category in categories:
    plt.bar(
        years,
        data_per_category[category],
        label=category,
        bottom=bottom,
        color=category_colors[category]
    )
    bottom = [bottom[i] + data_per_category[category][i] for i in range(len(years))]


plt.xlabel("Publication Year")
plt.ylabel("Number of Papers")
plt.title("Histogram of Selected Papers by Year and Category")
plt.xticks(years)
plt.legend(title="Research Category")
plt.grid(axis='y', linestyle='--', alpha=0.6)
plt.tight_layout()
plt.show()
