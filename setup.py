from setuptools import setup, find_packages

setup(
    name='mypal',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'requests',
    ],
    entry_points={
        'console_scripts': [
            'pal=package_manager:main',
        ],
    },
    author='Your Name',
    author_email='your.email@example.com',
    description='A simple GitHub package manager',
    url='https://github.com/yourusername/mypal',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
