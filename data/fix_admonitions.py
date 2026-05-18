import os, glob, re

base = 'BaofojiaoGuide/docs/subjects/9618-computer-science/paper-3/topics'
all_files = glob.glob(os.path.join(base, '**/*.md'), recursive=True)

for fpath in sorted(all_files):
    with open(fpath, 'rb') as f:
        raw = f.read()
    
    # Check if this file has admonitions
    if b':::' not in raw:
        continue
    
    try:
        text = raw.decode('utf-8')
    except:
        print(f'SKIP (encoding): {os.path.relpath(fpath, base)}')
        continue
    
    changed = False
    
    # Fix 1: Move ::: closing from end of content lines to its own line
    # Pattern: "content :::" -> "content\n:::"
    text = re.sub(r'([^\n])\n:::', r'\1\n\n:::', text)
    text = re.sub(r'(?<!\n)(:::)\s*$', r'\n\1', text, flags=re.MULTILINE)
    
    # Fix 2: Move ::: closing that's attached to the end of a line to its own line
    # Pattern: "...内容?:::" or "...内容？:::"
    text = re.sub(r'([^ \n])(:::)\s*(\n|$)', r'\1\n\2\3', text)
    
    # More targeted: find any ::: at end of content line (not preceded by blank line)
    lines = text.split('\n')
    new_lines = []
    for i, line in enumerate(lines):
        stripped = line.strip()
        # If line ends with ::: and has other content (not just :::)
        if stripped.endswith(':::') and stripped != ':::' and ':::' not in stripped[:-3]:
            # Split into content and ::: 
            content_part = line[:line.rfind(':::')]
            closing_part = line[line.rfind(':::'):]
            new_lines.append(content_part)
            new_lines.append(closing_part)
            changed = True
        else:
            new_lines.append(line)
    
    if changed:
        text = '\n'.join(new_lines)
    
    # Fix 3: Ensure proper blank lines around ::: blocks
    # After opening :::[...], ensure blank line before content
    text = re.sub(r'(:::\[[^\]]*\])(\n)(?!\n)', r'\1\n\n', text)
    # Before closing :::, ensure blank line
    text = re.sub(r'([^\n])\n(:::)\s*$', r'\1\n\n\2', text, flags=re.MULTILINE)
    
    # Fix 4: Remove any cases where ::: has no blank line before next content
    text = re.sub(r'(:::)\n\n\1', r'\1\n\1', text)  # adjacent ::: blocks
    
    if changed:
        with open(fpath, 'w', encoding='utf-8') as f:
            f.write(text)
        print(f'FIXED: {os.path.relpath(fpath, base)}')
    else:
        print(f'OK: {os.path.relpath(fpath, base)}')

print('\nDone!')
