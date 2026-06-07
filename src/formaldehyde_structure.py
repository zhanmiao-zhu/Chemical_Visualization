"""
Generate a 2D molecular structure image of formaldehyde.

This script uses RDKit to create and visualize the formaldehyde molecule.
The output image is saved to the output folder.
"""

import os
from pathlib import Path
from rdkit import Chem
from rdkit.Chem import Draw, AllChem


def create_formaldehyde_molecule():
    """
    Create a formaldehyde molecule (CH2O).
    
    Formaldehyde is the simplest aldehyde compound consisting of 
    a carbon atom double bonded to an oxygen atom with two hydrogen atoms 
    attached to the carbon.
    
    Returns:
        rdkit.Chem.Mol: RDKit molecule object for formaldehyde
    """
    # SMILES notation for formaldehyde (methanal)
    formaldehyde_smiles = "C=O"
    
    # Create molecule object from SMILES
    molecule = Chem.MolFromSmiles(formaldehyde_smiles)
    
    if molecule is None:
        raise ValueError("Failed to create formaldehyde molecule from SMILES")
    
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


def generate_formaldehyde_image(output_path):
    """
    Generate and save a 2D image of the formaldehyde molecule.
    
    Args:
        output_path (Path): Path where the image will be saved
    """
    print("Creating formaldehyde molecule...")
    molecule = create_formaldehyde_molecule()
    
    print(f"Generating 2D structure image...")
    # Create image with specific size
    image = Draw.MolToImage(molecule, size=(400, 400))
    
    # Save the image
    image.save(str(output_path))
    print(f"✓ Formaldehyde structure saved to: {output_path}")


def main():
    """Main execution function."""
    try:
        # Ensure output directory exists
        output_dir = ensure_output_directory()
        output_file = output_dir / "formaldehyde.png"
        
        # Generate the formaldehyde image
        generate_formaldehyde_image(output_file)
        
        print("\nSuccess! The formaldehyde molecule structure has been generated.")
        
    except ImportError as e:
        print(f"Error: Missing required package. {e}")
        print("Please install dependencies: pip install -r requirements.txt")
    except Exception as e:
        print(f"Error: {e}")
        raise


if __name__ == "__main__":
    main()
