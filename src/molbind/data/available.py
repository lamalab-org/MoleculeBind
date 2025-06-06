from enum import Enum, StrEnum

from molbind.data import (
    HSQCDataset,
    IrDataset,
    StringDataset,
    cNmrDataset,
    hNmrDataset,
)
from molbind.data.components.mb_tokenizers import (
    SMILES_TOKENIZER,
)
from molbind.models import HSQCEncoder, IrCNNEncoder, SmilesEncoder, cNmrEncoder, hNmrCNNEncoder


class StringModalities(StrEnum):
    SMILES = "smiles"
    BIGSMILES = "bigsmiles"
    POLYMER_NAME = "polymer_name"
    PSMILES = "psmiles"


class NonStringModalities(StrEnum):
    C_NMR = "c_nmr"
    H_NMR = "h_nmr"
    IR = "ir"
    HSQC = "hsqc"
    GRAPH = "graph"
    STRUCTURE = "structure"
    BIGSMILES = "bigsmiles"
    POLYMER_NAME = "polymer_name"
    PSMILES = "psmiles"


class ModalityConstants(Enum):
    """
    ModalityConstants[modality]: (data_type, dataset, encoder, tokenizer)
    """

    c_nmr = (list, cNmrDataset, cNmrEncoder, None)
    h_nmr = (list, hNmrDataset, hNmrCNNEncoder, None)
    ir = (list, IrDataset, IrCNNEncoder, None)
    smiles = (str, StringDataset, SmilesEncoder, SMILES_TOKENIZER)
    hsqc = (list, HSQCDataset, HSQCEncoder, None)

    @property
    def data_type(self):
        return self.value[0]

    @property
    def dataset(self):
        return self.value[1]

    @property
    def encoder(self):
        return self.value[2]

    @property
    def tokenizer(self):
        return self.value[3]
