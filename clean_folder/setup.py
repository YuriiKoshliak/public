from setuptools import setup, find_namespace_packages


setup(
    name='cleaner',
    version='1',
    description='Very useful sorter',
    url='None',
    author='I_am',
    author_email='example@example.com',
    license='O_o',
    packages=find_namespace_packages(),
    entry_points={'console_scripts': ['clean-folder = clean_folder.clean:main_entry']}
)