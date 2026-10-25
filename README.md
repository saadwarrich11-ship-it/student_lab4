# Lab 4: Reproducible Workspace, Git and NumPy Performance

Based on the supplied lab handout (notebook filename `lab3.ipynb` as instructed).

## Setup
```bash
python -m venv venv
# Windows: venv\Scripts\activate
# macOS/Linux: source venv/bin/activate
python -m pip install -r requirements.txt
python -m ipykernel install --user --name student_lab4 --display-name "Python (student_lab4)"
jupyter notebook
```
Open `notebooks/lab3.ipynb`, select the environment kernel, and **Restart & Run All**.

The notebook generates `data/processed/timing_results.csv` and `standardised.npy`.
The included timing results were measured in the preparation environment, **not on the student's device**. Rerun locally for your own measurements.
The handout requires at least 10 meaningful Git commits; uploading a ZIP or files in one web commit does not meet that requirement.
