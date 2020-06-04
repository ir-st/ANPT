from pynmap import portscan

if __name__ == '__main__':

  scan_target = input("请输入目标IP地址")
  portscan(scan_target)