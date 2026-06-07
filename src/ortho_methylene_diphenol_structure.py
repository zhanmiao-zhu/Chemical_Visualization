"""
Generate a 2D molecular structure image of ortho-linked methylene diphenol.

This script uses RDKit to create and visualize the ortho-linked methylene diphenol molecule.
The output image is saved to the output folder.
"""

import os
from pathlib import Path
from rdkit import Chem
from rdkit.Chem import Draw, AllChem


def create_ortho_methylene_diphenol_molecule():
    """
    Create a 2,2'-methylenediphenol (ortho-ortho linked) molecule.
    
    This compound (also known as ortho-ortho methylene diphenol) consists of two phenol rings 
    connected by a single methylene bridge (-CH2-). Both hydroxyl groups are at the 1-position 
    (ortho) and the methylene bridge is at the 2-position (ortho) on each phenol ring, creating 
    a symmetrical ortho-ortho-linked structure. This represents one of the key intermediate 
    products formed during phenol-formaldehyde condensation polymerization. The ortho linkage 
    pattern is one of several possible regioisomers (ortho, meta, para) that can form depending 
    on reaction conditions and the reactivity of different positions on the phenol ring.
    
    Returns:
        rdkit.Chem.Mol: RDKit molecule object for 2,2'-methylenediphenol
    """
    # SMILES notation for 2,2'-methylenediphenol (ortho-ortho linked methylene diphenol)
    # Valid SMILES: Oc1ccccc1Cc2ccccc2O
    # This represents: HO-Ph(2)-CH2-Ph(2)-OH where both OH and CH2 are ortho to each other
    ortho_methylene_diphenol_smiles = "Oc1ccccc1Cc2ccccc2O"
    
    # Create molecule object from SMILES
    molecule = Chem.MolFromSmiles(ortho_methylene_diphenol_smiles)
    
    if molecule is None:
        raise ValueError("Failed to create ortho-methylene diphenol molecule from SMILES")
    
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


def generate_ortho_methylene_diphenol_image(output_path):
    """
    Generate and save a 2D image of the ortho-methylene diphenol molecule.
    
    Args:
        output_path (Path): Path where the image will be saved
    """
    print("Creating ortho-linked methylene diphenol molecule...")
    molecule = create_ortho_methylene_diphenol_molecule()
    
    print(f"Generating 2D structure image...")
    # Create image with specific size
    image = Draw.MolToImage(molecule, size=(400, 400))
    
    # Save the image
    image.save(str(output_path))
    print(f"✓ Ortho-methylene diphenol structure saved to: {output_path}")


def main():
    """Main execution function."""
    try:
        # Ensure output directory exists
        output_dir = ensure_output_directory()
        output_file = output_dir / "ortho_methylene_diphenol.png"
        
        # Generate the ortho-methylene diphenol image
        generate_ortho_methylene_diphenol_image(output_file)
        
        print("\nSuccess! The 2,2'-methylenediphenol (ortho-ortho linked) molecule structure has been generated.")
        print("This structure represents an ortho-ortho-linked product of phenol-formaldehyde polymerization.")
        
    except ImportError as e:
        print(f"Error: Missing required package. {e}")
        print("Please install dependencies: pip install -r requirements.txt")
    except Exception as e:
        print(f"Error: {e}")
        raise


if __name__ == "__main__":
    main()
