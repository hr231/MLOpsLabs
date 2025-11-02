# DVC Lab - Data Version Control with Google Cloud Storage

## Overview

DVC (Data Version Control) is an open-source tool for versioning ML datasets. This lab demonstrates tracking datasets with DVC using Google Cloud Storage as remote storage.

Dataset: [Credit Card Dataset for Clustering](https://www.kaggle.com/datasets/arjunbhasin2013/ccdata)

## Setup

### 1. Install DVC with Google Cloud Support
```bash
pip install dvc[gs]
```

### 2. Configure Google Cloud Storage Remote
```bash
dvc remote add -d lab2 gs://<your-bucket-name>
dvc remote modify lab2 credentialpath <path-to-credentials.json>
```

### 3. Track Data with DVC
```bash
dvc add data/CC_GENERAL.csv
git add data/CC_GENERAL.csv.dvc data/.gitignore
git commit -m "Track dataset with DVC"
dvc push
```

## Version Comparison

| Aspect | Version 1 | Version 2 |
|--------|-----------|-----------|
| **MD5 Hash** | `c9b0bb7fc9e241b81da92c3528103664` | `841872c0e3ba7528202160f3afdf6513` |
| **Size** | 902,879 bytes | 1,020,772 bytes |
| **Rows** | 8,950 customers | 8,955 customers |
| **Git Commit** | `49f663e` | `cd7fc59` |
| **Changes** | Original dataset | Added 5 new customers |

## Key Commands

### Track and Push Data
```bash
dvc add data/CC_GENERAL.csv
git add data/CC_GENERAL.csv.dvc
git commit -m "Update dataset"
dvc push
```

### Switch to Version 1
```bash
git checkout 49f663e data/CC_GENERAL.csv.dvc
dvc checkout
```

### Switch to Version 2
```bash
git checkout cd7fc59 data/CC_GENERAL.csv.dvc
dvc checkout
```

### Check Status
```bash
dvc status
dvc status --cloud
```

## What Gets Stored Where

| Item | Stored In | Command |
|------|-----------|---------|
| Actual data (CC_GENERAL.csv) | Google Cloud Storage | `dvc push` |
| Tracking file (.dvc) | Git | `git push` |
| Credentials (.json) | Local only (gitignored) | N/A |

## Project Structure

```
Lab_1/
├── data/
│   ├── CC_GENERAL.csv          # Actual data (ignored by Git)
│   ├── CC_GENERAL.csv.dvc      # DVC tracking file
│   └── .gitignore              # Ignores actual data files
├── modify_data.py              # Script to create Version 2
├── check_version.py            # Script to verify dataset version
└── README.md                   # This file
```

## Key Concepts

- **Git tracks**: `.dvc` metadata files (small)
- **DVC tracks**: Actual data files (large)
- **Hash-based**: Each version has unique MD5 hash
- **Seamless switching**: Easy revert to any previous version
- **Cloud storage**: Team collaboration without bloating Git repo