def exec_cmd(cmd_line):
    process = Popen(cmd_line.split(), shell=True, stdout=PIPE)
    stdout, stderr = process.communicate()
    return stdout.decode('cp866')


cmd = 'sox tmp.wav message.flac pad .1 0 rate 16k > /null 2>&1'
key = "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"


def dictov():
    # Время начала работы программы
    tit1 = time.time()
    print(u"говорите в микрофон")
    record_to_file('tmp.wav')
    print(u"сделали-записываем в tmp.wav")
    exec_cmd(cmd)
    FileNameTmp = ('message.flac')  # переменная определяет имя фала
    url = "https://www.google.com/speech-api/v2/recognize?output=json&lang=ru-ru&key=" + key
    # url = "https://www.google.com/speech-api/v1/recognize?xjerr=1&client=chromium&lang=ru-RU"#гуглосервис
    flac = open(FileNameTmp, "rb").read()  # читаем файл
    header = {'Content-Type': 'audio/x-flac; rate=16000'}
    req = urllib2.Request(url, flac, header)
    data = urllib2.urlopen(req)
    t = data.read()
    # print t.decode('utf-8')

    txt = t.decode('utf-8')
    y = txt.split('\n')
    for i in json.loads(y[1])['result']:
        k = i.keys()
        u = i['alternative']
        # print u
        print
        u[0]['transcript']
        print
        u'уровень распознования ', u[0]['confidence']
        # for j in k:
        # print  i[j]

        # if i['confidence']<0.45:
        # speech.say(u"Пожалуйста, повторите команду!")
    try:
        slov = u[0]['transcript']
    except:
        pass
    os.remove("message.flac")
    # Время завершения работы программы
    tit2 = time.time()
    print
    u'скорость обработки: %.2f' % (tit2 - tit1)
    try:
        return slov.encode('cp1251')
    except:
        pass