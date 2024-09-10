from exec.inference import fetchModelResponse
from exec.flask_client import FlaskCustomClient

def checkModelPresence(model_class):
    flask_client = FlaskCustomClient(host='localhost')
    listof = flask_client.get_list_of_models()
    print(listof)

#checkModelPresence("ok")

'''fetchModelResponse({
    "game_id":"1",
    "event_id":"1",
    "url": "https://playai-cv-video-filter-prod.s3.us-east-2.amazonaws.com/data/sample_data/gamecls%3DMINECRAFT/game_id%3D1/event_id%3D1.npy?response-content-disposition=inline&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEC8aCXVzLWVhc3QtMiJHMEUCIEjbpKPQmucaofn0dIHkRMNsTrj3di2FNtgAfdg3FFVfAiEA%2F7aCsS9A07sC0K34qqu2Xzt2tEJZEDPNEvwhVeeksaUq%2FQIIWBAAGgw2NTQ2NTQ0MTk1ODgiDHsatMIv1qoOws20PyraAq4ZAHv%2Fk6P0HB7keEVCQcDvu8iSirHO4rqlSc0KJSFFvCw5ox37%2FZOIEmstwxnfoTsoBDBWCKxN7gYozsVWvuf%2BLfTDhMqHF%2BCDcbto3W4n7Yixnh%2BZv4DZm7Unp7LPk%2FXVJqy1EHhw6D13ML4Isd9jzvUf7s6AVO6ws38PRqfus0MtJyobLDr8MHakjEdy4ESildzP1dvSSvd6vHmWPbpF3hD7KtcShpI879fc32BmOJaY1rjMSys65kg2esxIXB1PU9Died46M39%2B6Z9XosAQHz626xZo53gtte%2FcpZ2pJ6Y%2Bh5IFDJQEY%2BpAPJXnvkMLmGbeE%2FZA8OujWOMBMEear94mdtrbhZuMU6O2Aag4YUfafd95P0RJNMPZstyS%2FaOAf55RxLYyql6Pd8wHxShBNxCKwgssim8wgqjkR%2F2R2YRnmehXakZn4zE%2FFmTRb1RN10Y151UKG04wwKz6tgY6swJQ2yUdYDgg3p6UvvzQ3FaMiC6c%2F3z4qL8ZyC1NKy%2FV%2BnbN2rDb612vPdgyqMc1qz0WZLergL%2B3Ut7gvbFxm4KP8RgkX%2FbTyQ2%2FcHF6Y%2B%2BEyq%2FJysbLpgGnrUciCEXvV%2BN4J44fcpEE7aXkhlFAmNm9IgRkcmOTuoe33JOg%2FnoHVY1u%2BsL1HtMIN%2FbRyArJjVEDBmTtc2kYtZZvg0%2BX9voJX7KeN1wCo6Iz8EHUc3pvGca7a08OZPaE%2F9oIKLn6NDyXv7xnD4ydreWr2RHHRMnJ90y68jGmEh%2B1QJ%2B6XHUT11jf7NUW46GuRr9X5eDLLMt4wA96KsuZbXZUqCwyuSfVnVMpSdqpmJncN5RlZt7iNKde%2BqwnPWY4w6y3w7%2FhBsQmdiQnm91gReL%2BYyXKA18TtzJH&X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Date=20240909T063251Z&X-Amz-SignedHeaders=host&X-Amz-Expires=7200&X-Amz-Credential=ASIAZQ3DRWKCC7QZ7BFF%2F20240909%2Fus-east-2%2Fs3%2Faws4_request&X-Amz-Signature=8441db493887f87cb35580f8efe5eb3a14a154e14b657c44a576bc74b1653758",
    "model_name":"pubg_mvit_v3/3.0"
})'''