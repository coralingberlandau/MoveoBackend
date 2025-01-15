 #  Moveo Task - Backend 


### 🔗 **Backend URL - Render **:  
✨ [Access the backend here!](https://moveobackend.onrender.com/) ✨


### 🌐 **Frontend URL - Netlify **:  
✨ [Access the frontend here!](https://moveo-coral.netlify.app/) ✨


---

# Learn JS

Welcome to our awesome coding platform! 🚀

## Tech Stack

### Frontend:
- **React** with **TypeScript** – A modern, fast, and scalable frontend framework to create a dynamic and responsive UI.

### Backend:
- **Python** with **Django** – A powerful and flexible backend framework to manage business logic, handle requests, and serve data.

### Database:
- **SQLite** – A lightweight and efficient relational database for storing and managing data.

### Deployment:
- **Backend**: Deployed on **Render** – A reliable cloud platform for running backend services.
- **Frontend**: Deployed on **Netlify** – A fast and user-friendly platform for frontend hosting.

## Overview

This platform allows users to solve coding challenges, interact in real-time, and track progress – all built with the latest web technologies. Whether you're a mentor or a student, this platform is designed to make learning and teaching JavaScript fun and collaborative! 💻💡

---


Tom is a professional JS lecturer who loves his students very much.
Unfortunately, Tom had to move to Thailand with his wife.
Tom wants to keep following his students' progress in their journey of becoming a JS master just like him!

Help Tom create an online coding web application with the following pages and features:
Lobby page (no need for authentication) :
The page should contain the title “Choose code block” and a list of at least 4 items that represent code blocks, each item can be represented by a name (for example - “Async case”)
Clicking on an item should redirect users to the corresponding code block page -
Code block page :
Contains the title and a text editor with the code block initial template and a role indicator (student/mentor).
Assume that the first user who opens the code block page is the mentor (Tom), after that, any other client will be counted as a student.
If Tom leaves the code-block page, students should be redirected to the lobby page, and any written code should be deleted.
The mentor will see the selected code block in a read-only mode.
The student will see the code block with the ability to change the code
Code changes should be displayed in real-time (Socket)
The code should have syntax highlighting
At any given time, each user can see how many students are in the room
Have a “solution” on a codeblock object (also insert manually), once the student changes the code to be equal to the solution, show a big smiley face on the screen :)

General guidelines:
Code blocks should be stored in a database of your choice (Relational or Not-Relational)
The initial state of the database should contain at least four code blocks which can be created manually.
Add clear comments to the code where needed.
The task requires the development of a client, server, and database. The client side must be implemented using React, while the server side can be built with any framework or language of your choice.


***Submission instructions: ***

1. Deploy the project and supply the url for the app.
You can use any service you would like for hosting your deployment (There are many free services for that purpose - railway.app, Netlify, Vercel etc. )

2. Upload your code to GitHub and attach a link to your GitHub repository.



