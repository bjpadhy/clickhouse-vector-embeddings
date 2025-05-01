# ClickHouse Vector Embeddings
In-database vector embeddings for semantic search using Clickhouse UDFs and sentence-transformers.

## About

This project demonstrates a novel approach to building semantic search capabilities by generating vector embeddings directly within Clickhouse. It eliminates the need for external preprocessing pipelines by leveraging Clickhouse's UDFs and Python integration.

## Features

- **In-Database Embeddings**: Generate embeddings directly in Clickhouse
- **Optimized Performance**: Utilize executable pools and data chunking
- **Sentence Transformer Integration**: Powered by the all-MiniLM-L6-v2 model
- **Simple Architecture**: Single system for both storage and semantic search

## Getting Started

### Prerequisites

- Clickhouse server with Python UDF support
- Python 3.7+
- Required Python packages:
  ```
  sentence-transformers>=2.2.0
  transformers>=4.18.0
  torch>=1.10.0
  ```

### Installation

1. Clone the repository
   ```bash
   git clone https://github.com/bjpadhy/clickhouse-vector-embeddings.git
   cd clickhouse-vector-embeddings
   ```

2. Setup the Python venv and install required packages
    ```bash
    # Setup and set venv ownership
    sudo mkdir -p /opt/clickhouse/venv && python3 -m venv /opt/clickhouse/venv
    sudo chown -R clickhouse:clickhouse /opt/clickhouse/venv

    # Activate and install packaged
    sudo -u clickhouse /opt/clickhouse/venv/bin/pip install sentence-transformers

    # Create model cache directory to load models
    sudo mkdir -p /opt/clickhouse/model_cache
    sudo chown -R clickhouse:clickhouse /opt/clickhouse/model_cache
    ```

3. Configure Clickhouse
   ```bash
   # Make the files executable
   chmod +x text_embedder.py
   chmod +x embedder.yaml
   
   # Copy the script to a location accessible by Clickhouse
   cp text_embedder.py /var/lib/clickhouse/user_scripts/text_embedder.py

   # Copy the config yaml to a location accessible by Clickhouse
   cp embedder.yaml /etc/clickhouse-server/embedder.yaml
   ```

## Usage
1. Generate embedding
    ```sql
    SELECT embed('Hello World!');
    ```
2. Using with semantic search
    ```sql
    WITH list_items AS
    (
        SELECT arrayJoin(['cake', 'grilled_chicken', 'shwarma', 'apple', 'pizza']) AS item
    )
    SELECT li.item,
           cosineDistance(embed(li.item), embed('italian')) AS similarity_score
    FROM list_items AS li
    ORDER BY similarity_score;
    ```
  ![Screenshot 2025-05-01 185636](https://github.com/user-attachments/assets/5162db41-7ae7-41cd-95f8-d781751c9509)



