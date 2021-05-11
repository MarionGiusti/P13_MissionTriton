# P13_Mission Triton
*Develop your own application [OpenClassrooms Project]*
![image](frontend/src/assets/logo_triton.png)
*****************************************************************************************************************
### About The Project:
MissionTriton is an application to follow campaign at sea (fishing, oceanographic, ...).
Connected user can:
- register a mission and add members, posts, shipcoordinates, pictures gallery.
- visit others missions

Non connected user can:
- register
- visit others missions

### Built with:
*Backend:*
* Python 3.8.2
* Django 3.1.4
* Django REST 3.12.2

*Frontend:*
* VueJS 2.6.12
* Vuetify 2.4.6
* Vuex 3.6.2

*Database:*
* PostgreSQL

*WebServer:*

### Getting Started locally:
*Prerequisites: Technical tools presented :point_up: must be installed*

##### Environment Variables:
Create a .env file in backend and frontend folders.
Copy those variables and change their values.

##### Backend:
|   Variable Name    |         Value         |
|--------------------|-----------------------|
| DJANGO_SECRET_KEY  | Django App Secret key |
| DATABASE_NAME      | Database name         |
| DATABASE_USER      | Database user         |
| DATABASE_PWD       | Database user pwd     |

##### Frontend:
|      Variable Name     |             Value              |
|------------------------|--------------------------------|
| VUE_APP_GOOGLEMAPS_KEY | Google Maps JavaScript Api Key |


### Monitoring:
- Travis-CI : continue integration, run app tests before a pull request

### Online version:
:ocean: :fish: :volcano: