# Heat Dome Analysis

This repository contains code and data used to analyze heat domes using geopotential height and temperature anomalies, as part of the course *LPHYS1351 - Projet personnel en physique* at UCLouvain. The main objective is to detect and characterize extreme heat dome events over the Northern Hemisphere through anomaly-based analysis.

## Contents

The data used in this project comes from the ERA5 reanalysis dataset.

- Data for Brussels
- Scripts to download geopotential and temperature data for the Northern Hemisphere (not included in this repository due to file size limitations)
- Final project report and a supplement focused on the Lytton heat dome event (June 2021)
- Several animations showing the evolution of geopotential and temperature fields

## Repository Structure

```
Heat-dome-analysis
├── Projet_final.pdf
├── notebooks # Jupyter notebooks with all the code
│ └── projet-Dômes-chaleur.ipynb
│ └── projet-Dômes-chaleur.pdf
├── data # Local ERA5 data and download scripts
│ ├── geopotential_bruxelles.nc
│ ├── temp_bx.nc
│ ├── téléchargement-géopotentiel.py
│ └── téléchargement-température.py
├── animations # MP4 animations of data evolution
├── Supplements # Project documents
│ ├── 2021 Heat Wave.pdf
├── requirements.txt # Python dependencies
└── README.md # Project documentation
```

## Getting Started

### Requirements

Make sure you have Python 3 installed. Required packages are listed in `requirements.txt`.

### Installation

1. Clone the repository:
```bash
git clone https://github.com/clemence-g/Heat-dome-analysis.git
```

2. Install the dependencies:
```
pip install -r requirements.txt
```

3. Download ERA5 data for the Northern Hemisphere. To set up your CDS API key, follow the instructions at:
[https://cds.climate.copernicus.eu/how-to-api]

Use the téléchargement-géopotentiel.py and téléchargement-température.py scripts to retrieve the required data.

4. Run the analysis using the notebook:
Open notebooks/anomaly_detection.ipynb in Jupyter and follow the cells.


