# SW's STAY-AT-HOME project
### *Being a back-end developer I really don't have much to show my skills. So to take advantage of **Stay-At-Home** period I decided to create a portfolio.*
### *The more I try, the more I find myself that I'm not really good at front-end/UI work. BUT! This will show that I tried. I really did.*

## 1. Practice using Django Template
- Three pages of HTML/CSS  
- Use Form to store/validate fields. 
- Practice using Bootstrap for mobile friendly view 

## 2. Practice third-party API call
- Mailgun call to send out email for visitors
- Pulling COVID 19 info from https://docs.corona.lmao-xd.wtf/ and modify the display.

## 3. Build a REST API and calling it from my template page
- Building REST API is more of my taste. 

## 4. Deployment using... Docker? 
- Docker container is used. I have failed and failed to learn Docker/Containerization, BUT I finally got it to work! 
- Learning channel: [Christian Kreuzberger](https://youtu.be/90LCcim-wHQ) (it'll take some time but for Django users it's very comprehensive)

## 5. Deployment Detail 
- The service is up and running. You can check out at [https://seongwonhan.com](https:seongwonhan.com)
- I struggled through ECS and decided to take a course
- In the mean time I provisioned an AWS EC2 instance and deployed my service using shell script 
 > Nginx is serving as a reverse proxy
 > Gunicorn is used as a HTTP -> WSGI server 
 > AWS components being used are : EC2, ALB, ROUTE53, CERTIFICATE MANAGER, S3

## 6. Stay-Home project continues
- My goal is to be able to deploy with ECS. 
- Also need to build a strong CI/CD environment. 
- Study continues... 