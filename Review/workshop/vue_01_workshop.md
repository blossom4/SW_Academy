# vue_01_workshop



```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta http-equiv="X-UA-Compatible" content="IE=edge">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Document</title>
  <style>
    .finished {
      text-decoration: line-through;
    }
  </style>
</head>
<body>
  <div id="app">
    <h1>Lunch Menu</h1>
    <button @click="getLunch">Get Lunch</button>
    <p>{{ pickMenu }}</p>

    <hr>
    <h1>Lotto</h1>
    <button @click="getNumbers">Get Numbers</button>
    <p>{{ pickNumber }}</p>
    <hr>

    <h1>TODO</h1>
    <select v-model="selected">
      <option>전체</option>
      <option>완료</option>
      <option>진행중</option>
    </select>
    <input @keydown.enter="addList" v-model="inputData" type="text" id="input">
    
    <ul>
      <li v-for="todo in todos" v-bind:class="{ finished: todo.finished }">
          <input type="checkbox" v-model="todo.finished">{{ todo.text }}
      </li>
    </ul>
    <button @click="exterminate">Exterminate</button>
  </div>
  

  <!-- vue, lodash -->
  <script src="https://cdn.jsdelivr.net/npm/vue/dist/vue.js"></script>
  <script src="https://cdn.jsdelivr.net/npm/lodash@4.17.21/lodash.min.js"></script>
  <script>
    
    const app = new Vue({
      el: '#app',
      data: {
        pickMenu: '',
        pickNumber: [],
        inputData: '',
        i: 0,
        todoList: [],
        selected: '전체',
      },
      methods: {

        // Lunch Menu
        getLunch: function () {
          this.pickMenu = _.sampleSize(['계란', '떡볶이', '국수', '비빔밥',], 1)        
        },

        // Lotto
        getNumbers: function () {
          const lottoNumber = _.range(1, 46)
          this.pickNumber = _.sortBy(_.sampleSize(lottoNumber, 6))          
        },

        // Todo List
        addList: function () {
          const data = this.inputData.trim()
          if (data) {
            const todo = {
              finished: false,
              text: data,
              id: this.i,
            }
            this.todoList.push(todo)
            this.i++
          }
          this.inputData = ''
        },
        exterminate: function () {
          this.todoList = this.todoList.filter((todo)=>{
            return todo.finished !== true
          })
          /*let i = 0
          let len = 0
          while (i < this.checked.length) {
            if (this.checked[i] === true) {
              len += 1
            } 
          }
          while (len != this.checked.length) {
            if (this.checked[i] === true) {
              this.checked.splice(i, 1)
            } else if (this.checked[i] === false) {
              i += 1
            }
          }*/
        }
      },
      computed: {
        todos: function () {
          if (this.selected === '완료') {
            return this.todoList.filter((todo)=>{
              return todo.finished === true
            })
          } else if (this.selected === '진행중') {
            return this.todoList.filter((todo)=>{
              return todo.finished === false
            })
          } else {
            return this.todoList
          }
        }
      }
    })
  </script>
</body>
</html>
```

