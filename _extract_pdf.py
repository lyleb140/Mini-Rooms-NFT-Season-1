import json, PyPDF2
from pathlib import Path
results = {}
paths = [Path(r"customminirooms_docs/customminirooms_full_docs.pdf"), Path(r"customminirooms-nft-roadmap.pdf")]
for p in paths:
    if not p.exists():
        results[p.name] = {'error': 'not found'}
        continue
    try:
        r = PyPDF2.PdfReader(str(p))
        txt = []
        for page in r.pages[:10]:
            try:
                txt.append(page.extract_text() or '')
            except Exception as e:
                txt.append(f"[extract error: {e}]")
        results[p.name] = {'pages': len(r.pages), 'sample': '\n'.join(txt)[:6000]}
    except Exception as e:
        results[p.name] = {'error': str(e)}
print(json.dumps(results, ensure_ascii=False))
