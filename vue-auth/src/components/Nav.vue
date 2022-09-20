<template>
  <nav class="navbar navbar-expand-md navbar-dark bg-dark mb-4">
    <div class="container-fluid">
      <router-link to="/" class="navbar-brand">Home</router-link>

      <div>
        <ul class="navbar-nav me-auto mb-2 mb-md-0" v-if="!auth">
          <li class="nav-item">
            <router-link to="/login" class="nav-link">Login</router-link>
          </li>
        </ul>

        <ul class="navbar-nav me-auto mb-2 mb-md-0" v-if="auth">
          <li class="nav-item">
            <router-link to="/history" class="nav-link">Historial</router-link>
          </li>
        </ul>

        <ul class="navbar-nav me-auto mb-2 mb-md-0" v-if="auth">
          <li class="nav-item">
            <a href="#" class="nav-link" @click="logout">Logout</a>
          </li>
        </ul>
      </div>
    </div>
  </nav>
</template>

<script lang="ts">
import {computed, onMounted, reactive} from 'vue';
import {useStore} from "vuex";
import {useRouter} from "vue-router";

export default {
  name: "Nav",
  setup() {
    const store = useStore();
    const router = useRouter();

    const auth = computed(() => store.state.authenticated)

    onMounted(async () => {

      if (localStorage.getItem("token") != "" && localStorage.getItem("token") != undefined) store.state.authenticated = true
    });

    const logout = async () => {
      localStorage.setItem('token', '')
      store.state.authenticated = false
      await router.push('/login');
    }

    return {
      auth,
      logout
    }
  }
}
</script>
