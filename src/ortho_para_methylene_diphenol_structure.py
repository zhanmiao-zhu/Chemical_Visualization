"""
Generate a 2D molecular structure image of 2,4'-methylenediphenol.

This script uses RDKit to create and visualize the 2,4'-methylenediphenol molecule.
The output image is saved to the output folder.
"""

import os
from pathlib import Path
from rdkit import Chem
from rdkit.Chem import Draw, AllChem


def create_ortho_para_methylene_diphenol_molecule():
    """
    Create a 2,4'-methylenediphenol (ortho-para linked) molecule.
    
    This compound consists of two phenol rings connected by a single methylene bridge (-CH2-).
    In the first phenol ring, the hydroxyl group (OH) is at position 1 and the methylene bridge 
    is at position 2 (ortho relative to the OH). In the second phenol ring, the hydroxyl group 
    is at position 4 (para relative to the methylene bridge attachment at position 1). 
    This asymmetrical isomer is one of the products formed during phenol-formaldehyde 
    condensation polymerization. Different regioisomers (ortho-ortho, ortho-meta, ortho-para, 
    meta-para, para-para) can form depending on reaction conditions and ring reactivity.
    
    Carbon numbering on benzene ring:
        6   1 (OH position)
        5   2 (Bridge position for ring 1 - ortho)
        4   3
    
    Ring 1: Position 1 = OH, Position 2 = CH2 bridge (ortho)
    Ring 2: Position 1 = CH2 bridge, Position 4 = OH (para from bridge)
    
    Returns:
        rdkit.Chem.Mol: RDKit molecule object for 2,4'-methylenediphenol
    """
    # SMILES notation for 2,4'-methylenediphenol (ortho-para linked methylene diphenol)
    # Valid SMILES: Oc1ccccc1Cc2ccc(O)cc2
    # This represents: HO-Ph(2)-CH2-Ph(4)-OH
    # Ring 1: O at position 1, CH2 at position 2 (ortho to OH)
    # Ring 2: CH2 at position 1, O at position 4 (para from CH2 attachment)
    ortho_para_methylene_diphenol_smiles = "Oc1ccccc1Cc2ccc(O)cc2"
    
    # Create molecule object from SMILES
    molecule = Chem.MolFromSmiles(ortho_para_methylene_diphenol_smiles)
    
    if molecule is None:
        raise ValueError("Failed to create 2,4'-methylenediphenol molecule from SMILES")
    
    # Add hydrogens for a complete representation
    molecule = Chem.AddHs(molecule)
    
    # Generate 2D coordinates for better visualization
    AllChem.Compute2DCoords(molecule)
    
    return molecule


def ensure_output_directory():
    """
    Create the output directory if it doesn't exist.
    
    Returns:
        Path: Path object pointing to the output directory
    """
    # Get the project root (parent of src directory)
    src_dir = Path(__file__).parent
    project_root = src_dir.parent
    output_dir = project_root / "output"
    
    # Create directory if it doesn't exist
    output_dir.mkdir(parents=True, exist_ok=True)
    
    return output_dir


def generate_ortho_para_methylene_diphenol_image(output_path):
    """
    Generate and save a 2D image of the 2,4'-methylenediphenol molecule.
    
    Args:
        output_path (Path): Path where the image will be saved
    """
    print("Creating 2,4'-methylenediphenol (ortho-para linked) molecule...")
    molecule = create_ortho_para_methylene_diphenol_molecule()
    
    print(f"Generating 2D structure image...")
    # Create image with specific size
    image = Draw.MolToImage(molecule, size=(400, 400))
    
    # Save the image
    image.save(str(output_path))
    print(f"✓ 2,4'-methylenediphenol structure saved to: {output_path}")


def main():
    """Main execution function."""
    try:
        # Ensure output directory exists
        output_dir = ensure_output_directory()
        output_file = output_dir / "ortho_para_methylene_diphenol.png"
        
        # Generate the 2,4'-methylenediphenol image
        generate_ortho_para_methylene_diphenol_image(output_file)
        
        print("\nSuccess! The 2,4'-methylenediphenol (ortho-para linked) molecule structure has been generated.")
        print("This structure represents an ortho-para-linked product of phenol-formaldehyde polymerization.")
        
    except ImportError as e:
        print(f"Error: Missing required package. {e}")
        print("Please install dependencies: pip install -r requirements.txt")
    except Exception as e:
        print(f"Error: {e}")
        raise


if __name__ == "__main__":
    main()
