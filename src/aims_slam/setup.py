from setuptools import setup

package_name = 'aims_slam'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='pepper_nano',
    maintainer_email='yatharthahuja1999@gmail.com',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'rs_pub = aims_slam.rs_pub:main',
            'data_pub = aims_slam.data_pub:main'
            
        ],
    },
)
