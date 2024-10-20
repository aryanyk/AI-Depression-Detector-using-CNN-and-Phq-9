# Depression Detector using CNN

## Overview
The **Depression Detector using CNN** is a machine learning project that utilizes Convolutional Neural Networks (CNNs) to identify signs of depression from various input data, such as images or text. This project aims to provide an automated tool for mental health assessment, offering insights that can aid in early diagnosis and intervention.

## Features
- **Image/Text Analysis**: Uses CNNs to analyze input data.
- **User-Friendly Interface**: Easy to use for both developers and end-users.
- **Real-Time Feedback**: Provides immediate results based on input data.

## Setup Instructions

### 1. Create a Virtual Environment
To ensure that your project dependencies are isolated, it's recommended to create a virtual environment. Follow these steps based on your operating system:

- **Windows:**
  ```bash
  py -m venv myenv
  myenv\Scripts\activate.bat

### 2. Install Necessary Requirements
Install all the required modules

- **Windows:**
  ```bash
  pip install -r requirements.txt


### 3. Make migrations and createsuper user
Go to main app folder where there is manage.py to make all the migrations and createsuperuser

- **Windows:**
  ```bash
  py  manage.py makemigrations
  pt manage.py migrate
  py manage.py createsuperuser



### 4. Now Run the Server
Run the wsgi server to see the website

- **Windows:**
  ```bash
  py manage.py runserver



