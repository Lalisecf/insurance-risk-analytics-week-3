
def calculate_loss_ratio(df):
    return df['TotalClaims'].sum() / df['TotalPremium'].sum()


def calculate_margin(df):
    return df['TotalPremium'] - df['TotalClaims']
