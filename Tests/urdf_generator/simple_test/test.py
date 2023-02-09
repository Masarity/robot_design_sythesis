from odio_urdf import *
import math

material_blue = Material(
  Color(
    rgba='0 0 .8 1'
  ),
  name='blue',
)

material_red = Material(
  Color(
    rgba='.8 0 0 1'
  ),
  name='blue',
)

base_link = Link( 
  Visual(
    Geometry(
      Cylinder( 
        length=0.6,
        radius=0.2
      ),
    ),
    material_blue
  ),
  Collision(
    Geometry(
      Cylinder( 
        length=0.6,
        radius=0.2
      ),
    )
  ),
  Inertial(
    Mass(value=10),
    Inertia(
      ixx=0.4,
      ixy=0.0,
      ixz=0.0,
      iyy=0.4,
      iyz=0.0,
      izz=0.2,
    )
  ),
  name='base_link'
)

right_leg = Link(
  Xacroproperty(value=math.pi, name='PI'),
  Visual(
    Geometry(
      Box(size = "0.6 0.1 0.2")
    ),
    Origin(
      rpy="0 ${PI/2} 0", 
      xyz="0 0 -0.3"
    ),
  ),
  Collision(
    Geometry(
      Cylinder( 
        length=0.6,
        radius=0.2
      ),
    )
  ),
  Inertial(
    Mass(value=10),
    Inertia(
      ixx=0.4,
      ixy=0.0,
      ixz=0.0,
      iyy=0.4,
      iyz=0.0,
      izz=0.2,
    )
  ),
  name='right_leg',
)

joint1 = Joint(
  Parent(base_link),
  Child(right_leg),
  Origin(xyz="0 -0.22 0.25") ,
  name='right_leg_joint'
)

robot = Robot(
  base_link,
  # right_leg,
  # joint1,
  name='pipi',
)

if __name__ == '__main__':
  import os

  dir = os.path.dirname(os.path.realpath(__file__))
  with open(dir + '/test.urdf', 'w') as f:
    f.write(robot.__str__())