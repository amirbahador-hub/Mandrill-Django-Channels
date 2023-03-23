
<h1 align="center">
  <br>
  <a href="https://www.workgenius.com/de/"><img src="readme.png" alt="WorkGenius" width="200"></a>
</h1>

<h4 align="center">A minimal WebSocket Application that can handel <a href="https://mandrillapp.com/" target="_blank">Mandrill</a> Events.</h4>

<p align="center">
  <a href="https://github.com/amirbahador-hub/WorkGenius/actions/workflows/tests.yml/badge.svg">
    <img src="https://github.com/amirbahador-hub/WorkGenius/actions/workflows/tests.yml/badge.svg"
         alt="TestBadge">
  </a>
</p>

<p align="center">
  <a href="#key-features">Key Features</a> •
  <a href="#how-to-use">How To Use</a> •
  <a href="#download">Download</a> •
  <a href="#credits">Credits</a> •
  <a href="#related">Related</a> •
  <a href="#license">License</a>
</p>

![screenshot](readme.gif)
## Project Setup


1. SetUp venv

    ```bash
    virtualenv venv
    source venv/bin/activate
    ```

2. install Dependencies
    ```bash
    pip install -r requirements.txt
    ```

3. spin off docker compose
    ```bash
    docker-compose -f docker-compose.dev.yml up -d
    ```

4. create your env
    ```bash
    cp .env.example .env
    ```

5. Create tables
    ```bash
    python manage.py migrate
    ```


6. run the project
    ```bash
    python manage.py runserver
    ```

7. for running the tests
    ```
    pytest . -rP
    ```

## Architecture
- Django, By default, is based on Model-View-Template (MVT) architecture.
- I improved DRF basic architecture with my [cookiecutter](https://github.com/amirbahador-hub/django_style_guide).
- It also respects separation of concerns, having api, services, selectors, serializers layers.

### Layers
- `Api`: Api is just an interface for calling other methods in a clean way.
- `Serializers`: Provides parsing capabilities for our input and output json responses and that's it we are not going to put any bussiness logic in here what so ever.
- `Services`: This is were our business logic lives, when ever we want to have a create or update or delete from the database we will put in in services.
- `Selectors`: Just like the name suggest when ever we want to select  something from the database we use selectors and just like services we  can put out business logic in here.
- `Utils`: any thing which doesn't need any database call when ever we  have some abstractions that can be used in `services` or `selectors` we will  use utils layer.
- `Views`: Just like the Api layer it's just an interface but it used for template rendering.
- `Consumers`: it's an interface for out websocket calls.
- `routing`: websocket router
- `urls`: api and template routers

### Patterns
Technically, when you are using frameworks you have little abstraactoins or desgin patterns beacuse most of the desgins are actually  in the library itself, But Beacuse Usaully when you have events you can use Observer Desgin pattern i used it to showoff my skills but in a real project with this scale this is an unnecessary abstraction:

![Observer Pattern](carbon.png)


## Libraries
- [Django](https://github.com/django/django): Django is a high-level Python web framework
- [Django Rest FrameWork](https://github.com/encode/django-rest-framework): A REST API communication framwork
- [Django Channels](https://github.com/django/channels): A WebSocket communaication framewrok
- [Swagger](https://github.com/tfranzel/drf-spectacular): Sane and flexible OpenAPI 3.0 schema generation for Django REST framework
- [Pytest](https://docs.pytest.org/en/7.2.x/): A Test Library
- [DjangoRedis](https://github.com/jazzband/django-redis): full featured Redis cache and session backend for Django.


## Future Improvements
- Eventho that we tried to isolate out bussins logic it's still depends on the redis, we can add another layer called mapper which will mappes python classes with any database.
- Better test covrage. we can add integration test using selenium for our templates and we we also must add more tests for our socket calls. 
- if we have lot's of socket calls then i would suggest to use a microservice artitucure and use Golang or Erlang for better socket handeling.
