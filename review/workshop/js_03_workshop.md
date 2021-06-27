# js_03_workshop





```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta http-equiv="X-UA-Compatible" content="IE=edge">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Document</title>
</head>
<body>
  <h1>AXIOS API DOG</h1>
  <button>GET DOG🐶</button>
  <img src="" alt="">
  <script src="https://cdn.jsdelivr.net/npm/axios/dist/axios.min.js"></script>
  <script>
    // dog.ceo의 api주소를 URL에 저장
    const URL = 'https://dog.ceo/api/breeds/image/random'

    
    const getDog = function () {
      // URL을 성공적으로 가져오면 반응한다.
      axios.get(URL)
        .then(function (response) {
          //data에 message에 url이 저장되어있어서 data.message로 불러온후 response하는것을 dogUrl에 저장
          const dogUrl = response.data.message
          // dogImg에 img를 넣고 src에 입력해주고 dogUrl을 실행한다.
          const dogImg = document.querySelector('img')
          dogImg.setAttribute('src', dogUrl)
          
      })
    }

    // button이라는 변수에 button 태그를 연결하고 click 할 시에 getDog함수를 실행한다.
    const button = document.querySelector('button')
    button.addEventListener('click', getDog)
  </script>

</body>
</html>
```



