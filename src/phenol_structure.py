"""
Generate a 2D molecular structure image of phenol.

This script uses RDKit to create and visualize the phenol molecule.
The output image is saved to the output folder.
"""

import os
from pathlib import Path
from rdkit import Chem
from rdkit.Chem import Draw, AllChem


def create_phenol_molecule():
    """
    Create a phenol molecule (C6H5OH).
    
    Phenol is a hydroxybenzene compound with a benzene ring 
    and a hydroxyl group attached.
    
    Returns:
        rdkit.Chem.Mol: RDKit molecule object for phenol
    """
    # SMILES notation for phenol (hydroxybenzene)
    phenol_smiles = "Oc1ccccc1"
    
    # Create molecule object from SMILES
    molecule = Chem.MolFromSmiles(phenol_smiles)
    
    if molecule is None:
        raise ValueError("Failed to create phenol molecule from SMILES")
    
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


def generate_phenol_image(output_path):
    """
    Generate and save a 2D image of the phenol molecule.
    
    Args:
        output_path (Path): Path where the image will be saved
    """
    print("Creating phenol molecule...")
    molecule = create_phenol_molecule()
    
    print(f"Generating 2D structure image...")
    # Create image with specific size
    image = Draw.MolToImage(molecule, size=(400, 400))
    
    # Save the image
    image.save(str(output_path))
    print(f"✓ Phenol structure saved to: {output_path}")


def main():
    """Main execution function."""
    try:
        # Ensure output directory exists
        output_dir = ensure_output_directory()
        output_file = output_dir / "phenol.png"
        
        # Generate the phenol image
        generate_phenol_image(output_file)
        
        print("\nSuccess! The phenol molecule structure has been generated.")
        
    except ImportError as e:
        print(f"Error: Missing required package. {e}")
        print("Please install dependencies: pip install -r requirements.txt")
    except Exception as e:
        print(f"Error: {e}")
        raise


if __name__ == "__main__":
    main()
