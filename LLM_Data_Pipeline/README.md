# LLM Data Pipeline Labs

Production-ready data pipeline examples for Large Language Model training, demonstrating efficient data loading, preprocessing, and distributed processing patterns.

## 📚 Overview

This repository contains 4 comprehensive examples covering essential data pipeline patterns for LLM training:

| File | Purpose | Dataset | Key Concepts |
|------|---------|---------|--------------|
| `Lab1.ipynb` | Basic LM Pipeline | WikiText-2 | Data loading, tokenization, fixed-length chunking, quality filtering |
| `Lab2.ipynb` | Streaming LM Pipeline | WikiText-2 | Memory-efficient streaming, train/val splits, rolling buffer |
| `streaming_shard_gpt2.py` | Multi-Process LM | WikiText-103 | Data parallelism, worker sharding, distributed processing |
| `streaming_shard.py` | Multi-Process Classification | IMDB Reviews | Binary sentiment analysis, parallel data loading |

## 🎯 Learning Objectives

### Lab 1: Foundational Pipeline
- Load and preprocess text datasets
- Apply quality filters to improve data quality
- Tokenize text efficiently with batched processing
- Create fixed-length training sequences
- Measure pipeline performance and efficiency

### Lab 2: Streaming Architecture
- Process large datasets without loading into RAM
- Implement streaming with train/validation splits
- Use rolling buffers for token concatenation
- Monitor real-time metrics and throughput
- Apply production-ready patterns

### Lab 3: Parallel Language Modeling
- Distribute data across multiple workers
- Implement manual sharding strategies
- Track per-worker performance metrics
- Coordinate parallel data processing
- Scale to larger datasets (WikiText-103)

### Lab 4: Classification Pipelines
- Build pipelines for supervised tasks
- Handle labeled data with sentiment classification
- Track label distributions across workers
- Compare classification vs LM preprocessing
- Optimize for longer sequence lengths

## 🚀 Quick Start

### Prerequisites

```bash
# Create conda environment
conda create -n ml-env python=3.10
conda activate ml-env

# Install dependencies
pip install transformers datasets torch
```

### Running Notebooks

```bash
# Start Jupyter
jupyter lab

# Open Lab1.ipynb or Lab2.ipynb and run all cells
```

### Running Scripts

```bash
# Language Modeling with 4 parallel workers
python streaming_shard_gpt2.py

# Sentiment Classification with 4 parallel workers
python streaming_shard.py
```

## 📖 Detailed Description

### Lab1.ipynb - Basic Language Model Pipeline

**What it does:**
- Loads WikiText-2 dataset and applies quality filters
- Removes empty/short texts to improve data quality
- Tokenizes using GPT-2 tokenizer
- Groups tokens into fixed 128-token blocks
- Creates PyTorch DataLoader for training

**Output includes:**
- Dataset statistics (samples, retention rate)
- Tokenization metrics (speed, token counts)
- Pipeline efficiency measurements
- Sample decoded text for validation

### Lab2.ipynb - Streaming Pipeline

**What it does:**
- Loads WikiText-2 in streaming mode (minimal memory)
- Processes both train and validation splits
- Tokenizes on-the-fly during iteration
- Implements rolling buffer for cross-document concatenation
- Provides real-time monitoring and metrics

**Output includes:**
- Train and validation data loaders
- Throughput measurements (tokens/sec)
- Progress tracking with timestamps
- Pipeline performance comparison

### streaming_shard_gpt2.py - Multi-Process Language Modeling

**What it does:**
- Launches 4 parallel worker processes
- Each worker handles 1/4 of WikiText-103 dataset
- Implements manual round-robin sharding
- Tracks per-worker metrics and throughput
- Demonstrates distributed training patterns

**Output includes:**
- Per-worker progress and statistics
- Batch shapes and token counts
- Individual worker throughput
- Overall parallel efficiency metrics

### streaming_shard.py - Multi-Process Classification

**What it does:**
- Binary sentiment classification on IMDB reviews
- 4 parallel workers process data simultaneously
- Tracks positive/negative label distribution
- Uses DistilBERT tokenizer
- Longer sequences (256 tokens) for movie reviews

**Output includes:**
- Sample text with sentiment labels
- Label distribution per worker
- Classification throughput (samples/sec)
- Worker coordination statistics

## 🔧 Technical Features

### Data Processing
- **Quality Filtering**: Remove low-quality samples
- **Efficient Tokenization**: Batched processing with HuggingFace
- **Fixed-Length Chunking**: Optimal for transformer models
- **Rolling Buffers**: Cross-document token concatenation

### Performance Optimization
- **Streaming**: Process datasets larger than RAM
- **Multi-Processing**: Parallel data loading across CPU cores
- **Manual Sharding**: Distribute data efficiently
- **Progress Tracking**: Real-time metrics and monitoring

### Production Patterns
- **Train/Val Splits**: Proper data separation
- **Throughput Metrics**: Performance measurement
- **Error Handling**: Robust pipeline design
- **Detailed Logging**: Comprehensive monitoring

## 📊 Example Output

### Lab1 Example
```
Loading dataset...
✓ Dataset loaded in 4.54s
Total samples: 36718

Applying quality filters...
After filtering: 17135 samples (removed 19583)
Data retention: 46.7%

✓ Tokenization completed in 6.86s
  Average tokens per sample: 144.0
  Total tokens in dataset: 2,328,337

✓ Created 18180 training sequences
  Efficiency: 99.9% of tokens retained
```

### streaming_shard_gpt2.py Example
```
MULTI-PROCESS STREAMING DATA PIPELINE
======================================================================
Configuration:
  Processes: 4
  Model: gpt2
  Dataset: WikiText-103 (streaming)

[rank 0] Batch 0 → torch.Size([4, 128]) | Tokens: 512 | Throughput: 256 tok/s
[rank 1] Batch 0 → torch.Size([4, 128]) | Tokens: 512 | Throughput: 245 tok/s
...
```

## 🎓 Use Cases

- **Learning**: Understand LLM data preprocessing pipelines
- **Research**: Experiment with different preprocessing strategies
- **Production**: Adapt patterns for real-world training
- **Teaching**: Educational examples for ML courses
- **Prototyping**: Quick setup for new LLM projects

## 📦 Dependencies

- `transformers` - HuggingFace model and tokenizer support
- `datasets` - Efficient dataset loading and streaming
- `torch` - PyTorch for DataLoader and tensor operations
- Python 3.8+

## 🤝 Contributing

Feel free to open issues or submit pull requests for improvements!

## 📝 License

MIT License - feel free to use for learning and production projects.

## 🔗 Resources

- [HuggingFace Datasets](https://huggingface.co/docs/datasets/)
- [Transformers Documentation](https://huggingface.co/docs/transformers/)
- [PyTorch DataLoader Guide](https://pytorch.org/tutorials/beginner/basics/data_tutorial.html)

---

**Note**: First run will download tokenizers and dataset shards (~10MB). Subsequent runs use cached data.

