"""Import the approved later sequence while retaining all legacy catalog IDs."""
from pathlib import Path
import hashlib,json,re,shutil
from PIL import Image

def import_later_lessons(root,web,lessons,bank,mounts):
    entries=json.loads((web/'content/sc2001-later-lessons.json').read_text())
    topics=json.loads((root/'content/sc2001-later-question-bank.json').read_text())
    audit=json.loads((root/'content/sc2001-later-answer-audit.json').read_text())
    assert audit['status']=='passed'
    assert audit['bank_sha256']==hashlib.sha256((root/'content/sc2001-later-question-bank.json').read_bytes()).hexdigest()
    used_questions={q['id'] for t in bank for q in t['qs']}
    used_topics={t['id'] for t in bank}
    for entry,topic in zip(entries,topics,strict=True):
        assert entry['id']==topic['lessonId']
        assert topic['id'] not in used_topics
        assert not used_questions.intersection(q['id'] for q in topic['qs'])
        used_topics.add(topic['id']);used_questions.update(q['id'] for q in topic['qs'])
        folder=root/entry['folder'];slug=folder.name
        media=json.loads((folder/'media-verification.json').read_text())
        assert media['passed'] and media['visual_inspection']=='pass'
        assert json.loads((folder/'speech-review.json').read_text())['passed']
        video=folder/f'malfoid-{slug}.mp4'
        assert hashlib.sha256(video.read_bytes()).hexdigest()==media['sha256']
        timeline=json.loads((folder/'timeline.json').read_text());beats=timeline['beats']
        transcript=[dict(id=b['id'],start=round(b['start'],2),end=round(b['end'],2),text=b['text']) for b in beats]
        chapters=[dict(title=b['visual']['head'],time=round(b['start'],2)) for b in beats]
        caption=f'/captions/{slug}.vtt'
        (web/'public'/caption.lstrip('/')).write_text('WEBVTT\n\n'+re.sub(r'(\d\d:\d\d:\d\d),(\d{3})',r'\1.\2',(folder/'captions.srt').read_text()))
        poster=f'/assets/{slug}.webp'
        image=Image.open(folder/'encoded-review-3.png').convert('RGB');image.thumbnail((540,960))
        image.save(web/'public'/poster.lstrip('/'),'WEBP',quality=82)
        url=f'/media/{slug}.mp4';audio=f'/media/{slug}.wav';source=f'/sources/{slug}.md'
        for route,file in [(url,video),(audio,folder/'narration.wav'),(source,folder/'README.md')]:
            if not file.is_file():raise FileNotFoundError(file)
            mounts[route]=str(file.relative_to(root))
        sourcecopy=web/'content/cloud-support'/source.lstrip('/')
        sourcecopy.parent.mkdir(parents=True,exist_ok=True);shutil.copyfile(folder/'README.md',sourcecopy)
        topic.update(slug=slug,lessonSlug=slug,group=entry['group'],courseId='sc2001')
        bank.append(topic)
        lessons.append(dict(slug=slug,courseId='sc2001',title=entry['title'],group=entry['group'],description=f"{entry['id']} · {entry['group']} · Week {entry['week']}",week=entry['week'],periodLabel='Weeks 8–13',duration=media['duration'],video=url,poster=poster,captions=caption,narration=audio,chapters=chapters,transcript=transcript,topicIds=[topic['id']],source=dict(summary=entry['sources']+' Later recordings unavailable; approved slides-and-notes grounding.',recording=None,map=source)))
