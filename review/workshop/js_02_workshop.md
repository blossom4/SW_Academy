# js_02_workshop





> **템플릿 코드를 통해 제시된 기능을 충족하는 todo app을 완성하시오.**

- TODO 아이템을 추가할 수 있다. 
- 아이템 클릭을 통해 아이템에 취소선을 추가하고 제거할 수 있다. 
- x 버튼을 통해 아이템을 삭제할 수 있다.

선택사항

- 빈 값의 데이터 입력 방지 
- 빈 값 입력 시 브라우저 팝업 출력하기 
- 데이터 작성 후 input value 초기화

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

    // submitElement.addEventListener('click', addTodo)

    submitElement.addEventListener('click', function(event){
      event.preventDefault()
      const todoElement = document.querySelector('#todo')
      const todo = todoElement.value

      if (todo.trim()) {
        // 문자열이 있다면
        const liElement = document.createElement('li')
        liElement.innerText = todo

        const btnElement = document.createElement('button')
        btnElement.innerText = 'x'
        btnElement.addEventListener('click', function(){
          liElement.remove()
        })
        liElement.appendChild(btnElement)

        liElement.addEventListener('click', function(event){
          // event.target.setAttribute('class', 'done')
          console.log(event.target.classList)
          event.target.classList.toggle('done')          
        })

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

