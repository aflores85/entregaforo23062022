<template>
  <q-page class="flex flex-center">
   <q-form
    x-on:submit="login"
    x-on:reset="reset"
    >
    <q-input
      filled
      v-model="username"
      label="usuario"
      hint="Tu nombre de usuario"
      lazy-rules
      :rules="[va1 => val && val.length > 0 || 'por favor ingrese su nomnbre de usuario']"
    />
    <q-input
      filled
      type="password"
      v-model="password"
      label="Contraseña"
      hint="Tu contraseña"
      lazy-rules
      :rules="[va1 => val && val.length > 0 || 'por favor ingrese su contraseña']"
    />

    <div>
      <q-btn label="Ingresar" type="submit" color="primary"/>
      <q-btn label="Cancelar" type="reset" color="primary" flat class="q-ml-sm" />
    </div>
   </q-form>
  </q-page>
</template>

<script>
export default {
  name: 'IndexPage',
  data () {
    return {
      username: '',
      password: ''
    }
  },
  methods: {
    login: function () {
      // cualquier dato q ingrese me deja entrar
    },
    reset: function () {

    }
  }
}
</script>
