import os
from datasets import load_dataset
from datasets import load_from_disk

datasets_path = "wikipedia_dump"

if os.path.exists(datasets_path):

    wiki = load_from_disk(datasets_path)

else:

    wiki = load_dataset("wikimedia/wikipedia", "20231101.en")

    wiki.save_to_disk("wikipedia_dump")

print(wiki)