from networkx import Graph

from molbind.data.components.datasets import (
    FingerprintMolBindDataset,
    GraphDataset,
    StringDataset,
)
from molbind.data.components.tokenizers import SELFIES_TOKENIZER, SMILES_TOKENIZER
from molbind.models.components.custom_encoders import (
    CustomFingerprintEncoder,
    GraphEncoder,
    SelfiesEncoder,
    SmilesEncoder,
)

AVAILABLE_ENCODERS = {
    "smiles": SmilesEncoder,
    "selfies": SelfiesEncoder,
    "graph": GraphEncoder,
    "nmr": None,
    "fingerprint": CustomFingerprintEncoder,
}

MODALITY_DATA_TYPES = {
    "fingerprint": list,
    "iupac_name": str,
    "smiles": str,
    "selfies": str,
    "graph": Graph,
    "nmr": str,
    "ir": str,
}

STRING_TOKENIZERS = {
    "smiles": SMILES_TOKENIZER,
    "selfies": SELFIES_TOKENIZER,
    "iupac_name": "iupac_name_tokenizer",
}

MODALITY_DATASETS = {
    "fingerprint": FingerprintMolBindDataset,
    "smiles": StringDataset,
    "selfies": StringDataset,
    "graph": GraphDataset,
    "nmr": StringDataset,
    "ir": StringDataset,
}