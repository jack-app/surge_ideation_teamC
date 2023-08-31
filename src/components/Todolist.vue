<template>
    <div>
      <h1>ToDo List</h1>
      <ul>
        <li v-for="todo in todos" :key="todo.id">{{ todo.text }}</li>
      </ul>
      <input v-model="newTodo" @keyup.enter="addTodo" placeholder="Add a new ToDo" />
    </div>
</template>
  
<script>
  import axios from 'axios';
  
  export default {
    data() {
      return {
        todos: [],
        newTodo: "",
      };
    },
    methods: {
      async addTodo() {
        try {
          console.log("OK", this.newTodo);
          const response = await axios.post("http://localhost:8000", {
            text: this.newTodo,
          });
          console.log(response.data);
          this.newTodo = "";
          this.fetchTodos();
        } catch (error) {
          console.error(error);
        }
      },
      async fetchTodos() {
        try {
          const response = await axios.get("http://localhost:8000");
          this.todos = response.data;
        } catch (error) {
          console.error(error);
        }
      },
    },
    created() {
      this.fetchTodos();
    },
  };
</script>
  