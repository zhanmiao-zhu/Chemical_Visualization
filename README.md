# Chemical Visualization

A project for generating and visualizing phenol-formaldehyde (phenolic resin) polymerization animations.

## Project Structure

### `/src`
**Python source code** - Contains the main scripts for:
- Molecular structure generation and manipulation
- Reaction simulation logic
- Data processing and analysis
- Animation frame generation (when implemented)

### `/assets`
**Static assets and data files** - Stores:
- Input molecular structure files (e.g., PDB, MOL2 formats)
- Texture maps and material definitions
- Reference data and constants for chemical reactions
- Base geometry for visualization

### `/output`
**Generated files** - Contains:
- Animation frames (images, video files)
- Molecular coordinate data
- Simulation results and logs
- Final rendered visualizations

### `/blender`
**Blender project files and scripts** - Includes:
- `.blend` files for 3D scene setup and rendering
- Blender Python scripts for automated rendering
- Camera and lighting configurations
- Material definitions and shaders

### `/docs`
**Documentation** - Contains:
- Project documentation and notes
- Research references and methodology
- Installation and usage guides
- Technical specifications

## Setup

1. Create a Python virtual environment:
   ```bash
   python -m venv venv
   ```

2. Activate the virtual environment:
   - Windows: `venv\Scripts\activate`
   - macOS/Linux: `source venv/bin/activate`

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Project Status

- [x] Initial project structure
- [ ] Molecular structure generation
- [ ] Polymerization simulation
- [ ] Blender visualization setup
- [ ] Animation generation

## Next Steps

- Define molecular model classes
- Implement reaction kinetics simulation
- Set up Blender Python API integration