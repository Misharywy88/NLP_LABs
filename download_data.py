"""Download the instructor-assigned datasets. Run from any directory."""
from pathlib import Path
import gzip
import io
import urllib.request
import zipfile

ROOT = Path(__file__).resolve().parent
DATASETS = {
    2: ('seriousran/appletwittersentimenttexts', 'apple-twitter-sentiment-texts.csv'),
    3: ('adizafar/large-random-tweets-from-pakistan', 'Random Tweets from Pakistan- Cleaned- Anonymous.csv'),
    4: ('PromptCloudHQ/amazon-reviews-unlocked-mobile-phones', 'Amazon_Unlocked_Mobile.csv'),
    5: ('prashant111/the-simpsons-dataset', 'simpsons_script_lines.csv'),
}

def download(lab):
    slug, member = DATASETS[lab]
    target = ROOT / f'Lab {lab}' / 'data' / (member + ('.gz' if lab == 4 else ''))
    if target.exists():
        print(f'Already available: {target.relative_to(ROOT)}')
        return
    url = 'https://www.kaggle.com/api/v1/datasets/download/' + slug
    with urllib.request.urlopen(url, timeout=180) as response:
        archive = zipfile.ZipFile(io.BytesIO(response.read()))
    content = archive.read(member)
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_bytes(gzip.compress(content, mtime=0) if lab == 4 else content)
    print(f'Downloaded: {target.relative_to(ROOT)}')

if __name__ == '__main__':
    for lab in DATASETS:
        download(lab)
