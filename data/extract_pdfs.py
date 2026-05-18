import pdfplumber, os, glob

qp_dir = 'papers/9618'
for f in sorted(glob.glob(os.path.join(qp_dir, '**/*_qp_*.pdf'), recursive=True)):
    base = os.path.basename(f)
    out = 'data/extracted/papers/' + base.replace('.pdf', '.txt')
    if os.path.exists(out):
        print(f'SKIP QP {base}')
        continue
    try:
        with pdfplumber.open(f) as pdf:
            text = ''
            for p in pdf.pages:
                t = p.extract_text()
                if t:
                    text += t + '\n'
        with open(out, 'w', encoding='utf-8') as fout:
            fout.write(text)
        print(f'OK QP {base} ({len(text)} chars)')
    except Exception as e:
        print(f'FAIL QP {base}: {e}')

for f in sorted(glob.glob(os.path.join(qp_dir, '**/*_ms_*.pdf'), recursive=True)):
    base = os.path.basename(f)
    out = 'data/extracted/ms/' + base.replace('.pdf', '.txt')
    if os.path.exists(out):
        print(f'SKIP MS {base}')
        continue
    try:
        with pdfplumber.open(f) as pdf:
            text = ''
            for p in pdf.pages:
                t = p.extract_text()
                if t:
                    text += t + '\n'
        with open(out, 'w', encoding='utf-8') as fout:
            fout.write(text)
        print(f'OK MS {base} ({len(text)} chars)')
    except Exception as e:
        print(f'FAIL MS {base}: {e}')

print('Done!')
