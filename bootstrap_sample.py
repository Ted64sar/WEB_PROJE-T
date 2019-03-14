from flask import Flask
from flask import url_for

app = Flask(__name__)


@app.route('/')
@app.route('/index')
def index():
    return '''<!doctype html>
                    <html lang="en">
                      <head>
                        <meta charset="utf-8">
                        <meta name="viewport" content="width=device-width,
                        initial-scale=1, shrink-to-fit=no">
                        <link rel="stylesheet"
                        href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css"
                        integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm"
                        crossorigin="anonymous">
                        <title>Привет, Яндекс!</title>
                      </head>
                      <body>
                        <h1>Привет, Яндекс!</h1>
                        <div class="alert alert-primary" role="alert">
                          добро пожаловать на страницу нашего проекта
                        </div>
                        <button type="button" class="btn btn-primary btn-lg btn-block">Пройти дальше</button>
                      </body>
                    </html>'''


@app.route('/bootstrap_sample')
def bootstrap():
    return'''<!doctype html>
            <html>
               <head>
                  <meta charset="utf-8">
                  <title>Bootstrap Carousel</title>
                  <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.1.1/css/bootstrap.min.css">
                  <button type="button" class="btn btn-outline-primary">Мне нравится</button>
                  </ul>
    <form class="form-inline my-2 my-lg-0">
      <input class="form-control mr-sm-2" type="search" placeholder="Search" aria-label="Search">
      <button class="btn btn-outline-success my-2 my-sm-0" type="submit">Search</button>
    </form>
  </div>
</nav>
               </head>
               <body>
                    <div id="carouselExampleIndicators" class="carousel slide" data-ride="carousel" align="center" style="background-color:gray">
                      <ol class="carousel-indicators">
                        <li data-target="#carouselExampleIndicators" data-slide-to="0" class="active"></li>
                        <li data-target="#carouselExampleIndicators" data-slide-to="1"></li>
                        <li data-target="#carouselExampleIndicators" data-slide-to="2"></li>
                        <li data-target="#carouselExampleIndicators" data-slide-to="3"></li>
                        <li data-target="#carouselExampleIndicators" data-slide-to="4"></li>
                      </ol>
                      <div class="carousel-inner">
                        <div class="carousel-item active">
                          <iframe width="1280"  height="720" src="https://www.youtube.com/embed/2YAa6NjFVjk" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen ></iframe>
                        </div>
                        <div class="carousel-item">
                          <iframe width="1280" height="720" src="https://www.youtube.com/embed/mHUOCxVT5ro" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
                        </div>
                        <div class="carousel-item">
                          <iframe width="1280" height="720" src="https://www.youtube.com/embed/mHUOCxVT5ro" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
                        </div>
                        <div class="carousel-item">
                          <iframe width="1280" height="720" src="https://www.youtube.com/embed/mHUOCxVT5ro" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
                        </div>
                        <div class="carousel-item">
                          <iframe width="1280" height="720" src="https://www.youtube.com/embed/1La4QzGeaaQ" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
                        </div>
                      </div>
                      <a class="carousel-control-prev" href="#carouselExampleIndicators" role="button" data-slide="prev">
                        <span class="carousel-control-prev-icon" aria-hidden="true"></span>
                        <span class="sr-only">Previous</span>
                      </a>
                      <a class="carousel-control-next" href="#carouselExampleIndicators" role="button" data-slide="next">
                        <span class="carousel-control-next-icon" aria-hidden="true"></span>
                        <span class="sr-only">Next</span>
                      </a>
                    </div>
                  <script src="https://code.jquery.com/jquery-3.3.1.slim.min.js"></script>
                  <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.14.3/umd/popper.min.js"></script>
                  <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.1.1/js/bootstrap.min.js"></script>
               </body>
                </html>'''


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')