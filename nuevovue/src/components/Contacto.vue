<template>
  <div class="contact">
    <h3 class="title">Contacto</h3>
    <form action class="form" submit.prevent="contact">
      <label class="form-label" for="#name"> Nombre </label>
      <input
        v-model="name"
        class="form-input"
        type="text"
        id="name"
        required
        placeholder="Nombre"
      >
      <label class="form-label" for="#email"> Email </label>
      <input
        v-model="email"
        class="form-input"
        type="email"
        id="email"
        placeholder="Email"
      >
      <input class="form-submit" type="submit" value="Contactar">
    </form>
  </div>
</template>

<script>
export default {
  data: () => ({
    name: "",
    email: ""
  }),
  methods: {
    contact() {
      console.log(this.name);
      console.log(this.email);
    }
  }
};
</script>


<style scoped></style>
