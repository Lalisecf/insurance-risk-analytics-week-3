import pandas as pd
from scipy.stats import ttest_ind, chi2_contingency


def calculate_claim_frequency(dataframe):
    return dataframe["HasClaim"].mean()


def calculate_claim_severity(dataframe):
    claims_only = dataframe[dataframe["TotalClaims"] > 0]
    return claims_only["TotalClaims"].mean()


def calculate_margin(dataframe):
    return dataframe["Margin"].mean()


def perform_ttest(group_a, group_b):
    stat, p_value = ttest_ind(group_a, group_b, nan_policy='omit')
    return stat, p_value


def perform_chi_square_test(contingency_table):
    chi2, p_value, dof, expected = chi2_contingency(contingency_table)
    return chi2, p_value
