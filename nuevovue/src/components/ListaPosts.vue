<template>
  <div>
    <h3>Listado de Posts</h3>
  <ul v-for="(posts, index) in posts" :key="index">
    <li>Identificador :{{ posts.id }}, Nombre del Posts: {{ posts.content }}</li>
  </ul>
  </div>
</template>

<script>
export default {
  name: "ListaPosts",
  data() {
    return {
      posts: [],
    };
  },
  methods: {
    GetPosts() {
      fetch("http://localhost:5000/api/v1/getPosts")
        .then((response) => response.json())
        .then((data) => {
          this.posts = data.posts;
        });
    },
  },
  mounted() {
    this.GetPosts();
  },
};
</script>
<style scoped></style>