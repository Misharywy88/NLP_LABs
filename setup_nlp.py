"""Install NLTK resources locally after installing requirements.txt."""
from pathlib import Path
import nltk

target = Path(__file__).resolve().parent / '.nltk_data'
target.mkdir(exist_ok=True)
for resource in ('punkt_tab', 'stopwords', 'wordnet', 'omw-1.4'):
    if not nltk.download(resource, download_dir=str(target), quiet=True):
        raise RuntimeError(f'Could not download NLTK resource: {resource}')
print('NLTK resources are ready.')
