import pandas as pd

def load_hsn_sac_data(file_path="HSN_SAC.xlsx"):
    """Loads HSN and SAC data from the Excel file."""
    df_hsn = pd.read_excel(file_path, sheet_name="HSN_MSTR", engine="openpyxl")
    df_sac = pd.read_excel(file_path, sheet_name="SAC_MSTR", engine="openpyxl")

    # Cleaning data
    df_hsn.columns = df_hsn.columns.str.strip()
    df_sac.columns = df_sac.columns.str.strip()

    df_hsn.drop_duplicates(subset=["HSNCode"], inplace=True)
    df_sac.drop_duplicates(subset=["SAC_CD"], inplace=True)

    df_hsn.dropna(inplace=True)
    df_sac.dropna(inplace=True)

    return df_hsn, df_sac

# Example usage
if __name__ == "__main__":
    df_hsn, df_sac = load_hsn_sac_data()
    print(df_hsn.head())
    print(df_sac.head())
