# DVC Experiment Summary

## 🎯 Objective
Demonstrate Data Version Control (DVC) with Google Cloud Storage for ML dataset versioning

## ✅ What We Accomplished

### 1. **Initial Setup**
- ✅ Initialized DVC in MLOpsLabs root directory
- ✅ Configured Google Cloud Storage bucket: `dvc-lab-bucket-gigachad-2025`
- ✅ Secured GCP credentials in `.gitignore`

### 2. **Version 1: Original Dataset**
- **Dataset:** CC_GENERAL.csv from Kaggle
- **Size:** 902,879 bytes
- **Rows:** 8,950 customers
- **MD5 Hash:** `c9b0bb7fc9e241b81da92c3528103664`
- **Git Commit:** `49f663e - Add DVC tracking for CC_GENERAL.csv dataset`
- **Action:** Tracked with DVC and pushed to Google Cloud Storage

### 3. **Version 2: Updated Dataset**
- **Modification:** Added 5 new synthetic customers using `modify_data.py`
- **Size:** 1,020,772 bytes
- **Rows:** 8,955 customers (+5)
- **New Customers:** C99998, C99997, C99996, C99995, C99994
- **MD5 Hash:** `841872c0e3ba7528202160f3afdf6513` (NEW!)
- **Git Commit:** `cd7fc59 - Update dataset to Version 2 - Added 5 new customers`
- **Action:** Tracked with DVC and pushed to Google Cloud Storage

### 4. **Version Switching Demo**
Successfully demonstrated switching between dataset versions:

**Switch to Version 1:**
```bash
git checkout 49f663e DVC_Labs/Lab_1/data/CC_GENERAL.csv.dvc
dvc checkout
# Result: 8,950 customers, original data restored
```

**Switch back to Version 2:**
```bash
git checkout main DVC_Labs/Lab_1/data/CC_GENERAL.csv.dvc
dvc checkout
# Result: 8,955 customers, new customers back!
```

## 🔑 Key Learnings

1. **Git tracks metadata (.dvc files)** - Small, lightweight tracking files
2. **DVC tracks actual data** - Large datasets stored in Google Cloud
3. **Hash-based versioning** - Each version has unique MD5 hash
4. **Seamless switching** - Easy to revert to any previous dataset version
5. **Cloud storage integration** - Team can sync data without bloating Git repo

## 📊 What Gets Stored Where?

| Item | Size | Stored In | Command |
|------|------|-----------|---------|
| CC_GENERAL.csv (Version 1) | 903 KB | Google Cloud Storage | `dvc push` |
| CC_GENERAL.csv (Version 2) | 1021 KB | Google Cloud Storage | `dvc push` |
| CC_GENERAL.csv.dvc | ~100 bytes | Git/GitHub | `git push` |
| modify_data.py | ~2 KB | Git/GitHub | `git push` |
| GCP Credentials | ~2 KB | Local only | ❌ NEVER push |

## 🚀 Real-World Use Cases

1. **Experiment Tracking:** Train models on different dataset versions
2. **Data Auditing:** Know exactly what data was used for each model
3. **Team Collaboration:** Share large datasets without Git issues
4. **Rollback:** Quickly revert to previous data if issues found
5. **Reproducibility:** Recreate exact experimental conditions

## 📁 Final Project Structure

```
MLOpsLabs/
├── .dvc/
│   └── config                    # DVC remote configuration
├── .git/                         # Git repository
├── dvc-lab-*.json               # GCP credentials (in .gitignore)
│
└── DVC_Labs/Lab_1/
    ├── data/
    │   ├── CC_GENERAL.csv        # Actual data (ignored by Git)
    │   ├── CC_GENERAL.csv.dvc    # DVC tracking file (in Git)
    │   ├── data.txt              # Test file
    │   └── data.txt.dvc          # DVC tracking file (in Git)
    ├── modify_data.py            # Script to create Version 2
    ├── check_version.py          # Script to verify current version
    ├── README.md                 # Lab instructions
    └── requirements.txt          # Dependencies
```

## 🎓 Commands Reference

### Setup
```bash
dvc init                                    # Initialize DVC
dvc remote add -d lab2 gs://bucket-name    # Add remote storage
dvc remote modify lab2 credentialpath ...  # Add credentials
```

### Tracking Data
```bash
dvc add data/file.csv                      # Track file with DVC
git add data/file.csv.dvc                  # Track .dvc file with Git
git commit -m "Track dataset"              # Commit to Git
dvc push                                   # Push data to cloud
```

### Version Switching
```bash
git checkout <commit> path/to/file.dvc     # Get specific .dvc version
dvc checkout                               # Sync actual data with .dvc file
```

### Status Checks
```bash
dvc status                                 # Check local status
dvc status --cloud                         # Check cloud sync status
```

## 🎉 Conclusion

This experiment successfully demonstrates DVC's power for versioning ML datasets:
- ✅ Data versioning with hashes
- ✅ Cloud storage integration
- ✅ Easy switching between versions
- ✅ Git-like workflow for data
- ✅ Team collaboration ready

**DVC = Git for Data** 🚀

