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
    # request = f'sudo -S <<< "pass\n" " networksetup -setairportnetwork en0 {ssid} {password}"'
    # os.system(request)
    # result = subprocess.run([request])
    result = subprocess.Popen(['su', 'lord', '-v', '-A'], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                              text=True)
    # print(result.communicate()[0])
    output, errors = result.communicate(input=f'networksetup -setairportnetwork en0 {ssid}, {password}')
    result.wait()
    print(f'Connection attempt to {ssid} ran with output: \n {output}')
    if errors:
        print(f'There was error: {errors}')


if __name__ == "__main__":
    main()
