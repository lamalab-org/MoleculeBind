from enum import Enum, StrEnum

from networkx import Graph
from numpy import ndarray

from molbind.data.components.datasets import (
    FingerprintMolBindDataset,
    GraphDataset,
    ImageDataset,
    IrDataset,
    MassSpecNegativeDataset,
    MassSpecPositiveDataset,
    MultiSpecDataset,
    StringDataset,
    StructureDataset,
    cNmrDataset,
    hNmrDataset,
)
from molbind.data.components.mb_tokenizers import (
    DESCRIPTION_TOKENIZER,
    SELFIES_TOKENIZER,
    SMILES_TOKENIZER,
)
from molbind.models.components.custom_encoders import (
    CustomFingerprintEncoder,
    CustomGraphEncoder,
    CustomStructureEncoder,
    DescriptionEncoder,
    ImageEncoder,
    IrCNNEncoder,
    IUPACNameEncoder,
    MassSpecNegativeEncoder,
    MassSpecPositiveEncoder,
    SelfiesEncoder,
    SmilesEncoder,
    cNmrEncoder,
    hNmrCNNEncoder,
    hNmrEncoder,
)


class StringModalities(StrEnum):
    SMILES = "smiles"
    SELFIES = "selfies"
    IUPAC_NAME = "iupac_name"
    DESCRIPTION = "description"


class NonStringModalities(StrEnum):
    C_NMR = "c_nmr"
    FINGERPRINT = "fingerprint"
    IMAGE = "image"
    GRAPH = "graph"
    H_NMR = "h_nmr"
    IR = "ir"
    MASS_SPEC_POSITIVE = "mass_spec_positive"
    MASS_SPEC_NEGATIVE = "mass_spec_negative"
    STRUCTURE = "structure"
    MULTI_SPEC = "multi_spec"
    H_NMR_CNN = "h_nmr_cnn"


class ModalityConstants(Enum):
    """
    ModalityConstants[modality]: (data_type, dataset, encoder, tokenizer)
    """

    c_nmr = (list, cNmrDataset, cNmrEncoder, None)
    description = (str, StringDataset, DescriptionEncoder, DESCRIPTION_TOKENIZER)
    fingerprint = (list, FingerprintMolBindDataset, CustomFingerprintEncoder, None)
    h_nmr = (list, hNmrDataset, hNmrEncoder, None)
    h_nmr_cnn = (list, hNmrDataset, hNmrCNNEncoder, None)
    iupac_name = (str, StringDataset, IUPACNameEncoder, None)
    ir = (list, IrDataset, IrCNNEncoder, None)
    mass_spec_negative = (list, MassSpecNegativeDataset, MassSpecNegativeEncoder, None)
    mass_spec_positive = (list, MassSpecPositiveDataset, MassSpecPositiveEncoder, None)
    smiles = (str, StringDataset, SmilesEncoder, SMILES_TOKENIZER)
    selfies = (str, StringDataset, SelfiesEncoder, SELFIES_TOKENIZER)
    graph = (Graph, GraphDataset, CustomGraphEncoder, None)
    structure = (Graph, StructureDataset, CustomStructureEncoder, None)
    image = (ndarray, ImageDataset, ImageEncoder, None)
    multi_spec = (list, MultiSpecDataset, IrCNNEncoder, None)

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
