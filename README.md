cat << 'EOF' > README.md
# 💊 MedSearch Challenge: Cost-Optimization Engine

**MedSearch** is a Python-based data science framework designed to solve a critical healthcare problem: **Medication Affordability**. This project provides an automated environment where developers can submit algorithms to find the most cost-effective medical alternatives based on chemical composition and dosage.

## 🚀 The Challenge
Given a pharmaceutical dataset, participants must create a recommendation engine that:
1. Identifies the exact `primary_ingredient` and `primary_strength` of a brand.
2. Filters out discontinued or invalid entries.
3. Suggests the top 5 cheapest alternatives available in the market.
4. Optimizes for **execution speed** and **memory efficiency**.

---

## 🛠️ Project Structure
```text
/MED_SEARCH
├── data/               # Contains Medsearch.csv
├── src/                # Core logic
│   └── evaluator.py    # The automated grading engine
├── submissions/        # Where participants drop their code
│   └── submission_template.py
├── .github/workflows/  # CI/CD (GitHub Actions)
├── requirements.txt    # Project dependencies
└── leaderboard.md      # Auto-generated rankings

## Team Member :-
Atharva Uttekar - 1132231120
Atharva Lokhande - 1132231225
Shruti Mane - 1132231335
