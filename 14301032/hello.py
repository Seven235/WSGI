import glob

def containAny(seq,aset):
    for c in seq:
      if c in aset:
        return True
    return False

def application(environ, start_response):
  if not containAny(environ['PATH_INFO'][1:],'.'):
    start_response('200 OK', [('Content-Type', 'text/html')])
    return 'Hello, %s' % (environ['PATH_INFO'][1:] or 'web')
  
  for filename in glob.glob(environ['PATH_INFO'][1:]):
    f = open(filename,'rb')
    start_response('200 OK', [('Content-Type', 'text/html')])
    htmlContent=f.read()
    f.close()
    return htmlContent
  start_response('404 Not Found', [('Content-Type', 'text/html')])
  return '404Notfound'
  
  
