from setuptools import setup, find_packages

requirements = [l.strip() for l in open('/var/lib/jenkins/workspace/sample_run_pythoncode/pythoncode-test/src/main/resources/requirements.txt').readlines()]
print("My Requirments are: ", requirements)

setup(
    name='${python_package}',
    url='${source_url}',
    version='${python_version}',
    author='saitejaa',
    author_email='saiteja9872@gmail.com',
    description='test',
    packages=find_packages(),
    install_requires=requirements,
    include_package_data=True,
)
