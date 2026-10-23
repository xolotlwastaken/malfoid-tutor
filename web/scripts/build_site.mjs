import {cp,readFile,writeFile,mkdir,rm,rename} from 'node:fs/promises';
import path from 'node:path';
import {fileURLToPath} from 'node:url';

const webRoot=path.resolve(path.dirname(fileURLToPath(import.meta.url)),'..');
const blobOrigin='https://paavbmflznh1t2ao.public.blob.vercel-storage.com';

export function cloudCatalog(catalog,hosted,origin=blobOrigin){
  const store=new URL(origin);
  if(store.protocol!=='https:'||!store.hostname.endsWith('.public.blob.vercel-storage.com'))throw new Error('Invalid media store');
  const result=structuredClone(catalog);
  for(const lesson of result.lessons){
    for(const key of ['video','narration']){
      if(!lesson[key])continue;
      const source=lesson[key],entry=hosted[source];
      if(!entry)throw new Error(`Media has not been uploaded: ${source}`);
      const url=new URL(entry.url);
      const filenames=[path.posix.basename(source),...(key==='narration'?[path.posix.basename(source).replace(/\.wav$/,'.mp3')]:[])];
      if(url.origin!==store.origin||!filenames.includes(path.posix.basename(url.pathname))||url.search||url.hash||!Number.isFinite(entry.size)||entry.size<=0||!/^[a-f0-9]{64}$/.test(entry.sha256))throw new Error(`Invalid hosted media: ${source}`);
      lesson[key]=url.href;
    }
  }
  return result;
}

export async function buildSite(root=webRoot){
  const catalog=JSON.parse(await readFile(path.join(root,'public/data/catalog.json'),'utf8'));
  const hosted=JSON.parse(await readFile(path.join(root,'content/hosted-media.json'),'utf8'));
  const settings=JSON.parse(await readFile(path.join(root,'content/hosting.json'),'utf8').catch(error=>{if(error.code==='ENOENT')return JSON.stringify({blobOrigin});throw error;}));
  const published=settings.publishedCourseIds;
  const selected=published?{...catalog,courses:catalog.courses.filter(c=>published.includes(c.id)),lessons:catalog.lessons.filter(l=>published.includes(l.courseId)),topics:catalog.topics.filter(t=>!t.courseId||published.includes(t.courseId))}:catalog;
  const cloud=cloudCatalog(selected,hosted,settings.blobOrigin);
  const manifest=JSON.parse(await readFile(path.join(root,'media-manifest.json'),'utf8'));
  const staged=path.join(root,'.cloud-build'),output=path.join(root,'dist');
  await rm(staged,{recursive:true,force:true});
  try{
    await cp(path.join(root,'public'),staged,{recursive:true});
    const keep=new Set(cloud.lessons.flatMap(l=>[l.poster,l.captions]).filter(Boolean));
    for(const lesson of catalog.lessons.filter(l=>!cloud.lessons.some(c=>c.slug===l.slug))){
      for(const route of [lesson.poster,lesson.captions].filter(Boolean)){
        if(keep.has(route))continue;
        if(!/^\/(assets|captions)\/[a-zA-Z0-9.-]+$/.test(route))throw new Error(`Unexpected excluded asset: ${route}`);
        await rm(path.join(staged,route.slice(1)),{force:true});
      }
    }
    for(const lesson of cloud.lessons){
      const route=lesson.source.map;if(!route)continue;
      if(!/^\/sources\/[a-zA-Z0-9-]+\.md$/.test(route)||!manifest[route])throw new Error(`Missing source notes: ${lesson.slug}`);
      const destination=path.join(staged,route.slice(1));
      await mkdir(path.dirname(destination),{recursive:true});
      await cp(path.join(root,'content/cloud-support',route.slice(1)),destination);
    }
    await cp(path.join(root,'content/cloud-support/question-bank.pdf'),path.join(staged,'question-bank.pdf'));
    const examBankSource=path.join(root,'SC2203_exam_question_bank.md');
    try{await cp(examBankSource,path.join(staged,'sc2203-exam-question-bank.md'));}
    catch(error){if(error.code!=='ENOENT')throw error;}
    await writeFile(path.join(staged,'data/catalog.json'),JSON.stringify(cloud));
    // Browser folder deployment receives only static output, never credentials or local masters.
    const config=JSON.parse(await readFile(path.join(root,'vercel.json'),'utf8').catch(error=>{if(error.code==='ENOENT')return '{}';throw error;}));
    const hostedConfig={...config,buildCommand:null,installCommand:null,outputDirectory:'.'};
    for(const rule of hostedConfig.headers??[])for(const header of rule.headers??[])if(header.key==='Content-Security-Policy')header.value=header.value.replace(/https:\/\/[a-zA-Z0-9-]+\.public\.blob\.vercel-storage\.com/g,settings.blobOrigin);
    await writeFile(path.join(staged,'vercel.json'),JSON.stringify(hostedConfig,null,2));
    await rm(output,{recursive:true,force:true});await rename(staged,output);
  }catch(error){await rm(staged,{recursive:true,force:true});throw error;}
  console.log(`Built ${cloud.lessons.length} lessons and ${cloud.topics.reduce((n,t)=>n+t.qs.length,0)} questions into dist.`);
}
if(process.argv[1]&&path.resolve(process.argv[1])===fileURLToPath(import.meta.url))await buildSite();
