import os

ext = 'mkv'
banword = 'rename.py'
episodes = os.listdir()
for episode in episodes:
	if episode != 'rename.py' or episode != 'ls.txt':
		oldname = episode
		episode = (((episode.lower()).replace('[nightsdl.com]','')).replace('-','')).title()
		newname = (((((episode.replace('Mkv','mkv')).replace('..','.')).replace('480P','480p')).replace(' ','.')).replace(".Webdl",''))
		newname = newname.replace('.Tehmovies.Biz','')
		newname = newname.replace('.Tehmovies_Bid','')
		newname = newname.replace('.Web.X264.Rmteam','')
		newname = newname.replace('.Hdtv.X264.Rmteam','')
		newname = newname.replace('.Hdtv.X264','')
		newname = newname.replace('.Web.X264','')
		newname = newname.replace('.Hdtv','')
		newname = newname.replace('.X264Msd','')
		newname = newname.replace('.X264','')
		os.rename(oldname,newname)
		print(oldname, '===>', newname)