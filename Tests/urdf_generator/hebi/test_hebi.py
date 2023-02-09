import odio_urdf
import subprocess


if __name__ == '__main__':
  res = subprocess.run(args=['rosrun', 'xacro', 'xacro', dir + '/urdf/kits/A-2084-01.xacro'], capture_output=True)
  # print(res.stdout)
  my_robot = odio_urdf.Robot(xacro_xml=res.stdout)

  import os

  dir = os.path.dirname(os.path.realpath(__file__))
  with open(dir + '/test.urdf', 'w') as f:
    f.write(my_robot.__str__())