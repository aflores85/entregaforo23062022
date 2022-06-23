<template>
  <div>
    <form @submit.prevent="sendForo">
      <input type="text" v-model="title" placeholder="Ingrese Titulo del foro" />
      <input type="text" v-model="content" placeholder="Ingrese contenido del foro" />
      <button type="submit">Nuevo Foro</button>
    </form>
  </div>
</template>

<script>

import ListaForosVue from './ListaForos.vue';

function sleep(milliseconds) {
  const date = Date.now();
  let currentDate = null;
  do {
    currentDate = Date.now();
  } while (currentDate - date < milliseconds);
}

export default {
  name: "formForo",
  data() {
    return {
      title: "",
      content: "",
    };
  },
  methods: {
    sendForo() {
      fetch("http://localhost:5000/api/v1/newforo", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({
          title: this.title,
          content: this.content,
        }),
      })
        .then((response) => response.json())
        .then((data) => {

          console.log(data);
          ListaForosVue.methods.getForos();
        
        });
    },
  },
};
</script>

<style scoped></style>

