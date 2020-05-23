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

## 5. Deployment Detail(latest update) 
- It is live! You can check out at [https://seongwonhan.com](https://seongwonhan.com)
- This service is running on Kubernetes(too much? I know.. ) 
### Little bit of info on what I'm using...
- Running on Kubernetes on EKS single node cluster(T3 Medium). Other personal projects are also running on the same cluster 
- Packaging: Helm
- Image hosting: Docker Hub
- Ingress: alb-ingress-controller
- Secrets: AWS secrets manager
- Static Files: AWS S3 
- Async: Celery(Broker) / Redis(Worker)

## 6. Stay Home project continues! 
- NO PIPELINE? 
> I was able to setup a CI/CD pipeline using CodeBuild on AWS, but I make small changes often and it takes more minutes than I can tolerate for this level of project. 
> So I decided to build a script to automate deployment.
> Also I saved some money

- Split Backend and Frontend
> I have very little knowledge at this point, so once I learn enough I'll be working it.
> It will take some time. 

- Continue learning K8s 
> I have a lot more to learn, and the service will only improve and be more efficient! 