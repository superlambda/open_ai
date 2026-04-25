import os,openai,backoff
import pandas as pd
from openai import OpenAI
import subprocess
subprocess.run('openai api fine_tunes.create --training_file data/prepared_data_prepared.jsonl --model curie --suffix "ultraman"'.split())

