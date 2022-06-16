<template>
  <div>
    <h3>Listado de Posts</h3>
  <ul v-for="(Posts, index) in Posts" :key="index">
    <li>Identificador :{{ Posts.id }}, Nombre del Posts: {{ Posts.content }}, Relacionado con Tema: {{ Posts.foro_id }}</li>
  </ul>
  </div>
</template>

<script>
export default {
  name: "ListaPosts",
  data() {
    return {
      Posts: [],
    };
  },
  methods: {
    getPosts() {
      fetch("http://localhost:5000/api/v1/getPosts")
        .then((response) => response.json())
        .then((data) => {
          this.Posts = data.Posts;
        });
    },
  },
  mounted() {
    this.getPosts();
  },
};
</script>
<style scoped></style>