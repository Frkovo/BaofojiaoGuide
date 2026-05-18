import os, glob

base = r'E:\Dev\BaofojiaoGuide\BaofojiaoGuide\docs\subjects\9618-computer-science\paper-4'

# Known correct Chinese words that should appear in files
keywords = ['常见错误', '题型', '解题方法', '考前', '评分', '考纲', '数组', '链表', '队列', '递归', '排序']

corrupted = []
ok_count = 0

for fpath in sorted(glob.glob(os.path.join(base, '**', '*.md'), recursive=True)):
    fname = os.path.relpath(fpath, base)
    try:
        with open(fpath, 'r', encoding='utf-8') as f:
            content = f.read()
    except UnicodeDecodeError:
        corrupted.append((fname, 'Cannot decode as UTF-8'))
        continue
    
    # Check for UTF-8 replacement character
    if '\ufffd' in content:
        corrupted.append((fname, 'Has replacement character'))
        continue
    
    # Check for garbled Chinese by looking for expected keywords
    has_valid_chinese = any(kw in content for kw in keywords)
    
    # Check title line
    title_ok = True
    for line in content.split('\n')[:5]:
        if line.startswith('title:'):
            title = line.split('title:', 1)[1].strip().strip("'\" ")
            # If title is short and should be Chinese but looks wrong
            break
    
    if '&lt;-' in content:
        # These files were modified by PowerShell - need to verify
        if not has_valid_chinese and any(ord(c) > 127 for c in content):
            corrupted.append((fname, 'Has high bytes but no valid Chinese keywords'))
        else:
            ok_count += 1
    else:
        ok_count += 1

print(f'Total files scanned: {ok_count + len(corrupted)}')
print(f'Potentially corrupted: {len(corrupted)}')
for fname, reason in corrupted:
    print(f'  {fname}: {reason}')
