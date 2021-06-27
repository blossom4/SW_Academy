[TOC]

# Youtube API 활용

## 기초

- HelloVue.vue지우기
  - App.vue에서도 관련된거 다 지우기

## SearchBar

> 원하는 유튜브 키워드를 검색하는 컴포넌트

- `App.vue`에서 일단 `import SearchBar`, 그리고 템플릿에 하위컴포넌트태그생성

  ```vue
  <template>
    <div id="app">
      <h1>my Youtube</h1>
      <SearchBar/>
    </div>
  </template>
  
  <script>
  import SearchBar from '@/components/SearchBar.vue'
  
  export default {
    name: 'App',
    components: {
      SearchBar, // vue 생성후에 함.
    }
  }
  </script>
  ```

- `components/SearchBar.vue`생성

  - div 생성

- `App.vue`에 `SearchBar,`  등록

- `SearchBar.vue`작성

  - input태그작성

  - input 태그에 이벤트와 실행함수 명시

  - 스크립트에 이름과 메서드 만들고 그 안에 방금 명시한 실행함수 생성

    - `console.log(event.target.value)` : event, target, value 각각 찍어보기
    - 위의 방식 혹은 v-model 사용 가능(사용할 것. 더 뷰스러움)

  - 객체를 반환하는 data함수 생성

    ```javascript
      data: function () {
        return {
          inputValue: ''
        }
      },
    ```

  - v-model명시

    - `<input type="text" @keyup.enter="onInputKeyword" v-model="inputValue">`

  - method 수정, 이벤트 함수 생성

    - emit, input-change는 이름, 이 이벤트를 발생시키는데 인자가 this.inputValue
      - 이 이벤트를 부모가 듣고있을 것

    ```javascript
      methods: {
        onInputKeyword: function () {
          this.$emit('input-change', this.inputValue)
          // console.log(this.inputValue)
        }
      }
    ```

### 데이터 저장과 함수실행 - App.vue

- 이벤트를 부모가 듣도록 하위컴포넌트태그에 명시

  - `<SearchBar @input-change="onInputChange"/>`

- 부모 컴포넌트의 메서드목록생성, 그 안에 이벤트를 들으면 실행할 함수 작성

  - inputText자리에 inputValue가 오는데 이름 다르게 설정한 것.

  ```javascript
    methods: {
      onInputChange: function (inputText) {
        console.log(inputText)
      }
    }
  ```

- 데이터 속성 함수형으로 만듬

  - 자식이 준 데이터를 저장해보자
  - 일단 해당 데이터 값비우고 명시만

  ```javascript
    data: function () {
      return {
        inputValue: ''
      }
  ```

- 다시 함수 작성,

  - 자식이 가진 데이터를 부모의 데이터에 저장

  ```javascript
    methods: {
      onInputChange: function (inputText) {
        this.inputValue = inputText
        // console.log(inputText)
      }
    }
  ```

- API_KEY 변수 저장, export 위에

  - 그냥 저장하는 것은 노출 위험

  - `.env.local`

    - `VUE_APP_YOUTUBE_API_KEY=AIzaSyDkN_W9-mb3saoil-E1BQCqIS-uNS0gs1Q`

    - 주의점:스트링을 표시하는 `''`가 없음. `=`도 붙여서 서술해야함

    - `.gitignore`에 이게 있어서 가능

      ```vue
      # local env files
      .env.local
      .env.*.local
      ```

  - App.vue에서 가져오기

    - `const API_KEY = process.env.VUE_APP_YOUTUBE_API_KEY`
      - `VUE_APP_`이 컨벤션임

- API_URL 변수 저장

  - `const API_URL = 'https://www.googleapis.com/youtube/v3/search'`

#### axios 가져오기 및 작성

- `$ npm i axios`

- 임포트

  - `import axios from 'axios'`

- 작성 전에 onInputChange에 params 작성 (API설명서보면 params안에 키값 등을 넣어줌)

  ```javascript
    methods: {
      onInputChange: function (inputText) {
        this.inputValue = inputText
        
        const params = {
          key: API_KEY,
          part: 'snippet',
          type: 'video',
  		q: this.iniputValue,
        }
      }
    }
  ```

- axios에서 명시해야 하는 것

  - method: 'get'
  - url: API_URL (어디서 가져올지)
  - parameter값

  ```javascript
        axios({
          method: 'get',
          url: API_URL,
          params: params, // 앞뒤가 똑같아서 생략 가능
  
        })
  ```

- .then 작성

  - 인자로 res
  - 애로우펑션 사용

  - console.log

  ```javascript
        axios({
          method: 'get',
          url: API_URL,
          params: params,
        })
          .then((res)=>{
            console.log(res)
          })
  ```

  개발자도구-vue에서 보면

  data-data-items-0-id-videoId의 값을 사용할 것

  `videoId: "3KqHqiVZRh4"`

#### data에 저장해주기

- videos라는 배열

  ```javascript
    data: function () {
      return {
        inputValue: '',
        videos: []
      }
    },
  ```

- .then에 저장

  - `this.videos = res.data.items`

  ```javascript
          .then((res)=>{
            // console.log(res)
            this.videos = res.data.items
          })
  ```

  - 들어왔는지 확인

## VideoList.vue 

> 검색된 비디오 목록을 보여주는 컴포넌트

- 일단 App.vue에서 안만들었지만 import
  - `import VideoList from '@/components/VideoList.vue'`
- 템플릿에 `  <VideoList/>`
- components에 `VideoList,` 추가

- 실제로 만들기

  ```vue
  <template>
    <div>
      <h1>List</h1>
    </div>
  </template>
  
  <script>
  export default {
    name: 'VideoList',
  }
  </script>
  
  <style>
  
  </style>
  ```

### App.vue에 있는 videos 데이터를 자식에게 넘겨주기

- VideoList.vue의 props로 받기

  ```vue
  <template>
    <div>
      <h1>{{ videos }}</h1>
    </div>
  </template>
  
  <script>
  export default {
    name: 'VideoList',
    props: {
      videos: Array,
    }
  }
  </script>
  ```

- App.vue의 하위컴포넌트태그에 v-bind 추가
  - `<VideoList videos="videos"/>`

prop과정 정리

![image-20210511112353772](Vue_js_04_Youtube.assets/image-20210511112353772.png)

1. 부모 컴포넌트의 data의 videos

2. video="videos"로 자식에게 넘겨줌

3. 자식 컴포넌트의 props에서 받음

4. 사용 {{ videos }} 



## VideoListItem.vue

- VideoList.vue

  - 미리 import
    - `import VideoListItem from '@/components/VideoListItem.vue'`
  - component `VideoListItem,`
  - `<VideoListItem/>`

- VideoListItem.vue 생성

  - 이번엔 div 안에 li도 넣자

    ```vue
    <template>
      <div>
        <li></li>
      </div>
    </template>
    
    <script>
    export default {
    
    }
    </script>
    
    <style>
    
    </style>
    ```

- 다시 VideoList.vue에 돌아와서 연결

  - `<VideoListItem v-for="video in videos" :key="video.etag"/>`
  - 또video를 자식에게 넘겨줘야 사용할 수 있겠지
  - 길어지니까 이렇게 쓸 수 있음

  ```html
      <VideoListItem 
        v-for="video in videos" 
        :key="video.etag"
        :video="video"
      />
  ```

- VideoListItem.vue, 자식 컴포넌트에서 보여주기

  ```vue
  <template>
    <div>
      <li>{{ video }}</li>
    </div>
  </template>
  
  <script>
  export default {
    name: 'VideoListItem',
    props: {
      video: Object,
    }
  }
  </script>
  
  <style>
  
  </style>
  ```

  - 이미지를 보여주자
    - 꼭 `:src` 세미콜론! v-bind여야함
  - props-videos-0-snippet-thumbnails-default-url

  ```html
  <img :src="video.snippet.thumbnails.default.url" alt="">
  ```



### 꾸미기

- 부트스트랩 링크 가져오기

- index.html에서 div (id="app")영역만 view로 관리하는거고 외부에 쓰면 그냥 html임.

  - 붙여넣어주자

  ```html
  <!DOCTYPE html>
  <html lang="">
    <head>
      <meta charset="utf-8">
      <meta http-equiv="X-UA-Compatible" content="IE=edge">
      <meta name="viewport" content="width=device-width,initial-scale=1.0">
      <link rel="icon" href="<%= BASE_URL %>favicon.ico">
      <title><%= htmlWebpackPlugin.options.title %></title>
      <!-- CSS only -->
      <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-wEmeIV1mKuiNpC+IOBjI7aAzPcEZeedi5yW5f2yOq55WWLwNGmvvx4Um1vskeMj0" crossorigin="anonymous">  
    </head>
    <body>
      <noscript>
        <strong>We're sorry but <%= htmlWebpackPlugin.options.title %> doesn't work properly without JavaScript enabled. Please enable it to continue.</strong>
      </noscript>
      <div id="app"></div>
      <!-- built files will be auto injected -->
      <!-- JavaScript Bundle with Popper -->
      <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0/dist/js/bootstrap.bundle.min.js" integrity="sha384-p34f1UUtsS3wqzfto5wAAmdvj+osOnFyQFpp4Ua3gs/ZVWx6oOypYoCJhGGScy+8" crossorigin="anonymous"></script>
    </body>
  </html>
  
  ```

- 이미지와 제목을 묶어서 만들어보자. 한땀한땀!

  - 좌우 여백주기위해 App.vue에 container클래스주기

    - `<div id="app" class="container">`

  - VideoListItem.vue에서 이제 시작.

  - d-flex속성주기

    - `<li class="d-flex">`

  - 중앙정렬

    - `<p class="text-center">{{ video.snippet.title }}</p>`

  - 전체 영역 차지할 수 있도록, 마음에 들게 조절하기

    ```html
        <li class="border d-flex justify-content-between align-items-center my-3">
          <img :src="video.snippet.thumbnails.default.url" alt="">
          <p class="text-center w-100">{{ video.snippet.title }}</p>
        </li>
    ```

- input태그도 바꿔주자. SearchBar.vue에서form-control 주자

  `<input class="form-control" type="text" @keyup.enter="onInputKeyword" v-model="inputValue">`



### selectVideo 함수(3) - onSelectVideo 함수(2) - onSelectVideo 함수(1)

#### VideoListItem.vue

- 자식에서 각 영화 눌렀을때 이벤트 발생, 실행함수 명시

  ```html
      <li
        class="border d-flex justify-content-between align-items-center my-3"
        @click="selectVideo"
      >
  ```

- 그 함수 만들기

  ```javascript
    methods: {
      selectVideo: function () {
        this.$emit('select-video', this.video)
      }
    }
  ```

#### VideoList.vue

- 부모가 듣기

  ```html
      <VideoListItem 
        v-for="video in videos" 
        :key="video.etag"
        :video="video"
        @select-video="onSelectVideo"
      />
  ```

- 즉, VideoList.vue 가 부모고, 자식 VideoListItem.vue에서 @click 이벤트가 발생됐을때 selectVideo  함수실행, 그 안에 emit으로 부모가 들음. 들으면 onSelectVideo라는 함수를 실행.
  근데 이 함수에서도 emit으로 App.vue로 보낼 것임.

- 함수 만들기

  - this.video가 video로 옴.

  ```javascript
    methods: {
      onSelectVideo: function (video) {
        this.$emit('select-video', video)
      }
    }
  ```

#### App.vue

- 듣자
  - 일부러 2와 3의 메서드 이름을 같게함

```html
<VideoList :videos="videos" @select-video="onSelectVideo"/>
```

- 함수 실행하자

  - 일단 비디오정보 오브젝트가 잘 나오는지 확인

    ```javascript
        onSelectVideo: function (video) {
          console.log(video)
        }
    ```

  - 정보 저장할 데이터 만들기 selectedVideo

    ```javascript
      data: function () {
        return {
          inputValue: '',
          videos: [],
          selectedVideo: {}, // ''로하니까 빌때 에러났었음
        }
    ```

    

  - 정보 저장

    ```javascript
        onSelectVideo: function (video) {
          // console.log(video)
          this.selectedVideo = video
        }
    ```

    - 이 비디오를 어디서 사용하냐 하면



## VideoDetail.vue

- App.vue에 임포트, 컴포넌트, 태그 추가

- 생성, div, 이름명시

- 부모에서 자식으로 데이터 보내주기

  - App.vue

  ```html
  <VideoDetail :video="selectedVideo"/>
  ```

  - VideoDetail.vue
    - props임에 주의

  ```vue
  <script>
  export default {
    name: 'VideoDetail',
    props: {
      video: Object,
    }
  }
  </script>
  ```

### computed 함수 만들기: 비디오 url 만들기

- 유튜브 공식 경로
  - https://www.youtube.com/embed/

```javascript
  computed: {
    videoURL: function () {
      const videoId = this.video.id.videoID
      return `https://www.youtube.com/embed/${videoId}`
    }
  }
```

- 사용하기: 비디오 출력
  - v-bind
    - `<iframe :src="videoURL" frameborder="0"></iframe>`
  - 아무것도 없을땐 에러가 나므로 v-if로 id값이 있으면 하고 없으면 출력안하게 설정
    - 그냥 video 하면 {}가 참으로 처리되기때문에 id로 해야함
    - `<iframe v-if="video.id" :src="videoURL" frameborder="0"></iframe>`

### 타이틀 데이터가 깨져서 출력되는 현상 해결하기

- lodash 설치했으니 활용.

- 이유: 인코딩이 안맞아서 특수문자가 깨지는거라고보면됨. 이스케이프처리를 안하도록 바꿔서 출력

- 필터라는 기능 사용

  - django safe와 같은 느낌

- VideoListItem.vue에 lodash import

  - `import _ from 'lodash'`

- filters작성

  ```javascript
    filters: {
      stringUnescape: function (rowText) {
        return _.unescape(rowText)
      }
    }
  ```

- filter 사용

  ```html
        <p class="text-center w-100">{{ video.snippet.title | stringUnescape}}</p>
  ```

  