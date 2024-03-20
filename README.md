# Zelthy Tutorial App

## Introduction
This repository contains the source code of the Zelthy Tutorial App, an app for managing patients.

## Application Walk-through

### Creating a Patient


https://github.com/Healthlane-Technologies/zelthy-tutorial-app/assets/22682748/903656a5-3f1a-4154-9454-6eb1eb10a07c


### Editing Patient Details



https://github.com/Healthlane-Technologies/zelthy-tutorial-app/assets/22682748/0ff99697-63a5-4db6-8589-c9d95f802ed1


### Patient Workflow


https://github.com/Healthlane-Technologies/zelthy-tutorial-app/assets/22682748/c583f10e-d516-4fb2-aa8a-ae6bd602ff9b


## Steps for setting up the app

### 1. Setup Zelthy framework
Setup the Zelthy Framework locally or through the GitPod option given in the [Zelthy repository](https://github.com/Healthlane-Technologies/zelthy3)

### 2. Create an app
Create an app named "MyFirstApp" in Zelthy through the app panel.

### 3. Transfering the code
Copy all the contents from inside the "MyFirstApp" folder in this repository to the "MyFirstApp" folder present in you Zelthy installation.

### 4. Create user roles
Create the below user roles from the App Panel.

1. PatientSupportExecutive
2. PatientSupportManager

### 5. Migrate models

To migrate the patient model, execute the following command:

```python
python manage.py ws_migrate MyFirstApp
```

### 6. Sync Static Files
To sync static files, run the commands below:

```python
python manage.py sync_static MyFirstApp
```

```python
python manage.py collectstatic
```

### 7. Setup Login Config

Configure the Login package to have the configs mentioned in the image below

<img width="1439" alt="image" src="https://github.com/Healthlane-Technologies/zelthy-tutorial-app/assets/22682748/42a69153-2db0-4cf3-ab40-0d9152be4f1d">

### 8. Setup Frame
Configure the Frames package to have the configs mentioned in the image below

![image (35)](https://github.com/Healthlane-Technologies/zelthy-tutorial-app/assets/22682748/19eb2758-87e1-45be-bf73-7286abc862fa)



Now you can create a user and login through ``/login`` route to access the application
