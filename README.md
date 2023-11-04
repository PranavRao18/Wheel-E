
# Wheel-E - Eco-friendly rides with Electric Taxi


The project, undertaken collaboratively with three teammates, aimed to craft a comprehensive and functional website that seamlessly integrated front-end and back-end technologies. Our focus was on creating an optimal user experience through UI/UX design principles. Leveraging HTML, TailwindCSS, and JavaScript, we constructed the front end, ensuring an intuitive and visually appealing interface. Simultaneously, the Django framework was employed for the backend, providing a robust foundation to support the site's functionalities. The goal was to merge these elements cohesively, delivering a user-friendly and fully operational website.

## Table of Contents
- [About](#about)
  - [What is Wheel-E](#what-is-wheel-e)
  - [Features](#features)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
- [TECH STACK used](#techstack---built-with)
- [Screenshots](#screenshots)
- [Team](#the-team)

## About
### What is Wheel-E?
 The website we developed was envisioned as an innovative solution in the realm of sustainable urban transportation. Dubbed "Wheel-E," it represented our dedication to addressing pressing global challenges outlined in Sustainable Development Goals 7 and 11, focusing on Affordable and Clean Energy and Sustainable Cities and Communities. Wheel-E was an exclusively electric vehicle taxi service designed to offer a more environmentally friendly and cost-effective mode of transportation. The platform was meticulously crafted to align with these goals, providing a user-friendly interface for passengers to book rides and experience the convenience of electric vehicle travel. Our intent was not only to offer a service but to contribute to a larger movement towards sustainability in urban mobility.

In building the website, our team prioritized both functionality and user experience. The front end was meticulously designed with an emphasis on intuitive UI/UX. Leveraging HTML, TailwindCSS, and JavaScript, we aimed to create a visually appealing and user-friendly interface that facilitated seamless navigation and booking processes. Simultaneously, the backend development using Django provided the necessary robustness to support the system's operations. This approach ensured the website's reliability and responsiveness, guaranteeing a smooth and efficient experience for users as they booked their electric vehicle rides.

Our project was executed within a specific timeframe, primarily during a hackathon, which drove our team's determination to not only meet the basic objectives but also to exceed expectations. As a result, we successfully developed a fully functional website that accommodated both passengers and drivers. The incorporation of Leaflet API for route optimization further enhanced the service's efficiency, reflecting our commitment to continuous improvement and innovation.

### Features

- **User-Friendly Booking Interface**
   - A straightforward and easy-to-navigate platform allowing passengers to input pickup and drop-off locations, select preferred ride options, and book electric vehicle rides seamlessly.
   - Instant access to available vehicles, along with estimated arrival times and fare calculations for different routes.

- **Interactive UI/UX Design**
   - A visually appealing design integrating HTML, TailwindCSS, and JavaScript for an attractive and user-friendly experience.
   - Intuitive layout and user interface components to ensure straightforward navigation, enhancing the overall user experience.

- **Driver Dashboard**
   - Tools and features for drivers to efficiently manage and organize ride requests and schedules.
   - Resources for drivers to access optimized routes, allowing them to pick the most efficient paths for travel.

- **Passenger Dashboard**
   -  A section where passengers can review previous ride details, aiding in planning and budgeting.

- **Route Optimization using Leaflet API**
   - Integration of Leaflet API to generate the shortest, most cost-effective, and environmentally friendly routes.
   - Providing interactive maps displaying routes to the users.

- **Secure Login and Registration**
   - Implementation of secure login protocols to protect user information.
   - A hassle-free registration process ensuring quick and efficient onboarding for both passengers and drivers.

- **Cost Calculation and Payment**
   - Calculating and displaying fare estimates based on selected routes and vehicle options.

- **Responsive Backend with Django**
   - A reliable and responsive backend system developed with Django, ensuring smooth operations.
   - Efficient data management and storage, ensuring optimal functionality for both passengers and drivers.


## Getting Started
## Prerequisites

Before you begin, ensure that you have the following prerequisites installed on your development environment:

1. **Python**: You'll need Python installed to run backend scripts microagents. You can download Python from the official website [here](https://www.python.org/downloads/).

Make sure all the required paths are added to PATH in the environment variables of your PC.


## Installation

Set up the server and compile the app yourself with the instructions provided.

Feel free to reach out to us if you have trouble following the guide. Contact details can be found [here](#the-team)

## Running the Server:

1. **Clone the Repository**: Begin by cloning the cli-Mate repository from GitHub to your local machine. This step ensures you have the server's source code.
    ```bash
    git clone https://github.com/PranavRao18/Wheel-E.git
    ```

2. **Change Directory**: Switch to the folder in which we have our app.
   ```bash
      cd wheele
    ```
    
3. **Create a Virtual Environment**: It's a good practice to work in a virtual environment to manage dependencies cleanly. Create a virtual environment using your preferred method. For example, you can use Python's `virtualenv` or `venv`.
    While in the cloned directory, run
    ```bash
    python -m venv .venv
    ```
4. **Activate the Virtual Environment**: Activate the virtual environment to isolate your project's dependencies. This step ensures that you work within a controlled environment for your server.
    - On Windows
      ```bash
      .venv\Scripts\activate
      ```
    - On macOs and Linux
      ```bash
      source .venv/bin/activate
      ```
      
5. **Install Requirements**: Install dependencies if prompted.
    ```bash
    pip install -r requirements.txt
    ```
    
6. **Database Migration**: Apply the database migrations. This step ensures that your database schema is up to date.
    ```bash
    python manage.py migrate
    ```
   
7. **Start the Server**: Launch the server with the given command. This action starts the server locally, and it will be accessible at the specified address (usually `http://localhost:8000/`).

    ```bash
    python manage.py runserver
    ```


These steps will help you set up and run the server smoothly. You're now ready to go!




## TECHSTACK - Built with

[![Tech](https://skillicons.dev/icons?i=html,css,tailwind,js,python,django)](https://skillicons.dev)

HTML, CSS, TailwindCSS, JavaScript, Python, Django

APIs: Leaflet, OpenStreetMap


## Screenshots

![Screenshot](https://github.com/PranavRao18/Wheel-E/assets/119714743/7ffce3a5-f6f0-473a-9359-fb6baf234d87)

![Screenshot](https://github.com/PranavRao18/Wheel-E/assets/119714743/126fe606-a9ab-4d7a-8620-865dc6ccf1a5)

![Screenshot](https://github.com/PranavRao18/Wheel-E/assets/119714743/6ad2ea9f-7723-48a0-a13c-50a33efe7d27)

![Screenshot](https://github.com/PranavRao18/Wheel-E/assets/119714743/0690048a-00e2-48f1-b69f-ac5689298768)

![Screenshot](https://github.com/PranavRao18/Wheel-E/assets/119714743/1a802bd8-407d-4e12-a66a-dbdad031c51c)

![Screenshot](https://github.com/PranavRao18/Wheel-E/assets/119714743/80d2546e-2ca8-445a-8874-8db99b9acbd1)

![Screenshot](https://github.com/PranavRao18/Wheel-E/assets/119714743/1ea30d32-689a-4dcb-b661-de487cdd05f6)



## The Team:
**Sanath Naik**

[![GitHub](https://img.shields.io/badge/GitHub-black?style=flat&logo=github)](https://github.com/me-sanath)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-blue?style=flat&logo=linkedin)](https://www.linkedin.com/in/sanath-naik/)

**Pranav Anantha Rao**

[![GitHub](https://img.shields.io/badge/GitHub-black?style=flat&logo=github)](https://github.com/PranavRao18)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-blue?style=flat&logo=linkedin)](https://www.linkedin.com/in/pranav-rao-b00926223/)

**K L Gireesh**

[![GitHub](https://img.shields.io/badge/GitHub-black?style=flat&logo=github)](https://github.com/Gireesh-KL)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-blue?style=flat&logo=linkedin)](https://www.linkedin.com/in/k-l-gireesh-b9b16027b/)

**Jayanth Shanbag**

[![GitHub](https://img.shields.io/badge/GitHub-black?style=flat&logo=github)](https://github.com/JayanthShanbag)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-blue?style=flat&logo=linkedin)](https://www.linkedin.com/in/jayanth-shanbag-82283a25b/)
