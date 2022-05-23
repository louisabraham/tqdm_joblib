from setuptools import setup


setup(
    name="tqdm_joblib",
    version="0.0.2",
    author="Louis Abraham",
    author_email="louis.abraham@yahoo.fr",
    license="CC BY-SA 4.0",
    description="Tracking progress of joblib.Parallel execution",
    url="https://stackoverflow.com/a/58936697/5133167",
    packages=["tqdm_joblib"],
    install_requires=[
        "tqdm",
    ],
)
