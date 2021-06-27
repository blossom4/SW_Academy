# js_01_workshop





> **제시된 CREATE, READ 기능을 충족하는 todo app을 완성하시오.**

- 필수사항
  - form 태그를 사용한다.
  - submit 되었을 시 todo가 작성된다. 
  - 작성 된 todo는 ul 태그의 li 태그로 추가된다. 
  - 작성 후 input value 값는 초기화 된다. 
  - (선택) 빈 값인 데이터는 입력을 방지한다.



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
  <style>
    .done {
      text-decoration: line-through;
    }
  </style>
  <!--form-->
  <form action="">
    <input type="text" id="todo">
    <input type="submit" id="submit">
  </form>

  <!--script-->
  <script>

    const submitElement = document.querySelector('#submit')

    submitElement.addEventListener('click', function(event){
      event.preventDefault()
      const todoElement = document.querySelector('#todo')
      const todo = todoElement.value

      if (todo.trim()) {
        // 문자열이 있다면
        const liElement = document.createElement('li')
        liElement.innerText = todo

        const ulElement = document.querySelector('ul')
        ulElement.appendChild(liElement)

        todoElement.value = ''      
      }
      else {
        alert('할일을 입력해주세요')
      }
    })
  </script>
</body>
</html>
```

