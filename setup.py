from setuptools import setup, find_packages

setup(
    name="EmotionDetection",
    version="0.1.0",
    author="Your Name",
    author_email="your.email@example.com",
    description="Emotion detection using Watson NLP",
    packages=find_packages(),
    install_requires=["requests"],
    python_requires=">=3.6",
)