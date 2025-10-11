# MoSEF Applied ML Project

## Setup Instructions

### Prerequisites

- Python 3.10 or higher (but less than 3.13)
- Poetry (for dependency management)

### Installation

1. **Install Poetry** (if not already installed):
   ```bash
   curl -sSL https://install.python-poetry.org | python3 -
   ```

2. **Install project dependencies**:
   ```bash
   poetry install
   ```

3. **Activate the virtual environment**:
   ```bash
   poetry shell
   ```

### Running Jupyter Notebooks

#### Method 1: Using Poetry directly

1. **Start Jupyter from the project root**:
   ```bash
   poetry run jupyter notebook
   ```

2. **Or start Jupyter Lab**:
   ```bash
   poetry run jupyter lab
   ```

#### Method 2: Using Poetry kernel with VS Code

1. **Install the Poetry kernel for Jupyter**:
   ```bash
   poetry run python -m ipykernel install --user --name mosef-ml --display-name "MoSEF ML"
   ```

2. **In VS Code**:
   - Open the notebook file (`.ipynb`) in VS Code
   - Click on the kernel selector in the top-right corner of the notebook
   - Select "MoSEF ML" from the list of available kernels
   - If you don't see it, click "Select Another Kernel..." → "Jupyter Kernel" → "MoSEF ML"

#### Method 3: Using Poetry shell + Jupyter

1. **Activate Poetry environment**:
   ```bash
   poetry shell
   ```

2. **Start Jupyter**:
   ```bash
   jupyter notebook
   ```

### Project Structure

```
ML-MoSEF/
├── data/                    # Dataset files
├── notebook/                # Jupyter notebooks
│   └── Analyse exploratoire de données (EDA).ipynb
├── pyproject.toml          # Poetry configuration
└── README.md               # This file
```

### Dependencies

The project includes the following key dependencies:
- **Data Analysis**: pandas, numpy
- **Visualization**: matplotlib, seaborn, plotly
- **Machine Learning**: scikit-learn
- **Notebooks**: jupyter
- **Utilities**: tqdm (progress bars)

### Troubleshooting

**If Poetry kernel doesn't appear in VS Code**:
1. Make sure you've run: `poetry run python -m ipykernel install --user --name mosef-ml --display-name "MoSEF ML"`
2. Restart VS Code
3. Try refreshing the kernel list in the notebook

**If you get import errors**:
1. Ensure you're using the correct kernel (MoSEF ML)
2. Verify dependencies are installed: `poetry show`
3. Try reinstalling: `poetry install --sync`
