## File for data gathering using github API key

from github import Github
import os
import time
from tqdm import tqdm


g = Github(_ENV)
print(g.get_user())

query = "langchain language:python"

result = g.search_repositories(query)


no_of_repos = 1000

for i in range(no_of_repos):
  print(result[i].clone_url)
  print(result[i].tags_url) 
  os.system(f"git clone {result[i].clone_url} repos/{result[i].owner.login}/{result[i].name}")


import os
d = "repos"

for dirpath, dirnames, filenames in tqdm(os.walk(d)):
  for f in filenames:
    full_path = os.path.join(dirpath,f)

    if full_path.endswith(".py"):
      # print(f"Keeping {full_path}")
      pass
    else:
      if d in full_path:
        os.remove(full_path)
      else:
        print("kuch to gadbad hai")
        time.sleep(60)
        
        

def get_dir_size(start_path='.'):
    total_size = 0
    for dirpath, dirnames, filenames in os.walk(start_path):
        for f in filenames:
            fp = os.path.join(dirpath, f)
            # skip if it is symbolic link
            if not os.path.islink(fp):
                total_size += os.path.getsize(fp)

    return total_size

def get_subdir_count(start_path='.'):
    subdir_count = 0
    for dirpath, dirnames, filenames in os.walk(start_path):
        subdir_count += len(dirnames)
        break  # we just want to count the subdirectories in the start_path, not sub-subdirectories

    return subdir_count

dir_to_check = "/content/repos"  # replace with your directory

print(f"Total size of '{dir_to_check}' is {get_dir_size(dir_to_check)/(1024*1024)} MB")
print(f"Number of subdirectories in '{dir_to_check}' is {get_subdir_count(dir_to_check)}")

import os 
import time

MAX_CHAR_LENGTH = 512
MIN_CHAR_LENGTH = 400

NEWLINECHAR= "<N>"

full_paths = []
for dirpath, dirnames, filenames in os.walk(d):
  for f in filenames:
    full_path = os.path.join(dirpath,f)
    full_paths.append(full_path)

with open("python_code_text_data.txt","a") as f:
  for fpath in full_paths:
    try:
      d = open(fpath,"r").read()
      fd = d.replace("\n", NEWLINECHAR)

      if 100 < len(d) <= MAX_CHAR_LENGTH:
        f.write(fd+'\n')
      else:
        sd = fd.split(f"{NEWLINECHAR}{NEWLINECHAR}")
        substring = ""
        for split in sd:
          substring += split+f"{NEWLINECHAR}{NEWLINECHAR}"
          if MIN_CHAR_LENGTH <= len(substring) <= MAX_CHAR_LENGTH:
            f.write(substring+'\n')
            substring = ""
    except Exception as e:
      print(str(e))