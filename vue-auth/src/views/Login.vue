<template>
  <div class="container">
    <form @submit.prevent="submit">
      <h1 class="h3 mb-3 fw-normal">Please sign in</h1>

      <input v-model="data.username" type="text" class="form-control" placeholder="Username" required>

      <input v-model="data.password" type="password" class="form-control" placeholder="Password" required>

      <button class="w-100 btn btn-lg btn-primary" type="submit">Sign in</button>
    </form>
  </div>
</template>

<script lang="ts">
import {onMounted, reactive} from 'vue';
import {useRouter} from "vue-router";
import {useStore} from "vuex";

export default {
  name: "Login",
  setup() {
    const data = reactive({
      username: '',
      password: ''
    });
    const router = useRouter();
    const store = useStore();

    onMounted(async () => {


      // if (!store.state.authenticated) await router.push('/login');
      if (localStorage.getItem("token") != "" && localStorage.getItem("token") != undefined) await router.push('/');

    });

    const submit = async () => {
      await fetch('http://localhost:8000/api/auth/', {
        method: 'POST',
        headers: {'Content-Type': 'application/json'},
        body: JSON.stringify(data)
      }).then(async response => {
        if (response.status == 400) return alert("Complete los campos")
        if (response.status == 401) return alert("Credenciales inválidas")

        const body = await response.json()
        localStorage.token = body.access
        store.state.authenticated = true

      }).catch(error => {
        alert(("Error de servidor"))
      });

      await router.push('/');
    }

    return {
      data,
      submit
    }

  }
}
</script>