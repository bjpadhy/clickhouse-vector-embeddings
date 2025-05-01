#!/opt/clickhouse/venv/bin/python3

import os
import sys
import json

# Model cache location
os.environ["TRANSFORMERS_CACHE"] = "/opt/clickhouse/model_cache"
os.environ["HF_HOME"] = "/opt/clickhouse/model_cache"

from sentence_transformers import SentenceTransformer

model = SentenceTransformer('all-MiniLM-L6-v2')

for size in sys.stdin:
    # Gather batched data for process
    texts = []
    for row in range(0, int(size)):
        texts.append(sys.stdin.readline())

    # Obtain the vector
    embeddings = model.encode(texts)

    # Dump the vectos
    for vector in embeddings:
        print(json.dumps(vector.tolist()))

    sys.stdout.flush()