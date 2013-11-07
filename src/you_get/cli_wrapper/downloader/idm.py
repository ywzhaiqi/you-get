import os
import subprocess

IDM_PATH = 'd:\\Program Files\\Internet Download Manager\\IDMan.exe'

def downloads(urls, title, ext):
	if not os.path.isfile(IDM_PATH):
		print('Error: not exists IDM.')
		return False

	for i, url in enumerate(urls):
	    filename = '%s[%02d].%s' % (title, i, ext)
	    addToIDM(url, filename)
	return True

def addToIDM(url, name=None, path=None):
    command = [IDM_PATH, '/d', url]
    if path:
        command.extend(['/p', path])
    if name:
        # command.extend(['/f', name.encode('gbk')])
        command.extend(['/f', name])
    command.append('/a')
    retcode = subprocess.call(command)
    if name:
        print('添加到IDM: ' + name)
    else:
        print('添加到IDM: ' + url)
    return retcode