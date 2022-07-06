<template>
  <div id="app">
    <h3>FORO DE TECNOLOGIA</h3>
   
    <div><FormForoVue></FormForoVue></div>
    <div><FormSubjectVue></FormSubjectVue></div>
    <div><FormPostsVue></FormPostsVue></div>
    <div><ListaForosVue></ListaForosVue></div>
    <div><ListaSubjectVue></ListaSubjectVue></div>
    <div><ListaPostsVue></ListaPostsVue></div>
   
     
  </div>
</template>

<script>
//import HelloWorld from './components/HelloWorld'

import FormForoVue from './components/FormForo.vue'
import FormPostsVue from './components/FormPosts.vue'
import FormSubjectVue from './components/FormSubject.vue'
import ListaSubjectVue from './components/ListaSubject.vue'
import ListaPostsVue from './components/ListaPosts.vue'
import ListaForosVue from './components/ListaForos.vue'

export default {
  name: 'App',
  components: {
    ListaForosVue, FormForoVue, FormPostsVue, FormSubjectVue, ListaSubjectVue, ListaPostsVue
 //   HelloWorld
  },
}
</script>

<style>
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
