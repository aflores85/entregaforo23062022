
<template>
  <div>
 
  <header style="text-align:center;">
  <hola-mundo-comp></hola-mundo-comp>
  </header>
    <h2> Dar de alta Foro </h2>
  <form-foro></form-foro>
  <h3> Dar de alta Tema en el Foro </h3>
  <Form-Subject></Form-Subject>
  <h4> Dar de alta un Posts </h4>
  <form-posts></form-posts>

  <h5 style="background-color:darkolivegreen"> <lista-foros></lista-foros></h5>
  <Lista-Subject style="background-color:darkgrey"></Lista-Subject>
  <h5 style="background-color:darkgrey">Lista de Posts</h5> <Lista-Posts></Lista-Posts>
    <Contacto></Contacto>  
  </div>
  


</template>


<script>
import HolaMundoComp from "../components/HolaMundoComp";
import ListaForos from "../components/ListaForos";
import FormForo from "../components/FormForo";
import FormSubject from "../components/FormSubject";
import ListaSubject from "../components/ListaSubject";
import Contacto from "../components/Contacto";
import Posts from "../components/ListaPosts";
import FormPosts from "../components/FormPosts";





export default {
  name: "InicioView",
  components: { HolaMundoComp, ListaForos, FormForo, FormSubject, ListaSubject, Contacto, Posts, FormPosts },
    
};
</script>

<style scoped></style>

