from setuptools import setup


setup(
    name="tqdm_joblib",
    version="0.0.1",
    author="Louis Abraham",
    author_email="louis.abraham@yahoo.fr",
    license="CC BY-SA 4.0",
    description="Tracking progress of joblib.Parallel execution",
    url="https://stackoverflow.com/a/58936697/5133167",
    install_requires=[
        "tqdm",
    ],
)
