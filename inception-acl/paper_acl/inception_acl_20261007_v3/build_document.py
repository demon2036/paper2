from pathlib import Path
import os,subprocess,json,time
HERE=Path(__file__).resolve().parent
os.chdir(HERE)
env=os.environ.copy();env['TEXINPUTS']='.:../vendor/acl-official:';env['BSTINPUTS']='.:../vendor/acl-official:'
start=time.time()
(HERE/'build/status.json').write_text(json.dumps({'status':'running','pid':os.getpid()}))
try:
 for step,cmd in enumerate([
  ['pdflatex','-interaction=nonstopmode','-halt-on-error','-file-line-error','-output-directory=build','main.tex'],
  ['bibtex','build/main'],
  ['pdflatex','-interaction=nonstopmode','-halt-on-error','-file-line-error','-output-directory=build','main.tex'],
  ['pdflatex','-interaction=nonstopmode','-halt-on-error','-file-line-error','-output-directory=build','main.tex'],
  ['pdflatex','-interaction=nonstopmode','-halt-on-error','-file-line-error','-output-directory=build','main.tex']
 ],1):
  print('STEP',step,' '.join(cmd),flush=True)
  subprocess.run(cmd,env=env,check=True)
 (HERE/'build/status.json').write_text(json.dumps({'status':'complete','seconds':time.time()-start}))
except Exception as e:
 (HERE/'build/status.json').write_text(json.dumps({'status':'error','error':str(e),'seconds':time.time()-start}))
 raise
