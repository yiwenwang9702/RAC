import numpy as np
from ..autocorrelation import RAC_f_all, RAC_f_ligand, RAC_ligand_ligand, RAC_mc_all, RAC_mc_ligand, property_notation

def NAO_NPA_names(definitions, option='Singlet') -> list:

    _properties = ['Weighted energy', 'Natural charge', 
    'Valence s occupancy', 'Valence s energy', 'Valence px occupancy', 'Valence px energy',
    'Valence py occupancy', 'Valence py energy', 'Valence pz occupancy', 'Valence pz energy']
    if option == 'Triplet':
        _properties = _properties + ['Natural Spin Density']
    _notations = [property_notation[_property] for _property in _properties]
    _suffix = {
        'Singlet': '_S',
        'Triplet': '_T',
        'Difference': '_diff'
    }
    _notations = [_notaion+_suffix[option] for _notaion in _notations]
    styles = ['MB', 'M', 'G']

    def helper(start, scope):
        _new = []
        for style in styles:
            for i  in range(len(_properties)):
                _new += ['_'.join([start, scope, style, _notations[i], str(d)]) for d in range(1, 11)]
        return _new
    names = []
    for definition in definitions:
        names += helper(definition[0], definition[1])

    return names

def NBO_names(definitions, option='singlet') -> list:
    # _properties = ['BD sg Occupancy', 'BD sg Energy', 'BD db Occupancy', 'BD db Energy', 'ABB sg Occupancy', 'ABB sg Energy', 'ABB db Occupancy', 'ABB db Energy']
    _notations = ['BD_sg_occ', 'BD_sg_nrg', 'BD_db_occ', 'BD_db_nrg', 'ABB_sg_occ', 'ABB_sg_nrg', 'ABB_db_occ', 'ABB_db_nrg']
    _suffix = {
        'singlet': '_S',
        'triplet alpha': '_T_a',
        'triplet beta': '_T_b',
        'diff': '_diff'
    }
    _notations = [_notaion+_suffix[option] for _notaion in _notations]
    styles = ['MB', 'M', 'G']

    def helper(start, scope):
        _new = []
        for style in styles:
            for i  in range(len(_notations)):
                _new += ['_'.join([start, scope, style, _notations[i], str(d)]) for d in range(1, 11)]
        return _new
    names = []
    for definition in definitions:
        names += helper(definition[0], definition[1])

    return names

def CMO_names(definitions, option='singlet') -> list:
    _notations = ['HOMO5', 'HOMO4', 'HOMO3', 'HOMO2', 'HOMO1', 'HOMO', 'LUMO', 'LUMO1', 'LUMO2', 'LUMO3', 'LUMO4', 'LUMO5']
    _suffix = {
        'singlet': '_S',
        'triplet alpha': '_T_a',
        'triplet beta': '_T_b'
    }
    _notations = [_notaion+_suffix[option] for _notaion in _notations]
    styles = ['MB', 'M', 'G']
    def helper(start, scope):
        _new = []
        for style in styles:
            for i in range(len(_notations)):
                _new += ['_'.join([start, scope, style, _notations[i], str(d)]) for d in range(1, 11)]
        return _new
    names = []
    for definition in definitions:
        names += helper(definition[0], definition[1])

    return names

def RAC_full(mol, _properties, depth=(1,10), three_d=False) -> np.ndarray:

    f_all_MB = RAC_f_all(mol, _properties=_properties, depth=depth, operation='multiply', style='Moreau-Broto', three_d=three_d)
    f_all_M = RAC_f_all(mol, _properties=_properties, depth=depth, style='Moran', three_d=three_d)
    f_all_G = RAC_f_all(mol, _properties=_properties, depth=depth, style='Geary', three_d=three_d)
    
    f_CN_MB = RAC_f_ligand(mol, 'CN', _properties=_properties, depth=depth, operation='multiply', style='Moreau-Broto', three_d=three_d)
    f_CN_M = RAC_f_ligand(mol, 'CN', _properties=_properties, depth=depth, style='Moran', three_d=three_d)
    f_CN_G = RAC_f_ligand(mol, 'CN', _properties=_properties, depth=depth, style='Geary', three_d=three_d)
    
    f_NN_MB = RAC_f_ligand(mol, 'NN', _properties=_properties, depth=depth, operation='multiply', style='Moreau-Broto', three_d=three_d)
    f_NN_M = RAC_f_ligand(mol, 'NN', _properties=_properties, depth=depth, style='Moran', three_d=three_d)
    f_NN_G = RAC_f_ligand(mol, 'NN', _properties=_properties, depth=depth, style='Geary', three_d=three_d)
    
    full_feature = np.concatenate((f_all_MB, f_all_M, f_all_G, f_CN_MB, f_CN_M, f_CN_G, f_NN_MB, f_NN_M, f_NN_G))

    return full_feature

def RAC_mc(mol,  _properties, depth=(1,10), three_d=False) -> np.ndarray:

    mc_all_MB = RAC_mc_all(mol, _properties=_properties, depth=depth, operation='multiply', style='Moreau-Broto', three_d=three_d)
    mc_all_M = RAC_mc_all(mol, _properties=_properties, depth=depth, style='Moran', three_d=three_d)
    mc_all_G = RAC_mc_all(mol, _properties=_properties, depth=depth, style='Geary', three_d=three_d)
    
    mc_CN_MB = RAC_mc_ligand(mol, 'CN', _properties=_properties, depth=depth, operation='multiply', style='Moreau-Broto', three_d=three_d)
    mc_CN_M = RAC_mc_ligand(mol, 'CN', _properties=_properties, depth=depth, style='Moran', three_d=three_d)
    mc_CN_G = RAC_mc_ligand(mol, 'CN', _properties=_properties, depth=depth, style='Geary', three_d=three_d)
    
    mc_NN_MB = RAC_mc_ligand(mol, 'NN', _properties=_properties, depth=depth, operation='multiply', style='Moreau-Broto', three_d=three_d)
    mc_NN_M = RAC_mc_ligand(mol, 'NN', _properties=_properties, depth=depth, style='Moran', three_d=three_d)
    mc_NN_G = RAC_mc_ligand(mol, 'NN', _properties=_properties, depth=depth, style='Geary', three_d=three_d)
    
    full_feature = np.concatenate((mc_all_MB, mc_all_M, mc_all_G, mc_CN_MB, mc_CN_M, mc_CN_G, mc_NN_MB, mc_NN_M, mc_NN_G))

    return full_feature

def RAC_cross_scope(mol, _properties, depth=(1,10), three_d=False) -> np.ndarray:

    CN1, CN2, NN = mol.CN1, mol.CN2, mol.get_specific_ligand('NN')[0]

    CN1_NN_MB = RAC_ligand_ligand(mol, CN1, NN, _properties=_properties, depth=depth, operation='multiply', style='Moreau-Broto', three_d=three_d)
    CN1_NN_M = RAC_ligand_ligand(mol, CN1, NN, _properties=_properties, depth=depth, style='Moran', three_d=three_d)
    CN1_NN_G = RAC_ligand_ligand(mol, CN1, NN, _properties=_properties, depth=depth, style='Geary', three_d=three_d)

    CN2_NN_MB = RAC_ligand_ligand(mol, CN2, NN, _properties=_properties, depth=depth, operation='multiply', style='Moreau-Broto', three_d=three_d)
    CN2_NN_M = RAC_ligand_ligand(mol, CN2, NN, _properties=_properties, depth=depth, style='Moran', three_d=three_d)
    CN2_NN_G = RAC_ligand_ligand(mol, CN2, NN, _properties=_properties, depth=depth, style='Geary', three_d=three_d)

    CN1_CN2_MB = RAC_ligand_ligand(mol, CN1, CN2, _properties=_properties, depth=depth, operation='multiply', style='Moreau-Broto', three_d=three_d)
    CN1_CN2_M = RAC_ligand_ligand(mol, CN1, CN2, _properties=_properties, depth=depth, style='Moran', three_d=three_d)
    CN1_CN2_G = RAC_ligand_ligand(mol, CN1, CN2, _properties=_properties, depth=depth, style='Geary', three_d=three_d)

    full_feature = np.concatenate((CN1_NN_MB, CN1_NN_M, CN1_NN_G, CN2_NN_MB, CN2_NN_M, CN2_NN_G, CN1_CN2_MB, CN1_CN2_M, CN1_CN2_G))

    return full_feature