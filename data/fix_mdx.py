import os, glob, re

base = 'BaofojiaoGuide/docs/subjects/9618-computer-science/paper-3/topics'
all_files = glob.glob(os.path.join(base, '**/*.md'), recursive=True)

for fpath in all_files:
    try:
        with open(fpath, 'r', encoding='utf-8') as f:
            content = f.read()
    except UnicodeDecodeError:
        # File is corrupted, try reading with other encoding
        try:
            with open(fpath, 'r', encoding='gbk') as f:
                content = f.read()
            with open(fpath, 'r', encoding='utf-8') as f:
                content = f.read()
        except:
            content = None
    
    if content is None:
        # File is corrupted beyond repair, recreate from scratch
        continue
    
    changed = False
    
    # Fix 1: Add blank line before <details> if not preceded by blank line
    content = re.sub(r'([^\n])\n(<details>)', r'\1\n\n\2', content)
    if re.search(r'([^\n])\n(<details>)', content):
        changed = True
    
    # Fix 2: Replace <details>...</details> that spans a single line with proper multi-line
    # Actually, let's just ensure <details> tags are always on their own lines
    
    # Fix 3: Replace bare <= and < in text (not in fenced code or backticks)
    lines = content.split('\n')
    new_lines = []
    in_fence = False
    
    for line in lines:
        if line.strip().startswith('```'):
            in_fence = not in_fence
            new_lines.append(line)
            continue
        
        if not in_fence:
            # Fix <= in MS text
            line = re.sub(r'(?<!`)<=', '`<=`', line)
            line = re.sub(r'(?<!`)>=', '`>=`', line)
            # Fix bare < that's not HTML/JSX tag
            # Only fix < followed by text (not by / or space or >)
            line = re.sub(r'(?<!`)<(?![ />\n])', '`<`', line)
        
        new_lines.append(line)
    
    new_content = '\n'.join(new_lines)
    
    if new_content != content:
        changed = True
    
    if changed:
        with open(fpath, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f'FIXED: {fpath}')
    else:
        print(f'OK: {fpath}')

print('\nDone!')
