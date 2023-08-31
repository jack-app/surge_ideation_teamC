import { createRouter, createWebHistory } from 'vue-router'
import TodolistView from '../views/TodolistView.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: TodolistView
    }
  ]
})

export default router
