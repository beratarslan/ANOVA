#####################################################
# ANOVA (Analysis of Variance)
######################################################

# Used to compare the means of more than two groups.

df = sns.load_dataset("tips")
df.head()

df.groupby("day")["total_bill"].mean()

##############################
# 1. Form the Hypotheses
##############################

# H0: m1 = m2 = m3 = m4
# There is no difference between the group means.

# H1: There is a difference.

##############################
# 2. Assumption Check
##############################

# Normality assumption
# Homogeneity of variance assumption

# If assumptions are met, use one-way ANOVA
# If assumptions are not met, use Kruskal-Wallis test

# H0: The normality assumption is satisfied.

# We converted the categories of a categorical variable into an iterative object
# By iterating through this list, we can perform the normality test (Shapiro-Wilk test) for each group.

for group in list(df["day"].unique()):
    pvalue = shapiro(df.loc[df["day"] == group, "total_bill"])[1]
    print(group, 'p-value: %.4f' % pvalue)


# H0: The homogeneity of variance assumption is satisfied.

test_stat, pvalue = levene(df.loc[df["day"] == "Sun", "total_bill"],
                           df.loc[df["day"] == "Sat", "total_bill"],
                           df.loc[df["day"] == "Thur", "total_bill"],
                           df.loc[df["day"] == "Fri", "total_bill"])
print('Test Stat = %.4f, p-value = %.4f' % (test_stat, pvalue))


##############################
# 3. Hypothesis Test and p-value Interpretation
##############################

# None of the assumptions hold.
df.groupby("day").agg({"total_bill": ["mean", "median"]})


# H0: There is no statistically significant difference between the group means.

# Parametric ANOVA test:
f_oneway(df.loc[df["day"] == "Thur", "total_bill"],
         df.loc[df["day"] == "Fri", "total_bill"],
         df.loc[df["day"] == "Sat", "total_bill"],
         df.loc[df["day"] == "Sun", "total_bill"])

# Non-parametric ANOVA test:
kruskal(df.loc[df["day"] == "Thur", "total_bill"],
        df.loc[df["day"] == "Fri", "total_bill"],
        df.loc[df["day"] == "Sat", "total_bill"],
        df.loc[df["day"] == "Sun", "total_bill"])
#
from statsmodels.stats.multicomp import MultiComparison
comparison = MultiComparison(df['total_bill'], df['day'])
tukey = comparison.tukeyhsd(0.05)
print(tukey.summary())
