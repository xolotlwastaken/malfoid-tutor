import test from 'node:test';
import assert from 'node:assert/strict';
import {cloudCatalog} from '../scripts/build_site.mjs';
const origin='https://paavbmflznh1t2ao.public.blob.vercel-storage.com';
const catalog={lessons:[{slug:'lesson',video:'/media/lesson.mp4',narration:'/media/lesson.wav',captions:'/captions/lesson.vtt',source:{map:'/sources/lesson.md'}}],topics:[{id:1,qs:[{id:42,answer:'A'}]}]};
const entry=extension=>({url:`${origin}/media/lesson.${extension}`,size:100,sha256:'a'.repeat(64)});
const hosted={'/media/lesson.mp4':entry('mp4'),'/media/lesson.wav':entry('wav')};
test('cloud builds use hosted media without changing captions, question identities or local data',()=>{
 const output=cloudCatalog(catalog,hosted);
 assert.equal(output.lessons[0].video,hosted['/media/lesson.mp4'].url);
 assert.equal(output.lessons[0].narration,hosted['/media/lesson.wav'].url);
 assert.equal(catalog.lessons[0].video,'/media/lesson.mp4');
 assert.deepEqual(output.topics,catalog.topics);
 assert.equal(output.lessons[0].captions,catalog.lessons[0].captions);
 assert.deepEqual(output.lessons[0].source,catalog.lessons[0].source);
});
test('cloud builds fail when media is missing or points outside the connected store',()=>{
 assert.throws(()=>cloudCatalog(catalog,{}),/has not been uploaded/);
 assert.throws(()=>cloudCatalog(catalog,{...hosted,'/media/lesson.mp4':{...entry('mp4'),url:'http://localhost:4173/media/lesson.mp4'}}),/Invalid hosted media/);
});

test('the deployment output contains supporting files but excludes local secrets and keeps the source catalogue local',async t=>{
 const {mkdtemp,mkdir,writeFile,readFile,access,rm}=await import('node:fs/promises');
 const {tmpdir}=await import('node:os');const path=await import('node:path');
 const {buildSite}=await import('../scripts/build_site.mjs');
 const root=await mkdtemp(path.join(tmpdir(),'malfoid-cloud-'));t.after(()=>rm(root,{recursive:true,force:true}));
 for(const dir of ['public/data','content/cloud-support/sources'])await mkdir(path.join(root,dir),{recursive:true});
 await writeFile(path.join(root,'public/data/catalog.json'),JSON.stringify(catalog));
 await writeFile(path.join(root,'public/index.html'),'<main>Subjects</main>');
 await writeFile(path.join(root,'content/hosted-media.json'),JSON.stringify(hosted));
 await writeFile(path.join(root,'content/cloud-support/sources/lesson.md'),'Lesson source notes');
 await writeFile(path.join(root,'content/cloud-support/question-bank.pdf'),'%PDF-test');
 await writeFile(path.join(root,'media-manifest.json'),JSON.stringify({'/sources/lesson.md':'original-outside-web/notes.md'}));
 await writeFile(path.join(root,'.env.local'),'SECRET=not-public');
 await buildSite(root);
 const built=JSON.parse(await readFile(path.join(root,'dist/data/catalog.json'),'utf8'));
 assert.equal(built.lessons[0].video,entry('mp4').url);
 assert.equal(await readFile(path.join(root,'dist/sources/lesson.md'),'utf8'),'Lesson source notes');
 assert.equal(await readFile(path.join(root,'dist/question-bank.pdf'),'utf8'),'%PDF-test');
 await assert.rejects(access(path.join(root,'dist/.env.local')));
 assert.equal(JSON.parse(await readFile(path.join(root,'public/data/catalog.json'),'utf8')).lessons[0].video,'/media/lesson.mp4');
});

test('a newly selected Blob store supports root uploads and compressed narration',()=>{
 const store='https://selected-store.public.blob.vercel-storage.com';
 const output=cloudCatalog(catalog,{
  '/media/lesson.mp4':{...entry('mp4'),url:store+'/lesson.mp4'},
  '/media/lesson.wav':{...entry('wav'),url:store+'/lesson.mp3'}
 },store);
 assert.equal(output.lessons[0].video,store+'/lesson.mp4');
 assert.equal(output.lessons[0].narration,store+'/lesson.mp3');
 assert.throws(()=>cloudCatalog(catalog,hosted,'http://localhost:4173'),/Invalid media store/);
});
