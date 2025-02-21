# Simulasi Sistem Jadwal Perkuliahan ( College Schedule Simulation)

## Introduction

This app created to fulfill the final examination of Algorithm and Data Structure Lesson. Created using Python with Django as it's framework.

## Installation

Make sure you have **Docker** Installed on your computer. if you don't click here [GET DOCKER](https://www.docker.com/)

1. Clone the repository

```git
git clone https://github.com/mcqeems/jadwal_perkuliahan
```

2. Build the app using docker

```docker
docker build -t college-schedule-simulation .
```

3. Run the docker container

```docker
docker run -p 8000:8000 college-schedule-simulation .
```

## Usage

To login as a student use this account:

- **Name:** mustaqim

- **Password:** serahludah

To login as Lecture use this account:

- **Name:** ustadzeko

- **Password:** serahludah

To enter the admin panel add **/admin/** at the end of the url.

- **Name:** admin

- **Password:** admin
