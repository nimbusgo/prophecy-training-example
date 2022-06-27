from setuptools import setup, find_packages

setup(
    name='hospital_beds_report',
    version='1.0',
    packages=find_packages(include=('job*',)),
    description='hospital_beds_report',
    install_requires=[
        'prophecy-libs==1.1.8'
    ],
    entry_points={
        'console_scripts': [
            'main = job.pipeline:main',
        ],
    },
    extras_require={
        'test': ['pytest', 'pytest-html'],
    }
)
