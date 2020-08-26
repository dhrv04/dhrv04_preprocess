import setuptools

with open('README.md', 'r') as file:

	long_description = file.read()

setuptools.setup(
	name = 'dhrv04_preprocess', # Should be Unique
	version = '0.1',
	author = 'Dhruv Singh',
	author_email = 'dhrv04@gmail.com',
	description = 'This is a preprocessing package.',
	Long_description = long_description,
	Long_description_content_type = 'text/markdown',
	packages = setuptools.find_packages(),
	classifiers =  ['Programming Language :: Python :: 3', 'Operating System :: OS Independent'],
	python_version = 3.6
	) 