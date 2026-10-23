"""Prepare smaller streaming copies; original lesson masters remain unchanged."""
from pathlib import Path
import concurrent.futures,hashlib,json,subprocess,threading
ROOT=Path(__file__).resolve().parents[2];WEB=ROOT/'web';OUT=WEB/'.hosting-media/media'
OUT.mkdir(parents=True,exist_ok=True)
manifest=json.loads((WEB/'media-manifest.json').read_text());index_path=OUT.parent/'index.json'
index=json.loads(index_path.read_text()) if index_path.exists() else {};lock=threading.Lock()
items=[(route,ROOT/source) for route,source in manifest.items() if Path(source).suffix in ('.mp4','.wav')]
def prepare(item):
 route,source=item;digest=hashlib.sha256(source.read_bytes()).hexdigest();video=source.suffix=='.mp4'
 destination=OUT/(Path(route).stem+('.mp4' if video else '.mp3'))
 if route in index and index[route]['sourceSha256']==digest and destination.exists():return
 temporary=destination.with_name(destination.stem+'.encoding'+destination.suffix)
 options=['-vf','scale=720:1280','-c:v','libx264','-preset','veryfast','-crf','26','-threads','3','-c:a','aac','-b:a','64k','-movflags','+faststart'] if video else ['-vn','-c:a','libmp3lame','-b:a','64k','-ac','1']
 subprocess.run(['ffmpeg','-hide_banner','-loglevel','error','-y','-i',str(source),*options,str(temporary)],check=True)
 # Require a readable complete container before publishing it in the upload index.
 probe=json.loads(subprocess.check_output(['ffprobe','-v','error','-show_entries','format=duration','-of','json',str(temporary)],text=True))
 temporary.replace(destination)
 entry={'path':str(destination.relative_to(WEB)),'sourceSha256':digest,'sha256':hashlib.sha256(destination.read_bytes()).hexdigest(),'size':destination.stat().st_size,'duration':float(probe['format']['duration'])}
 with lock:
  index[route]=entry;index_path.write_text(json.dumps(index,indent=2)+'\n');print(f'{len(index)}/{len(items)} ready: {destination.name} ({entry["size"]/1e6:.1f} MB)',flush=True)
with concurrent.futures.ThreadPoolExecutor(max_workers=3) as pool:
 for _ in pool.map(prepare,items):pass
print(f'COMPLETE: {len(index)} files, {sum(v["size"] for v in index.values())/1e6:.1f} MB',flush=True)
