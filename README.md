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

### FLow chart and CNN architecture:
![flowchart](https://github.com/user-attachments/assets/eff7e728-e607-4a04-988c-ee25ed835d7b)
![CNN](https://github.com/user-attachments/assets/82b5dabb-2ba1-4388-b81f-8c913c31b5c2)

### Sample Dataset Images:
![dataset-cover](https://github.com/user-attachments/assets/f5e3e949-e0ae-4053-b630-19275e56ddab)


### Screenshots of the web app

![home page](https://github.com/user-attachments/assets/5fa9bad4-817a-482d-bfe9-fe4158f86c4d)


![gettinf started](https://github.com/user-attachments/assets/38f998f9-13c1-4038-8292-1e5f93b54b29)
![dashboard](https://github.com/user-attachments/assets/cada77aa-6c46-4686-a6bd-ae724db4c52e)
![input](https://github.com/user-attachments/assets/f96d48bb-dba6-41bd-87a8-bdfaf1f27040)

![result](https://github.com/user-attachments/assets/5b4a6c26-9d60-40ff-9f5b-5e129715d7fa)

![consult](https://github.com/user-attachments/assets/d6b6042b-a874-45bb-9293-3cda14251fb3)

