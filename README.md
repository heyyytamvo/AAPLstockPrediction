<!-- Improved compatibility of back to top link: See: https://github.com/othneildrew/Best-README-Template/pull/73 -->
<a name="readme-top"></a>
<!--
*** Thanks for checking out the Best-README-Template. If you have a suggestion
*** that would make this better, please fork the repo and create a pull request
*** or simply open an issue with the tag "enhancement".
*** Don't forget to give the project a star!
*** Thanks again! Now go create something AMAZING! :D
-->



<!-- PROJECT SHIELDS -->
<!--
*** I'm using markdown "reference style" links for readability.
*** Reference links are enclosed in brackets [ ] instead of parentheses ( ).
*** See the bottom of this document for the declaration of the reference variables
*** for contributors-url, forks-url, etc. This is an optional, concise syntax you may use.
*** https://www.markdownguide.org/basic-syntax/#reference-style-links
-->
[![MIT License][license-shield]][license-url]
[![LinkedIn][linkedin-shield]][linkedin-url]



<!-- PROJECT LOGO -->
<br />
<div align="center">

<h3 align="center">Open API for Apple Stock Price Prediction </h3>
  <a href="http://heyyytamvo.io.vn/api/apple">
    <img src="images/Product.png" alt="Logo">
  </a>
  <!-- <p align="center">
    <br />
    <a href="https://github.com/heyyytamvo/AAPLstockPrediction"><strong>Explore the docs »</strong></a>
    <br />
    <br />
    <a href="http://heyyytamvo.io.vn/api/apple">View Product</a>
  </p> -->
</div>



<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li><a href="#about-the-project">About The Project</a></li>
    <li><a href="#built-with">Built With</a></li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgments">Acknowledgments</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project


This is an Open API for Apple Stock Prediction. The deep learning model is the LSTM trained by Tensorflow and Keras in Google Colab. The Model will look up the record in the last 15 days to make a prediction of AAPL Close Price on the next day. The deployment server will be updated at 9:30 AM (EST) every days.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

### Built With
* [![Python][Python.org]][Python-url]
* [![Tensorlow][Tensorflow.org]][Tensorflow-url]
* [![Flask][Flask.com]][Flask-url]
* [![Nginx][Nginx.com]][Nginx-url]
* [![Gunicorn][Gunicorn.com]][Gunicorn-url]
* [![Docker][Docker.com]][Docker-url]
<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- GETTING STARTED -->
## Getting Started

This is an example of how you may give instructions on setting up your backend server locally.


### Installation
#### Prerequisites
The `python interpreter` version should be`3.10.x`
#### Installation with Git
```bash
  git clone https://github.com/heyyytamvo/AAPLstockPrediction.git
  cd ~/AAPLstockPrediction
  python3 -m venv myEnv
  . myEnv/bin/activate
  pip install -r requirements.txt
  gunicorn -b 127.0.0.1 -w 1 aap:aap
```
#### Installation with Docker 

```bash
  docker pull heyyytamvo/openapi:aapl
  docker run -p 3000:3500 heyyytamvo/openapi:aapl
```

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- USAGE EXAMPLES -->
## Usage
After finishing the installation, please visit: `http://localhost:3000/api/apple` to get the response from the server.

Or you can send request to my deployment server: `http://heyyytamvo.io.vn/api/apple`

<p align="right">(<a href="#readme-top">back to top</a>)</p>




<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE` for more information.

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- CONTACT -->
## Contact

Tam T. Vo - [@linkedin](https://www.linkedin.com/in/heytamvo/) - tamvoforwork@gmail.com


<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[license-shield]: https://img.shields.io/github/license/othneildrew/Best-README-Template.svg?style=for-the-badge
[license-url]: https://github.com/heyyytamvo/AAPLstockPrediction/blob/main/LICENSE
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://www.linkedin.com/in/heytamvo/
[product-screenshot]: images/screenshot.png

[Python.org]: https://img.shields.io/badge/python-black?style=for-the-badge&logo=python
[Python-url]: https://www.python.org
[Tensorflow.org]: https://img.shields.io/badge/tensorflow-black?style=for-the-badge&logo=tensorflow
[Tensorflow-url]: https://www.tensorflow.org
[Flask.com]: https://img.shields.io/badge/flask-black?style=for-the-badge&logo=flask
[Flask-url]: https://flask.palletsprojects.com/en/3.0.x/
[Nginx.com]: https://img.shields.io/badge/nginx-black?style=for-the-badge&logo=nginx
[Nginx-url]: https://docs.nginx.com/nginx/admin-guide/web-server/
[Gunicorn.com]: https://img.shields.io/badge/gunicorn-black?style=for-the-badge&logo=gunicorn
[Gunicorn-url]: https://gunicorn.org
[Docker.com]: https://img.shields.io/badge/docker-black?style=for-the-badge&logo=docker
[Docker-url]: https://www.docker.com
