import fire
import pandas as pd
from molbind.data.utils.fingerprint_utils import get_morgan_fingerprint_from_smiles


def add_fingerprint_column_to_dataframe(
    csv_data_path: str, radius: int = 4, nbits: int = 2048
):
    """
    Add fingerprint column to a DataFrame

    Args:
        data (pl.DataFrame): DataFrame
        radius (int, optional): radius of the fingerprint. Defaults to 2.
        nbits (int, optional): number of bits in the fingerprint. Defaults to 2048.

    Returns:
        pl.DataFrame: DataFrame with fingerprint column
    """

    # Load data
    data = pd.read_csv(csv_data_path)

    # Add fingerprint column
    data["fingerprint"] = data["smiles"].apply(
        lambda x: get_morgan_fingerprint_from_smiles(x, radius, nbits)
    )

    # Save data to pkl
    data.to_pickle(csv_data_path.replace(".csv", ".pkl"))


if __name__ == "__main__":
    fire.Fire(add_fingerprint_column_to_dataframe)