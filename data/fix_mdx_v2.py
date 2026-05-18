import os, glob, re

base = 'BaofojiaoGuide/docs/subjects/9618-computer-science/paper-3/topics'
all_files = glob.glob(os.path.join(base, '**/*.md'), recursive=True)

for fpath in all_files:
    try:
        with open(fpath, 'rb') as f:
            raw = f.read()
        
        # First, try to decode and fix encoding issues
        text = raw.decode('utf-8', errors='replace')
        
        # Revert the damage from fix_mdx.py v1:
        # Fix 1: `<`details> → <details>
        text = re.sub(r'`<`details>', '<details>', text)
        text = re.sub(r'`<`summary>', '<summary>', text)
        text = re.sub(r'</summary>', '</summary>', text)
        
        # Fix 2: `<`letter> → <letter> (BNF patterns)
        text = re.sub(r'`<`(\w+)>', r'<\1>', text)
        
        # Fix 3: `<=` → <= (MS patterns that got double-wrapped)
        text = re.sub(r'`<=`', '<=', text)
        text = re.sub(r'`>=`', '>=', text)
        
        # Fix 4: Other `<` that shouldn't have backticks (e.g. <summary)
        text = re.sub(r'`<`([a-zA-Z/])', r'<\1', text)
        
        # Fix 5: Remove replacement characters (U+FFFD) from corrupted Chinese
        text = text.replace('\ufffd', '')
        
        # Fix 6: Add blank line before <details> if not present
        text = re.sub(r'([^\n])\n(<details>)', r'\1\n\n\2', text)
        
        # Fix 7: Separate <details> and <summary> onto their own lines
        text = text.replace('<details><summary>', '<details>\n<summary>')
        
        # Fix 8: Ensure </summary> is followed by a blank line
        text = text.replace('</summary>\n', '</summary>\n\n')
        
        # Fix 9: In MS list items inside details, ensure < and <= in comparisons are escaped
        # Actually, they should be fine inside <details> since it's markdown content
        
        # Write back
        with open(fpath, 'w', encoding='utf-8') as f:
            f.write(text)
        
        print(f'FIXED: {os.path.relpath(fpath, base)}')
    except Exception as e:
        print(f'ERROR: {os.path.relpath(fpath, base)}: {e}')

print('\nDone!')
