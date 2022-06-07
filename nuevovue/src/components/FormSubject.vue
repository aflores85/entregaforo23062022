<template>
  <div>
    <form @submit.prevent="sendSubject">
      <input type="text" v-model="title" placeholder="Ingrese Titulo del tema" />
      <input type="text" v-model="content" placeholder="Ingrese contenido del tema"/>
      <input type="text" v-model="foro_id" placeholder="Ingrese el id del foro"/>
      <button type="submit">Nuevo Subject</button>
    </form>
  </div>
</template>

<script>
export default {
  name: "FormSubject",
  data() {
    return {
      title: "",
      content: "",
      foro_id:"",
    };
  },
  methods: {
    sendSubject() {
      fetch("http://localhost:5000/api/v1/newsubject", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({
          title: this.title,
          content: this.content,
          foro_id:this.foro_id,
        }),
      })
        .then((response) => response.json())
        .then((data) => {
          console.log(data);
        });
    },
  },
};
</script>

<style scoped></style>

