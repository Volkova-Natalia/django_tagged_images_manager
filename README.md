## Local testing the project

* Clone the project  
* Create **.env** file in [root](https://github.com/Volkova-Natalia/django_tagged_images_manager/) directory like [.env.sample](https://github.com/Volkova-Natalia/django_tagged_images_manager/blob/master/.env.sample)  
* Set environment variables in the **.env** file (uncommented variables - **OBLIGATORILY**, exclude *AWS_* variables)  
* Run tests in docker using command  
```
docker-compose -f docker-compose.test.yml up
```  
* Stops containers and removes containers, networks, volumes, and images created by command up  
```
docker-compose -f docker-compose.test.yml down
```  

<br>

## Work in AWS

* You have to set **ALL** environment variables, which are uncommented in file [.env.sample](https://github.com/Volkova-Natalia/django_tagged_images_manager/blob/master/.env.sample)  
* You should use [docker-compose.aws.yml](https://github.com/Volkova-Natalia/django_tagged_images_manager/blob/master/docker-compose.aws.yml) to running the service  
```
docker-compose -f docker-compose.aws.yml up
```  

<br>

## Work description

* You can create, read, update and delete images, using API:  
```
/manager/images/
/manager/images/{int:image_id}/
```  

* You can create, read, update and delete tags, using API:  
```
/manager/tags/
/manager/tags/{str:tag_value}/
```  

* You can add a tag to an image, update a tag in an image and delete a tag from an image, using API:  
```
/manager/images/{int:image_id}/tags/
/manager/images/{int:image_id}/tags/{str:tag_value}/
```  


When you add a tag to an image:
1. If the tag exists, the image will get a link to the tag.  
1. If the tag does not exist, the tag will be created and then the image will get a link to the tag.  

When you update a tag in an image:
1. If new tag (from request body) exists, the image will change a link from old tag to new tag.  
1. If new tag does not exist, the tag will be created and then the image will change a link from old tag to new tag.  

***Note:** Old tag in table of tags does not change. Only a link between the image and the tag changes.*  

When you delete a tag from an image:
The tag is deleted from the list of tags of the image.  
***Note:** The tag in table of tags is not deleted. Only a link between the image and the tag is deleted.*  
