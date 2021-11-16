import setuptools

setuptools.setup(
    name='deep_sort',
    version='1.0.3',
    description='Package based on Deep SORT multi-object tracking algorithm',
    url='https://github.com/CalculatedSystems/deep_sort',
    author='Erika Deckter',
    install_requires=['numpy==1.21.4', 'opencv-python==4.5.4.58', 'scikit-learn==0.22.2', 'tensorflow==2.7.0'],
    author_email='erika@calculatedsystems.com',
    packages=['deepsort', 'deepsort/application_util', 'deepsort/deep_sort', 'deepsort/tools'],
    include_package_data=True
)
