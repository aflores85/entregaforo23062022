import { createRouter, createWebHistory } from 'vue-router'
import InicioView from '../views/InicioView'

const routes = [
  {
    path: '/',
    name: 'inicio',
    component: InicioView
  },
  ]
  const router = createRouter({
    history: createWebHistory(process.env.BASE_URL),
    routes,
  });

export default router
