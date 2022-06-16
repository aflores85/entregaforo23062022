<template>
  <div>
    <form @submit.prevent="sendPosts">
      <input type="text" v-model="title" placeholder="Ingrese Titulo del Posts" />
      <input type="text" v-model="content" placeholder="Ingrese contenido del Posts"/>
      <input type="text" v-model="Subject_id" placeholder="Ingrese el id del Tema"/>
      <input type="text" v-model="image_url" placeholder="Ingrese el id del Tema"/>
    <button type="submit">Nuevo Posts</button>
    </form>
  </div>
</template>

<script>
export default {
  name: "FormPosts",
  data() {
    return {
      title: "",
      content: "",
      Subject_id:"",
      image_url:"",
    };
  },
  methods: {
    sendPosts() {
      fetch("http://localhost:5000/api/v1/newpost", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({
          title: this.title,
          content: this.content,
          Subject_id:this.Subject_id,
          image_url:this.image_url,
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

