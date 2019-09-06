# Remote Wand
A RESTful API for Wand, a simple ImageMagick binding for Python. 

# Built With
1. Django REST framework
2. Wand
3. ImageMagick

# API Usage
## Endpoints Summary
* GET: 
    * GET: `/images/{imageId}/?width={width in %}&height={height in %}`
    * GET: `/images/{imageId}/?rotate_by={angle}`
    * GET: `/images/{imageId}/?radius={radius}&sigma={sigma}`
    * GET: `/images/{imageId}/?operator={operator}&value={value}&channel={channel}`
    * GET: `/uploads/`
    * GET: `/uploads/{imageId}`
* POST: 
    * POST: '/uploads/'
* PUT: 
    * PUT: '/uploads/{imageId}/'
* DELETE: 
    * DELETE: '/uploads/{imageId}/'
    

### GET: `/images/{imageId}/?width={width in %}&height={height in %}`
Resize the image.

#### Example usage: `GET http://localhost:8000/images/5/?width=50&height=50`

#### Example result:
![1](https://user-images.githubusercontent.com/22634590/64441767-1e41d180-d0ec-11e9-840d-b9652832ab60.PNG)


### GET: `/images/{imageId}/?rotate_by={angle}`
Rotate the image.

#### Example usage: `GET http://localhost:8000/images/5/?rotate_by=75`

#### Example result:
![2](https://user-images.githubusercontent.com/22634590/64464113-464d2700-d124-11e9-9567-87dd50a0ed8b.PNG)

### GET: `/images/{imageId}/?radius={radius}&sigma={sigma}`
Charcol transform.

#### Example usage: `GET http://localhost:8000/images/5/?radius=1.5&sigma=0.5`

#### Example result:
![3](https://user-images.githubusercontent.com/22634590/64464273-fa4eb200-d124-11e9-910b-5ba7a6c34c67.PNG)


### GET: `/images/{imageId}/?operator={operator}&value={value}&channel={channel}`
Evaluate expression.

#### Example usage: `GET http://localhost:8000/images/5/?operator=rightshift&value=1&channel=blue`

#### Example Result:
![5](https://user-images.githubusercontent.com/22634590/64464446-91b40500-d125-11e9-95b9-beef752cc683.PNG)

### GET: `/uploads/`
Get details about all uploaded images.

#### Example usage: `GET http://localhost:8000/uploads/`

#### Example Output:
```json
[
    {
        "id": 5,
        "image_file": "http://localhost:8000/media/pic_folder/skyline.jpg"
    },
    {
        "id": 6,
        "image_file": "http://localhost:8000/media/pic_folder/river.jpg"
    }
]
```

### GET: `/uploads/{imageId}`
Get details about an uploaded image.

#### Example usage: `GET http://localhost:8000/uploads/5`

#### Example Output:
```json
{
    "id": 5,
    "image_file": "http://localhost:8000/media/pic_folder/skyline.jpg"
}
```

### POST: `/uploads/`
Upload an image.

Payload:
Image (as form data)

#### Example usage: `POST http://localhost:8000/uploads/`

#### Example Output:
```json
{
    "id": 8,
    "image_file": "http://localhost:8000/media/pic_folder/Google_Keep.PNG"
}
```

### PUT: `/uploads/{imageId}/`
Change an image.

Payload:
Image (as form data)

#### Example usage: `PUT http://localhost:8000/uploads/8/`

#### Example Output:
Returns the details of new image.
```json
{
    "id": 8,
    "image_file": "http://localhost:8000/media/pic_folder/Google_Keep.PNG"
}
```

### DELETE: `/uploads/{imageId}/`
Delete an image.

#### Example usage: `DELETE http://localhost:8000/uploads/8/`

#### Example Output:
Returns the details of deleted image.
```json
{
    "id": 8,
    "image_file": "http://localhost:8000/media/pic_folder/Google_Keep.PNG"
}
```

# Features
### Currently implemented
* Resizing and cropping
* Transformation (rotation)
* Special Effects (charcol transform)
* Color Enhancement (evaluate expression)

### Todo
* Unit tests
* Cache data with memcached
* Hosting
