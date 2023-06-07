# Introducing ManageTeach: Empowering Educational Institutions with Open-Source Efficiency
 
## Overview:
ManageTeach is an upcoming open-source platform designed to revolutionize educational management for schools and institutions. Our goal is to provide a comprehensive solution that simplifies administrative tasks, including attendance tracking, scheduling, and record-keeping. By harnessing the power of open-source contributions, ManageTeach aims to empower educators and administrators, enabling them to optimize their time and resources for enhanced teaching and learning experiences.

## Open-Source Collaboration:
We believe in the power of collaboration and welcome contributions from developers, educators, and enthusiasts alike. By fostering an open-source community, we aim to create a platform that evolves based on real-world needs and diverse perspectives. Together, we can shape ManageTeach into a robust and customizable solution that meets the unique requirements of educational institutions around the globe. Join us on this exciting journey and make a meaningful impact in the field of education through open-source innovation.

## History:
Originally developed as part of The Lockdown Project, a successful initiative that started in June 2021, ManageTeach was initially tailored to meet the specific needs of that project. However, recognizing the broader demand for a versatile educational management platform, we have now expanded its capabilities to serve a wider audience, providing a robust solution to the challenges faced by schools and educational institutions worldwide.

## Usage
*(Working Python 3+ installation is required)*
- To start using ManageTeach, install all the packages as detailed in `requirements.txt` using:

    ```
    pip install -r requirements.txt 
    ```

- Once this is done, you can just run the initial installation using: 
    ```
    python3 manage.py runserver
    ```
- You can then go to the admin on your host
    ```
    http://<yourhostname>/admin
    ``` 
    and login using the username `admin` and password `admin`.
- It is highly recommended that after this step, you create a new user with the same permissions as admin through the portal AND/OR either delete the admin account, or change its password to something more secure.

- You can now add new students of various grades as well as tutors, who can register through `http://<yourhostname>/register` to start using the portal.

- **NOTE:** Registration is only required for tutors in the current version. Students can and should not register, as they would be able to access information privy to tutors.