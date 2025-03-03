# ANOVA (Analysis of Variance) - Statistical Hypothesis Testing

This repository demonstrates the use of Analysis of Variance (ANOVA) to compare the means of multiple groups and tests assumptions before applying statistical methods like one-way ANOVA and Kruskal-Wallis tests. The example dataset used is `tips` from Seaborn.

## 1. **ANOVA (Analysis of Variance)**

### Problem:
ANOVA is used to compare the means of more than two groups to determine if there is a statistically significant difference between them. In this example, we compare the total bill amounts across different days (`Sun`, `Sat`, `Thur`, `Fri`) in a restaurant dataset.

### Steps:
1. **Form the Hypotheses:**
   - **H0**: m1 = m2 = m3 = m4 — There is no difference between the group means.
   - **H1**: There is a difference between the group means.
   
2. **Assumption Check:**
   - **Normality assumption**: Using the Shapiro-Wilk test to check the normality of data in each group.
   - **Homogeneity of variance assumption**: Using Levene's test to check for equal variances across groups.
   
3. **Test:**
   - If assumptions are met, perform **one-way ANOVA** (parametric test).
   - If assumptions are not met, use **Kruskal-Wallis test** (non-parametric test).

4. **Post-Hoc Test**:
   - If the ANOVA test shows a significant difference, use **Tukey's HSD** (Honestly Significant Difference) test to compare all pairs of groups.

## 2. **Dataset:**
The analysis uses the `tips` dataset from Seaborn, which contains data on restaurant tips, including the total bill, the day of the week, and whether the customer was a smoker or not.

- **Columns of interest**:
  - `day`: Day of the week (e.g., Sun, Sat, Thur, Fri)
  - `total_bill`: Total amount of the bill

### Code Explanation:
1. **Data Loading and Preprocessing**:
   - Load the `tips` dataset and group by `day` to calculate the mean of `total_bill` for each group.
   
2. **Hypothesis Testing**:
   - **Shapiro-Wilk Test**: Used to check if the data follows a normal distribution.
   - **Levene’s Test**: Used to check if the variances between groups are equal (homogeneity of variance).
   
3. **ANOVA and Kruskal-Wallis Test**:
   - **One-way ANOVA** is used when assumptions are met (normality and homogeneity of variance).
   - **Kruskal-Wallis Test** is used when assumptions are not met.

4. **Post-Hoc Analysis**:
   - **Tukey's HSD** test is performed to identify which specific groups are different after finding a significant result from ANOVA.

## 3. **Requirements**:
- Python 3.x
- Pandas
- NumPy
- SciPy
- Seaborn
- Statsmodels
