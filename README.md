# RPEval

**This is a work-in-progress application and is not intended to be used for medical advice**

## Project Description
The goal of this application is to create an environment where athletes are able to upload and keep track of their lifting progress. Upon completion of a lift, the application calulates a rate of perceived exertion (RPE) evaluation as well as other useful information about the lift.

For those interested in sampling what the application has to offer currently, the program can be run after copying the repo by executing `python RPEval.py` from the command line

## Progress

As of the first commit, the ground work for the UI has begun
with a customized video widget to display an athletes video.
The object tracking method to be used for the rpeval algorithm
has also begun development but has not yet been integrated

### Athlete Select Page
![Select Page](./assets/images/readme_pics/select_page.jpg)

### Home Page
![Home Page](./assets/images/readme_pics/home_page.jpg)

### Lift Tracking
![Object Tracking](./assets/images/readme_pics/tracking_example.jpg)

## TODO

* Finish the main 3 UI frames (Home, New Lift, and Past Lift)

* Implement a database acess layer and database implementation using SQLite for athlete and video data

* Integrate customizable object tracking into application

## Credits

* The UI implements customtkinter courtesy of Tom Schimansky

* The [Object Tracking Method](https://mpolinowski.github.io/docs/IoT-and-Machine-Learning/ML/2021-12-10--opencv-optical-flow-tracking/2021-12-10/) (not yet implemented but results shown) was created by Mike Polinowski using opencv to implement Lucas-Kanade optical flow

* The application features images (and sample videos in the near future) of [Trevor Diedrich](https://www.instagram.com/trevor_diedrich/), [Rayan Ahmed](https://www.instagram.com/rayan.liv3s/), and [Traison Diedrich](https://www.instagram.com/traiiison/) as example athletes