import subprocess
import os
import sys


def main():
    outcmd = "screencapture /tmp/try.jpeg"

    # traditional date/time stamped screen capture file to the default desktop
    # outcmd = "{} {} {} {}".format('screencapture', '-x', '-R332,330,770,75', '-p')

    try:
        # ordinarily we would not use shell=True due to security concerns
        subprocess.check_output([outcmd], shell=True)
    except subprocess.CalledProcessError as e:
        print('Python error: [%d]\n{}\n'.format(e.returncode, e.output))


if __name__ == '__main__':
    sys.exit(main())