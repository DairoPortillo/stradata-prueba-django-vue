import {createRouter, createWebHistory, RouteRecordRaw} from 'vue-router'
import Home from '@/views/Home.vue'
import Login from '@/views/Login.vue'
import History from '@/views/History.vue'

const routes: Array<RouteRecordRaw> = [
    {path: '/', component: Home},
    {path: '/login', component: Login},
    {path: '/history', component: History},
]

const router = createRouter({
    history: createWebHistory(process.env.BASE_URL),
    routes
})

export default router
