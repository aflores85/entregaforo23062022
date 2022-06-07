<template>
  <div>
    <h1>Listado de Foros Activos</h1>
  <ul v-for="(foro, index) in foros" :key="index">
    <li>Identificador: {{ foro.id }},Titulo del Foro: {{ foro.content }}</li>
  </ul>
  </div>
</template>

<script>
export default {
  name: "ListaForos",
  data() {
    return {
      foros: [],
    };
  },
  methods: {
    getForos() {
      fetch("http://localhost:5000/api/v1/getforo")
        .then((response) => response.json())
        .then((data) => {
          this.foros = data.foros;
        });
    },
  },
  mounted() {
    this.getForos();
  },
};
</script>

<style scoped></style>