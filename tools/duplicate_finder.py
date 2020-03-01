import os
import hashlib
from tqdm import tqdm


# Remove duplicates
indir = "test_duplicates/"
files = os.listdir(indir)
files = [f for f in files if os.path.isfile(os.path.join(indir, f))]

filepaths = [os.path.join(indir, file) for file in files]
hash_dict = {}

for file in tqdm(filepaths):
	with open(file, 'r') as fopen:
		text = fopen.read().splitlines()
		for line in reversed(text):
			if "platform" in line:
				text.remove(line)
	hash_dict[file] = hashlib.sha1(repr(text).encode()).hexdigest()


flipped = {}
for key, value in hash_dict.items():
    if value not in flipped:
        flipped[value] = [key]
    else:
        flipped[value].append(key)


duplicated = []
for circs in flipped.values():
	if len(circs) > 1:
		duplicated.append(circs)


print(duplicated)
print(len(set(hash_dict.values())), len(hash_dict.values()))
