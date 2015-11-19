__author__ = 'v-mudrak-8l'

import urllib2

dyn_admin_url_constant = '/dyn/admin/nucleus/'
def sendCurlRequest(socket, component_path, username, password):
    gh_url = 'http://' + socket + dyn_admin_url_constant + component_path
    #print(gh_url)
    req = urllib2.Request(gh_url)
    password_manager = urllib2.HTTPPasswordMgrWithDefaultRealm()
    password_manager.add_password(None, gh_url, username, password)

    auth_manager = urllib2.HTTPBasicAuthHandler(password_manager)
    opener = urllib2.build_opener(auth_manager)

    urllib2.install_opener(opener)
    try:
        handler = urllib2.urlopen(req, timeout=3.0)
        if handler.getcode() != 200:
            print ("%s : %s" % (socket, "ERROR"))
    except urllib2.URLError as e:
        print("%s : %s" % (socket, "UrlError"))
    except socket.timeout as e:
        print("%s : %s" % (socket, "Socket Timeout"))

