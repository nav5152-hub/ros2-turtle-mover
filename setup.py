from setuptools import find_packages, setup
import os
from glob import glob

package_name = 'my_robot'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
   data_files=[
    ('share/ament_index/resource_index/packages',
        ['resource/my_robot']),
    ('share/my_robot', ['package.xml']),
    (os.path.join('share', 'my_robot', 'launch'), glob('launch/*.py')),
],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='yunseo',
    maintainer_email='yunseo@todo.todo',
    description='TODO: Package description',
    license='TODO: License declaration',
    extras_require={
        'test': [
            'pytest',
        ],
    },
    entry_points={
   'console_scripts': [
    'turtle_mover = my_robot.turtle_mover:main',
    'obstacle_avoider = my_robot.obstacle_avoider:main',
    'two_turtles = my_robot.two_turtles:main',
],
    },
)
