import pwd
import subprocess
import os


def main():
    scan()


def scan():
    os.system("/System/Library/PrivateFrameworks/Apple80211.framework/Versions/Current/Resources/airport -s")
    # for arg in sys.argv[1:]:
    #     print(arg)


def connect(ssid, password):
    # print(pwd.getpwnam('lord'))
    # os.system(f'networksetup -setairportnetwork en0 {ssid} {password}')
    # result = subprocess.Popen(['sudo', '-S', '992128NJVJuhfabzMAC', 'networksetup', '-setairportnetwork en0'], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    # output,errors=result.communicate(input=f'{ssid}, {password}')
    # result.wait()
    request = f'sudo -S <<< "pass\n" " networksetup -setairportnetwork en0 {ssid} {password}"'
    os.system(request)
    # result = subprocess.run([request])
    # print(f'Connection attempt to {ssid} ran with output: \n {result}')
    # if errors:
    #     print(f'There was error {errors}')



if __name__ == "__main__":
    main()