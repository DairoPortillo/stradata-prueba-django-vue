<template>
  <div class="container">
    <div class="row">
      <table class="table">
        <thead>
        <tr>
          <th scope="col">ID</th>
          <th scope="col">Usuario</th>
          <th scope="col">Busqueda</th>
          <th scope="col">Porcentaje</th>
          <th scope="col">Fecha</th>
        </tr>
        </thead>
        <tbody>
        <tr v-for="(resultado, index) in data.resultados" :key="index">
          <td><button @click="detail(resultado.id)" type="button" class="btn btn-link" data-bs-toggle="modal" data-bs-target="#exampleModal">
            {{resultado.id}}
          </button></td>
          <td>{{resultado.username}}</td>
          <td>{{resultado.busqueda}}</td>
          <td>{{resultado.porcentaje}}%</td>
          <td>{{resultado.created}}</td>
        </tr>
        </tbody>
      </table>
    </div>

    <!-- Modal -->
    <div class="modal fade" id="exampleModal" tabindex="-1" aria-labelledby="exampleModalLabel" aria-hidden="true">
      <div class="modal-dialog">
        <div class="modal-content">
          <div class="modal-header">
            <h5 class="modal-title" id="exampleModalLabel">Busqueda: {{data.detail.busqueda}}</h5>
            <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
          </div>
          <div class="modal-body">
            <div class="table-responsive">
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
                <tr v-for="(resultado, index) in data.detail.resultados_historial" :key="index">
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
          <div class="modal-footer">
            <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Close</button>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script lang="ts">
import {onMounted, reactive} from 'vue';
import {useRouter} from "vue-router";
import {useStore} from "vuex";

export default {
  name: "History",
  setup() {
    const data = reactive({
      resultados: [],
      detail: {}
    });
    const router = useRouter();
    const store = useStore();

    onMounted(async () => {

      // if (!store.state.authenticated) await router.push('/login');
      if (localStorage.getItem("token") == "" || localStorage.getItem("token") == undefined) await router.push('/login');

      try {
        const response = await fetch('http://localhost:8000/api/historial/', {
          headers: {'Content-Type': 'application/json',
            'Authorization': 'Bearer '+ localStorage.token},
        });

        if (response.status == 401) return alert("Sin Session")

        data.resultados = await response.json();

      } catch (e) {
        alert("Error servidor")
      }

    });

    return {
      data
    }
  },
  methods: {
    async detail(id: any) {
      try {
        const response = await fetch('http://localhost:8000/api/historial/'+id+"/", {
          headers: {'Content-Type': 'application/json',
            'Authorization': 'Bearer '+ localStorage.token},
        });

        if (response.status == 401) return alert("Sin Session")

        this.data.detail = await response.json();

      } catch (e) {
        alert("Error servidor")
      }
    }
  }
}
</script>