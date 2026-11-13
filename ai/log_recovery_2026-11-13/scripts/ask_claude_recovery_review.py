from pathlib import Path
from datetime import datetime,timezone
import subprocess,json,hashlib
root=Path(__file__).resolve().parents[1];out=root/'ai_logs/claude_recovery_review';out.mkdir(exist_ok=False)
prompt=(root/'CLAUDE_RECOVERY_CORRIGENDUM.md').read_text();(out/'prompt.txt').write_text(prompt)
argv=['/opt/homebrew/bin/claude','--print','--safe-mode','--tools','Read,Glob,Grep','--allowedTools','Read,Glob,Grep','--strict-mcp-config','--mcp-config','{"mcpServers":{}}','--disable-slash-commands','--no-session-persistence','--permission-mode','default','--system-prompt','You are an authentic-record recovery auditor. Work only within the supplied current directory and only read visible records. No external paths, opaque-body decryption, hidden reasoning inspection, reconstruction, writes, networking, or hardware work. Use Read/Glob/Grep to seek exact identity-matched plaintext counterparts. Report honest null results.','--output-format','stream-json','--verbose','--max-budget-usd','4']
receipt={'argv':argv,'cwd':str(root),'started_utc':datetime.now(timezone.utc).isoformat(),'prompt_sha256':hashlib.sha256(prompt.encode()).hexdigest(),'granted_tools':['Read','Glob','Grep']}
raw=''
try:
 with (out/'stderr.txt').open('w') as err:
  r=subprocess.run(argv,input=prompt,text=True,cwd=root,stdout=subprocess.PIPE,stderr=err,timeout=240)
 raw=r.stdout;receipt['returncode']=r.returncode
except subprocess.TimeoutExpired as exc:
 raw=exc.stdout or '';raw=raw.decode() if isinstance(raw,bytes) else raw;receipt['error']='240-second timeout'
except Exception as exc:receipt['error']=repr(exc)
kept=[];omitted=0;final=None
for line in raw.splitlines():
 try:e=json.loads(line)
 except ValueError:omitted+=1;continue
 kind=e.get('type')
 if kind in ('assistant','user'):
  msg=e.get('message',{});blocks=[]
  for b in msg.get('content',[]):
   if b.get('type') in ('text','tool_use','tool_result'):blocks.append(b)
   else:omitted+=1
  if blocks:kept.append({'type':kind,'message':{'role':msg.get('role'),'content':blocks},'source_event_sha256':hashlib.sha256(line.encode()).hexdigest()})
 elif kind=='result':
  final=e;kept.append(e)
 elif kind=='system':kept.append({k:e[k] for k in ('type','subtype','session_id','model') if k in e})
 else:omitted+=1
(out/'visible_trace.jsonl').write_text(''.join(json.dumps(x,ensure_ascii=False)+'\n' for x in kept))
if final:
 (out/'response.json').write_text(json.dumps(final,indent=2)+'\n');(out/'response.md').write_text(final.get('result','')+'\n')
receipt.update(ended_utc=datetime.now(timezone.utc).isoformat(),visible_events=len(kept),omitted_internal_or_reasoning_blocks=omitted,final_result_received=final is not None)
(out/'receipt.json').write_text(json.dumps(receipt,indent=2)+'\n');print(json.dumps(receipt,indent=2))
