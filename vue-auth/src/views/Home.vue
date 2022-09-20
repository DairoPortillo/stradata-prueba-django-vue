<template>
  <div class="container">
    <form @submit.prevent="submit" class="row g-3">
      <div class="col-auto">
        <input v-model="data.nombre" type="text" class="form-control" id="nombre" placeholder="Nombre a buscar">
      </div>
      <div class="col-auto">
        <input v-model="data.porcentaje" type="number" class="form-control" id="porcentaje" placeholder="porcentaje" step="0.01">
      </div>
      <div class="col-auto">
        <button type="submit" class="btn btn-primary mb-3">Buscar</button>
      </div>
      <div class="col-auto mt-2">
        <div class="alert alert-success" role="alert" v-if="data.statusOk">
          Exitoso con resultados
        </div>
        <div class="alert alert-warning" role="alert" v-if="data.statusEmpty">
          Exitoso sin resultados
        </div>
      </div>
    </form>
    <div class="row">
      <table class="table">
        <thead>
        <tr>
          <th scope="col">Nombre</th>
          <th scope="col">Tipo Persona</th>
          <th scope="col">Tipo Cargo</th>
          <th scope="col">Departamento</th>
          <th scope="col">Municipio</th>
          <th scope="col">% Coincidencia</th>
        </tr>
        </thead>
        <tbody>
            <tr v-for="(resultado, index) in data.resultados" :key="index">
              <td>{{resultado.nombre}}</td>
              <td>{{resultado.tipo_persona}}</td>
              <td>{{resultado.tipo_cargo}}</td>
              <td>{{resultado.departamento}}</td>
              <td>{{resultado.municipio}}</td>
              <td>{{resultado.ratio.toFixed(2)}}</td>
            </tr>
        </tbody>
      </table>
    </div>
  </div>
</template>

<script lang="ts">
import {onMounted, reactive, ref} from 'vue';
import {useStore} from "vuex";
import {useRouter} from "vue-router";

export default {
  name: "Home",
  setup() {
    const router = useRouter();
    const store = useStore();

    const data = reactive({
      nombre: '',
      porcentaje: '',
      statusOk: false,
      statusEmpty: false,
      resultados: []
    });

    onMounted(async () => {

      // if (!store.state.authenticated) await router.push('/login');
      if (localStorage.getItem("token") == "" || localStorage.getItem("token") == undefined) await router.push('/login');

    });

    const submit = async () => {

      data.statusEmpty = false
      data.statusOk = false

      try {
        const response = await fetch('http://localhost:8000/api/personas/'
            +"?nombre="+data.nombre+"&porcentaje="+data.porcentaje, {
          headers: {'Content-Type': 'application/json',
            'Authorization': 'Bearer '+ localStorage.token},
        });

        if (response.status == 401) return alert("Sin Session")

        const content = await response.json();

        if (content.length == 0){
          data.statusEmpty = true
        }else{
          data.statusOk = true
        }

        data.resultados = content


      } catch (e) {
        alert("Error servidor")
      }
    }

    return {
      data,
      submit
    }

  }
}
</script>
