"""
Generate a 2D molecular structure image of phenol connected by methylene bridge.

This script uses RDKit to create and visualize the phenol-CH2-phenol molecule.
The output image is saved to the output folder.
"""

import os
from pathlib import Path
from rdkit import Chem
from rdkit.Chem import Draw, AllChem


def create_phenol_ch2_phenol_molecule():
    """
    Create a phenol-CH2-phenol molecule.
    
    This compound consists of two phenol rings connected by a methylene bridge (-CH2-).
    It is a common condensation product formed during the early stages of 
    phenol-formaldehyde polymerization.
    
    Returns:
        rdkit.Chem.Mol: RDKit molecule object for phenol-CH2-phenol
    """
    # SMILES notation for phenol-CH2-phenol
    # This represents two hydroxybenzene rings connected by a single carbon atom
    phenol_ch2_phenol_smiles = "Oc1ccc(Cc2ccc(O)cc2)cc1"
    
    # Create molecule object from SMILES
    molecule = Chem.MolFromSmiles(phenol_ch2_phenol_smiles)
    
    if molecule is None:
        raise ValueError("Failed to create phenol-CH2-phenol molecule from SMILES")
    
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


def generate_phenol_ch2_phenol_image(output_path):
    """
    Generate and save a 2D image of the phenol-CH2-phenol molecule.
    
    Args:
        output_path (Path): Path where the image will be saved
    """
    print("Creating phenol-CH2-phenol molecule...")
    molecule = create_phenol_ch2_phenol_molecule()
    
    print(f"Generating 2D structure image...")
    # Create image with specific size
    image = Draw.MolToImage(molecule, size=(400, 400))
    
    # Save the image
    image.save(str(output_path))
    print(f"✓ Phenol-CH2-phenol structure saved to: {output_path}")


def main():
    """Main execution function."""
    try:
        # Ensure output directory exists
        output_dir = ensure_output_directory()
        output_file = output_dir / "phenol_ch2_phenol.png"
        
        # Generate the phenol-CH2-phenol image
        generate_phenol_ch2_phenol_image(output_file)
        
        print("\nSuccess! The phenol-CH2-phenol molecule structure has been generated.")
        
    except ImportError as e:
        print(f"Error: Missing required package. {e}")
        print("Please install dependencies: pip install -r requirements.txt")
    except Exception as e:
        print(f"Error: {e}")
        raise


if __name__ == "__main__":
    main()
