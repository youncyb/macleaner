import re
import os
import sys
import plistlib
import prettytable
import subprocess
from colorama import Fore, Back, Style


def red(s):
    return Fore.LIGHTRED_EX + s + Fore.RESET


def green(s):
    return Fore.LIGHTGREEN_EX + s + Fore.RESET


def yellow(s):
    return Fore.LIGHTYELLOW_EX + s + Fore.RESET


def white(s):
    return Fore.LIGHTWHITE_EX + s + Fore.RESET



def output(out):
    tb = prettytable.PrettyTable()
    tb.field_names = ['ID', 'Folder/File', 'Size']
    for o in out:
        tb.add_row(o[1:])
    print(tb)

def parse_plist(path):
    if not os.path.isfile(path):
        return None
    with open(path, 'rb') as f:
        pl = plistlib.load(f)
    return [pl['CFBundleExecutable'], pl['CFBundleIdentifier'].rsplit('.')[1]]



def get_size(path):
    total = 0
    if os.path.isfile(path):
        total += os.path.getsize(path)
    else:
        for entry in os.scandir(path):
            if entry.is_file():
                total += entry.stat().st_size
            elif entry.is_dir():
                total += get_size(entry.path)
    return total


def size_human(num):
    base = 1024
    for x in ['B ', 'KB', 'MB', 'GB']:
        if num < base and num > -base:
            return "%3.0f%s" % (num, x)
        num /= base
    return "%3.0f %s" % (num, 'TB')


def get_clean_folders():
    folders = [
        '~/Library/Application Support',
        '~/Library/Preferences/',
        '~/Library/Caches/',
        '~/Library/Logs/',
        '~/Library/Application Support/CrashReporter/',
        '~/Library/Saved Application State/',
        '~/Library/LaunchAgents/',
        '/Library/Caches',
        '/Library/Logs',
        '/Library/Preferences/',
        '/Library/Application Support',
        '/Applications',
        '/private/var/db/receipts',
        '/Library/StagedExtensions/Library/Extensions',
        '/Library/StagedExtensions/Library/Application Support',
        '/Library/Extensions/',
        '~'
    ]
    for folder1 in os.listdir('/var/folders/'):
        folder1_path = os.path.join('/var/folders/', folder1)
        if os.path.isdir(folder1_path) and folder1 != 'zz':
            for folder2 in os.listdir(folder1_path):
                folder2_path = os.path.join(folder1_path, folder2)
                if os.path.isdir(folder2_path):
                    folders.append(folder2_path)
    return map(os.path.expanduser, folders)


def find_folders(name):
    real_clean_folders = []
    id_ = 0
    for folder in get_clean_folders():
        for f in os.listdir(folder):
            if f.startswith('com.apple'):
                continue
            f_word = ''.join(re.findall('[a-zA-Z0-9.]', f)).lower()
            if len([x for x in name if ''.join(re.findall('[a-zA-Z0-9.]', x)).lower() in f_word]):
                path = os.path.join(folder, f)
                size = size_human(int(get_size(path)))
                real_clean_folders.append([path, red(str(id_)), yellow(path), green(size)])
                id_ += 1
    return real_clean_folders

def rm_rf(path):
    p = subprocess.Popen('rm -rf "{path}"'.format(path=path), shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    (stdout, stderr) = p.communicate()
    return stderr.decode('utf-8')

def main():
    usage = 'usage: python3 {script} name'.format(script=sys.argv[0])
    if len(sys.argv) < 2:
        print(usage)
        exit()
    path = '/Applications/{app}/Contents/Info.plist'.format(app=sys.argv[1])
    name = []
    deleted_folders = []
    flag = parse_plist(path)
    if flag:
        print(green('[+]Searches app Info.plist successfully'))
        name = flag
    else:
        print(yellow('[*]Searches app Info.plist failed, native input will be used'))
        name.append(sys.argv[1])
    folders = find_folders(name)
    if len(folders):
        print(green('[+]Found the following results:'))
        output(folders)
        read = input('[+]Please confirm the deleted id (e.g.: 0 1 3 or all):')
        print(green('[+]Your choices: {choice}'.format(choice=read)))
        if read == 'all':
            deleted_folders = [x[0] for x in folders]
        else:
            read = [x for x in re.split('\s+', read) if len(x)]
            read = [int(read[i]) for i in range(len(read)) if int(read[i]) < len(folders)]
            deleted_folders = [folders[x][0] for x in read]
            if len(deleted_folders) == 0:
                print(red('[-]Wrong input'))
                exit()
        count = 0
        for f in deleted_folders:
            stderr = rm_rf(f)
            if stderr:
                print(red('[-]Failed to delete: {reason}'.format(reason=stderr)))
            else:
                print(green('[+]Successfully deleted: {f}'.format(f=f)))
                count += 1
        print(yellow('[*]{count} files cleaned'.format(count=count)))

    else:
        print(red('[-]No residual files found'))

main()
