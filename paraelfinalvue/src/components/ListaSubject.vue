<template>
  <div>
    <h4>Listado de temas</h4>
 
  <ul v-for="(Subject, index) in Subject" :key="index">
    <li>Identificador :{{ Subject.id }}, Nombre del tema: {{ Subject.content }}, Relacionado con Foro: {{ Subject.foro_id }}</li>
  </ul>
  </div>
</template>

<script>
export default {
  name: "ListaSubject",
  data() {
    return {
      Subject: [],
    };
  },
  methods: {
    getSubject() {
      fetch("http://localhost:5000/api/v1/getsubject")
        .then((response) => response.json())
        .then((data) => {
          this.Subject = data.Subject;
        });
    },
  },
  mounted() {
    this.getSubject();
  },
};
</script>
<style type="text/css">
    table, th, td {
      border:1px solid black;
      }
      th, td {
        padding: 15px;
      }

      th{
        text-align: center;
      }
</style>
