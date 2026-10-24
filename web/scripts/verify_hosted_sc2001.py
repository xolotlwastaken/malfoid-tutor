"""Verify the newly uploaded bytes before registering their public routes."""
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor
from urllib.request import Request,urlopen
from urllib.parse import quote
import hashlib,json
WEB=Path(__file__).resolve().parents[1]
settings=json.loads((WEB/'content/hosting.json').read_text())
index=json.loads((WEB/'.hosting-media/index.json').read_text())
items=[(route,entry) for route,entry in index.items() if Path(route).name.startswith('sc2001-')]
assert len(items)==62

def verify(item):
    route,entry=item;url=settings['blobOrigin']+'/'+quote(Path(entry['path']).name)
    with urlopen(Request(url,method='HEAD'),timeout=30) as response:
        assert response.status==200
        assert int(response.headers['Content-Length'])==entry['size'],route
    digest=hashlib.sha256()
    with urlopen(url,timeout=60) as response:
        while chunk:=response.read(1024*1024):digest.update(chunk)
    assert digest.hexdigest()==entry['sha256'],route
    if route.endswith('.mp4'):
        with urlopen(Request(url,headers={'Range':'bytes=0-63'}),timeout=30) as response:
            assert response.status==206 and len(response.read())==64,route
    print('Verified',route,flush=True)
    return route,dict(url=url,size=entry['size'],sha256=entry['sha256'])

with ThreadPoolExecutor(max_workers=4) as pool:verified=dict(pool.map(verify,items))
path=WEB/'content/hosted-media.json';hosted=json.loads(path.read_text())
for route,entry in verified.items():
    assert route not in hosted or hosted[route]==entry
    hosted[route]=entry
path.write_text(json.dumps(hosted,indent=2)+'\n')
report=dict(status='passed',files=len(verified),total_bytes=sum(x['size'] for x in verified.values()),remote_sha256_verified=True,video_ranges_verified=True,origin=settings['blobOrigin'])
(WEB/'.hosting-media/sc2001-upload-verification.json').write_text(json.dumps(report,indent=2)+'\n')
print('Registered',len(verified),'verified public routes')
