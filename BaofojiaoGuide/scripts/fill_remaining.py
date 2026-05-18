import sys, os
sys.stdout.reconfigure(encoding='utf-8')

B = r'E:\Dev\BaofojiaoGuide\BaofojiaoGuide\docs\subjects\9231-further-mathematics\topics'

FILES = {
    'matrices-fp2/last-minute-summary.md': 
        '---\ntitle: Last-Minute Summary\nsidebar_position: 7\n---\n\n# Last-Minute Summary - Matrices (FP2)\n\n## Must-know\ndet(A - lambda I) = 0 gives eigenvalues\n(A - lambda I)e = 0 gives eigenvectors\nA = PDP^{-1} for diagonalisation\nA^n = PD^nP^{-1} for powers\n\n## Remember\ndet = 0 does NOT mean inconsistent\nEigenvector order matches eigenvalue order in D\nCayley-Hamilton: p(A) = 0\n',
    
    'integration/last-minute-summary.md':
        '---\ntitle: Last-Minute Summary\nsidebar_position: 7\n---\n\n# Last-Minute Summary - Integration\n\n## Which inverse to use\nint dx/sqrt(a^2-x^2) = sin^{-1}(x/a) NOT sinh^{-1}\nint dx/sqrt(x^2+a^2) = sinh^{-1}(x/a) NOT cosh^{-1}\nint dx/(a^2+x^2) = (1/a)tan^{-1}(x/a)\n\n## Arc length vs surface area\nArc: int sqrt(1+(dy/dx)^2) dx\nSurface: 2pi int y sqrt(1+(dy/dx)^2) dx\n\n## Reduction formula\nIntegration by parts gives I_n in terms of I_{n-1} or I_{n-2}\n',
    
    'differentiation/last-minute-summary.md':
        '---\ntitle: Last-Minute Summary\nsidebar_position: 7\n---\n\n# Last-Minute Summary - Differentiation\n\n## Sign traps\nd/dx(cos^{-1}x) = -1/sqrt(1-x^2) negative sign!\nd/dx(tanh^{-1}x) = 1/(1-x^2) NOT 1/(1+x^2)\nd/dx(cosh x) = +sinh x NOT -sinh x\n\n## Maclaurin\nf(x) = f(0) + f(0)x + f(0)x^2/2! + ...\nEvaluate derivatives at x = 0\n',
    
    'complex-numbers/last-minute-summary.md':
        '---\ntitle: Last-Minute Summary\nsidebar_position: 7\n---\n\n# Last-Minute Summary - Complex Numbers\n\n## Key formulas\n(cos t + i sin t)^n = cos nt + i sin nt\ncos t = (z+z^{-1})/2\nsin t = (z-z^{-1})/(2i)\nRoots of unity: e^{2pi i k/n} for k = 0,...,n-1\nSum of all roots = 0\n\n## C + iS method\nSum GP of exponentials, separate real and imaginary parts\n',
    
    'differential-equations/last-minute-summary.md':
        '---\ntitle: Last-Minute Summary\nsidebar_position: 7\n---\n\n# Last-Minute Summary - Differential Equations\n\n## 1st order\ndy/dx + Py = Q gives IF = e^{int P dx}\nd/dx(IF*y) = IF*Q\n\n## 2nd order\nAE: am^2+bm+c=0\nCF from root type (real/repeated/complex)\nPI matching RHS form\n\n## Warnings\nIF sign is critical\nOverlap means multiply PI by x or x^2\nApply ICs after CF+PI not before\n',
}

for relpath, content in FILES.items():
    full = os.path.join(B, relpath)
    with open(full, 'w', encoding='utf-8') as f:
        f.write(content)
    sz = os.path.getsize(full)
    print(f'OK {relpath} ({sz} bytes)')

print('\nAll 5 files written')
