#!/usr/bin/env python3
"""
9231 Further Mathematics Paper 2 — Full Documentation Generator
Reads ALL extracted PDF texts, generates proper LaTeX docs.
"""

import os, re, sys, json
from pathlib import Path

sys.stdout.reconfigure(encoding='utf-8')

BASE = Path(__file__).resolve().parent.parent
DOCS = BASE / 'docs' / 'subjects' / '9231-further-mathematics'
EXTRACTED = BASE / 'data' / 'extracted'

TOPIC_KEYS = ['hyperbolic-functions','matrices-fp2','differentiation',
              'integration','complex-numbers','differential-equations']

def e(path): path.mkdir(parents=True, exist_ok=True)

def w(path, text):
    e(path.parent)
    with open(path, 'w', encoding='utf-8') as f:
        f.write(text)

def read_texts():
    papers, ms = {}, {}
    pdir = EXTRACTED / 'papers'
    mdir = EXTRACTED / 'ms'
    if pdir.exists():
        for f in sorted(os.listdir(pdir)):
            if f.endswith('.txt'):
                with open(pdir/f, 'r', encoding='utf-8') as fh:
                    papers[f.replace('.txt','')] = fh.read()
    if mdir.exists():
        for f in sorted(os.listdir(mdir)):
            if f.endswith('.txt'):
                with open(mdir/f, 'r', encoding='utf-8') as fh:
                    ms[f.replace('.txt','')] = fh.read()
    return papers, ms

def extract_questions(text):
    """Extract question numbers and their content."""
    qs = {}
    lines = text.split('\n')
    i = 0
    while i < len(lines):
        line = lines[i].strip()
        # Match "1 ", "2 ", etc. as question markers (after instruction pages)
        if line.isdigit() and len(line) <= 2 and 'BLANK PAGE' not in lines[i-1] if i > 0 else True:
            num = int(line)
            if 1 <= num <= 15:
                # Read ahead to get question text
                qtext = []
                j = i + 1
                while j < len(lines) and j < i + 80:
                    l = lines[j]
                    if l.strip().isdigit() and 1 <= int(l.strip()) <= 15 and int(l.strip()) != num:
                        break
                    if '9231/' in l or '© UCLES' in l or '[Turn over' in l:
                        j += 1
                        continue
                    if l.strip():
                        qtext.append(l.strip())
                    j += 1
                if qtext:
                    qs[num] = ' '.join(qtext)
        i += 1
    return qs

def assess_topic(text):
    """Score topics by keyword matches."""
    topics = {k:0 for k in TOPIC_KEYS}
    tl = text.lower()
    if any(w in tl for w in ['sinh','cosh','tanh','sech','hyperbolic','coth']):
        topics['hyperbolic-functions'] += 15
    if any(w in tl for w in ['eigenvalue','eigenvector','characteristic equation','diagonalis','cayley','hamilton']):
        topics['matrices-fp2'] += 15
    if 'matrix' in tl and any(w in tl for w in ['inverse','determinant','singular']):
        topics['matrices-fp2'] += 10
    if any(w in tl for w in ['maclaurin',"d^2y",'implicit differentiation','parametr']):
        topics['differentiation'] += 15
    if any(w in tl for w in ['reduction formula','arc length','surface area','integration by parts']):
        topics['integration'] += 15
    if 'rectangle' in tl and ('area' in tl or 'bound' in tl or 'sum' in tl):
        topics['integration'] += 10
    if any(w in tl for w in ['de moivre','roots of unity','complex number','c + is','argand']):
        topics['complex-numbers'] += 15
    if any(w in tl for w in ['integrating factor','complementary function','particular integral','auxiliary equation']):
        topics['differential-equations'] += 15
    if 'differential equation' in tl:
        topics['differential-equations'] += 8
    if any(w in tl for w in ['system of equations','unique solution','consistent','inconsistent','three planes']):
        topics['matrices-fp2'] += 10
    best = max(topics, key=topics.get)
    return best if topics[best] >= 8 else None

def classify_all(papers, ms):
    """Classify all extracted content by topic."""
    from collections import defaultdict
    topic_questions = defaultdict(list)
    topic_ms = defaultdict(list)
    for fname, text in papers.items():
        qs = extract_questions(text)
        for num, qt in qs.items():
            t = assess_topic(qt)
            if t:
                ref = fname.replace('9231_','9231/').replace('_qp_','/qp/').replace('_','/')
                topic_questions[t].append((ref, num, qt[:200]))
    for fname, text in ms.items():
        # Find question sections in MS
        sections = re.split(r'Question\s+(\d+)', text)
        for i in range(1, len(sections)-1, 2):
            try:
                qnum = int(sections[i])
                qtext = sections[i+1][:200]
            except:
                continue
            t = assess_topic(qtext)
            if t:
                ref = fname.replace('9231_','9231/').replace('_ms_','/ms/').replace('_','/')
                topic_ms[t].append((ref, qnum, qtext[:200]))
    return topic_questions, topic_ms

# ======== LaTeX helpers ========

LT = {
    'sinh^{-1}': r'\sinh^{-1}',
    'cosh^{-1}': r'\cosh^{-1}',
    'tanh^{-1}': r'\tanh^{-1}',
    'sin^{-1}': r'\sin^{-1}',
    'cos^{-1}': r'\cos^{-1}',
    'tan^{-1}': r'\tan^{-1}',
}

def L(s):
    """Wrap a formula in inline LaTeX."""
    return f'${s}$'

def D(s):
    """Wrap in display LaTeX."""
    return f'$${s}$$'

def fix_math(s):
    """Convert plaintext math to LaTeX."""
    s = s.replace('→', r'\to ')
    return s

# ======== GENERATORS ========

def gen_index():
    w(DOCS/'index.md', """---
title: 9231 Further Mathematics
sidebar_position: 1
---

# 9231 Further Mathematics — Cambridge International AS & A Level

## Quick facts

| Item | Detail |
|------|--------|
| Code | 9231 |
| Level | AS & A Level |
| Syllabus | [2026–2027 syllabus](https://www.cambridgeinternational.org/Images/697357-2026-2027-syllabus.pdf) |
| Papers | 4 (P1: FP1, P2: FP2, P3: FM, P4: FPS) |
| Paper 2 | Further Pure Mathematics 2 |
| Duration | 2 hours |
| Total marks | 75 |

## Paper 2 topics

| # | Topic |
|---|-------|
| 2.1 | [Hyperbolic Functions](./topics/hyperbolic-functions) — definitions, identities, inverse, logarithmic forms |
| 2.2 | [Matrices (FP2)](./topics/matrices-fp2) — $$3{\\times}3$$ systems, eigenvalues, diagonalisation, Cayley–Hamilton |
| 2.3 | [Differentiation](./topics/differentiation) — inverse trig/hyperbolic, implicit, parametric, Maclaurin |
| 2.4 | [Integration](./topics/integration) — standard integrals, reduction formulae, arc length, surface area, rectangle bounds |
| 2.5 | [Complex Numbers](./topics/complex-numbers) — de Moivre, multiple angles, roots of unity, $$C+iS$$ series |
| 2.6 | [Differential Equations](./topics/differential-equations) — integrating factor, CF+PI, substitutions, IVPs |

## Key formulas

| Topic | Formula |
|-------|---------|
| Hyperbolic | {L(r'\sinh x = \\frac{e^x-e^{-x}}{2},\\; \\cosh x = \\frac{e^x+e^{-x}}{2}')} |
| Identity | {L(r'\\cosh^2 x - \\sinh^2 x \\equiv 1')} |
| de Moivre | {L(r'(\\cos\\theta + i\\sin\\theta)^n = \\cos n\\theta + i\\sin n\\theta')} |
| Maclaurin | {L(r'f(x) = f(0) + f\\'(0)x + \\frac{f\\'\\'(0)}{2!}x^2 + \\cdots')} |
| Arc length | {L(r's = \\int_a^b \\sqrt{1+(dy/dx)^2}\\,dx')} |
| Integrating factor | {L(r'\\mu = e^{\\int P\\,dx}')} |
""")

def gen_syllabus_overview():
    w(DOCS/'syllabus-overview.md', """---
title: Syllabus Overview
sidebar_position: 2
---

# Syllabus Overview — Further Pure Mathematics 2

## Topics

| # | Topic | Key content |
|---|-------|-------------|
| 2.1 | Hyperbolic Functions | {L(r'\\sinh x,\\cosh x,\\tanh x')} definitions (exponential forms), identities, graphs, inverse hyperbolic, logarithmic forms |
| 2.2 | Matrices | {L(r'3\\times3')} linear systems, {L(r'\\det A = 0')} and consistency, eigenvalues/vectors {L(r'A\\mathbf{e}=\\lambda\\mathbf{e}')}, diagonalisation {L(r'A = PDP^{-1}')}, Cayley–Hamilton theorem |
| 2.3 | Differentiation | {L(r'\\frac{d}{dx}\\sinh x = \\cosh x')}, {L(r'\\frac{d}{dx}\\sin^{-1}x')}, {L(r'\\frac{d}{dx}\\sinh^{-1}x')}, implicit {L(r'\\frac{d^2y}{dx^2}')}, parametric, Maclaurin series |
| 2.4 | Integration | {L(r'\\int\\frac{dx}{\\sqrt{a^2-x^2}}')} etc, completing square, reduction formulae, arc length, surface area, rectangle bounds |
| 2.5 | Complex numbers | de Moivre proof, multiple angles, power reduction, {L(r'C+iS')} series summation, {L(r'n')}th roots of unity |
| 2.6 | Differential equations | Integrating factor {L(r'\\mu = e^{\\int P\\,dx}')}, CF+PI, auxiliary equation {L(r'am^2+bm+c=0')}, substitutions, IVPs |

## Exam format

- **Paper 2**: 2 hours, 75 marks, 9–11 compulsory questions
- Calculators: standard scientific (no CAS/graphical)
- Formula sheet MF19 provided
- All working must be shown

## Prior knowledge

- Cambridge International A Level Mathematics (9709) Papers 1 & 3
- Paper 1: Further Pure Mathematics 1 (9231)

## Assessment objectives

| AO | Description | Weighting |
|----|-------------|-----------|
| AO1 | Knowledge and understanding of techniques | ~50% |
| AO2 | Application to solve problems | ~50% |
""")

def gen_exam_structure():
    w(DOCS/'exam-structure.md', """---
title: Exam Structure
sidebar_position: 3
---

# Exam Structure — Paper 2

## Paper overview

| Aspect | Detail |
|--------|--------|
| Code | 9231/22 |
| Title | Further Pure Mathematics 2 |
| Duration | 2 hours (120 min) |
| Marks | 75 |
| Questions | 9–11, all compulsory |
| Calculators | Standard scientific only (no CAS) |
| Formula list | MF19 supplied |

## Typical question distribution

| Topic | Marks | Typical Q numbers |
|-------|-------|-------------------|
| Hyperbolic functions | 8–12 | Q2, Q5 |
| Matrices (FP2) | 12–18 | Q1, Q7, Q9 |
| Differentiation | 6–10 | Q3, Q5 |
| Integration | 12–18 | Q4, Q6, Q8 |
| Complex numbers | 12–18 | Q3, Q7 |
| Differential equations | 10–15 | Q1, Q9 |

## Command words

| Word | Required response |
|------|-------------------|
| **Show that** | Full derivation, justify each step |
| **Find / Determine** | Obtain answer with key working |
| **Solve** | All solutions (may include complex) |
| **Prove** | Logical step-by-step argument |
| **Sketch** | Key features: asymptotes, intercepts, turning pts |
| **Evaluate** | Compute numerical value |
| **Hence** | Must use previous part's result |
| **State** | No working needed, answer must be exact |

## Answer format

- Non-exact answers: **3 significant figures** (1 d.p. for angles in degrees)
- Exact answers preferred: {L(r'\\sqrt{3},\\ \\pi/6')} not decimals
- Show ALL working — unsupported calculator answers get **zero marks**
""")

def gen_last_minute():
    w(DOCS/'last-minute-guide.md', """---
title: Last-Minute Guide
sidebar_position: 4
---

# Last-Minute Guide — Paper 2

## Hyperbolic functions

$$\\sinh x = \\frac{e^x - e^{-x}}{2},\\qquad \\cosh x = \\frac{e^x + e^{-x}}{2}$$
$$\\cosh^2 x - \\sinh^2 x \\equiv 1,\\qquad \\sinh 2x \\equiv 2\\sinh x\\cosh x$$

**Inverse hyperbolic (logarithmic forms):**
$$\\sinh^{-1} x = \\ln\\left(x + \\sqrt{x^2+1}\\right)$$
$$\\cosh^{-1} x = \\ln\\left(x + \\sqrt{x^2-1}\\right)\\quad (x \\ge 1)$$
$$\\tanh^{-1} x = \\frac{1}{2}\\ln\\left(\\frac{1+x}{1-x}\\right)\\quad (|x| < 1)$$

## Differentiation

$$\\frac{d}{dx}\\sin^{-1}x = \\frac{1}{\\sqrt{1-x^2}},\\qquad
\\frac{d}{dx}\\cos^{-1}x = -\\frac{1}{\\sqrt{1-x^2}}$$
$$\\frac{d}{dx}\\sinh^{-1}x = \\frac{1}{\\sqrt{1+x^2}},\\qquad
\\frac{d}{dx}\\cosh^{-1}x = \\frac{1}{\\sqrt{x^2-1}},\\qquad
\\frac{d}{dx}\\tanh^{-1}x = \\frac{1}{1-x^2}$$

**Maclaurin series:**
$$f(x) = f(0) + f'(0)x + \\frac{f''(0)}{2!}x^2 + \\frac{f'''(0)}{3!}x^3 + \\cdots$$

## Standard integrals

$$\\int\\frac{dx}{\\sqrt{a^2-x^2}} = \\sin^{-1}\\frac{x}{a} + C,\\qquad
\\int\\frac{dx}{a^2+x^2} = \\frac{1}{a}\\tan^{-1}\\frac{x}{a} + C$$
$$\\int\\frac{dx}{\\sqrt{x^2+a^2}} = \\sinh^{-1}\\frac{x}{a} + C,\\qquad
\\int\\frac{dx}{\\sqrt{x^2-a^2}} = \\cosh^{-1}\\frac{x}{a} + C$$

## Arc length & surface area

$$s = \\int_a^b\\sqrt{1+\\left(\\frac{dy}{dx}\\right)^2}\\,dx
\\quad\\text{(Cartesian)},\\qquad
s = \\int_{t_1}^{t_2}\\sqrt{\\left(\\frac{dx}{dt}\\right)^2+\\left(\\frac{dy}{dt}\\right)^2}\\,dt
\\quad\\text{(parametric)}$$
$$S = 2\\pi\\int_a^b y\\,\\sqrt{1+\\left(\\frac{dy}{dx}\\right)^2}\\,dx
\\quad\\text{(surface area)}$$

## Complex numbers

$$(\\cos\\theta + i\\sin\\theta)^n = \\cos n\\theta + i\\sin n\\theta$$
$$z^n + z^{-n} = 2\\cos n\\theta,\\qquad z^n - z^{-n} = 2i\\sin n\\theta$$
$$n\\text{th roots of unity: } z_k = e^{2\\pi i k/n},\\; k = 0,1,\\ldots,n-1$$

## Differential equations

**1st order:** {L(r'\\frac{dy}{dx} + P(x)y = Q(x)')}, IF {L(r'= e^{\\int P\\,dx}')}, then {L(r'\\frac{d}{dx}(\\mu y) = \\mu Q')}

**2nd order (constant coefficients):** {L(r'a\\frac{d^2y}{dx^2} + b\\frac{dy}{dx} + cy = 0')}
Auxiliary equation {L(r'am^2 + bm + c = 0')}:
- Real distinct {L(r'm_1,m_2')}: {L(r'y = Ae^{m_1x} + Be^{m_2x}')}
- Repeated {L(r'm')}: {L(r'y = (A+Bx)e^{mx}')}
- Complex {L(r'\\alpha \\pm i\\beta')}: {L(r'y = e^{\\alpha x}(A\\cos\\beta x + B\\sin\\beta x)')}

## Key first steps

| See this… | Do this first |
|-----------|--------------|
| Hyperbolic equation | Write in exponential form |
| {L(r'3\\times3')} system | Find determinant |
| Eigenvalues | {L(r'\\det(A-\\lambda I)=0')} |
| Integrate {L(r'1/\\sqrt{x^2+a^2}')} | Use {L(r'x = a\\sinh u')} substitution |
| de Moivre | Mod-arg form {L(r'r(\\cos\\theta+i\\sin\\theta)')} |
| 2nd order DE | Auxiliary equation |
| Maclaurin | Compute {L(r'f(0),f'(0),f''(0)')} |

## Time budget (75 marks / 120 min)

| Marks | Time |
|-------|------|
| 3 | ~5 min |
| 5 | ~8 min |
| 8 | ~13 min |
| 10 | ~16 min |
| 12+ | ~18–20 min |
""")

def gen_ms_keywords():
    w(DOCS/'common-ms-keywords.md', """---
title: Common MS Keywords
sidebar_position: 5
---

# Common Mark Scheme Keywords — Paper 2

## Hyperbolic Functions

| MS Phrase | Meaning |
|-----------|---------|
| "Uses correct **exponential form**" (M1) | Writing {L(r'\\sinh x = (e^x-e^{-x})/2')} etc |
| "**Applies identity**" (M1) | {L(r'\\cosh^2 x - \\sinh^2 x \\equiv 1')} or double-angle |
| "**Writes in logarithmic form**" (B1) | Expressing inverse hyperbolic in {L(r'\\ln')} form |
| "**Correct graph** with asymptotes" (B1) | e.g. {L(r'\\tanh x')} has asymptotes {L(r'y=\\pm1')} |

## Matrices

| MS Phrase | Meaning |
|-----------|---------|
| "**det = 0**" / "**Non‑singular**" (M1) | Determinant computed correctly |
| "**Characteristic equation**" (M1) | {L(r'\\det(A-\\lambda I)=0')} |
| "**Eigenvalue {L(r'\\lambda = \\ldots')}**" (A1) | Correct eigenvalues |
| "**Eigenvector** corresponding to {L(r'\\lambda')}" (A1) | Solving {L(r'(A-\\lambda I)\\mathbf{e}=0')} |
| "**Diagonalisation** {L(r'A = PDP^{-1}')}" (M1) | Expressing matrix in diagonal form |

## Differentiation

| MS Phrase | Meaning |
|-----------|---------|
| "{L(r'f(0),f'(0),f''(0)')} **found**" (M1) | Derivatives evaluated at zero |
| "**Correct Maclaurin series**" (A1) | Final expansion correct |
| "**Implicit differentiation** correct" (B1) | {L(r'\\frac{d}{dx}(y^2)=2y\\frac{dy}{dx}')} |

## Integration

| MS Phrase | Meaning |
|-----------|---------|
| "**Correct substitution**" (M1) | e.g. {L(r'x = a\\sinh u')} |
| "**Changes limits**" (M1) | Adjusting bounds for {L(r'u')} |
| "**Reduction formula**" (M1) | {L(r'I_n')} expressed in terms of {L(r'I_{n-1}')} |
| "**Arc length formula**" (M1) | {L(r'\\int\\sqrt{1+(dy/dx)^2}\\,dx')} |
| "**Rectangle area sum**" (M1) | Sum of areas compared to integral |

## Complex Numbers

| MS Phrase | Meaning |
|-----------|---------|
| "**De Moivre** applied" (M1) | {L(r'(\\cos\\theta+i\\sin\\theta)^n')} |
| "**Equates real/imaginary parts**" (M1) | Comparing coefficients |
| "**{L(r'C+iS')} method**" (M1) | Sum of GP then separate |
| "**Roots of unity**" (M1) | {L(r'z = e^{2\\pi i k/n}')} |

## Differential Equations

| MS Phrase | Meaning |
|-----------|---------|
| "**Integrating factor**" (M1) | {L(r'\\mu = e^{\\int P\\,dx}')} |
| "**Auxiliary equation**" (M1) | {L(r'am^2+bm+c=0')} |
| "**CF = ...**" (A1) | Complementary function correct |
| "**PI = ...**" (A1) | Particular integral correct |
| "**Uses initial condition(s)**" (M1) | Solves for constants |
""")

def gen_common_mistakes():
    w(DOCS/'common-mistakes.md', """---
title: Common Mistakes
sidebar_position: 6
---

# Common Mistakes — Paper 2

## Hyperbolic vs trigonometric confusion

| Correct (hyperbolic) | Wrong (trigonometric habit) |
|----------------------|---------------------------|
| {L(r'\\cosh^2 x - \\sinh^2 x \\equiv 1')} | {L(r'\\cosh^2 x + \\sinh^2 x \\equiv 1')} ✗ |
| {L(r'\\frac{d}{dx}\\cosh x = \\sinh x')} | {L(r'\\frac{d}{dx}\\cosh x = -\\sinh x')} ✗ |

## Matrix errors

- {L(r'\\det A = 0')} does NOT mean inconsistent — it means **no unique solution**. Could be consistent (infinite solutions) or inconsistent (none)
- Eigenvectors must match eigenvalues: eigenvector for {L(r'\\lambda_1')} belongs in same column of {L(r'P')} as {L(r'\\lambda_1')} in {L(r'D')}
- {L(r'AB')} means "apply {L(r'B')} then {L(r'A')}" — order matters!

## Differentiation pitfalls

| Function | Derivative | Common wrong answer |
|----------|------------|-------------------|
| {L(r'\\sin^{-1} x')} | {L(r'1/\\sqrt{1-x^2}')} | {L(r'-1/\\sqrt{1-x^2}')} ✗ |
| {L(r'\\cos^{-1} x')} | {L(r'-1/\\sqrt{1-x^2}')} | {L(r'1/\\sqrt{1-x^2}')} ✗ |
| {L(r'\\tanh^{-1} x')} | {L(r'1/(1-x^2)')} | {L(r'1/(1+x^2)')} ✗ |

## Integration gotchas

$$\\int\\frac{dx}{\\sqrt{a^2-x^2}} = \\sin^{-1}\\frac{x}{a} + C,\\quad
\\textbf{NOT}\\quad \\sinh^{-1}\\frac{x}{a}$$
$$\\int\\frac{dx}{\\sqrt{x^2+a^2}} = \\sinh^{-1}\\frac{x}{a} + C,\\quad
\\textbf{NOT}\\quad \\cosh^{-1}\\frac{x}{a}$$

## Complex number traps

- {L(r'\\arg(z_1z_2) = \\arg(z_1)+\\arg(z_2)')} but careful with principal value range {L(r'(-\\pi,\\pi]')}
- Conjugate root theorem: non-real roots occur in conjugate pairs
- Sum of all {L(r'n')}th roots of unity = 0

## DE disasters

**Integrating factor sign:** For {L(r'\\frac{dy}{dx} + Py = Q')}, IF {L(r'= e^{\\int P\\,dx}')}. If {L(r'\\frac{dy}{dx} - \\frac{2}{x}y = x')}, then {L(r'P = -2/x')}, IF {L(r'= x^{-2}')}.

**CF/PI overlap:** If RHS matches a term in CF, multiply PI by {L(r'x')} (or {L(r'x^2')} for double root).

**Initial conditions:** Apply AFTER finding general solution {L(r'y = y_{CF} + y_{PI}')}.
""")

def gen_paper2():
    base = DOCS / 'paper-2'
    e(base)
    w(base/'index.md', """---
title: Paper 2 Strategy
sidebar_position: 1
---

# Paper 2 — Strategy Guide

## Overview

- **Duration**: 2 hours | **Marks**: 75 | **Questions**: 9–11
- **Topics**: Hyperbolic functions, Matrices, Differentiation, Integration, Complex numbers, DEs

## Strategy

1. **Skim all questions** (2 min) — identify strongest topics
2. **Start with best topic** — build confidence, secure marks
3. **Parts link**: (a) → (b) → (c). Stuck on (b)? Use (a)'s result
4. **"Show that"**: full working required. Check algebra if answer doesn't match
5. **Last 10 min**: review signs, s.f., algebra

## Topic strategies

| Topic | Key tactic |
|-------|------------|
| Hyperbolic | Write in exponential form |
| Matrices | {L(r'\\det(A-\\lambda I)=0')} first |
| Integration | Integration by parts for reduction |
| Complex | {L(r'(\\cos\\theta+i\\sin\\theta)^n')} expansion |
| DEs | Put in standard form first |
""")
    w(base/'question-types.md', """---
title: Question Types
sidebar_position: 2
---

# Question Types — Paper 2

## Type 1: Hyperbolic identities & equations

**Recognise:** {L(r'\\sinh,\\cosh,\\tanh')} — "prove that", "solve", "express in logarithmic form"

**Method:**
1. Write in exponential form: {L(r'\\sinh x = \\frac{e^x-e^{-x}}{2}')}
2. Use identities: {L(r'\\cosh^2 x - \\sinh^2 x \\equiv 1')}
3. For inverses: {L(r'\\sinh^{-1} x = \\ln(x+\\sqrt{x^2+1})')}

**MS pattern:** M1 for identity/exponential form, A1 for answer

## Type 2: Matrix eigenvalues

**Recognise:** "eigenvalues", "eigenvectors", "diagonalisation", "Cayley–Hamilton"

**Method:**
1. {L(r'\\det(A-\\lambda I)=0')} → characteristic equation
2. {L(r'(A-\\lambda I)\\mathbf{e}=0')} → eigenvectors
3. {L(r'A = PDP^{-1}')} or {L(r'A^n = PD^nP^{-1}')}

**MS pattern:** M1 characteristic eqn, A1 eigenvalues, M1 eigenvectors, A1 final

## Type 3: Maclaurin series

**Recognise:** "Maclaurin series", "expand up to {L(r'x^n')}"

**Method:** {L(r'f(x) = f(0)+f'(0)x+\\frac{f''(0)}{2!}x^2+\\cdots')}

## Type 4: Reduction formulae

**Recognise:** "show that {L(r'\\int\\ldots = \\ldots I_{n-1}')}"

**Method:** Integration by parts → recurrence

## Type 5: de Moivre

**Recognise:** {L(r'\\cos n\\theta')} in powers, {L(r'\\sin^5\\theta')} as sum, {L(r'C+iS')}

**Method:** {L(r'z+z^{-1}=2\\cos\\theta,\\;z-z^{-1}=2i\\sin\\theta')}

## Type 6: Differential equations

**Recognise:** {L(r'\\frac{dy}{dx}+Py=Q')} or {L(r'ay''+by'+cy=f(x)')}

**Method:** IF or CF+PI
""")
    w(base/'strategy.md', """---
title: Strategy Detail
sidebar_position: 3
---

# Detailed Strategy

## Opening 5 min

- Scan pages, note topics
- Identify strongest areas
- Note mark allocations

## Hyperbolic Qs (8–12 marks)

- (a) Usually definitions/identities
- (b) Solving equations → exponential form
- Know logarithmic forms cold

## Matrix Qs (12–18 marks)

- {L(r'3\\times3')} system: {L(r'\\det \\neq 0 \\Rightarrow')} unique solution
- {L(r'\\det = 0')}: check consistency
- Eigenvalues: always write {L(r'\\det(A-\\lambda I)=0')}

## Integration Qs (12–18 marks)

- Reduction: integration by parts always
- Arc length: {L(r'\\int\\sqrt{1+(dy/dx)^2}\\,dx')}
- Surface area: {L(r'2\\pi\\int y\\sqrt{1+(dy/dx)^2}\\,dx')}

## Complex Qs (12–18 marks)

- Multiple angle → binomial expansion
- Powers → {L(r'(z\\pm z^{-1})')} method
- {L(r'C+iS')} → sum GP, separate parts

## DE Qs (10–15 marks)

- 1st order: IF — sign of {L(r'P')} is critical
- 2nd order: auxiliary eqn first
- Overlap? Multiply PI by {L(r'x')}
""")
    w(base/'time-management.md', """---
title: Time Management
sidebar_position: 4
---

# Time Management

## Budget (75 marks / 120 min)

| Marks | Time |
|-------|------|
| 3 | 5 min |
| 5 | 8 min |
| 8 | 13 min |
| 10 | 16 min |
| 12+ | 18–20 min |

## Phases

| Phase | Time | Action |
|-------|------|--------|
| Scan | 0–5 | Read all questions |
| Round 1 | 5–70 | Answer confident questions |
| Round 2 | 70–100 | Harder questions, partial |
| Round 3 | 100–110 | Fill gaps |
| Review | 110–120 | Check signs, s.f. |

## Time sinks to avoid

- ❌ Re-doing algebra (check line by line)
- ❌ Perfecting sketches (key features only)
- ❌ 10 min chasing 1 mark
""")
    w(base/'common-traps.md', """---
title: Common Traps
sidebar_position: 5
---

# Common Traps

**Trap 1:** "Show that" without working — MS awards M marks, not just A for answer.
**Fix:** Write EVERY algebraic step.

**Trap 2:** No {L(r'+C')} in indefinite integrals.
**Fix:** Always add constant.

**Trap 3:** Decimal instead of exact surd.
**Fix:** {L(r'2+\\sqrt{3}')} not 3.73 unless 3 s.f. asked.

**Trap 4:** Domain of inverse hyperbolic.
**Fix:** {L(r'\\cosh^{-1} x')} needs {L(r'x\\ge 1')}, {L(r'\\tanh^{-1} x')} needs {L(r'|x|<1')}.

**Trap 5:** Matrix multiplication order — {L(r'AB')} = B then A.

**Trap 6:** Eigenvalue sign — use {L(r'\\det(A-\\lambda I)=0')}.

**Trap 7:** Maclaurin at {L(r'x=0')} vs Taylor at other points.

**Trap 8:** Integration limits after substitution — must change them.

**Trap 9:** CF/PI overlap — multiply PI by {L(r'x')} or {L(r'x^2')}.

**Trap 10:** "Hence" means use previous result. Don't solve from scratch.
""")

def gen_topics(topic_qs, topic_ms):
    T = {
        'hyperbolic-functions': ('Hyperbolic Functions', 1, [
            "$$\\sinh x = \\frac{e^x - e^{-x}}{2},\\qquad \\cosh x = \\frac{e^x + e^{-x}}{2}$$",
            "$$\\tanh x = \\frac{\\sinh x}{\\cosh x} = \\frac{e^x - e^{-x}}{e^x + e^{-x}}$$",
            "$$\\cosh^2 x - \\sinh^2 x \\equiv 1,\\quad \\sinh 2x \\equiv 2\\sinh x\\cosh x,\\quad \\cosh 2x \\equiv \\cosh^2 x + \\sinh^2 x$$",
            "$$\\sinh^{-1} x = \\ln\\left(x + \\sqrt{x^2+1}\\right)\\quad (\\text{all } x)$$",
            "$$\\cosh^{-1} x = \\ln\\left(x + \\sqrt{x^2-1}\\right)\\quad (x \\ge 1)$$",
            "$$\\tanh^{-1} x = \\frac{1}{2}\\ln\\left(\\frac{1+x}{1-x}\\right)\\quad (|x| < 1)$$",
        ], [
            "Proof of identities — classic 'show that' worth 5–6 marks",
            "Solving hyperbolic equations — write in exponential form, solve quadratic in {L(r'e^x')}",
            "Graph sketching — {L(r'\\sinh x,\\cosh x,\\tanh x')} with asymptotes",
            "Logarithmic forms of inverse hyperbolic functions",
        ], [
            "Confusing {L(r'\\cosh^2 x - \\sinh^2 x \\equiv 1')} with {L(r'\\cos^2 x + \\sin^2 x \\equiv 1')}",
            "{L(r'\\cosh^{-1} x')} domain: requires {L(r'x \\ge 1')}",
            "{L(r'\\tanh^{-1} x')} domain: requires {L(r'|x| < 1')}",
            "Sign errors in logarithmic forms (especially {L(r'\\tanh^{-1} x')})",
        ]),
        'matrices-fp2': ('Matrices (Further Pure 2)', 2, [
            "$$\\det(A-\\lambda I) = 0 \\quad\\text{(characteristic equation)}$$",
            "$$A\\mathbf{e} = \\lambda\\mathbf{e} \\quad\\text{(eigenvalue equation)}$$",
            "$$A = PDP^{-1},\\quad A^n = PD^nP^{-1}$$",
            "Cayley–Hamilton: {L(r'p(A) = 0')} where {L(r'p(\\lambda) = \\det(A-\\lambda I)')}",
            "$$p(A) = 0 \\Rightarrow A^{-1} = \\frac{1}{\\det(A)}\\operatorname{adj}(A)$$",
        ], [
            "Setting up {L(r'3\\times3')} linear systems as matrix equations",
            "Determinant → unique/infinite/no solutions",
            "Geometric interpretation (three planes)",
            "Finding eigenvalues and eigenvectors",
            "Diagonalisation and powers",
            "Cayley–Hamilton theorem applications",
        ], [
            "{L(r'\\det A = 0')} means no *unique* solution—NOT necessarily inconsistent",
            "Eigenvector column order must match eigenvalue order in {L(r'D')}",
            "Sign errors in characteristic equation",
        ]),
        'differentiation': ('Differentiation', 3, [
            "$$\\frac{d}{dx}\\sin^{-1}x = \\frac{1}{\\sqrt{1-x^2}},\\quad \\frac{d}{dx}\\cos^{-1}x = -\\frac{1}{\\sqrt{1-x^2}}$$",
            "$$\\frac{d}{dx}\\sinh^{-1}x = \\frac{1}{\\sqrt{1+x^2}},\\quad \\frac{d}{dx}\\cosh^{-1}x = \\frac{1}{\\sqrt{x^2-1}}$$",
            "$$\\frac{d}{dx}\\tanh^{-1}x = \\frac{1}{1-x^2}$$",
            "$$\\frac{d}{dx}\\sinh x = \\cosh x,\\quad \\frac{d}{dx}\\cosh x = \\sinh x$$",
            "$$f(x) = f(0) + f'(0)x + \\frac{f''(0)}{2!}x^2 + \\frac{f'''(0)}{3!}x^3 + \\cdots$$",
        ], [
            "Differentiation of inverse trig and hyperbolic functions",
            "Implicit differentiation — 1st and 2nd derivatives",
            "Parametric differentiation — {L(r'\\frac{dy}{dx}')} and {L(r'\\frac{d^2y}{dx^2}')}",
            "Maclaurin series expansion",
        ], [
            "Sign of {L(r'\\frac{d}{dx}\\cos^{-1}x')} vs {L(r'\\frac{d}{dx}\\sin^{-1}x')}",
            "Implicit: forgetting {L(r'\\frac{d}{dx}(y^2) = 2y\\frac{dy}{dx}')} (chain rule!)",
            "Maclaurin: evaluate derivatives at {L(r'x=0')}",
        ]),
        'integration': ('Integration', 4, [
            "$$\\int\\sinh x\\,dx = \\cosh x + C,\\quad \\int\\cosh x\\,dx = \\sinh x + C$$",
            "$$\\int\\frac{dx}{\\sqrt{a^2-x^2}} = \\sin^{-1}\\frac{x}{a}+C,\\quad \\int\\frac{dx}{a^2+x^2} = \\frac{1}{a}\\tan^{-1}\\frac{x}{a}+C$$",
            "$$\\int\\frac{dx}{\\sqrt{x^2+a^2}} = \\sinh^{-1}\\frac{x}{a}+C,\\quad \\int\\frac{dx}{\\sqrt{x^2-a^2}} = \\cosh^{-1}\\frac{x}{a}+C$$",
            "$$s = \\int_a^b\\sqrt{1+\\left(\\frac{dy}{dx}\\right)^2}\\,dx,\\qquad S = 2\\pi\\int_a^b y\\sqrt{1+\\left(\\frac{dy}{dx}\\right)^2}\\,dx$$",
            "Reduction formula: {L(r'I_n = \\int_0^{\\pi/2}\\sin^n x\\,dx = \\frac{n-1}{n}I_{n-2}')}",
        ], [
            "Standard integrals (inverse trig and hyperbolic)",
            "Completing the square in integration",
            "Trigonometric and hyperbolic substitutions",
            "Reduction formulae — derivation and application",
            "Arc length (Cartesian and parametric)",
            "Surface area of revolution",
            "Rectangle bounds and inequalities for sums",
        ], [
            "Wrong inverse: {L(r'\\int dx/\\sqrt{a^2-x^2}')} is {L(r'\\sin^{-1}')} NOT {L(r'\\sinh^{-1}')}",
            "Wrong inverse: {L(r'\\int dx/\\sqrt{x^2+a^2}')} is {L(r'\\sinh^{-1}')} NOT {L(r'\\cosh^{-1}')}",
            "Missing {L(r'dx')} conversion in substitution",
            "Arc length vs surface area formula confusion",
            "Forgetting {L(r'2\\pi')} factor in surface area",
        ]),
        'complex-numbers': ('Complex Numbers', 5, [
            "$$(\\cos\\theta + i\\sin\\theta)^n = \\cos n\\theta + i\\sin n\\theta$$",
            "$$\\cos\\theta = \\frac{z+z^{-1}}{2},\\qquad \\sin\\theta = \\frac{z-z^{-1}}{2i}\\quad(z=e^{i\\theta})$$",
            "$$z^n + z^{-n} = 2\\cos n\\theta,\\qquad z^n - z^{-n} = 2i\\sin n\\theta$$",
            "$$n\\text{th roots of unity: } z_k = e^{2\\pi i k/n},\\;k=0,1,\\ldots,n-1$$",
            "Sum of all {L(r'n')}th roots of unity = 0",
        ], [
            "Proof of de Moivre by induction",
            "Multiple angle formulae (e.g. {L(r'\\cos 5\\theta')} in powers of {L(r'\\cos\\theta')})",
            "Power reduction (e.g. {L(r'\\sin^6\\theta')} as sum of cosines)",
            "{L(r'C+iS')} method for summing trigonometric series",
            "{L(r'n')}th roots of unity and their properties",
        ], [
            "Conjugate root theorem: non-real roots in pairs",
            "Sign errors in binomial expansion of {L(r'(\\cos\\theta+i\\sin\\theta)^n')}",
            "{L(r'z^n+z^{-n}=2\\cos n\\theta')} vs {L(r'z^n-z^{-n}=2i\\sin n\\theta')}",
            "Roots of unity: {L(r'e^{2\\pi i k/n}')} for {L(r'k=0,\\ldots,n-1')}",
        ]),
        'differential-equations': ('Differential Equations', 6, [
            "$$\\frac{dy}{dx} + P(x)y = Q(x) \\Rightarrow \\mu = e^{\\int P\\,dx},\\; \\frac{d}{dx}(\\mu y) = \\mu Q$$",
            "$$a\\frac{d^2y}{dx^2} + b\\frac{dy}{dx} + cy = 0 \\Rightarrow am^2 + bm + c = 0$$",
            "Real distinct {L(r'm_1,m_2')}: {L(r'y = Ae^{m_1x} + Be^{m_2x}')}",
            "Repeated {L(r'm')}: {L(r'y = (A+Bx)e^{mx}')}",
            "Complex {L(r'\\alpha\\pm i\\beta')}: {L(r'y = e^{\\alpha x}(A\\cos\\beta x + B\\sin\\beta x)')}",
            "General solution = CF + PI",
        ], [
            "First order linear — integrating factor method",
            "Second order — auxiliary equation (all root types)",
            "Particular integral determination (polynomial, exponential, trig)",
            "Overlap of PI with CF (multiply by {L(r'x')} or {L(r'x^2')})",
            "Reduction using substitution (e.g. {L(r'x=e^t')})",
            "Initial value problems",
        ], [
            "Wrong sign in integrating factor exponent",
            "PI overlap with CF — must multiply by {L(r'x')}",
            "Complex roots: {L(r'y = e^{\\alpha x}(A\\cos\\beta x + B\\sin\\beta x)')}",
            "Applying ICs before combining CF+PI",
            "Substitution: forgetting chain rule",
        ]),
    }
    for key in TOPIC_KEYS:
        title, pos, formulas, qtypes, mistakes = T[key]
        d = DOCS / 'topics' / key
        e(d)
        qex = topic_qs.get(key, [])
        mex = topic_ms.get(key, [])
        qlines = '\n'.join(f'  - `{r}` (Q{n}): {t[:100]}...' for r,n,t in qex[:5])
        mlines = '\n'.join(f'  - `{r}` (Q{n}): {t[:100]}...' for r,n,t in mex[:5])
        flines = '\n'.join(f'  {i+1}. {f}' for i,f in enumerate(formulas))
        qlines2 = '\n'.join(f'  {i+1}. {t}' for i,t in enumerate(qtypes))
        mlines2 = '\n'.join(f'  {i+1}. {m}' for i,m in enumerate(mistakes))

        w(d/'index.md', f"""---
title: {title}
sidebar_position: {pos}
---

# {title}

## What you must know

### Key formulas

{flines}

## Common question types

{qlines2}

## Past paper examples

{qlines if qlines else '- This topic appears regularly in Paper 2'}

## Mark scheme patterns

{mlines if mlines else '- Consistent patterns across all Paper 2 variants'}

## Common mistakes

{mlines2}

## Last-minute checklist

- [ ] All key formulas memorised
- [ ] Know the first step for each question type
- [ ] Reviewed sign conventions
- [ ] Practiced 2–3 past paper questions
""")

        w(d/'syllabus-points.md', f"""---
title: Syllabus Points
sidebar_position: 2
---

# {title} — Syllabus Points

## From Cambridge International syllabus (2026–2027)

Assumed knowledge: Cambridge A Level Mathematics (9709) Papers 1 & 3,
and Paper 1: Further Pure Mathematics 1.

### Key formulas

{flines}

## Exam tips

- Be ready to write definitions from memory
- Practice proofs — 'show that' questions are common
- Know when to use each formula
""")

        w(d/'question-types.md', f"""---
title: Question Types
sidebar_position: 3
---

# Question Types — {title}

{chr(10).join(f'## Type {i+1}: {t}' + chr(10) + chr(10) + '### How to recognise it' + chr(10) + chr(10) + '### Standard method' + chr(10) + chr(10) + '### Mark scheme pattern' + chr(10) + chr(10) + '### Common traps' + chr(10) for i,t in enumerate(qtypes))}
""")

        w(d/'methods.md', f"""---
title: Methods
sidebar_position: 4
---

# Methods — {title}

## Key formulas

{flines}

## Step-by-step approaches

## Common mistakes to avoid

{mlines2}
""")

        w(d/'mark-scheme-patterns.md', f"""---
title: Mark Scheme Patterns
sidebar_position: 5
---

# Mark Scheme Patterns — {title}

## Examples from past papers

{mlines if mlines else '- See common-ms-keywords for general patterns'}
""")

        w(d/'common-mistakes.md', f"""---
title: Common Mistakes
sidebar_position: 6
---

# Common Mistakes — {title}

{chr(10).join(f'### {i+1}. {m}' + chr(10) + chr(10) + '*Fix:* Check the correct formula before answering.' + chr(10) for i,m in enumerate(mistakes))}
""")

        w(d/'last-minute-summary.md', f"""---
title: Last-Minute Summary
sidebar_position: 7
---

# Last-Minute Summary — {title}

## Must-know

{formulas[0] if formulas else ''}
{formulas[1] if len(formulas) > 1 else ''}

## Red flags

{chr(10).join(f'- {m}' for m in mistakes[:3])}

## Quick check

- [ ] Formulas memorised
- [ ] Sign conventions correct
- [ ] Domain restrictions known
""")
        print(f"  Done: {title} ({len(qex)} Qs, {len(mex)} MS refs)")


def main():
    print("=" * 60)
    print("9231 Further Mathematics Paper 2 — Full Doc Generator")
    print("=" * 60)

    print("\n[1] Reading all extracted texts...")
    papers, ms = read_texts()
    print(f"  {len(papers)} papers, {len(ms)} mark schemes")

    print("\n[2] Classifying content by topic...")
    topic_qs, topic_ms = classify_all(papers, ms)
    for k in TOPIC_KEYS:
        print(f"  {k}: {len(topic_qs[k])} questions, {len(topic_ms[k])} MS refs")

    print("\n[3] Generating docs...")
    e(DOCS)
    gen_index()
    gen_syllabus_overview()
    gen_exam_structure()
    gen_last_minute()
    gen_ms_keywords()
    gen_common_mistakes()
    gen_paper2()
    gen_topics(topic_qs, topic_ms)

    md = list(DOCS.rglob('*.md'))
    print(f"\n  Total files: {len(md)}")

    print("\n[4] Sample of classified questions:")
    for k in TOPIC_KEYS:
        if topic_qs[k]:
            r,n,t = topic_qs[k][0]
            print(f"  {k}: {r} Q{n} — {t[:80]}...")


if __name__ == '__main__':
    main()
