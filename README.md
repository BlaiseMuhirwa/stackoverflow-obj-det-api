# stackoverflow-obj-det-api


## Getting Started 

You will notice that this repository has an auto-generated openapi client. 
This client code is generated using the API spec found under src/api.yaml. 

However, I was not able to fully integrate this client code with my back-end Django 
server in time. 

This code was auto-generated by running 
```shell
$ make generate-api
```

Then, the api was copied over to `stackoverflow_api/detection/api_client/`

### Starting the server 

Before getting started, we will need to install all dependencies used. 
Dependency management is done with poetry. If you don't have poetry installed, 
please follow the official installation guide [here](https://python-poetry.org/docs/#installing-with-the-official-installer)

Once that's done, we will need to install dependencies. Run 
```shell
$ make install
```

Then, we need to run some initial migrations that come with Django and start the server. 
The following two commands do this for us 

```shell
$ make migrate
$ make start-server
```

If you've already ran the migrations, you should see an output that looks like this
```shell
cd stackoverflow_api && poetry run python manage.py migrate
Operations to perform:
  Apply all migrations: admin, auth, contenttypes, sessions
Running migrations:
  No migrations to apply.
```

The last command should ouput something like this
```
cd stackoverflow_api && poetry run python manage.py runserver
Watching for file changes with StatReloader
Performing system checks...

System check identified no issues (0 silenced).
July 09, 2024 - 01:13:10
Django version 5.0.6, using settings 'stackoverflow_api.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CONTROL-C.
```


### Testing the POST endpoint 
I tested the endpoint `/api/v1/users` with the following command 
```shell
curl -X POST http://localhost:8000/api/v1/users/ \
            -H "Content-Type: application/json" \
            -d '{"query": "person"}' \
            -s -o response.json \
            -w "HTTP Status: %{http_code}\nTime Total: %{time_total}s\n"
```

which should yield the following results
```json
[
  {
    "user_id": 22656,
    "display_name": "Jon Skeet",
    "profile_image": "https://www.gravatar.com/avatar/6d8ebb117e8d83d74ea95fbdd0f87e13?s=256&d=identicon&r=PG",
    "object_detected": false,
    "bounding_boxes": [],
    "detection_time_ms": 2006.4289569854736
  },
  {
    "user_id": 6309,
    "display_name": "VonC",
    "profile_image": "https://i.sstatic.net/I4fiW.jpg?s=256",
    "object_detected": true,
    "bounding_boxes": [
      {
        "x": 9.685370445251465,
        "y": 5.875068187713623,
        "width": 226.17505741119385,
        "height": 247.6845784187317
      }
    ],
    "detection_time_ms": 1679.805040359497
  },
  {
    "user_id": 1144035,
    "display_name": "Gordon Linoff",
    "profile_image": "https://www.gravatar.com/avatar/e514b017977ebf742a418cac697d8996?s=256&d=identicon&r=PG",
    "object_detected": false,
    "bounding_boxes": [],
    "detection_time_ms": 1761.1958980560303
  },
  {
    "user_id": 157882,
    "display_name": "BalusC",
    "profile_image": "https://www.gravatar.com/avatar/89927e2f4bde24991649b353a37678b9?s=256&d=identicon&r=PG",
    "object_detected": true,
    "bounding_boxes": [
      {
        "x": 0.288818359375,
        "y": 0.83192378282547,
        "width": 255.711181640625,
        "height": 239.31881779432297
      }
    ],
    "detection_time_ms": 1749.335765838623
  },
  {
    "user_id": 100297,
    "display_name": "Martijn Pieters",
    "profile_image": "https://www.gravatar.com/avatar/24780fb6df85a943c7aea0402c843737?s=256&d=identicon&r=PG",
    "object_detected": false,
    "bounding_boxes": [],
    "detection_time_ms": 1768.6207294464111
  },
  {
    "user_id": 157247,
    "display_name": "T.J. Crowder",
    "profile_image": "https://i.sstatic.net/lUM5Z.jpg?s=256",
    "object_detected": true,
    "bounding_boxes": [
      {
        "x": 34.299522399902344,
        "y": 28.074819564819336,
        "width": 193.05109405517578,
        "height": 150.36556434631348
      }
    ],
    "detection_time_ms": 1838.4442329406738
  },
  {
    "user_id": 23354,
    "display_name": "Marc Gravell",
    "profile_image": "https://i.sstatic.net/CrVFH.png?s=256",
    "object_detected": true,
    "bounding_boxes": [
      {
        "x": 21.993398666381836,
        "y": 32.58916091918945,
        "width": 230.5392551422119,
        "height": 223.41083908081055
      }
    ],
    "detection_time_ms": 1639.7666931152344
  },
  {
    "user_id": 29407,
    "display_name": "Darin Dimitrov",
    "profile_image": "https://www.gravatar.com/avatar/e3a181e9cdd4757a8b416d93878770c5?s=256&d=identicon&r=PG",
    "object_detected": false,
    "bounding_boxes": [],
    "detection_time_ms": 1669.26908493042
  },
  {
    "user_id": 115145,
    "display_name": "CommonsWare",
    "profile_image": "https://i.sstatic.net/wDnd8.png?s=256",
    "object_detected": false,
    "bounding_boxes": [],
    "detection_time_ms": 1864.7119998931885
  },
  {
    "user_id": 893,
    "display_name": "Greg Hewgill",
    "profile_image": "https://www.gravatar.com/avatar/747ffa5da3538e66840ebc0548b8fd58?s=256&d=identicon&r=PG",
    "object_detected": true,
    "bounding_boxes": [
      {
        "x": 25.40813446044922,
        "y": 11.642889976501465,
        "width": 221.18599700927734,
        "height": 240.10117435455322
      }
    ],
    "detection_time_ms": 1590.5749797821045
  }
]
```



## Improvements I could have made given more time

* Don't hardcode the object detection confidence threshold.
* Test more objects other than "person"
* Integrate the client code so that it makes the requests for us
* Some performance improvements, such as model caching. Right now the model is re-initialized on 
every request, which is not good. I ended up using a pre-trained Faster R-CNN as you can see in the 
`/stackoverflow_api/detection/views.py` file. 





