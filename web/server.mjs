import { createServer } from 'node:http';
import { createReadStream } from 'node:fs';
import { readFile, stat, realpath } from 'node:fs/promises';
import path from 'node:path';
import { fileURLToPath } from 'node:url';

const appRoot = path.dirname(fileURLToPath(import.meta.url));
const workspace = path.dirname(appRoot);
const publicRoot = path.join(appRoot, 'public');
const manifest = JSON.parse(await readFile(path.join(appRoot, 'media-manifest.json'), 'utf8'));
const mime = {'.html':'text/html; charset=utf-8','.css':'text/css; charset=utf-8','.mjs':'text/javascript; charset=utf-8','.json':'application/json; charset=utf-8','.webp':'image/webp','.svg':'image/svg+xml','.mp4':'video/mp4','.vtt':'text/vtt; charset=utf-8','.pdf':'application/pdf','.wav':'audio/wav','.md':'text/plain; charset=utf-8'};

/** Only public assets and explicitly listed videos/PDF can be served. */
export function studyServer() {
  return createServer(async (req,res) => {
    try {
      if (!['GET','HEAD'].includes(req.method)) { res.writeHead(405,{'Allow':'GET, HEAD'}).end(); return; }
      const pathname = decodeURIComponent(new URL(req.url, 'http://localhost').pathname);
      let file;
      if (manifest[pathname]) file = path.resolve(workspace,manifest[pathname]);
      else if (pathname === '/question-bank.pdf') file = path.join(workspace,'output/pdf/SC2001_Weeks_1-7_MCQ_Review.pdf');
      else if (pathname === '/sc2203-exam-question-bank.md') file = path.join(workspace,'SC2203_exam_question_bank.md');
      else {
        file = path.resolve(publicRoot,'.'+(pathname === '/' ? '/index.html' : pathname));
        const actual = await realpath(file);
        if (!actual.startsWith(publicRoot+path.sep)) { res.writeHead(403).end(); return; }
        file=actual;
      }
      const info = await stat(file);
      if (!info.isFile()) { res.writeHead(404).end(); return; }
      const headers = {'Content-Type':mime[path.extname(file)] || 'application/octet-stream','Accept-Ranges':'bytes','X-Content-Type-Options':'nosniff','Referrer-Policy':'no-referrer','Cache-Control':'no-cache'};
      if (pathname === '/' || pathname.endsWith('.html')) headers['Content-Security-Policy']="default-src 'self'; script-src 'self'; style-src 'self'; img-src 'self' data:; media-src 'self'; connect-src 'self'; object-src 'none'; base-uri 'self'; frame-ancestors 'none'";
      let start=0,end=info.size-1,status=200;
      if (req.headers.range) {
        const range = /^bytes=(\d*)-(\d*)$/.exec(req.headers.range);
        if (!range || (!range[1] && !range[2])) { res.writeHead(416,{'Content-Range':`bytes */${info.size}`}).end(); return; }
        if (!range[1]) start=Math.max(0,info.size-Number(range[2]));
        else { start=Number(range[1]); if(range[2]) end=Math.min(Number(range[2]),end); }
        if (!Number.isSafeInteger(start) || !Number.isSafeInteger(end) || start>end || start>=info.size) { res.writeHead(416,{'Content-Range':`bytes */${info.size}`}).end(); return; }
        status=206;headers['Content-Range']=`bytes ${start}-${end}/${info.size}`;
      }
      headers['Content-Length']=end-start+1;
      res.writeHead(status,headers);
      if (req.method==='HEAD') { res.end(); return; }
      const stream=createReadStream(file,{start,end});
      res.on('close',()=>stream.destroy());
      stream.on('error',()=>res.destroy());stream.pipe(res);
    } catch (error) { if(!res.headersSent)res.writeHead(error.code==='ENOENT' || error.code==='ENOTDIR' ? 404 : 400);res.end('This file is not available.'); }
  });
}
if (process.argv[1] && path.resolve(process.argv[1]) === fileURLToPath(import.meta.url)) {
  const port=Number(process.env.PORT || 4173);
  studyServer().listen(port,'127.0.0.1',()=>console.log(`Malfoid Study is ready at http://localhost:${port}`));
}
