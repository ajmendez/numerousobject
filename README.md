== General from the cameras page
x Request URL:https://useast1-auth-1.manything.com/login?version=1.1&email=xxx&password=xxx
    # Log into service
x Request URL:https://useast1-auth-1.manything.com/deviceinfo?uid=xxx&token=xxx
    # get information about a device
x Request URL:https://useast1-logger-xxx.manything.com/liveSession?uid=xxx&token=xxx
    # get status of camera
x Request URL:https://useast1-logger-xxx.manything.com/capturethumb?uid=xxx&token=xxx
    # Request a thumbnail?
x Request URL:https://useast1-logger-xxx.manything.com/session?uid=xxx&startt=1&offset=0&limit=20&token=xxx
    # get session info
x Request URL:https://useast1-logger-xxx.manything.com/listthumbs?uid=xxx&startt=1450844347&endt=1450844377&mingap=900&token=xxx
    # list 
x Request URL:https://useast1-logger-xxx.manything.com/getsettings?uid=xxx&token=xxx
    # get device settings
x Request URL:https://useast1-logger-xxx.manything.com/sessionthumb?uid=xxx&session=1450570911&token=xxx
    # get thumbnails for sessions
x Request URL:https://useast1-logger-xxx.manything.com/video?uid=xxx&startt=1450629093&endt=1450844377&token=xxx&session=1450629093
    # request video info
x Request URL:https://useast1-logger-xxx.manything.com/get?uid=xxx&time=1450569600&lod=2&token=xxx
    # get audio / video movements
x Request URL:https://useast1-logger-xxx.manything.com/getstill/UID/1450844965/TOKEN
    grab an still image
x Request URL:https://useast1-logger-xxx.manything.com/listclips?uid=xxx&token=xxx
    # list clips and timelapse

Request URL:https://useast1-logger-xxx.manything.com/add
    # post meta data?



== Clicked on a session
x Request URL:https://useast1-logger-xxx.manything.com/liststills?uid=xxx1&startt=1450628441&endt=1450628561&mingap=1&token=xxx&session=1450628501

== Clicked on a timelapse
x Request URL:https://useast1-logger-xxx.manything.com/listclips?uid=xxx&token=xxx
x Request URL:https://useast1-logger-xxx.manything.com/getthumb/UID/1450845427/TOKEN
x Request URL:https://useast1-logger-xxx.manything.com/timelapse?description=day+3&session=1450629093&uid=xxx&shared=0&token=xxx&allowmanything=0&startt=1450629093.586&endt=1450913985.615


== Streamed audio /video
Request URL:https://useast1-wowza-xxx.manything.com/open/1
Request URL:https://useast1-wowza-xxx.manything.com/idle/1658608939/0
Request URL:https://useast1-wowza-xxx.manything.com/send/1658608939/1
    # payload: 9playï<UIDD>_669615?userToken=<TOKEN>